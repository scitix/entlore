"""BM25 baseline -- naive sparse retrieval (Okapi BM25) -> single-turn generation.

Control-group purpose: provides a naive floor of **classic term-frequency retrieval that does not rely on embeddings**
(inherently a different family from the vector-based rag). Self-contained implementation (Okapi BM25, ~40 lines, zero new deps),
avoiding pulling in rank_bm25/jieba for one naive baseline.
Chunking/context/generation fully reuse the rag setting (heading-aware chunking 800/100, 80k context, RAG_SYSTEM_PROMPT);
the only variable is the retriever: sparse BM25 replaces dense vectors.

Tokenization (bilingual corpus): lowercasing -> Latin words `[a-z0-9]+` + CJK character-level unigram + bigram
(no tokenizer dependency; bigrams provide Chinese phrase recall). Stopwords are not treated specially (BM25 idf naturally suppresses high-frequency terms).
"""
from __future__ import annotations
import json
import math
import re
import time
from collections import Counter

from . import config
from ._gen import generate, compute_cost
from .base import AnswerResult, Baseline, register
from .corpus import Corpus
from .rag import RAG_SYSTEM_PROMPT, _chunk_doc, _chunk_retrieval_text

_LATIN = re.compile(r"[a-z0-9]+")
_CJK = re.compile(r"[一-鿿]")


def _tokenize(text: str) -> list[str]:
    text = (text or "").lower()
    toks = _LATIN.findall(text)
    cjk = _CJK.findall(text)
    toks += cjk                                   # single characters
    toks += [cjk[i] + cjk[i + 1] for i in range(len(cjk) - 1)]   # adjacent-character bigrams
    return toks


class BM25Index:
    """In-memory Okapi BM25 (lazy-load chunks.jsonl then fit once; answer reuses the same instance)."""

    def __init__(self, index_dir, top_k: int | None = None,
                 k1: float | None = None, b: float | None = None):
        import threading
        from pathlib import Path
        self.dir = Path(index_dir)
        self.top_k = top_k or config.BM25_TOP_K
        self.k1 = k1 if k1 is not None else config.BM25_K1
        self.b = b if b is not None else config.BM25_B
        self._ready = False
        self._lock = threading.Lock()
        self._chunks: list[dict] | None = None
        self._tf: list[Counter] | None = None
        self._idf: dict[str, float] | None = None
        self._dl: list[int] | None = None
        self._avgdl: float = 0.0

    def load(self) -> None:
        """Thread-safe lazy load + fit (tool loop / eval concurrency share one instance): all fields are made ready
        atomically inside the lock, `_ready` set last, avoiding a half-initialized state being read by a concurrent retrieve
        (list index / NoneType race)."""
        if self._ready:
            return
        with self._lock:
            if self._ready:
                return
            if not (self.dir / "chunks.jsonl").exists():
                raise FileNotFoundError(
                    f"BM25 chunk store missing: {self.dir} (first run `python -m src.baselines.cli build --baseline bm25`)")
            chunks = [json.loads(l) for l in open(self.dir / "chunks.jsonl", encoding="utf-8")]
            tf_list, dl, df = [], [], Counter()
            for c in chunks:
                # On par with RAG: metadata (authors/report_date/department etc.) is included in the searchable text
                # (recheck P1-1: otherwise BM25 cannot see frontmatter metadata, hurting person_timeline/department_attribution questions)
                toks = _tokenize(_chunk_retrieval_text(c))
                tf = Counter(toks)
                tf_list.append(tf)
                dl.append(len(toks))
                for t in tf:
                    df[t] += 1
            n = len(chunks)
            avgdl = (sum(dl) / n) if n else 0.0
            idf = {t: math.log((n - d + 0.5) / (d + 0.5) + 1.0) for t, d in df.items()}
            self._chunks, self._tf, self._dl, self._avgdl, self._idf = chunks, tf_list, dl, avgdl, idf
            self._ready = True

    def retrieve(self, question: str, top_k: int | None = None) -> list[dict]:
        self.load()
        q = [t for t in _tokenize(question) if t in self._idf]
        if not q:
            return []
        k1, b, avgdl = self.k1, self.b, self._avgdl or 1.0
        scores = []
        for i, tf in enumerate(self._tf):
            s, norm = 0.0, k1 * (1 - b + b * self._dl[i] / avgdl)
            for t in q:
                f = tf.get(t)
                if f:
                    s += self._idf[t] * (f * (k1 + 1)) / (f + norm)
            if s > 0:
                scores.append((s, i))
        scores.sort(reverse=True)
        k = top_k or self.top_k
        return [dict(self._chunks[i], _score=float(s)) for s, i in scores[:k]]


@register("bm25")
class BM25Baseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None,
                 index_dir=None, top_k: int | None = None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self.index_dir = index_dir or config.BM25_INDEX_DIR
        self.top_k = top_k or config.BM25_TOP_K
        self._index = BM25Index(self.index_dir, self.top_k)

    # ---------- offline: chunk store (BM25 stats are fit at load time, no need to persist embeddings) ----------
    def prepare(self, log=print) -> None:
        t0 = time.time()
        docs = self.corpus.docs()
        all_chunks: list[dict] = []
        for p in docs:
            rel = self.corpus.rel(p)
            all_chunks += _chunk_doc(rel, self.corpus.read(rel) or "",
                                     self.corpus.group, config.CHUNK_SIZE, config.CHUNK_OVERLAP)
        self.index_dir.mkdir(parents=True, exist_ok=True)
        with open(self.index_dir / "chunks.jsonl", "w", encoding="utf-8") as f:
            for c in all_chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        (self.index_dir / "index_meta.json").write_text(json.dumps(
            {"retriever": "bm25-okapi", "group": self.corpus.group, "k1": config.BM25_K1,
             "b": config.BM25_B, "total_chunks": len(all_chunks), "total_files": len(docs),
             "build_time_s": round(time.time() - t0, 1)}, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"[bm25.build] {len(docs)} docs -> {len(all_chunks)} chunks -> {self.index_dir}")

    # ---------- online: BM25 top-k -> single-turn generation (mirrors rag, only the retriever changes) ----------
    def answer(self, question: dict) -> AnswerResult:
        t0 = time.time()
        q = question["question"]
        hits = self._index.retrieve(q, self.top_k)
        parts, total = [], 0
        for r in hits:
            block = f"[source: {r['source_file']}]\n[location: {r.get('heading_path','')}]\n{_chunk_retrieval_text(r)}"
            if total + len(block) > config.MAX_CONTEXT_CHARS:
                break
            parts.append(block); total += len(block)
        context = "\n\n---\n\n".join(parts)
        if not context:
            # A genuine "no retrieval results" (not an infrastructure failure) -- no [ERROR] prefix, to avoid being misjudged by is_infra_error and retried (recheck P2-2)
            return AnswerResult("No relevant chunks retrieved for this query (BM25).", "bm25",
                                wall_time_s=time.time() - t0)
        user = f"## Reference materials:\n\n{context}\n\n## Question:\n{q}\n\nPlease answer the question based on the above materials."
        text, usage = generate(RAG_SYSTEM_PROMPT, user, model=self.model, max_tokens=config.GEN_MAX_TOKENS)
        return AnswerResult(text, "bm25", tokens=usage, cost_usd=compute_cost(usage, self.model),
                            wall_time_s=time.time() - t0, context_chars=len(context))
