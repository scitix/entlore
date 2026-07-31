# Provenance

- **Source repository**: https://github.com/GoogleCloudPlatform/knowledge-catalog (the `okf/` directory)
- **Copy date**: 2026-07-15
- **Source commit (main HEAD)**: d44368c15e38
- **License**: Apache-2.0 (see LICENSE.md in this directory, redistributed alongside the spec and code)

## Vendored manifest

| File | Purpose |
|---|---|
| `SPEC.md` | OKF v0.1 specification text |
| `reference_agent/bundle/document.py` | `OKFDocument`: frontmatter required-key validation / serialization |
| `reference_agent/bundle/paths.py` | `concept_id_to_path`: concept-id validation (ASCII segments) and on-disk path |
| `reference_agent/bundle/index.py` | `regenerate_indexes`: official index-tree generation (directory describer is injectable) |
| `reference_agent/bundle/synthesizer.py` | official directory-describer interface (this repo injects a relay implementation in place of Gemini) |
| `reference_agent/sources/base.py` | `Source`/`ConceptRef` data-source abstraction (this repo implements CorpusSource) |
| `reference_agent/sources/bigquery.py` | official BigQuery source (unused; kept as-is for a complete redistribution) |

## This repo's side (not official; see the OKF section of docs/baselines.md)

- Orchestration (`src/baselines/okf.py`): corpus enumeration, LLM enrichment (type/description/tags),
  Related/Cited-by link materialization, bundle vector index, and `okf_manifest.json` (src → cid mapping).
- Intentional, disclosed deviations: the body is a lossless mirror of the source document (the official agent is synthesis-style); source frontmatter is merged into `source_meta`.
- The `resource` frontmatter uses a custom scheme `corpus://<relative-path>` pointing at this repo's corpus;
  the scorer `src/evaluator.py:_okf_map()` and the oracle rely on the manifest's src → cid mapping.
