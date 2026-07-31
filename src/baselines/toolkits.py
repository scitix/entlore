"""Shared tool constructors: each pipeline **composes** its own toolset from these building blocks (no runtime switches).

- search_tool(vindex)        semantic retrieval (vector; the benchmark's sole retrieval form)
- get_page_tool(corpus)      read a page's full text by exact path (15k truncation + fuzzy suggestions)
- get_index_tool(corpus)     read directory pages (supports subdirectory index.md -- an OKF bundle is a hierarchical index tree)
- follow_links_tool(corpus)  read a page's Related / Cited by neighbors (OKF format bonus)
"""
from __future__ import annotations
import re

from . import config
from .corpus import Corpus
from .loop import Tool

_PAGE_CAP = 15000


def search_tool(vindex, group: str, top_k: int | None = None) -> Tool:
    k = top_k or config.SEARCH_TOP_K

    def fn(args: dict) -> dict:
        query = args.get("query", "")
        if not query:
            return {"content": "[ERROR] query is required", "next_action": "Provide a search query."}
        hits = vindex.retrieve(query, top_k=k)
        if not hits:
            return {"content": f"No results for '{query}'.",
                    "next_action": "Try rephrasing the query."}
        lines = [f"Found {len(hits)} results for '{query}':"]
        for r in hits:
            lines.append(f"\n[{group}] {r['source_file']} (score: {r['_score']:.3f})")
            if r.get("heading_path"):
                lines.append(f"  Section: {r['heading_path']}")
            lines.append(f"  Snippet: {r['text'][:500]}")
        return {"content": "\n".join(lines),
                "next_action": "Read promising pages in full via get_page, or submit_answer when ready."}

    return Tool("search", "Semantic retrieval of relevant pages (returns paths and snippets).",
                {"query": {"type": "string", "description": "Search query (1-200 chars)"}},
                ["query"], fn)


def get_page_tool(corpus: Corpus, cap: "int | None" = _PAGE_CAP) -> Tool:
    # cap=None: no truncation (oracle must give the complete gold page; audit P1-2 -- the gold evidence
    # spans of 31 oracle_agentic / 38 oracle_okf questions lie beyond char 15000, so truncation would
    # make the "perfect-evidence ceiling" a misnomer).
    def fn(args: dict) -> dict:
        path = args.get("path", "")
        if not path:
            return {"content": "[ERROR] path is required", "next_action": "Provide the page path."}
        content = corpus.read(path)
        if content is None:
            sug = corpus.fuzzy(path)
            if sug:
                return {"content": f"[ERROR] Page not found: {path}\nDid you mean: {', '.join(sug)}",
                        "next_action": f"Try: {sug[0]}"}
            return {"content": f"[ERROR] Page not found: {path}",
                    "next_action": "Use search or get_index."}
        if cap is not None and len(content) > cap:
            content = content[:cap] + f"\n\n... [truncated, total: {len(content)} chars]"
        return {"content": content,
                "next_action": "Use this page to answer; search for more, or submit_answer when ready."}

    return Tool("get_page", "Read the full content of a page by its exact relative path.",
                {"path": {"type": "string", "description": "Page relative path (e.g. dir/doc.md)"}},
                ["path"], fn)


def get_index_tool(corpus: Corpus, hierarchical: bool = False) -> Tool:
    """Directory-page reader. When hierarchical=True (OKF), supports reading index.md of any subdirectory."""
    def fn(args: dict) -> dict:
        sub = (args.get("path") or "").strip().strip("/") if hierarchical else ""
        rel = f"{sub}/index.md" if sub else "index.md"
        idx = corpus.read(rel)
        if idx is None:
            return {"content": f"[ERROR] No index at '{rel}'.",
                    "next_action": "Use search to find content directly."}
        if len(idx) > 10000:
            idx = idx[:10000] + "\n... [truncated]"
        return {"content": idx,
                "next_action": "Choose relevant entries, then get_page (or get_index of a subdirectory)."}

    params = {"path": {"type": "string",
                       "description": "Subdirectory path (empty = root). The index tree is layered by concept type."}} \
        if hierarchical else {}
    return Tool("get_index", "Read a knowledge-base directory page (index) to understand the overall structure.", params, [], fn)


_LINK_LINE = re.compile(r"^- \[([^\]]+)\]\((/[^)]+?)\.md\)(?: - (.*))?$")


def follow_links_tool(corpus: Corpus) -> Tool:
    """OKF-specific: parse a concept's Related / Cited by blocks and return a neighbor list (makes the format bonus explicit)."""
    def fn(args: dict) -> dict:
        path = args.get("path", "")
        content = corpus.read(path) if path else None
        if content is None:
            return {"content": f"[ERROR] Page not found: {path}",
                    "next_action": "Provide a concept path that you have seen in index/search results."}
        out, section = [], None
        for line in content.splitlines():
            if line.startswith("## Related"):
                section = "Related"; out.append("## Related"); continue
            if line.startswith("## Cited by"):
                section = "Cited by"; out.append("## Cited by"); continue
            if line.startswith("#"):
                section = None; continue
            if section:
                m = _LINK_LINE.match(line.strip())
                if m:
                    title, target, desc = m.group(1), m.group(2).lstrip("/") + ".md", m.group(3) or ""
                    out.append(f"- {target} — {title}" + (f": {desc}" if desc else ""))
        if len(out) <= 1:
            return {"content": f"No Related/Cited-by links on {path}.",
                    "next_action": "Use search or get_index to find other pages."}
        return {"content": f"Links from {path}:\n" + "\n".join(out),
                "next_action": "get_page any neighbor that looks relevant."}

    return Tool("follow_links",
                "List a concept page's Related / Cited by neighbors (with paths and descriptions), for navigating along the knowledge graph.",
                {"path": {"type": "string", "description": "Concept page relative path"}},
                ["path"], fn)
