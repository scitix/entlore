"""Centralized config: reads relay credentials and model names from the project-root .env. Read-only, never prints secrets."""
from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_env() -> dict:
    env: dict[str, str] = {}
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    # allow real environment variables to override
    for k in list(env):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


ENV = load_env()
API_BASE = ENV.get("API_BASE", "").rstrip("/")
# Multi-key round-robin: API_KEY supports comma-separated keys (raises concurrency, rate ~= x number of keys); single API_KEY stays as the first key (backward compat)
API_KEYS = [k.strip() for k in ENV.get("API_KEY", "").split(",") if k.strip()]
API_KEY = API_KEYS[0] if API_KEYS else ""
CHAT_MODEL = ENV.get("CHAT_MODEL", "DeepSeek-V4-Flash")   # default: lightweight LLM for questions/auditing/scoring
GEN_MODEL = ENV.get("GEN_MODEL", "gpt-5.5")              # document body generation (strong model, lowers defect rate)
# Anthropic native-protocol endpoint (the claude family goes here, not the OpenAI endpoint)
# Token rotation trusts the .env **verbatim** (load_env's "process-environment override" semantics
# let stale ANTHROPIC_* variables in a long-lived session clobber a new token -- the 2026-07-16 incident);
# fall back to the process environment only when .env does not set it
def _env_file_raw(key: str) -> str:
    f = ROOT / ".env"
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith(f"{key}="):
                return line.split("=", 1)[1].strip()
    return ""

ANTHROPIC_BASE_URL = _env_file_raw("ANTHROPIC_BASE_URL") or os.environ.get("ANTHROPIC_BASE_URL", "")
# The gateway /proxy route has been retired (2026-07-16; requests there always 401 invalid x-api-key): strip it regardless of source
if ANTHROPIC_BASE_URL.rstrip("/").endswith("/proxy"):
    ANTHROPIC_BASE_URL = ANTHROPIC_BASE_URL.rstrip("/")[: -len("/proxy")]
ANTHROPIC_AUTH_TOKEN = (_env_file_raw("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_AUTH_TOKEN")
                        or os.environ.get("ANTHROPIC_API_KEY", ""))
# same multi-key round-robin (claude side)
ANTHROPIC_AUTH_TOKENS = [k.strip() for k in ANTHROPIC_AUTH_TOKEN.split(",") if k.strip()]
ANTHROPIC_AUTH_TOKEN = ANTHROPIC_AUTH_TOKENS[0] if ANTHROPIC_AUTH_TOKENS else ""
# When the judge (claude opus) and the system-under-test (the OpenAI-compatible endpoint) share the same host/origin, the judge reuses all API_KEYS for multi-key round-robin --
# otherwise a single anthropic key handling 64-way concurrency hits the rate limit, making score far slower than the 3-key generation phase (measured bottleneck).
def _host(u):
    return u.split("//")[-1].split("/")[0] if u else ""
if API_BASE and ANTHROPIC_BASE_URL and _host(API_BASE) == _host(ANTHROPIC_BASE_URL):
    _seen, _merged = set(), []
    for _k in ANTHROPIC_AUTH_TOKENS + API_KEYS:      # explicit anthropic keys first, then merge in all keys from the OpenAI-compatible endpoint, dedup while preserving order
        if _k and _k not in _seen:
            _seen.add(_k); _merged.append(_k)
    ANTHROPIC_AUTH_TOKENS = _merged
    ANTHROPIC_AUTH_TOKEN = ANTHROPIC_AUTH_TOKENS[0] if ANTHROPIC_AUTH_TOKENS else ""
# Turn off chain-of-thought (EKWB_NO_THINK=1): inject enable_thinking=false for non-gpt-5/non-claude models.
# Measured: glm-5.2/Qwen3.5 with default thinking return empty and slow under a short max_tokens; disabling it yields content, is faster, and produces fewer empty blocks.
NO_THINK = (ENV.get("EKWB_NO_THINK") or os.environ.get("EKWB_NO_THINK", "")).strip().lower() in ("1", "true", "yes")
ALT_CHAT_MODEL = ENV.get("ALT_CHAT_MODEL", CHAT_MODEL)
EMBED_MODEL = ENV.get("EMBED_MODEL", "Qwen/Qwen3-Embedding-8B")
JUDGE_MODEL = ENV.get("JUDGE_MODEL", CHAT_MODEL)
try:
    MAX_CONCURRENCY = int(ENV.get("LLMWIKI_MAX_CONCURRENCY", "6"))
except ValueError:
    MAX_CONCURRENCY = 6

OUT = ROOT / "out"
SEED = ROOT / "src" / "seed" / "governance_seed.yaml"
