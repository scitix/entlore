"""LLM generation base: uses src/llm.py's low-level client directly to obtain real token usage (chat() does not
return usage, which the TCO report needs), and unifies cost accounting. Supports both Claude (Anthropic native) and OpenAI-compatible endpoints."""
from __future__ import annotations

from .. import llm

# Price per million tokens (USD). Edit this table for your own models/providers; unknown models fall back to DEFAULT_PRICING.
PRICING = {
    # -- the 6 models under test (real prices, provided by the user 2026-07) --
    "gpt-5.5": {"input": 5.0, "output": 30.0},
    "DeepSeek-V4-Pro": {"input": 0.14, "output": 0.28},
    "DeepSeek-V4-Flash": {"input": 0.07, "output": 0.14},
    "Qwen/Qwen3.5-397B-A17B": {"input": 0.48, "output": 2.88},
    "glm-5.2": {"input": 1.4, "output": 4.4},
    "MiniMaxAI/MiniMax-M2.7": {"input": 0.3, "output": 1.2},
    "kimi-k2.6": {"input": 0.95, "output": 4.0},
    # -- judge / others (estimated) --
    "claude-opus-4-8": {"input": 15.0, "output": 75.0},
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0},
    "claude-haiku-4-5-20251001": {"input": 1.0, "output": 5.0},
    "gpt-5.4": {"input": 5.0, "output": 15.0},
    "gpt-5.4-mini": {"input": 1.0, "output": 4.0},
}
DEFAULT_PRICING = {"input": 3.0, "output": 12.0}


def compute_cost(usage: dict, model: str) -> float:
    p = PRICING.get(model, DEFAULT_PRICING)
    return (usage.get("input_tokens", 0) * p["input"]
            + usage.get("output_tokens", 0) * p["output"]) / 1_000_000


def _is_claude(model: str) -> bool:
    return model.lower().startswith("claude")


class _EmptyCompletion(Exception):
    """API 200 but content empty (a thinking model under a short max_tokens spends its budget on reasoning and returns empty content).
    Carries this call's usage so TCO does not lose the real tokens."""
    def __init__(self, usage: dict):
        self.usage = usage or {"input_tokens": 0, "output_tokens": 0}


def generate(system: str, user: str, *, model: str, max_tokens: int = 4096,
             temperature: float = 0.1) -> tuple[str, dict]:
    """Single-turn generation -> (text, usage{input_tokens,output_tokens}). Captures real usage for TCO.
    Retries with the same params as the tool loop (4 exponential backoffs) -- a single-turn pipeline should not lose points to one network timeout.
    An **empty completion** is likewise treated as a retryable failure (triggers a retry); if still empty after 4 tries, return `[ERROR] empty completion`,
    counted by the runner as generation_infra (no answer file written, enters the re-run loop), no longer silently scored 0."""
    from tenacity import Retrying, stop_after_attempt, wait_exponential

    def _try() -> tuple[str, dict]:
        text, usage = _generate_once(system, user, model=model, max_tokens=max_tokens,
                                     temperature=temperature)
        if not text.strip():
            raise _EmptyCompletion(usage)      # trigger backoff retry (network jitter / transient empty block can self-heal)
        return text, usage

    try:
        for attempt in Retrying(stop=stop_after_attempt(4),
                                wait=wait_exponential(multiplier=1, min=2, max=20), reraise=True):
            with attempt:
                return _try()
    except _EmptyCompletion as e:
        return "[ERROR] empty completion after retries", e.usage


def _generate_once(system: str, user: str, *, model: str, max_tokens: int,
                   temperature: float) -> tuple[str, dict]:
    if _is_claude(model):
        r = llm._anthropic_client().messages.create(
            model=model, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": user}])
        text = "".join(getattr(b, "text", "") for b in r.content).strip()
        usage = {"input_tokens": r.usage.input_tokens, "output_tokens": r.usage.output_tokens}
        return text, usage
    kwargs = dict(model=model, messages=[{"role": "system", "content": system},
                                         {"role": "user", "content": user}])
    if model.lower().startswith("gpt-5"):
        kwargs["extra_body"] = {"max_completion_tokens": max_tokens}
    else:
        kwargs["temperature"] = temperature
        kwargs["max_tokens"] = max_tokens
    # The single-turn path previously missed calling apply_no_think (only the agent loop/graphrag did) -- when EKWB_NO_THINK=1,
    # inject enable_thinking=false for non-gpt-5/claude models, eliminating empty completions from thinking models under short max_tokens.
    llm.apply_no_think(kwargs, model)
    r = llm.next_client().chat.completions.create(**kwargs)
    text = (r.choices[0].message.content or "").strip()
    u = r.usage
    usage = {"input_tokens": getattr(u, "prompt_tokens", 0) if u else 0,
             "output_tokens": getattr(u, "completion_tokens", 0) if u else 0}
    return text, usage
