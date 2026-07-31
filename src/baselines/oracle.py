"""Oracle upper-bound baseline: **physically removes retrieval from the system** to measure "the synthesis ceiling given perfect evidence".

Definition (2026-07-16 P5 purification):
- Evidence resolution is a **single-level pointer**: the bank's required_facts / evidence_policy.canonical point to real corpus
  documents, hard-asserted to fully resolve at startup -- if resolution fails, refuse to run; no multi-level ambiguity from grounding scan / vector fallback
  (pointer health is guaranteed on the question-bank side by scripts/repair_evidence_pointers.py);
- **Abstention questions and oracle_excluded questions are not in the oracle-testable set**: oracle measures "synthesis given the right evidence",
  an abstention question has no "right evidence", forcing it in would create leakage or fake credit (the runner filters them via filter_questions);
- The loop-type oracle **has no retrieval tool** (get_page + submit_answer), the phrasing asserts the pages are complete,
  and must contain no wording that induces autonomous retrieval; budget 40 (measured ~31 steps reading all 16 pages + submit).

Three modes:
- oracle_rag         : gold evidence documents' full text directly as context -> single-turn generation (perfect-recall ceiling)
- oracle_agentic_rag : gold document paths enter the prompt, the tool loop reads them page by page and synthesizes (perfect-navigation ceiling)
- oracle_okf         : gold source documents mapped via okf_manifest's src->cid to bundle concept paths,
                       the loop runs on the bundle (perfect index-chain ceiling)
"""
from __future__ import annotations
import json
import time
from pathlib import Path

from . import config
from .. import evidence_anchors
from ._gen import generate, compute_cost
from .base import AnswerResult, Baseline, register
from .corpus import Corpus
from .loop import run_loop_answer
from .rag import RAG_SYSTEM_PROMPT
from .toolkits import get_page_tool

_PREAMBLE = "[System retrieval results] The following are all the pages relevant to this question; please read each one and then answer directly."

ORACLE_LOOP_PROMPT = """You are an enterprise knowledge-base QA assistant. The system has already completed retrieval; the pages listed below the question are all the pages relevant to this question.

Tools:
- get_page: read the full text of a page by its exact path
- submit_answer: submit the final answer

Please read each listed page, then answer based on what you read and submit.

## Answer requirements
- **Use only information you have read**; do not fabricate or speculate about facts not present in the pages
- If the page content is insufficient to answer, state clearly what is missing

## Citation format (must follow)
After each key factual assertion, cite its source: `[source: group/path]`; the path must be a page you actually read.

Available knowledge-base groups: {groups}"""


class OracleUnresolvable(RuntimeError):
    """Oracle purity assertion failed: a testable question's evidence pointers did not fully resolve (fix the bank first, then run oracle)."""


class GoldResolver:
    """Question id -> gold evidence document (corpus relative path). Single-level pointer, no fallback."""

    def __init__(self, corpus: Corpus, bank_path: Path | None = None, cap: int | None = None):
        self.corpus = corpus
        self.cap = cap or config.ORACLE_DOC_CAP
        bp = bank_path or config.bank_path()
        self.bank = {r["id"]: r for r in map(json.loads, open(bp, encoding="utf-8"))}
        self._stems = ({document_id: corpus.index.relative_path(document_id)
                        for document_id in corpus.index.ids()}
                       if corpus.index is not None else
                       {p.stem: self.corpus.rel(p) for p in corpus.docs()})

    def eligibility(self, qid: str) -> str:
        """'ok' | exclusion reason. Excluded questions are not in the oracle-testable set."""
        gp = self.bank.get(qid)
        if gp is None:
            return "not_in_bank"
        if gp.get("answer_status") not in (None, "answerable"):
            return "unanswerable"
        if (gp.get("_provenance") or {}).get("oracle_excluded"):
            return "oracle_excluded"
        return "ok"

    def pointers(self, qid: str) -> list[str]:
        gp = self.bank[qid]
        evs = set()
        for f in gp.get("required_facts", []):
            for e in f.get("required_evidence", []):
                evs.add(str(e).split("#")[0])
        for vs in (gp.get("evidence_policy", {}).get("canonical") or {}).values():
            for e in vs:
                evs.add(str(e).split("#")[0])
        return sorted(evs)

    def docs_for(self, qid: str) -> list[str]:
        """gold document relative paths; a testable question that fails to resolve raises OracleUnresolvable (no fallback)."""
        pointers = self.pointers(qid)
        missing = [document_id for document_id in pointers if document_id not in self._stems]
        if missing or not pointers:
            raise OracleUnresolvable(
                f"question {qid} evidence pointers did not all resolve to the public manifest: {missing or pointers}")
        rels = [self._stems[document_id] for document_id in pointers]
        return rels          # do not cap at 16 docs: oracle = perfect-recall ceiling, must give all gold documents (B review #6);
                             # context size is bounded by oracle_rag's ORACLE_MAX_CHARS / the loop-type's page-by-page read budget

    def canonical_evidence(self, qid: str) -> list[tuple[str, str, list]]:
        """Used by lc_oracle: an ordered deduplicated list of (rel, anchor, span_candidates) from evidence_policy.canonical.
        anchor is preserved (`#p<N>` paragraph-offset contract); span_candidates = this fact's fact_preview + provenance
        canonical_span_text, for locating the paragraph online when the pointer is not stamped. Empty canonical falls back to required_evidence (whole doc)."""
        gp = self.bank[qid]
        canon = (gp.get("evidence_policy", {}) or {}).get("canonical") or {}
        fid2prev = {rf.get("fact_id"): rf.get("fact_preview", "")
                    for rf in gp.get("required_facts", [])}
        prov_spans = (gp.get("_provenance") or {}).get("canonical_span_text") or []
        if isinstance(prov_spans, str):
            prov_spans = [prov_spans]
        out: list[tuple[str, str, list]] = []
        for fid, vs in canon.items():
            cands = [t for t in ([fid2prev.get(fid)] + list(prov_spans)) if t]
            for e in vs:
                s = str(e)
                stem, anchor = (s.split("#", 1) + [""])[:2]
                if stem not in self._stems:          # fail-closed: do not silently skip a missing evidence stem (B review #6)
                    raise OracleUnresolvable(
                        f"question {qid} canonical evidence document not in corpus: {stem}")
                if self.corpus.index is not None:
                    try:
                        self.corpus.index.resolve_pointer(s, require_paragraph=True)
                    except ValueError as exc:
                        raise OracleUnresolvable(
                            f"question {qid} canonical evidence cannot be resolved: {s}") from exc
                out.append((self._stems[stem], anchor, cands))
        if not out:
            out = [(r, "", []) for r in self.docs_for(qid)]
        seen, ded = set(), []
        for rel, a, cands in out:
            if (rel, a) not in seen:
                seen.add((rel, a)); ded.append((rel, a, cands))
        return ded          # lc_oracle sets no 16-doc cap (trimmed by LC_ORACLE_MAX_CHARS budget, B review #6)

    def filter_questions(self, questions: list[dict]) -> tuple[list[dict], dict]:
        """Oracle-testable-set filter + purity hard assertion (full validation at startup, refuse to run on failure)."""
        kept, skipped, dead = [], {}, []
        for q in questions:
            el = self.eligibility(q["id"])
            if el != "ok":
                skipped[q["id"]] = el
                continue
            try:
                self.docs_for(q["id"])
            except OracleUnresolvable:
                dead.append(q["id"])
                continue
            kept.append(q)
        if dead:
            raise OracleUnresolvable(
                f"{len(dead)} questions have unresolved evidence pointers (examples {dead[:5]}); "
                f"fix the bank first or add an oracle_excluded marker")
        return kept, skipped


class _OracleBase(Baseline):
    """Shared pieces of the three oracles: resolver, phrasing, loop toolset (only get_page + submit), budget."""

    def __init__(self, corpus: Corpus | None = None, model: str | None = None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self._resolver: GoldResolver | None = None

    def resolver(self) -> GoldResolver:
        if self._resolver is None:
            self._resolver = GoldResolver(self.corpus)
        return self._resolver

    def filter_questions(self, questions: list[dict]) -> tuple[list[dict], dict]:
        return self.resolver().filter_questions(questions)

    def _guard(self, qid: str) -> None:
        el = self.resolver().eligibility(qid)
        if el != "ok":
            raise OracleUnresolvable(f"question {qid} not in the oracle-testable set ({el}); the runner should filter_questions first")

    @staticmethod
    def _augment(question_text: str, paths: list[str]) -> str:
        lst = "\n".join(f"- {p}" for p in paths)
        return f"{question_text}\n\n{_PREAMBLE}\n{lst}"

    def _loop(self, page_corpus: Corpus, question_text: str, approach: str) -> AnswerResult:
        # oracle uses **untruncated** get_page: it must give the complete gold page to the model, otherwise it is not a "perfect-evidence ceiling" (audit P1-2)
        return run_loop_answer(self.model, ORACLE_LOOP_PROMPT.format(groups=page_corpus.group),
                               [get_page_tool(page_corpus, cap=None)], question_text, approach,
                               max_iter=config.ORACLE_MAX_ITER)


@register("oracle_rag")
class OracleRagBaseline(_OracleBase):
    """Perfect-recall ceiling: gold evidence documents' **full text** directly as context, single-turn generation."""

    def answer(self, question: dict) -> AnswerResult:
        t0 = time.time()
        self._guard(question["id"])
        rels = self.resolver().docs_for(question["id"])
        parts, total, used = [], 0, []
        for rel in rels:
            txt = self.corpus.read(rel) or ""
            block = f"[source: {rel}]\n{txt}"
            if total + len(block) > config.ORACLE_MAX_CHARS:
                break
            parts.append(block); total += len(block); used.append(rel)
        user = (f"## Reference materials (full documents):\n\n" + "\n\n---\n\n".join(parts)
                + f"\n\n## Question:\n{question['question']}\n\nPlease answer the question based on the above materials.")
        text, usage = generate(RAG_SYSTEM_PROMPT, user, model=self.model,
                               max_tokens=config.GEN_MAX_TOKENS)
        r = AnswerResult(text, "oracle_rag", tokens=usage, cost_usd=compute_cost(usage, self.model),
                         wall_time_s=time.time() - t0, context_chars=total)
        # trace records the **actually injected** docs (not the full rels); documents skipped over budget are not falsely reported as prefetched
        r.trace = [{"tool": "oracle_prefetch", "docs": used,
                    "gold_docs_total": len(rels), "truncated": len(used) < len(rels)}]
        return r


@register("oracle_agentic_rag")
class OracleAgenticRagBaseline(_OracleBase):
    """Perfect-navigation ceiling: gold document paths enter the prompt, the loop reads them page by page and synthesizes (no retrieval tool)."""

    def answer(self, question: dict) -> AnswerResult:
        self._guard(question["id"])
        rels = self.resolver().docs_for(question["id"])
        r = self._loop(self.corpus, self._augment(question["question"], rels), "oracle_agentic_rag")
        if r.trace is not None:
            r.trace.insert(0, {"tool": "oracle_prefetch", "docs": rels})
        return r


@register("oracle_okf")
class OracleOKFBaseline(_OracleBase):
    """Perfect index-chain ceiling: gold source documents mapped via manifest src->cid to bundle concept paths, the loop runs on the bundle."""

    def __init__(self, corpus: Corpus | None = None, model: str | None = None, bundle_dir=None):
        super().__init__(corpus=corpus, model=model)
        self.bundle = Path(bundle_dir or config.OKF_BUNDLE_DIR)
        self._map: dict | None = None
        self._bc: Corpus | None = None

    def _src2cid(self) -> dict:
        if self._map is None:
            from .okf import load_manifest
            m = load_manifest(self.bundle)
            self._map = m.get("src_to_cid") or {}
            if not self._map:
                raise OracleUnresolvable(
                    f"okf_manifest.json missing the src_to_cid mapping ({self.bundle}); recompile the bundle first")
        return self._map

    def answer(self, question: dict) -> AnswerResult:
        self._guard(question["id"])
        rels = self.resolver().docs_for(question["id"])
        src2cid = self._src2cid()
        miss = [r for r in rels if r not in src2cid]
        if miss:                                        # fail-closed: refuse if any gold document lacks a cid mapping (do not silently drop)
            raise OracleUnresolvable(
                f"question {question['id']}'s gold documents lack a src_to_cid mapping in okf_manifest: {miss[:5]}")
        cpaths = [src2cid[r] + ".md" for r in rels]
        if not cpaths:
            raise OracleUnresolvable(f"question {question['id']} has no gold documents")
        if self._bc is None:
            self._bc = Corpus(root=self.bundle, group=self.corpus.group)
        r = self._loop(self._bc, self._augment(question["question"], cpaths), "oracle_okf")
        if r.trace is not None:
            r.trace.insert(0, {"tool": "oracle_prefetch", "docs": cpaths})
        return r


@register("lc_oracle")
class LCOracleBaseline(_OracleBase):
    """Long-context gold-evidence-passage ceiling: resolve canonical evidence into **exact paragraphs** (located by anchor),
    concatenate into one long context, and answer in a **single turn** (no tools, no retrieval). Measures "the pure understanding/synthesis ceiling given the right exact evidence passages".

    Distinct from oracle_rag: (1) uses evidence_policy.canonical minimal evidence set (not the broad required set);
    (2) **paragraph-level** (`#p<N>` paragraph-offset contract, see src/evidence_anchors.py) rather than whole documents;
    (3) no 200k/16-doc cap, the long window fits everything.

    anchor contract: `#p<N>[,<M>]` -> the N-th paragraph of the body (after stripping frontmatter) (the exact evidence passage); the offset is computed at generation time from the
    fact span text (gold._ev -> evidence_anchors.make_pointer). `#fact:`/letter-code/no anchor -> whole document;
    in that case, if the bank carries the fact's span text (fact_preview / provenance), locate the paragraph online as precisely as possible (fallback).
    genre/report/event operators have no span text, so their canonical stays whole-document (see docs/baselines.md)."""

    def _resolve_passage(self, rel: str, anchor: str, span_candidates=()) -> tuple[str, str, str]:
        """(rel, anchor, span candidates) -> (rel, label, passage_text). `#p<N>` takes the exact paragraph;
        otherwise use span candidates to locate online; if neither works -> whole document."""
        txt = self.corpus.read(rel) or ""
        body = evidence_anchors.strip_frontmatter(txt)
        kind, idxs = evidence_anchors.parse_anchor(anchor)
        paras = evidence_anchors.split_paragraphs(body)
        if kind == "para":
            picked = [(i, paras[i]) for i in idxs if 0 <= i < len(paras)]
            if picked:
                return (rel, "¶" + ",".join(str(i) for i, _ in picked),
                        "\n\n".join(p for _, p in picked))
        for span in span_candidates:                       # fallback: not stamped with #p but has a span -> locate online
            n = evidence_anchors.locate_paragraph(body, span)
            if n is not None and 0 <= n < len(paras):
                return rel, f"¶{n}", paras[n]
        return rel, "", txt                                # whole document

    def answer(self, question: dict) -> AnswerResult:
        t0 = time.time()
        self._guard(question["id"])
        ev = self.resolver().canonical_evidence(question["id"])
        parts, total, used = [], 0, []
        for rel, anchor, cands in ev:
            _, hp, passage = self._resolve_passage(rel, anchor, cands)
            tag = f"[evidence: {rel}" + (f" › {hp}" if hp else "") + "]"
            block = f"{tag}\n{passage}"
            if total + len(block) > config.LC_ORACLE_MAX_CHARS:
                break
            parts.append(block); total += len(block); used.append(tag)
        user = ("## Exact evidence passages (the system has completed retrieval; the following are all the evidence needed to answer this question):\n\n"
                + "\n\n---\n\n".join(parts)
                + f"\n\n## Question:\n{question['question']}\n\nAnswer based solely on the evidence passages above.")
        text, usage = generate(RAG_SYSTEM_PROMPT, user, model=self.model,
                               max_tokens=config.GEN_MAX_TOKENS)
        r = AnswerResult(text, "lc_oracle", tokens=usage, cost_usd=compute_cost(usage, self.model),
                         wall_time_s=time.time() - t0, context_chars=total)
        r.trace = [{"tool": "lc_oracle_prefetch", "passages": used}]
        return r
