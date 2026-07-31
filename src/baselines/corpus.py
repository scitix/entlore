"""Corpus reading abstraction.

When a formal release has a ``_manifest.json``, reading is strictly delegated to ``CorpusIndex``;
a limited compatibility mode is retained for historical benchmark bundles that lack a release manifest.
"""
from __future__ import annotations
from pathlib import Path

from . import config
from ..corpus_index import CorpusIndex

_SKIP = {"index.md", "SCHEMA.md", "log.md", "_ds_manifest.json"}


class Corpus:
    def __init__(self, root: Path | str | None = None, group: str | None = None,
                 *, require_manifest: bool = False, verify_hashes: bool = False):
        self.root = Path(root or config.CORPUS_DIR)
        self.group = group or config.GROUP
        manifest = self.root / "_manifest.json"
        if require_manifest and not manifest.is_file():
            raise FileNotFoundError(f"released corpus manifest missing: {manifest}")
        self.index = (CorpusIndex(self.root, verify_hashes=verify_hashes)
                      if manifest.is_file() else None)

    def docs(self) -> list[Path]:
        """All retrievable documents (relative paths), excluding index/SCHEMA/log."""
        if self.index is not None:
            return self.index.paths()
        return [p for p in sorted(self.root.rglob("*.md"))
                if p.name not in _SKIP
                and not any(part.startswith("_") for part in p.relative_to(self.root).parts)]

    def rel(self, p: Path) -> str:
        return p.relative_to(self.root).as_posix()

    def read(self, relpath: str) -> str | None:
        if self.index is not None:
            value = str(relpath).split("#", 1)[0]
            try:
                if value in self.index:
                    return self.index.read(value)
                return self.index.read_path(Path(value).as_posix())
            except ValueError:
                return None
        p = self.root / relpath
        if not p.is_file() and not relpath.endswith(".md"):
            p = self.root / f"{relpath}.md"
        if not p.is_file():          # missing or a directory (the agent may request a directory path) -> treat as not found, don't crash
            return None
        return p.read_text(encoding="utf-8", errors="replace")

    def fuzzy(self, relpath: str, limit: int = 5) -> list[str]:
        stem = Path(relpath).stem
        if not stem:
            return []
        if self.index is not None:
            return [self.index.relative_path(document_id)
                    for document_id in self.index.ids() if stem in document_id][:limit]
        # Substring match over a fixed, safe glob — never interpolate agent-supplied text into the
        # glob pattern (a stem containing `*`/`**` made `rglob(f"*{stem}*")` raise "Invalid pattern").
        return [self.rel(c) for c in sorted(self.root.rglob("*.md")) if stem in c.name][:limit]

    def index_md(self) -> str | None:
        p = self.root / "index.md"
        return p.read_text(encoding="utf-8", errors="replace") if p.exists() else None

    def exists(self) -> bool:
        return self.root.exists() and bool(self.docs())

    def released_ids(self) -> set[str]:
        if self.index is not None:
            return set(self.index.released_ids)
        return {path.stem for path in self.docs()}
