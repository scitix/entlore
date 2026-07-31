"""Baseline interface contract + registry (the 4th reusable registry, same philosophy as operator_registry / archetypes / org_spec).

Adding a custom baseline = subclass Baseline and implement answer(), register it with @register("name") and it can be called by the CLI/evaluation.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class AnswerResult:
    """Unified product of one answering pass (TCO-traceable)."""
    answer: str
    approach: str
    tokens: dict = field(default_factory=dict)      # {"input_tokens","output_tokens"}
    cost_usd: float = 0.0
    wall_time_s: float = 0.0
    context_chars: int = 0
    trace: list | None = None                        # the agent's tool-call log


class Baseline(ABC):
    """Unified interface for baselines under test. prepare() is an optional offline step (rag builds an index / wiki compiles / agent needs none)."""
    name: str = "base"

    def prepare(self) -> None:
        """Offline preparation (build index / compile). No-op by default."""
        return None

    @abstractmethod
    def answer(self, question: dict) -> AnswerResult:
        """Answer a single question. question contains at least {id, question, requires_groups?}."""
        raise NotImplementedError


REGISTRY: dict[str, type[Baseline]] = {}


def register(name: str):
    def deco(cls):
        cls.name = name
        REGISTRY[name] = cls
        return cls
    return deco


def get_baseline(name: str, **kwargs) -> Baseline:
    if name not in REGISTRY:
        raise KeyError(f"unknown baseline '{name}'; available: {sorted(REGISTRY)}")
    return REGISTRY[name](**kwargs)
