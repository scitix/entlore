"""Manifest-backed access to a released corpus.

The public manifest is the only authority for released documents.  Files under
``_quarantine``/``_stale`` (and any other unlisted file) are intentionally
invisible through this API.  Evidence emitters and resolvers share the
``src.evidence_anchors`` paragraph contract, so ``#p<N>`` cannot drift between
generation and evaluation.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterator

from . import evidence_anchors


class CorpusIndexError(ValueError):
    """The released-corpus identity or evidence contract is invalid."""


@dataclass(frozen=True)
class ResolvedEvidence:
    pointer: str
    document_id: str
    relative_path: str
    anchor: str
    paragraph_indices: tuple[int, ...]
    text: str
    record: dict


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


class CorpusIndex:
    """Validated ``document_id -> path -> content`` index for one release."""

    def __init__(self, root: str | Path, *, verify_hashes: bool = False):
        self.root = Path(root).resolve()
        self.manifest_path = self.root / "_manifest.json"
        if not self.manifest_path.is_file():
            raise CorpusIndexError(f"released corpus manifest missing: {self.manifest_path}")
        try:
            payload = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise CorpusIndexError(f"invalid corpus manifest: {self.manifest_path}") from exc
        if not isinstance(payload, list):
            raise CorpusIndexError("_manifest.json must be an array")

        self._records: dict[str, dict] = {}
        self._paths: dict[str, str] = {}
        self._ids_by_path: dict[str, str] = {}
        stems: set[str] = set()
        for offset, source in enumerate(payload):
            if not isinstance(source, dict):
                raise CorpusIndexError(f"manifest row {offset} is not an object")
            row = dict(source)
            document_id = str(row.get("id") or "").strip()
            relative_path = str(row.get("path") or "").strip()
            if not document_id or "#" in document_id:
                raise CorpusIndexError(f"invalid document id at manifest row {offset}: {document_id!r}")
            if document_id in self._records:
                raise CorpusIndexError(f"duplicate document id: {document_id}")
            safe = self._validate_relative_path(relative_path)
            if safe in self._ids_by_path:
                raise CorpusIndexError(f"duplicate corpus path: {safe}")
            stem = PurePosixPath(safe).stem
            if stem != document_id:
                raise CorpusIndexError(
                    f"manifest id/path stem mismatch: {document_id!r} != {stem!r}")
            if stem in stems:
                raise CorpusIndexError(f"duplicate document stem: {stem}")
            path = self.root / Path(*PurePosixPath(safe).parts)
            if not path.is_file():
                raise CorpusIndexError(f"manifest document missing: {safe}")
            skeleton = path.with_suffix(".skeleton.txt")
            if not skeleton.is_file():
                raise CorpusIndexError(f"manifest skeleton missing: {skeleton.relative_to(self.root)}")
            if verify_hashes:
                expected = row.get("output_sha256")
                if expected and _sha256(path) != expected:
                    raise CorpusIndexError(f"corpus sha256 mismatch: {safe}")
                expected_skeleton = row.get("skeleton_sha256")
                if expected_skeleton and _sha256(skeleton) != expected_skeleton:
                    raise CorpusIndexError(f"skeleton sha256 mismatch: {safe}")
            self._records[document_id] = row
            self._paths[document_id] = safe
            self._ids_by_path[safe] = document_id
            stems.add(stem)

        self.manifest_sha256 = _sha256(self.manifest_path)
        self.build_meta = self._load_json_object(self.root / "_build_meta.json")
        self.build_fingerprint = str(self.build_meta.get("build_fingerprint") or "")
        self._text_cache: dict[str, str] = {}
        self._skeleton_cache: dict[str, str] = {}
        self._paragraph_cache: dict[str, tuple[str, ...]] = {}

    @staticmethod
    def _validate_relative_path(value: str) -> str:
        if not value or not value.isascii():
            raise CorpusIndexError(f"corpus path must be non-empty ASCII: {value!r}")
        pure = PurePosixPath(value)
        if pure.is_absolute() or value != pure.as_posix():
            raise CorpusIndexError(f"corpus path must be normalized and relative: {value!r}")
        if pure.suffix != ".md" or any(part in ("", ".", "..") for part in pure.parts):
            raise CorpusIndexError(f"invalid corpus path: {value!r}")
        if any(part.startswith("_") for part in pure.parts):
            raise CorpusIndexError(f"private/history path cannot be released: {value!r}")
        return pure.as_posix()

    @staticmethod
    def _load_json_object(path: Path) -> dict:
        if not path.is_file():
            return {}
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise CorpusIndexError(f"invalid JSON object: {path}") from exc
        if not isinstance(value, dict):
            raise CorpusIndexError(f"expected JSON object: {path}")
        return value

    def __len__(self) -> int:
        return len(self._records)

    def __contains__(self, document_id: str) -> bool:
        return document_id in self._records

    @property
    def released_ids(self) -> frozenset[str]:
        return frozenset(self._records)

    def ids(self) -> list[str]:
        return list(self._records)

    def records(self) -> Iterator[dict]:
        for document_id in self._records:
            yield dict(self._records[document_id])

    def record(self, document_id: str) -> dict:
        try:
            return dict(self._records[document_id])
        except KeyError as exc:
            raise CorpusIndexError(f"unknown released document id: {document_id}") from exc

    def relative_path(self, document_id: str) -> str:
        try:
            return self._paths[document_id]
        except KeyError as exc:
            raise CorpusIndexError(f"unknown released document id: {document_id}") from exc

    def document_id_for_path(self, relative_path: str) -> str:
        value = PurePosixPath(str(relative_path)).as_posix()
        try:
            return self._ids_by_path[value]
        except KeyError as exc:
            raise CorpusIndexError(f"path is not in released manifest: {relative_path}") from exc

    def path(self, document_id: str) -> Path:
        return self.root / Path(*PurePosixPath(self.relative_path(document_id)).parts)

    def skeleton_path(self, document_id: str) -> Path:
        return self.path(document_id).with_suffix(".skeleton.txt")

    def paths(self) -> list[Path]:
        return [self.path(document_id) for document_id in self._records]

    def read(self, document_id: str) -> str:
        if document_id not in self._text_cache:
            self._text_cache[document_id] = self.path(document_id).read_text(
                encoding="utf-8", errors="replace")
        return self._text_cache[document_id]

    def read_path(self, relative_path: str) -> str:
        return self.read(self.document_id_for_path(relative_path))

    def read_skeleton(self, document_id: str) -> str:
        if document_id not in self._skeleton_cache:
            self._skeleton_cache[document_id] = self.skeleton_path(document_id).read_text(
                encoding="utf-8", errors="replace")
        return self._skeleton_cache[document_id]

    def body(self, document_id: str) -> str:
        return evidence_anchors.strip_frontmatter(self.read(document_id))

    def paragraphs(self, document_id: str) -> tuple[str, ...]:
        if document_id not in self._paragraph_cache:
            self._paragraph_cache[document_id] = tuple(
                evidence_anchors.split_paragraphs(self.body(document_id)))
        return self._paragraph_cache[document_id]

    def make_pointer(self, document_id: str, paragraph_indices: list[int] | tuple[int, ...]) -> str:
        if document_id not in self:
            raise CorpusIndexError(f"unknown released document id: {document_id}")
        indices = tuple(int(index) for index in paragraph_indices)
        paragraphs = self.paragraphs(document_id)
        if not indices or any(index < 0 or index >= len(paragraphs) for index in indices):
            raise CorpusIndexError(f"paragraph index out of range for {document_id}: {indices}")
        return f"{document_id}#{evidence_anchors.format_para_anchor(list(indices))}"

    def resolve_pointer(self, pointer: str, *, require_paragraph: bool = True) -> ResolvedEvidence:
        value = str(pointer or "").strip()
        document_id, separator, anchor = value.partition("#")
        if document_id not in self:
            raise CorpusIndexError(f"evidence pointer targets unreleased document: {value!r}")
        kind, indices = evidence_anchors.parse_anchor(anchor if separator else "")
        if require_paragraph and kind != "para":
            raise CorpusIndexError(f"final evidence pointer must use #p<N>: {value!r}")
        paragraphs = self.paragraphs(document_id)
        if kind == "para":
            assert indices is not None
            if not indices or any(index < 0 or index >= len(paragraphs) for index in indices):
                raise CorpusIndexError(f"evidence paragraph out of range: {value!r}")
            selected = tuple(indices)
            text = "\n\n".join(paragraphs[index] for index in selected)
        else:
            selected = tuple(range(len(paragraphs)))
            text = self.read(document_id)
        return ResolvedEvidence(
            pointer=value,
            document_id=document_id,
            relative_path=self.relative_path(document_id),
            anchor=anchor if separator else "",
            paragraph_indices=selected,
            text=text,
            record=self.record(document_id),
        )

