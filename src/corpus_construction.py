"""Corpus frontmatter helpers used by the retrieval baselines.

Released, evaluation-only subset: the released corpus documents carry a leading YAML
frontmatter block (document_type / report_date / authors / department, etc.). The RAG/BM25
baselines split it off from the body and optionally fold selected fields into the retrieval
text. The corpus-construction/materialization side of the original project is not part of
this release.
"""
from __future__ import annotations
import re

import yaml

# Frontmatter fields the baselines may render into retrieval/context text.
REPORT_METADATA_KEYS = ("document_type", "report_date", "report_time", "authors", "department")

_FRONTMATTER = re.compile(r"^﻿?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)", re.DOTALL)


def split_frontmatter(text: str) -> tuple[dict, str]:
    """Return ``(metadata, body)`` for a leading YAML frontmatter block.

    Malformed or non-mapping YAML is treated as no frontmatter so callers never
    silently discard user-visible content.
    """
    value = text or ""
    match = _FRONTMATTER.match(value)
    if not match:
        return {}, value
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}, value
    if not isinstance(metadata, dict):
        return {}, value
    return {str(key): val for key, val in metadata.items()}, value[match.end():].lstrip("\r\n")
