"""OKF baseline -- Open Knowledge Format v0.1 (GoogleCloudPlatform/knowledge-catalog/okf).

**The format-materialization layer fully references the official code** (vendored @ d44368c15e38, Apache-2.0):
- `reference_agent.bundle.document.OKFDocument` -- frontmatter serialization / required-key validation;
- `reference_agent.bundle.paths.concept_id_to_path` -- concept id validation (ASCII segments) and on-disk path;
- `reference_agent.bundle.index.regenerate_indexes` -- official index tree generation
  (directory descriptions go through this repo's relay via injected synthesize, replacing the default Gemini);
- `reference_agent.sources.base.Source/ConceptRef` -- official data-source abstraction; this file implements CorpusSource.

Still belonging to this repo (the official spec explicitly says "anyone can produce", the production side is open):
- corpus enumeration + one cheap LLM enrichment per doc (type/description/tags);
- body = lossless mirror of the source text (unlike the official agent's synthesized style; a deliberate deviation, see docs/baselines.md);
- Related/Cited by (§4.1 extension) with # Citations (§8) and resource=corpus:// (evaluator depends on it);
- root index okf_version frontmatter (§11 recommended).

Answering (P4 ceiling): OKF's thesis is "the format carries navigation", so the answering side uses a **navigation toolset**
to exploit the format bonus fully -- get_index (hierarchical index tree) + get_page + follow_links (Related/Cited-by neighbors) + search
(bundle vector index, built by the same pipeline as rag at prepare time). Independent loop and prompt, borrowing no other pipeline.

Compilation is a **single complete pipeline**: enumerate -> enrich -> official materialize -> official index tree -> vector index -> manifest
(the src->cid mapping goes into okf_manifest.json; scorer/oracle no longer scan frontmatter). No incremental/surgical path:
recompile = pay the full enrichment cost again, in exchange for products that strictly correspond to the code.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

from .. import llm
from . import config
from .base import AnswerResult, Baseline, register
from .corpus import Corpus
from .loop import run_loop_answer
from .rag import VectorIndex
from .toolkits import follow_links_tool, get_index_tool, get_page_tool, search_tool

# ---- vendored official package (third_party/okf/reference_agent) ----
_TP = str(config.ROOT / "third_party" / "okf")
if _TP not in sys.path:
    sys.path.insert(0, _TP)
from reference_agent.bundle.document import OKFDocument            # noqa: E402
from reference_agent.bundle.paths import concept_id_to_path        # noqa: E402
from reference_agent.bundle.index import regenerate_indexes        # noqa: E402
from reference_agent.sources.base import ConceptRef, Source        # noqa: E402

_COMPILE_TS = "2026-01-01T00:00:00+00:00"
_MAX_LINKS = 15
_SEGMENT_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_.\-]*")   # same as official paths._SEGMENT_RE

_ENRICH_SYS = (
    "You catalog a knowledge passage into Open Knowledge Format frontmatter. "
    "Return STRICT JSON with keys: type, description, tags. "
    "`type` is a short concept kind, Title Case (e.g. Project, Person, Policy, Incident, "
    "Report, Department, Concept). `description` is ONE factual sentence. `tags` is a list of "
    "3-7 short lowercase keywords (salient entities/topics). No extra keys."
)

OKF_SYSTEM_PROMPT = """You are an enterprise knowledge-base QA assistant. The knowledge base is an Open Knowledge Format (OKF) bundle:
- Each page is a concept, organized into directories by type (e.g. report/, policy/, project/)
- Each directory level has an index.md index tree that can be browsed level by level
- The Related (related concepts) and Cited by (reverse references) at the end of a concept page are navigable knowledge-graph edges

Tool semantics:
- get_index: read the directory index tree (a subdirectory can be specified)
- search: semantic retrieval of relevant concepts (returns paths and snippets)
- get_page: read the full text of a concept by its exact path
- follow_links: list the Related / Cited by neighbors of a concept
- submit_answer: submit the final answer

How to combine browsing / searching / edge navigation is entirely up to you.

## Answer requirements
- **Use only information you have read**; do not fabricate or speculate about facts not present in the knowledge base
- When information is insufficient, state clearly what is missing

## Citation format (must follow)
After each key factual assertion, cite its source: `[source: group/path]`;
the path must be a page you actually read; for information whose source is uncertain, mark it as [source: inferred] rather than fabricating a path.

Available knowledge-base groups: {groups}"""


def _ascii_seg(s: str, fallback_key: str) -> str:
    """Official concept id segments must be ASCII ([A-Za-z0-9_][A-Za-z0-9_.-]*);
    Chinese/illegal segments are deterministically downgraded to doc-<md5>."""
    s = (s or "").strip()
    if _SEGMENT_RE.fullmatch(s):
        return s[:80]
    cleaned = re.sub(r"[^A-Za-z0-9_.\-]+", "-", s).strip("-.")
    if cleaned and _SEGMENT_RE.fullmatch(cleaned):
        return cleaned[:80]
    return "doc-" + hashlib.md5(fallback_key.encode("utf-8")).hexdigest()[:10]


def _type_dir(typ: str) -> str:
    return _ascii_seg(typ.lower().replace(" ", "-"), typ) or "concept"


def _doc_title(rel: str, text: str) -> str:
    m = re.search(r"^title:\s*(.+)$", text[:400], re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return Path(rel).stem


def _first_sentence(text: str) -> str:
    body = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)
    s = re.split(r"(?<=[。.!?])\s", body.strip(), maxsplit=1)
    return (s[0] if s else "").strip()[:300]


def _enrich_one(job) -> dict:
    rel, title, text = job
    user = f"Title: {title}\n\nPassage:\n{text[:2000]}"
    try:
        obj = llm.chat_json(_ENRICH_SYS, user, max_tokens=400)
        typ = str(obj.get("type") or "Concept").strip() or "Concept"
        desc = str(obj.get("description") or "").strip() or _first_sentence(text)
        tags = obj.get("tags") or []
        if not isinstance(tags, list):
            tags = [str(tags)]
        tags = [str(t).strip().lower() for t in tags if str(t).strip()][:7]
        return {"type": typ, "description": desc[:300], "tags": tags}
    except Exception:
        return {"type": "Concept", "description": _first_sentence(text), "tags": []}


class CorpusSource(Source):
    """Local-corpus implementation of the official Source abstraction: each markdown = one first-class concept (§8 mirror)."""
    name = "ekwb_corpus"

    def __init__(self, corpus: Corpus, metas: dict):
        self.corpus = corpus
        self.metas = metas          # rel -> {type, description, tags}
        self._refs: list[ConceptRef] | None = None

    def list_concepts(self) -> list[ConceptRef]:
        if self._refs is not None:
            return self._refs
        used, refs = set(), []
        for p in self.corpus.docs():
            rel = self.corpus.rel(p)
            meta = self.metas[rel]
            td = _type_dir(meta["type"])
            name = _ascii_seg(Path(rel).stem, rel)
            cid = (td, name)
            n = 2
            while cid in used:
                cid = (td, f"{name}-{n}"); n += 1
            used.add(cid)
            refs.append(ConceptRef(id=cid, type=meta["type"], resource=f"corpus://{rel}",
                                   hint={"rel": rel}))
        self._refs = refs
        return refs

    def read_concept(self, ref: ConceptRef) -> dict:
        rel = ref.hint["rel"]
        text = self.corpus.read(rel) or ""
        body = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL).strip() or text.strip()
        # Fidelity: source frontmatter metadata (security/effective_from/status/owner etc.) is not lost
        # when stripped -- it is merged verbatim into the OKF frontmatter's source_meta (the §4.1 extension model allows extra keys)
        source_meta = {}
        m = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.DOTALL)
        if m:
            try:
                import yaml as _yaml
                fm = _yaml.safe_load(m.group(1)) or {}
                if isinstance(fm, dict):
                    source_meta = {str(k): v for k, v in fm.items()
                                   if isinstance(v, (str, int, float, bool)) and str(v).strip()}
            except Exception:
                pass
        return {"title": _doc_title(rel, text), "body": body,
                "source_meta": source_meta, **self.metas[rel]}


def _synthesize_via_relay(rel_path: str, children: list, *, model: str) -> str:
    """The directory describer injected into the official regenerate_indexes: goes through this repo's relay
    (replacing the default Gemini); subdirectories can hold thousands of concepts, so children is truncated to 60 to avoid prompt explosion."""
    if not children:
        return ""
    sample = children[:60]
    contents = "\n".join(f"- {t}: {d}" if d else f"- {t}" for t, d in sample)
    more = f"\n(and {len(children) - len(sample)} more entries)" if len(children) > len(sample) else ""
    try:
        return llm.chat(
            "You summarize a directory in an Open Knowledge Format bundle in ONE sentence (max ~25 words). "
            "Be concrete and factual. Output the sentence only.",
            f"Directory: {rel_path}\nContents:\n{contents}{more}",
            temperature=0.2, max_tokens=80).strip()
    except Exception:
        titles = ", ".join(t for t, _ in sample if t)[:200]
        return f"Contains {len(children)} entries: {titles}."


def load_manifest(bundle: Path) -> dict:
    """The bundle's okf_manifest.json (compile product; contains the src->cid mapping)."""
    for cand in (bundle.parent / "okf_manifest.json", bundle / "okf_manifest.json"):
        if cand.exists():
            return json.loads(cand.read_text(encoding="utf-8"))
    return {}


@register("okf")
class OKFBaseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None,
                 bundle_dir=None, index_dir=None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self.bundle = Path(bundle_dir or config.OKF_BUNDLE_DIR)
        self.index_dir = Path(index_dir) if index_dir else (
            config.OKF_INDEX_DIR if Path(bundle_dir or config.OKF_BUNDLE_DIR) == config.OKF_BUNDLE_DIR
            else Path(str(self.bundle) + "_vindex"))
        self._bundle_corpus: Corpus | None = None
        self._vindex: VectorIndex | None = None

    # ---------------- offline: single complete compile pipeline ----------------
    def prepare(self, log=print) -> None:
        t0 = time.time()
        # Directory-level exclusive lock: prevent the same okf directory from being written by two build
        # processes concurrently (driver child process + manual parallel build share it; flock auto-releases
        # on process exit). After acquiring the lock, re-check: if a concurrent process already built it, skip (idempotent).
        import fcntl
        self.bundle.parent.mkdir(parents=True, exist_ok=True)
        self._build_lockf = open(self.bundle.parent / ".build.lock", "w")
        fcntl.flock(self._build_lockf, fcntl.LOCK_EX)
        _omf = self.bundle.parent / "okf_manifest.json"
        if _omf.exists():
            try:
                _gm = json.loads(_omf.read_text(encoding="utf-8"))
                if _gm.get("build_model") == llm.config.CHAT_MODEL and (_gm.get("src_to_cid") or {}):
                    log(f"[okf.build] {self.bundle.parent} already built by a concurrent process (build_model={_gm.get('build_model')}), skipping rebuild")
                    return
            except Exception:
                pass
        docs_src = self.corpus.docs()
        jobs = []
        for p in docs_src:
            rel = self.corpus.rel(p)
            text = p.read_text(encoding="utf-8", errors="replace")
            jobs.append((rel, _doc_title(rel, text), text))
        log(f"[okf.build] enriching {len(docs_src)} docs (full, no incremental path)...")
        fresh = llm.pmap(_enrich_one, jobs)
        metas = {rel: m for (rel, _t, _x), m in zip(jobs, fresh)}

        source = CorpusSource(self.corpus, metas)
        refs = source.list_concepts()
        docs = []
        for ref in refs:
            c = source.read_concept(ref)
            docs.append({"cid": "/".join(ref.id), "ref": ref, **c, "src": ref.hint["rel"]})
        self._link(docs)

        if self.bundle.exists():
            import shutil; shutil.rmtree(self.bundle)
        by = {d["cid"]: d for d in docs}
        for d in docs:
            body = f"# Overview\n{d['body']}\n"
            if d["links"]:
                body += "\n## Related\n" + "\n".join(
                    f"- [{by[t]['title']}](/{t}.md) - {by[t]['description']}" for t in d["links"]) + "\n"
            if d["cited_by"]:
                body += "\n## Cited by\n" + "\n".join(
                    f"- [{by[s]['title']}](/{s}.md)" for s in d["cited_by"][:_MAX_LINKS]) + "\n"
            body += f"\n# Citations\n1. [{d['src']}](corpus://{d['src']})\n"
            fm = {"type": d["type"], "title": d["title"], "description": d["description"] or d["title"],
                  "timestamp": _COMPILE_TS, "resource": f"corpus://{d['src']}", "tags": d["tags"]}
            if d.get("source_meta"):
                fm["source_meta"] = d["source_meta"]
            doc = OKFDocument(frontmatter=fm, body=body)
            doc.validate()                                    # official required-key validation
            fp = concept_id_to_path(self.bundle, d["ref"].id)  # official path rule (ASCII segments)
            fp.parent.mkdir(parents=True, exist_ok=True)
            fp.write_text(doc.serialize(), encoding="utf-8")

        # official index tree generation (directory descriptions -> injected relay synthesize)
        written = regenerate_indexes(self.bundle, model="relay", synthesize=_synthesize_via_relay)
        # §11: the root index declares okf_version (the official reference bundle omits it; the SPEC recommends it, we do)
        ri = self.bundle / "index.md"
        if ri.exists() and not ri.read_text(encoding="utf-8").startswith("---"):
            ri.write_text('---\nokf_version: "0.1"\n---\n\n' + ri.read_text(encoding="utf-8"),
                          encoding="utf-8")

        # bundle vector index (same pipeline as rag; the data plane of the search tool)
        from .rag import RagBaseline
        RagBaseline(corpus=Corpus(root=self.bundle, group=self.corpus.group),
                    index_dir=self.index_dir).prepare(log=log)

        # manifest: src->cid mapping + build identity (recheck P1-1: record build_model/corpus_sha/embed for the reuse-gate check)
        import hashlib as _hl
        _cmf = Path(self.corpus.root) / "_manifest.json"
        (self.bundle.parent / "okf_manifest.json").write_text(
            json.dumps({"okf_version": "0.1", "compiler": "official@d44368c15e38",
                        "docs": len(docs), "vindex": str(self.index_dir),
                        "build_model": llm.config.CHAT_MODEL, "embedding_model": config.RAG_EMBED_MODEL,
                        "corpus_manifest_sha256": (_hl.sha256(_cmf.read_bytes()).hexdigest()
                                                   if _cmf.exists() else None),
                        "src_to_cid": {d["src"]: d["cid"] for d in docs}},
                       ensure_ascii=False), encoding="utf-8")
        nlinks = sum(len(d["links"]) for d in docs)
        log(f"[okf.build] DONE {len(docs)} concepts, {nlinks} links, {len(written)} indexes, "
            f"{time.time()-t0:.0f}s -> {self.bundle}")

    def _link(self, docs):
        pats = [(re.compile(r"(?<![0-9A-Za-z])" + re.escape(d["title"].strip()) + r"(?![0-9A-Za-z])"), d)
                for d in docs if len(d["title"].strip()) >= 3]
        cited = defaultdict(list)
        for d in docs:
            out = []
            for pat, tgt in pats:
                if tgt["cid"] == d["cid"]:
                    continue
                if pat.search(d["body"]):
                    out.append(tgt["cid"])
                    if len(out) >= _MAX_LINKS:
                        break
            d["links"] = out
            for t in out:
                cited[t].append(d["cid"])
        for d in docs:
            d["cited_by"] = cited.get(d["cid"], [])

    # ---------------- online: navigation-toolset loop (exploit the format bonus fully) ----------------
    def _bc(self) -> Corpus:
        if self._bundle_corpus is None:
            self._bundle_corpus = Corpus(root=self.bundle, group=self.corpus.group)
        return self._bundle_corpus

    def _vx(self) -> VectorIndex:
        if self._vindex is None:
            self._vindex = VectorIndex(self.index_dir, config.SEARCH_TOP_K)
        return self._vindex

    def _tools(self) -> list:
        bc = self._bc()
        return [get_index_tool(bc, hierarchical=True), search_tool(self._vx(), bc.group),
                get_page_tool(bc), follow_links_tool(bc)]

    def answer(self, question: dict) -> AnswerResult:
        r = run_loop_answer(self.model, OKF_SYSTEM_PROMPT.format(groups=self.corpus.group),
                            self._tools(), question["question"], "okf")
        return r
