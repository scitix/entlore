"""Baseline runtime config -- the **single point table** for all environment variables (2026-07-16 refactor P1.2).

Paths default to the dataset/ shipped with the repo, all overridable via environment variables; model/key/embedding
reuse the top-level src/config.py (reads .env, see .env.example). Zero private paths.

| Environment variable      | Default                       | Description |
|---------------------------|-------------------------------|-------------|
| EKWB_DATASET              | dataset/                      | Dataset root (bank/questions/corpus) |
| EKWB_CORPUS               | $EKWB_DATASET/corpus          | Corpus tree |
| EKWB_BANK                 | (auto-detect v2.2->v2)        | golden packets bank |
| EKWB_GROUP                | synbench-v02                  | Knowledge-base group name (for tool hints) |
| EKWB_RAG_INDEX            | eval_export/rag_index_self    | RAG vector index directory |
| EKWB_BM25_INDEX           | eval_export/bm25_index_self   | BM25 chunk store directory (naive baseline) |
| EKWB_BM25_TOP_K           | 24                            | BM25 retrieval count (same as rag for comparison) |
| EKWB_BM25_K1 / _B         | 1.5 / 0.75                    | Okapi BM25 parameters |
| EKWB_LC_ORACLE_MAX_CHARS  | 400000                        | lc_oracle long-context budget (fit all evidence passages) |
| EKWB_OKF_BUNDLE           | $EKWB_DATASET/okf_bundle      | OKF bundle directory |
| EKWB_OKF_INDEX            | $EKWB_OKF_BUNDLE sibling _vindex | Vector index of the OKF bundle |
| EKWB_GRAPHRAG_DIR         | $EKWB_DATASET/graphrag_index  | GraphRAG index-product directory (graph/communities/reports/embedding) |
| EKWB_GRAPHRAG_MAX_GLEAN   | 1                             | entity-extraction gleaning continuation rounds (official default 1) |
| EKWB_GRAPHRAG_MAX_CLUSTER | 10                            | Leiden max single-community size (hierarchical_leiden) |
| EKWB_GRAPHRAG_LEVEL       | -1                            | community level for answering (-1 = reports of all levels enter the retrieval pool) |
| EKWB_GRAPHRAG_REPORT_TOPK | 5                             | community reports returned per global_search call |
| EKWB_GRAPHRAG_LOCAL_TOPK  | 8                             | entities/neighbors returned per local_search call |
| EKWB_SUT_MODEL            | claude-sonnet-4-6             | model under test |
| EKWB_CHUNK_SIZE/OVERLAP   | 800 / 100                     | chunking setting |
| EKWB_RAG_TOP_K            | 24                            | RAG retrieval count (P2 high-ceiling setting) |
| EKWB_SEARCH_TOP_K         | 10                            | items returned per in-loop search tool call |
| EKWB_MAX_CONTEXT_CHARS    | 80000                         | RAG context budget |
| EKWB_GEN_MAX_TOKENS       | 4096                          | single-turn answer output budget |
| EKWB_AGENT_MAX_ITER       | 30                            | loop budget |
| EKWB_AGENT_MAX_TOKENS     | 4096                          | per-turn loop output budget |
| EKWB_AGENT_CTX_CHARS      | 240000                        | context guardrail (collapse oldest tool results) |
| EKWB_RAG_EMBED_MODEL      | .env EMBED_MODEL              | index-build embedding (query side auto-pairs from index_meta) |
| EKWB_ORACLE_MAX_CHARS     | 200000                        | oracle_rag context budget |
| EKWB_ORACLE_DOC_CAP       | 16                            | oracle evidence-document cap |
| EKWB_ORACLE_MAX_ITER      | 40                            | oracle loop budget (P5.3) |

(top-level .env / environment: API_BASE, API_KEY, EMBED_MODEL, JUDGE_MODEL, ANTHROPIC_BASE_URL,
 ANTHROPIC_AUTH_TOKEN, LLMWIKI_MAX_CONCURRENCY, LLMWIKI_TIMEOUT -- see src/config.py)
"""
from __future__ import annotations
import os
from pathlib import Path

from .. import config as _cfg

ROOT = _cfg.ROOT

# ---- corpus / product paths ----
DATASET_DIR = Path(os.environ.get("EKWB_DATASET", str(ROOT / "dataset")))
CORPUS_DIR = Path(os.environ.get("EKWB_CORPUS", str(DATASET_DIR / "corpus")))
RAG_INDEX_DIR = Path(os.environ.get("EKWB_RAG_INDEX", str(ROOT / "eval_export" / "rag_index_self")))
BM25_INDEX_DIR = Path(os.environ.get("EKWB_BM25_INDEX", str(ROOT / "eval_export" / "bm25_index_self")))
OKF_BUNDLE_DIR = Path(os.environ.get("EKWB_OKF_BUNDLE", str(DATASET_DIR / "okf_bundle")))
OKF_INDEX_DIR = Path(os.environ.get("EKWB_OKF_INDEX", str(OKF_BUNDLE_DIR) + "_vindex"))
GRAPHRAG_DIR = Path(os.environ.get("EKWB_GRAPHRAG_DIR", str(DATASET_DIR / "graphrag_index")))
GROUP = os.environ.get("EKWB_GROUP", "synbench-v02")


def bank_path() -> Path:
    """golden packets bank: explicitly set via EKWB_BANK, otherwise auto-detected under EKWB_DATASET (v2.2 preferred)."""
    p = os.environ.get("EKWB_BANK")
    if p:
        return Path(p)
    for name in ("golden_packets_v2.2.jsonl", "golden_packets_v2.jsonl"):
        c = DATASET_DIR / name
        if c.exists():
            return c
    raise FileNotFoundError(f"bank not found under {DATASET_DIR} (specify with EKWB_BANK)")


# ---- system under test (SUT) ----
SUT_MODEL = os.environ.get("EKWB_SUT_MODEL", "claude-sonnet-4-6")

# ---- RAG (P2 high-ceiling setting: feed recall to its fullest within the standard single-turn form) ----
CHUNK_SIZE = int(os.environ.get("EKWB_CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.environ.get("EKWB_CHUNK_OVERLAP", "100"))
RAG_TOP_K = int(os.environ.get("EKWB_RAG_TOP_K", "24"))
SEARCH_TOP_K = int(os.environ.get("EKWB_SEARCH_TOP_K", "10"))
MAX_CONTEXT_CHARS = int(os.environ.get("EKWB_MAX_CONTEXT_CHARS", "80000"))
RAG_EMBED_MODEL = os.environ.get("EKWB_RAG_EMBED_MODEL", _cfg.EMBED_MODEL)

# ---- BM25 (naive sparse-retrieval baseline; self-contained implementation, no new deps) ----
BM25_TOP_K = int(os.environ.get("EKWB_BM25_TOP_K", "24"))
BM25_K1 = float(os.environ.get("EKWB_BM25_K1", "1.5"))
BM25_B = float(os.environ.get("EKWB_BM25_B", "0.75"))

# ---- tool loop ----
AGENT_MAX_ITER = int(os.environ.get("EKWB_AGENT_MAX_ITER", "30"))
AGENT_MAX_TOKENS = int(os.environ.get("EKWB_AGENT_MAX_TOKENS", "4096"))
AGENT_CTX_CHARS = int(os.environ.get("EKWB_AGENT_CTX_CHARS", "240000"))
# per-question total budget guardrail (audit P2-1): cumulative token / wall-time caps, preventing a non-converging model from burning millions of tokens
AGENT_MAX_TOTAL_TOKENS = int(os.environ.get("EKWB_AGENT_MAX_TOTAL_TOKENS", "400000"))
AGENT_MAX_WALL_S = int(os.environ.get("EKWB_AGENT_MAX_WALL_S", "900"))
GEN_MAX_TOKENS = int(os.environ.get("EKWB_GEN_MAX_TOKENS", "4096"))

# ---- GraphRAG (Microsoft graphrag @v2.7.2 vendored; faithful reproduction on the index side) ----
GRAPHRAG_MAX_GLEAN = int(os.environ.get("EKWB_GRAPHRAG_MAX_GLEAN", "1"))
GRAPHRAG_MAX_CLUSTER = int(os.environ.get("EKWB_GRAPHRAG_MAX_CLUSTER", "10"))
GRAPHRAG_LEVEL = int(os.environ.get("EKWB_GRAPHRAG_LEVEL", "-1"))
GRAPHRAG_REPORT_TOPK = int(os.environ.get("EKWB_GRAPHRAG_REPORT_TOPK", "5"))
GRAPHRAG_LOCAL_TOPK = int(os.environ.get("EKWB_GRAPHRAG_LOCAL_TOPK", "8"))

# ---- Oracle (P5: the synthesis upper bound after removing retrieval from the system) ----
ORACLE_MAX_CHARS = int(os.environ.get("EKWB_ORACLE_MAX_CHARS", "200000"))
ORACLE_DOC_CAP = int(os.environ.get("EKWB_ORACLE_DOC_CAP", "16"))
ORACLE_MAX_ITER = int(os.environ.get("EKWB_ORACLE_MAX_ITER", "40"))
LC_ORACLE_MAX_CHARS = int(os.environ.get("EKWB_LC_ORACLE_MAX_CHARS", "400000"))
