"""Self-contained baselines-under-test package (zero private-framework deps, uses only src/llm.py + src/config.py).

Evaluated pipelines (registered on import):
  - bm25        : Okapi BM25 sparse retrieval top-k -> single-turn generation (naive sparse-retrieval floor; self-contained, no embedding)
  - rag         : vector retrieval top-k -> single-turn generation (high-ceiling implementation of standard single-turn RAG)
  - agentic_rag : multi-turn autonomous tool loop x vector retrieval (same index as rag)
  - okf         : navigation tool loop over an Open Knowledge Format bundle (makes the format bonus explicit)
  - graphrag    : Microsoft GraphRAG (vendored) entity graph + Leiden community reports, two-tool loop
                  (okf's sibling format branch; makes the community-graph bonus explicit)

oracle upper bounds (retrieval physically removed from the system; not on the main leaderboard, shown as a separate upper-bound band):
  - oracle_rag / oracle_agentic_rag / oracle_okf
  - lc_oracle   : canonical exact evidence passages concatenated into a long context, single-turn (perfect passage-level recall ceiling)

Shared layer: loop.py (unified tool loop + protocol adapters) / toolkits.py (tool building blocks) / config.py (single env table).
Extension: subclass Baseline and implement answer(), register it with @register("name").
"""
from .base import AnswerResult, Baseline, REGISTRY, get_baseline, register  # noqa: F401
from . import bm25, rag, agentic_rag, okf, graphrag, oracle, closed_book  # noqa: F401  triggers @register

__all__ = ["AnswerResult", "Baseline", "REGISTRY", "get_baseline", "register",
           "bm25", "rag", "agentic_rag", "okf", "graphrag", "oracle", "closed_book"]
