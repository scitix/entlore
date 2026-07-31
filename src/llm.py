"""OpenAI-compatible relay client: chat / embed / concurrent map. With retries."""
from __future__ import annotations
import itertools
import json
import math
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, Iterable

from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from . import config

_TIMEOUT = float(config.ENV.get("LLMWIKI_TIMEOUT", "120"))   # slow-thinking models (glm) often exceed 120s; tunable via env
# Multi-key round-robin: one client per key, round-robin spreads the rate limit (concurrency x number of keys). With a single-element API_KEYS this is equivalent to the original behavior.
_KEYS = config.API_KEYS or [config.API_KEY]
# Lazy construction: build the OpenAI clients on first use, not at import. This lets the package be
# imported (evaluator/baselines) before credentials are configured — the OpenAI SDK raises if api_key
# is empty at construction. Clients are still built once and reused (round-robin over the keys).
_CLIENTS: "list | None" = None
_rr = itertools.count()


def _clients() -> list:
    global _CLIENTS
    if _CLIENTS is None:
        _CLIENTS = [OpenAI(base_url=config.API_BASE, api_key=k, timeout=_TIMEOUT, max_retries=0) for k in _KEYS]
    return _CLIENTS


def next_client() -> OpenAI:
    """Thread-safe round-robin pick of a client (itertools.count().__next__ is atomic)."""
    cs = _clients()
    return cs[next(_rr) % len(cs)]


def apply_no_think(kwargs: dict, model: str) -> dict:
    """When config.NO_THINK is set, inject enable_thinking=false for non-gpt-5/non-claude models (vLLM chat_template_kwargs)."""
    if config.NO_THINK and not model.lower().startswith(("gpt-5", "claude")):
        eb = kwargs.get("extra_body") or {}
        ctk = dict(eb.get("chat_template_kwargs") or {})
        ctk["enable_thinking"] = False
        eb["chat_template_kwargs"] = ctk
        kwargs["extra_body"] = eb
    return kwargs


_anthropic_clients = None
_arr = itertools.count()


def __getattr__(name):
    # backward compat: llm._client lazily resolves to the first OpenAI client (built on first access)
    if name == "_client":
        return _clients()[0]
    raise AttributeError(name)


def _anthropic_client():
    global _anthropic_clients
    if _anthropic_clients is None:
        import anthropic
        toks = config.ANTHROPIC_AUTH_TOKENS or [config.ANTHROPIC_AUTH_TOKEN]
        _anthropic_clients = [anthropic.Anthropic(base_url=config.ANTHROPIC_BASE_URL, api_key=t,
                                                  timeout=180.0, max_retries=0) for t in toks]
    return _anthropic_clients[next(_arr) % len(_anthropic_clients)]
_emb_cache: dict[str, list[float]] = {}
_lock = threading.Lock()


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=20))
def chat(system: str, user: str, *, model: str | None = None, temperature: float = 0.7,
         max_tokens: int = 2048, json_mode: bool = False) -> str:
    m = model or config.CHAT_MODEL
    if m.lower().startswith("claude"):
        # claude family: Anthropic native protocol (system is separate, max_tokens is required, no response_format)
        r = _anthropic_client().messages.create(
            model=m, max_tokens=max_tokens, system=system,
            messages=[{"role": "user", "content": user}])
        txt = "".join(getattr(b, "text", "") for b in r.content).strip()
        return re.sub(r"<think>.*?</think>", "", txt, flags=re.DOTALL).strip()
    kwargs = dict(model=m, messages=[{"role": "system", "content": system},
                                     {"role": "user", "content": user}])
    if m.lower().startswith("gpt-5"):
        # gpt-5.x: use max_completion_tokens; temperature/top_p are restricted by the beta and must be omitted.
        # Passed via extra_body (same JSON on the wire), compatible with older openai SDKs (1.43 lacks this named parameter)
        kwargs["extra_body"] = {"max_completion_tokens": max_tokens}
    else:
        kwargs["temperature"] = temperature
        kwargs["max_tokens"] = max_tokens
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    apply_no_think(kwargs, m)
    resp = next_client().chat.completions.create(**kwargs)
    txt = (resp.choices[0].message.content or "").strip()
    # strip the <think>...</think> that reasoning models may emit
    txt = re.sub(r"<think>.*?</think>", "", txt, flags=re.DOTALL).strip()
    return txt


def _parse_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```", 2)[1] if "```" in raw else raw
        raw = raw[4:].strip() if raw.lower().startswith("json") else raw.strip()
    try:
        return json.loads(raw)
    except Exception:
        i, j = raw.find("{"), raw.rfind("}")
        if i >= 0 and j > i:
            return json.loads(raw[i:j + 1])
        raise


def judge_json(system: str, user: str, **kw) -> dict:
    """For the evaluation judge: always uses config.JUDGE_MODEL (separate from the generation model, to avoid self-evaluation bias)."""
    kw.setdefault("model", config.JUDGE_MODEL)
    return chat_json(system, user, **kw)


def chat_json(system: str, user: str, *, max_tokens: int = 1500, **kw) -> dict:
    """Request JSON. Reasoning models burn tokens; on empty/truncated output, retry with a larger budget."""
    last = None
    for mt in (max_tokens, max_tokens * 2):
        raw = chat(system, user, max_tokens=mt, **kw)
        if raw.strip():
            try:
                return _parse_json(raw)
            except Exception as e:
                last = e
    if last:
        raise last
    raise ValueError("empty LLM response for JSON request")


@retry(stop=stop_after_attempt(4), wait=wait_exponential(multiplier=1, min=2, max=20))
def _embed_raw(texts: list[str]) -> list[list[float]]:
    resp = next_client().embeddings.create(model=config.EMBED_MODEL, input=texts, encoding_format="float")
    return [d.embedding for d in resp.data]


def embed(texts: list[str]) -> list[list[float]]:
    out: list[list[float] | None] = [None] * len(texts)
    todo, idx = [], []
    for i, t in enumerate(texts):
        if t in _emb_cache:
            out[i] = _emb_cache[t]
        else:
            todo.append(t); idx.append(i)
    for b in range(0, len(todo), 32):
        chunk = todo[b:b + 32]
        vecs = _embed_raw(chunk)
        for k, v in zip(chunk, vecs):
            with _lock:
                _emb_cache[k] = v
        for local, orig in zip(range(b, b + len(chunk)), idx[b:b + 32]):
            out[orig] = _emb_cache[chunk[local - b]]
    return [o for o in out]  # type: ignore


def cosine(a: list[float], b: list[float]) -> float:
    s = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a)); nb = math.sqrt(sum(y * y for y in b))
    return s / (na * nb + 1e-9)


def pmap(fn: Callable, items: Iterable, workers: int | None = None) -> list:
    items = list(items)
    w = workers or config.MAX_CONCURRENCY
    with ThreadPoolExecutor(max_workers=max(1, w)) as ex:
        return list(ex.map(fn, items))
