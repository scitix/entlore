"""Evidence-pointer anchor contract (single source of truth) -- `#p<N>` paragraph offsets.

A pointer looks like `stem` or `stem#<anchor>`:
- `p<N>`        -> the Nth paragraph (0-indexed) of the document body (after stripping YAML frontmatter), split on blank lines; multiple paragraphs `p<N>,<M>`.
                  This is the **exact evidence-paragraph** contract that lc_oracle locates against; the offset is computed from the fact-span text at generation time.
- `fact:<fid>` / `repair` / letter family codes (t/o/m/p/r/w/d/ev/okr) / no anchor -> **whole document** (backward compat, imprecise).

**Emission and parsing must share this module's split_paragraphs/strip_frontmatter**, otherwise paragraph indices misalign.
The evaluator still does doc-level grounding via `split("#")[0]` (the anchor is transparent to it); this contract does not change the scoring rubric.
"""
from __future__ import annotations
import re

_FM = re.compile(r"^﻿?---\s*\n.*?\n---\s*\n?", re.DOTALL)
_PARA_SPLIT = re.compile(r"\n[ \t]*\n")
_WS = re.compile(r"\s+")
_TOK = re.compile(r"[A-Za-z0-9]+|[一-鿿]")


def strip_frontmatter(text: str) -> str:
    """Strip the YAML frontmatter (`---\\n...\\n---`) at the start of the document. Returns unchanged if none."""
    return _FM.sub("", text or "", count=1).lstrip("\n")


def split_paragraphs(body: str) -> list[str]:
    """Split the body into paragraphs on blank lines (non-empty blocks, stable order/index). Shared by emission and parsing to keep indices consistent."""
    return [p.strip() for p in _PARA_SPLIT.split(body or "") if p.strip()]


def _norm(s: str) -> str:
    return _WS.sub(" ", (s or "").strip())


def locate_paragraph(body: str, span_text: str) -> int | None:
    """Which paragraph (0-indexed) the span text falls in. Three-level fallback: exact substring -> whitespace-normalized substring -> highest token overlap.
    body must already be strip_frontmatter'd. Returns None if it cannot be located."""
    span = (span_text or "").strip()
    if not span:
        return None
    paras = split_paragraphs(body)
    if not paras:
        return None
    for i, p in enumerate(paras):                       # 1) exact substring
        if span in p:
            return i
    nspan = _norm(span)
    if nspan:
        for i, p in enumerate(paras):                   # 2) substring after whitespace normalization
            if nspan in _norm(p):
                return i
    span_toks = set(_TOK.findall(span.lower()))          # 3) token overlap (max Jaccard-ish)
    if span_toks:
        best, best_ov = None, 0.0
        for i, p in enumerate(paras):
            pt = set(_TOK.findall(p.lower()))
            if not pt:
                continue
            ov = len(span_toks & pt) / len(span_toks)
            if ov > best_ov:
                best, best_ov = i, ov
        if best is not None and best_ov >= 0.6:
            return best
    return None


def parse_anchor(anchor: str) -> tuple[str, list[int] | None]:
    """anchor -> ("para", [N,...]) | ("whole", None). Only `p<N>[,<M>]` is a paragraph offset; everything else = whole document."""
    a = (anchor or "").strip()
    if a.startswith("p") and len(a) > 1:
        rest = a[1:]
        if re.fullmatch(r"\d+(,\d+)*", rest):
            return "para", [int(x) for x in rest.split(",")]
    return "whole", None


def format_para_anchor(indices: list[int]) -> str:
    return "p" + ",".join(str(i) for i in indices)


def make_pointer(regs, fid: str) -> str:
    """Build the canonical evidence pointer for a fact, with an exact paragraph offset where possible.

    `regs` is duck-typed: `regs.facts[fid].encoded_in` (document stem), `regs.docs[stem].spans[fid]`
    (list of span texts for this fact within the document), `regs.docs[stem].clean_text` (unannotated body).
    The paragraph hit by any span -> `stem#p<N>`; otherwise fall back to `stem#fact:<fid>` (= whole document, backward compat).
    Missing fact -> `?#fact:<fid>` (reuses the old gold._ev fallback)."""
    f = getattr(regs, "facts", {}).get(fid)
    if not f:
        return f"?#fact:{fid}"
    stem = f.encoded_in
    d = getattr(regs, "docs", {}).get(stem)
    if d is not None:
        body = strip_frontmatter(getattr(d, "clean_text", "") or "")
        for span in (getattr(d, "spans", {}) or {}).get(fid, []) or []:
            n = locate_paragraph(body, span)
            if n is not None:
                return f"{stem}#{format_para_anchor([n])}"
    return f"{stem}#fact:{fid}"
