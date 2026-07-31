"""Closed-book control baseline: **provides no retrieval context**, answers purely from parametric knowledge.

Purpose: quantify "how much can pure parametric memory answer". For this benchmark's **anonymized synthetic
enterprise corpus**, closed-book should approach 0 -- i.e., the answers (anonymized entities, internal events,
private metrics) cannot appear in the model's pretraining. Thus closed_book is the key honesty/no-leakage
control: if a question can be answered closed-book, that question is hittable by parametric knowledge or a
shortcut and is not truly testing "retrieval + grounding". When tabulated alongside the retrieval pipelines,
closed_book is the "floor lower bound" for all system pipelines.
"""
from __future__ import annotations
import time

from . import config
from ._gen import generate, compute_cost
from .base import AnswerResult, Baseline, register
from .corpus import Corpus

CLOSED_BOOK_SYSTEM = (
    "You are an enterprise knowledge-base QA assistant. **No reference materials are provided right now**; answer using only the knowledge you already possess.\n"
    "If you do not know the answer, or cannot be certain, answer clearly \"Cannot answer based on the available materials\"; do not fabricate or speculate."
)


@register("closed_book")
class ClosedBookBaseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None, **kwargs):
        self.corpus = corpus            # unused; only to keep the constructor signature consistent with other baselines
        self.model = model or config.SUT_MODEL

    def prepare(self, log=print) -> None:
        return None                     # no index / no offline step

    def answer(self, question: dict) -> AnswerResult:
        t0 = time.time()
        q = question["question"]
        text, usage = generate(CLOSED_BOOK_SYSTEM, q, model=self.model,
                               max_tokens=config.GEN_MAX_TOKENS)
        return AnswerResult(text, "closed_book", tokens=usage,
                            cost_usd=compute_cost(usage, self.model),
                            wall_time_s=time.time() - t0, context_chars=0)
