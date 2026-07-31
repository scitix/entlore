# Provenance

- **Source repository**: https://github.com/microsoft/graphrag
- **Origin**: PyPI sdist `graphrag-2.7.2.tar.gz` (corresponds to GitHub tag `v2.7.2`)
- **Copy date**: 2026-07-22
- **License**: MIT (see `LICENSE` in this directory, redistributed alongside the code; each file retains its original MIT header)

## Vendored manifest (**index-side format-definition IP**, byte-identical redistribution)

| File | Purpose | Where this repo uses it |
|---|---|---|
| `graphrag/prompts/index/extract_graph.py` | `GRAPH_EXTRACTION_PROMPT` / `CONTINUE_PROMPT` / `LOOP_PROMPT`: tuple-delimiter entity/relationship extraction + gleaning continuation prompts | `src/baselines/graphrag.py`, called per chunk in the extraction step |
| `graphrag/prompts/index/community_report.py` | `COMMUNITY_REPORT_PROMPT`: structured community JSON report (title/summary/rating/findings) | called per community in the community-report step |
| `graphrag/index/operations/cluster_graph.py` | `cluster_graph` / `_compute_leiden_communities`: hierarchical Leiden community detection (calls `graspologic.hierarchical_leiden`) | community-detection step |
| `graphrag/index/utils/stable_lcc.py` | `stable_largest_connected_component`: deterministic largest connected component (dependency of `cluster_graph`) | same as above (via cluster_graph) |
| `graphrag/index/utils/string.py` | `clean_str`: entity/relationship field cleaning (character-for-character identical to the official parsing) | extraction-result parsing |

`__init__.py` is an **empty package marker** added by this repo (the upstream file of the same name pulls in datashaper/config runtime assembly, irrelevant to this redistribution, so it is not vendored).
The subtree's top-level package name is still `graphrag`, located by `src/baselines/graphrag.py` via `sys.path.insert(0, third_party/graphrag)`
(same approach as `third_party/okf`'s `reference_agent`); putting it first on `sys.path` pins the vendored version
regardless of whether another `graphrag` is installed in the environment.

## Not vendored (intentionally, same philosophy as okf: only vendor the format IP that is actually executed)

- **Query engine** (`graphrag/query/**`: local/global/drift search and the map-reduce context builder):
  the official query is a single-shot map-reduce that depends on its own LLM client and token budgeter; this benchmark's answering side goes through this repo's unified
  tool loop (`src/baselines/loop.py`), whose tools are **pure retrieval** (no LLM call inside a tool, to keep TCO accounting at a single point),
  so the answering prompt is written in this repo (see `src/baselines/graphrag.py:GRAPHRAG_SYSTEM_PROMPT`),
  and the official query system prompt is not used. Attribution: same as okf — okf likewise only vendors the bundle/index side, with the answering prompt written here.
- **Extraction driver loop** (`graphrag/index/operations/extract_graph/graph_extractor.py`): its `_process_document`
  depends on the official `ChatModel` async protocol and config defaults; this repo reimplements the equivalent
  extract → gleaning (CONTINUE) → loopcheck (LOOP) three-stage logic via an `llm.chat` relay, and **reuses verbatim** the official `_process_results`
  tuple-delimiter parsing (entity/relationship records, `clean_str`, weight summation, description concatenation).
- **The datashaper wrapper around community detection**: only the pure `cluster_graph` function is taken (it depends only on networkx + graspologic).

## This repo's side (not official; see the graphrag section of `docs/baselines.md`)

- corpus enumeration + heading-aware chunking (reuses `src/baselines/rag.py:_chunk_doc`, as text units);
- the relay driver and concurrency for extraction/reporting (`llm.pmap`), and cost accounting (`_gen.compute_cost`);
- graph merging, community-report input-table (entities/relationships) assembly, and community-report embedding index;
- the two answering tools (`global_search` for community-report retrieval / `local_search` for entity neighbors) and `GRAPHRAG_SYSTEM_PROMPT`;
- `graphrag_manifest.json` (src → entity/community reverse lookup, the source for scorer/trace mapping).
