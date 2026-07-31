# Baselines

All baselines are **self-contained**: they depend only on `src/llm.py` + `src/baselines/config.py`
(which read `.env`), with no private framework. Clone and run. Register a new one by subclassing
`Baseline` and decorating with `@register("name")`.

The four "measured" pipelines (`rag`, `agentic_rag`, `okf`, `graphrag`) **use vector retrieval only**
(reflecting common industry practice). `bm25` is an intentional naive sparse-retrieval floor.

| Baseline | Mechanism | What it isolates |
|---|---|---|
| `closed_book` | model answers with no retrieval | parametric-memory floor |
| `bm25` | Okapi BM25 (self-contained, ~40 lines) sparse top-k -> single-turn answer | lexical sparse retrieval |
| `rag` | heading-aware chunks (800/100) -> embedding index -> cosine top-k=24 -> single-turn answer | standard single-turn RAG ceiling |
| `agentic_rag` | multi-turn tool loop (`search` + `get_page` + `submit_answer`) over the same vector index | + multi-turn autonomy (vs `rag`) |
| `okf` | tool loop over an OKF bundle (concept pages + Related/Cited-by links + index tree) | + knowledge-format substrate |
| `graphrag` | dual-tool loop (`global_search` community reports / `local_search` entity neighbors) over an induced entity graph | + graph substrate (sibling of `okf`) |
| `oracle_rag` | gold evidence documents fed whole, single-turn | upper bound under perfect recall |
| `oracle_agentic_rag` | gold document paths in the prompt, loop reads them | upper bound under perfect navigation |
| `oracle_okf` | gold bundle index chain in the prompt | upper bound under perfect index chain |

**Ablation ladder**: `rag -> agentic_rag` adds autonomy; `agentic_rag -> {okf, graphrag}` are two
parallel "knowledge-format substrate" branches (OKF concept+link vs entity graph + community
summaries) that can be compared head to head. `X vs oracle_X` isolates the retrieval/navigation loss
of form X.

## Building indexes

```bash
python scripts/build_indexes.py --baseline bm25,rag     # fast
python scripts/build_indexes.py --baseline okf          # LLM enrichment per doc
python scripts/build_indexes.py --baseline graphrag     # entity extraction + Leiden (expensive)
```

Indexes are not shipped (bm25/rag are small but corpus-derived; graphrag/okf are large and
model-dependent). `graphrag`/`okf` are compiled with the model set by `--model` (or `EKWB_SUT_MODEL`).

## Model API

`src/llm.py` routes `claude*` to the Anthropic native protocol and everything else to the
OpenAI-compatible chat API (`API_BASE`). Optional comma-separated multi-key rotation raises
throughput. The judge uses `JUDGE_MODEL` (kept distinct from the model under test).
Cost accounting uses a per-model price table in `src/baselines/_gen.py` (edit for your models).
