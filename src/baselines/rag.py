"""RAG baseline: markdown chunking -> embedding vector index -> cosine top-k retrieval -> single-turn generation.

An honest implementation of standard single-turn RAG, feeding recall to its ceiling within that form (P2 high-ceiling setting):
heading-aware chunking (chunk_size=800/overlap=100) + top-k=24 + 80k-char context budget;
no rerank / query-rewrite or other extra stages -- those are systems engineering, not "the ceiling of standard RAG".
The whole benchmark uses only vector retrieval (respecting industry practice; no substring/keyword fallback)."""
from __future__ import annotations
import hashlib
import json
import re
import threading
import time

import numpy as np

from .. import llm
from ..corpus_construction import REPORT_METADATA_KEYS, split_frontmatter
from . import config
from ._gen import generate, compute_cost
from .base import AnswerResult, Baseline, register
from .corpus import Corpus

RAG_SYSTEM_PROMPT = (
    "You are an enterprise knowledge-base QA assistant. Answer the user's question based ONLY on the retrieved document snippets below.\n"
    "If the retrieved content contains no relevant information, state clearly \"Cannot answer based on the available materials\".\n"
    "Do not fabricate or speculate about information not mentioned in the documents. Keep answers structured and well-organized.\n"
    "Note: document snippets may come from different sources and times; analyze them holistically."
)

# ==== markdown chunking (heading #{1,4}, paragraph/sentence-boundary-aware splitting) ====
_HEADING = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)


def _make_chunk_id(source_file: str, sect_idx: int, start: int, end: int) -> str:
    # Include the in-document section index: eliminates ID collisions when different heading sections
    # have identical local start/end offsets (old version used only source_file:start:end -> GraphRAG
    # dict merge silently dropped chunks, audit P1-1).
    return hashlib.md5(f"{source_file}:{sect_idx}:{start}:{end}".encode()).hexdigest()[:12]


def _split_by_headings(text: str) -> list[tuple[str, str]]:
    sections, stack, last_pos, last_path = [], [], 0, ""
    for m in _HEADING.finditer(text):
        if last_pos < m.start():
            content = text[last_pos:m.start()].strip()
            if content:
                sections.append((last_path, content))
        level = len(m.group(1))
        title = m.group(2).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        last_path = " > ".join(h[1] for h in stack)
        last_pos = m.end() + 1
    if last_pos < len(text):
        content = text[last_pos:].strip()
        if content:
            sections.append((last_path, content))
    if not sections:
        sections = [("", text.strip())]
    return sections


def _split_section(text: str, size: int, overlap: int, source_file: str,
                   heading_path: str, group: str, sect_idx: int = 0) -> list[dict]:
    if len(text) <= size:
        return [{"id": _make_chunk_id(source_file, sect_idx, 0, len(text)), "text": text,
                 "source_file": source_file, "heading_path": heading_path,
                 "group": group, "char_count": len(text)}]
    chunks, start = [], 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            para = text.rfind("\n\n", start, end)
            if para > start + size // 2:
                end = para + 2
            else:
                sent = max(text.rfind("。", start, end), text.rfind(".", start, end),
                           text.rfind("\n", start, end))
                if sent > start + size // 2:
                    end = sent + 1
        ct = text[start:end].strip()
        if ct:
            chunks.append({"id": _make_chunk_id(source_file, sect_idx, start, end), "text": ct,
                           "source_file": source_file, "heading_path": heading_path,
                           "group": group, "char_count": len(ct)})
        start = end - overlap
        if start >= len(text) - overlap:
            break
    return chunks


def _chunk_doc(relpath: str, text: str, group: str, size: int, overlap: int) -> list[dict]:
    if not text.strip():
        return []
    frontmatter, body = split_frontmatter(text)
    metadata = {key: frontmatter[key] for key in REPORT_METADATA_KEYS if key in frontmatter}
    chunks = []
    for sect_idx, (hp, sect) in enumerate(_split_by_headings(body)):
        chunks += _split_section(sect, size, overlap, relpath, hp, group, sect_idx)
    if metadata:
        for chunk in chunks:
            chunk.update(metadata)
    return chunks


def _chunk_metadata_text(chunk: dict) -> str:
    """Render stored metadata for retrieval/context without mutating chunk body text."""
    labels = {
        "document_type": "Document type",
        "report_date": "Report date",
        "report_time": "Report time",
        "authors": "Authors",
        "department": "Department",
    }
    # `department` is the target relation of L3-H attribution questions (it should be "absent from the
    # published source", derivable only via the graph person->dept edge). Rendering it into flat
    # retrieval text would leak that latent relation to bm25/rag/graphrag, so drop department from retrieval text.
    RETRIEVAL_METADATA_KEYS = tuple(k for k in REPORT_METADATA_KEYS if k != "department")
    lines = []
    for key in RETRIEVAL_METADATA_KEYS:
        value = chunk.get(key)
        if value in (None, "", []):
            continue
        if isinstance(value, list):
            value = ", ".join(str(item) for item in value)
        lines.append(f"{labels[key]}: {value}")
    return "\n".join(lines)


def _chunk_retrieval_text(chunk: dict) -> str:
    metadata = _chunk_metadata_text(chunk)
    return f"{metadata}\n\n{chunk['text']}" if metadata else chunk["text"]


# Embedding model context cap (Qwen3-Embedding-8B=40960 tokens). Truncate conservatively by chars to
# guard against GraphRAG's over-long entity descriptions merged across many source chunks (measured at
# 77423 tokens for one) blowing past 400. Taking a representative prefix does not hurt retrieval signal.
_EMBED_MAX_CHARS = 24000


def _embed(texts: list[str], batch_size: int = 64, model: str | None = None) -> np.ndarray:
    """Batch embedding (encoding_format=float). model defaults to RAG_EMBED_MODEL.
    Each input is truncated to _EMBED_MAX_CHARS (guard against over-long). Batches run **concurrently**
    (to saturate embedding TPM, especially graphrag's 220k entities)."""
    from concurrent.futures import ThreadPoolExecutor
    import tenacity
    texts = [(t[:_EMBED_MAX_CHARS] if isinstance(t, str) and len(t) > _EMBED_MAX_CHARS else t)
             for t in texts]
    mdl = model or config.RAG_EMBED_MODEL
    batches = [texts[i:i + batch_size] for i in range(0, len(texts), batch_size)]

    @tenacity.retry(stop=tenacity.stop_after_attempt(5),
                    wait=tenacity.wait_exponential(multiplier=1, min=2, max=20))
    def _one(b):
        r = llm.next_client().embeddings.create(input=b, model=mdl, encoding_format="float")
        return [d.embedding for d in r.data]

    workers = max(1, min(getattr(config, "MAX_CONCURRENCY", 64), len(batches)))
    with ThreadPoolExecutor(max_workers=workers) as ex:
        parts = list(ex.map(_one, batches))   # order preserved
    out = [v for part in parts for v in part]
    return np.asarray(out, dtype=np.float32)


class VectorIndex:
    """Vector index load/retrieve (shared by rag and agentic_rag, B2).
    The query-side embed model is **auto-paired from index_meta.json** -- index and query must use the
    same model and dimension; the global EMBED_MODEL in `.env` may have been upgraded (lesson: v02 index
    at 1024 dims vs a new model at 4096 dims, matmul crashed outright)."""

    def __init__(self, index_dir, top_k: int | None = None):
        from pathlib import Path
        self.dir = Path(index_dir)
        self.top_k = top_k or config.RAG_TOP_K
        self._chunks: list[dict] | None = None
        self._normed = None
        self.embed_model: str | None = None
        self._load_lock = threading.Lock()

    def load(self) -> None:
        if self._chunks is not None:
            return
        with self._load_lock:                    # double-checked lock: prevent multiple workers each loading a copy -> memory doubling/OOM
            if self._chunks is not None:
                return
            self._load_locked()

    def _load_locked(self) -> None:
        if not (self.dir / "embeddings.npy").exists():
            raise FileNotFoundError(
                f"RAG vector index missing: {self.dir} (first run `python -m src.baselines.cli build --baseline rag`,"
                f" and confirm EKWB_RAG_INDEX points to the index paired with EKWB_DATASET)")
        meta_f = self.dir / "index_meta.json"
        meta = json.loads(meta_f.read_text(encoding="utf-8")) if meta_f.exists() else {}
        self.embed_model = meta.get("embedding_model") or config.RAG_EMBED_MODEL
        emb = np.load(self.dir / "embeddings.npy").astype(np.float32, copy=False)
        norms = np.linalg.norm(emb, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        emb /= norms                      # in-place normalization (eliminates a full doubling copy of emb/norms;
        self._normed = emb                # graphrag's 220k-entity 3.6GB embeddings once doubled -> 220GB cgroup OOM)
        self._chunks = [json.loads(l) for l in open(self.dir / "chunks.jsonl", encoding="utf-8")]

    def retrieve(self, question: str, top_k: int | None = None) -> list[dict]:
        self.load()
        qv = _embed([question], model=self.embed_model)[0]
        n = np.linalg.norm(qv)
        if n == 0:
            return []
        sims = self._normed @ (qv / n)
        k = top_k or self.top_k
        top = np.argsort(sims)[::-1][:k]
        return [dict(self._chunks[i], _score=float(sims[i])) for i in top if sims[i] > 0]


@register("rag")
class RagBaseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None,
                 index_dir=None, top_k: int | None = None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self.index_dir = index_dir or config.RAG_INDEX_DIR
        self.top_k = top_k or config.RAG_TOP_K
        self._vindex = VectorIndex(self.index_dir, self.top_k)

    # ---------- offline: build index ----------
    def prepare(self, log=print) -> None:
        t0 = time.time()
        docs = self.corpus.docs()
        all_chunks: list[dict] = []
        for p in docs:
            rel = self.corpus.rel(p)
            all_chunks += _chunk_doc(rel, self.corpus.read(rel) or "",
                                     self.corpus.group, config.CHUNK_SIZE, config.CHUNK_OVERLAP)
        log(f"[rag.build] {len(docs)} docs -> {len(all_chunks)} chunks, embedding ({config.RAG_EMBED_MODEL})...")
        emb = _embed([_chunk_retrieval_text(c) for c in all_chunks])
        self.index_dir.mkdir(parents=True, exist_ok=True)
        np.save(self.index_dir / "embeddings.npy", emb)
        with open(self.index_dir / "chunks.jsonl", "w", encoding="utf-8") as f:
            for c in all_chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        meta = {"group": self.corpus.group, "embedding_model": config.RAG_EMBED_MODEL,
                "embedding_dim": int(emb.shape[1]), "chunk_size": config.CHUNK_SIZE,
                "chunk_overlap": config.CHUNK_OVERLAP, "total_chunks": len(all_chunks),
                "total_files": len(docs), "build_time_s": round(time.time() - t0, 1)}
        (self.index_dir / "index_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                                                        encoding="utf-8")
        log(f"[rag.build] saved -> {self.index_dir} ({meta['total_chunks']} chunks, dim {meta['embedding_dim']})")

    def _retrieve(self, question: str) -> list[dict]:
        return self._vindex.retrieve(question, self.top_k)

    # ---------- online: answering ----------
    def answer(self, question: dict) -> AnswerResult:
        t0 = time.time()
        q = question["question"]
        hits = self._retrieve(q)
        parts, total = [], 0
        for r in hits:
            metadata = _chunk_metadata_text(r)
            meta_line = f"[document metadata: {metadata.replace(chr(10), '; ')}]\n" if metadata else ""
            block = (f"[source: {r['source_file']}]\n[location: {r['heading_path']}]\n"
                     f"{meta_line}{r['text']}")
            if total + len(block) > config.MAX_CONTEXT_CHARS:
                break
            parts.append(block)
            total += len(block)
        context = "\n\n---\n\n".join(parts)
        if not context:
            return AnswerResult("[ERROR] No relevant chunks retrieved", "rag", wall_time_s=time.time() - t0)
        user = f"## Reference materials:\n\n{context}\n\n## Question:\n{q}\n\nPlease answer the question based on the above materials."
        text, usage = generate(RAG_SYSTEM_PROMPT, user, model=self.model, max_tokens=config.GEN_MAX_TOKENS)
        return AnswerResult(text, "rag", tokens=usage, cost_usd=compute_cost(usage, self.model),
                            wall_time_s=time.time() - t0, context_chars=len(context))
