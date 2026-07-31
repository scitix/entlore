"""Agentic RAG baseline: multi-turn autonomous tool loop x vector retrieval (**same index** as the rag baseline).

Attribution chain: rag->agentic_rag quantifies the "multi-turn autonomy" gain; agentic_rag->okf quantifies the "substrate format" gain.
Toolset = search (vector) + get_page + submit_answer; goal prompt (retrieval strategy fully autonomous,
ablation showed instruction-following masks the behavioral default). Budget 30 iterations, aligned with the measured line."""
from __future__ import annotations

from . import config
from .base import AnswerResult, Baseline, register
from .corpus import Corpus
from .loop import run_loop_answer
from .rag import VectorIndex
from .toolkits import get_page_tool, search_tool

AGENTIC_RAG_PROMPT = """You are an enterprise knowledge-base QA assistant. Use the provided tools to find evidence in the knowledge base and answer the question.

Tool semantics:
- search: semantic retrieval of relevant pages (returns paths and snippets)
- get_page: read the full text of a page by its exact path
- submit_answer: submit the final answer

How to search, how many rounds to search, and how many pages to read closely are entirely up to you.

## Answer requirements
- **Use only retrieved information**; do not fabricate or speculate about facts not present in the knowledge base
- When information is insufficient, state clearly what is missing

## Citation format (must follow)
After each key factual assertion, cite its source: `[source: group/path]`;
the path must be a page you actually read; for information whose source is uncertain, mark it as [source: inferred] rather than fabricating a path.

Available knowledge-base groups: {groups}"""


@register("agentic_rag")
class AgenticRagBaseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None,
                 max_iterations: int | None = None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self.max_iter = max_iterations or config.AGENT_MAX_ITER
        self._vindex = VectorIndex(config.RAG_INDEX_DIR, config.RAG_TOP_K)

    def prepare(self, log=print) -> None:
        self._vindex.load()   # missing index raises FileNotFoundError directly (hints to build rag first)
        log(f"[agentic_rag] index ok: {self._vindex.dir}"
            f"(embed={self._vindex.embed_model}, chunks={len(self._vindex._chunks)})")

    def _tools(self) -> list:
        return [search_tool(self._vindex, self.corpus.group), get_page_tool(self.corpus)]

    def answer(self, question: dict) -> AnswerResult:
        return run_loop_answer(self.model, AGENTIC_RAG_PROMPT.format(groups=self.corpus.group),
                               self._tools(), question["question"], "agentic_rag",
                               max_iter=self.max_iter)
