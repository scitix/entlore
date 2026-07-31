"""Unified tool loop: one iteration algorithm + two thin protocol adapters (Anthropic tool_use / OpenAI function-calling).

Design (2026-07-16 refactor P1.1):
- Each pipeline **brings its own toolset** (Tool list) and system prompt; composition expresses the differences, no cross-pipeline runtime switches;
- Single point for loop semantics: temperature 0.1 / 4 exponential-backoff retries per API call / context guardrail (collapse oldest tool results) /
  submit_answer termination / budget-exhaustion error -- behavior is equivalent across both protocols;
- Adapters only handle message shape and response parsing, and contain no loop logic.
"""
from __future__ import annotations
import json
import time
from dataclasses import dataclass, field
from typing import Callable

from tenacity import Retrying, stop_after_attempt, wait_exponential

from .. import llm
from . import config
from ._gen import compute_cost


@dataclass
class Tool:
    """A tool callable by the loop. fn(args) -> {"content": str, "next_action": str}."""
    name: str
    description: str
    params: dict                      # JSON Schema properties
    required: list[str]
    fn: Callable[[dict], dict] = field(repr=False, default=None)


SUBMIT = Tool("submit_answer", "Submit the final answer. Call this once you have gathered enough information.",
              {"answer": {"type": "string"}}, ["answer"], None)


def _retry_call(fn):
    """In-loop API calls retry with the same params as llm.chat (4 exponential backoffs); only exhaustion counts as infra."""
    for attempt in Retrying(stop=stop_after_attempt(4),
                            wait=wait_exponential(multiplier=1, min=2, max=20), reraise=True):
        with attempt:
            return fn()


_COLLAPSED_MARK = "[context guardrail: this tool result has been collapsed; re-read it if needed]"


def _shrink_messages(messages: list, budget_chars: int) -> None:
    """Context guardrail: when total history chars exceed the budget, collapse tool results starting from
    the oldest into short summaries until back within budget.
    Prevents long-history snowballing -> API over-limit -> infra free-pass (models with short context get systematically favored)."""
    def _total():
        return sum(len(json.dumps(m, ensure_ascii=False, default=str)) for m in messages)
    if _total() <= budget_chars:
        return
    for m in messages:
        if _total() <= budget_chars:
            return
        # OpenAI form: role=tool plain-text result
        if m.get("role") == "tool" and isinstance(m.get("content"), str) \
                and len(m["content"]) > 400 and _COLLAPSED_MARK not in m["content"]:
            m["content"] = m["content"][:160] + "\n…" + _COLLAPSED_MARK
            continue
        # Claude form: role=user with content being a list of tool_result blocks
        if m.get("role") == "user" and isinstance(m.get("content"), list):
            for blk in m["content"]:
                if isinstance(blk, dict) and blk.get("type") == "tool_result" \
                        and isinstance(blk.get("content"), str) \
                        and len(blk["content"]) > 400 and _COLLAPSED_MARK not in blk["content"]:
                    blk["content"] = blk["content"][:160] + "\n…" + _COLLAPSED_MARK
                    if _total() <= budget_chars:
                        break


@dataclass
class _Turn:
    """A protocol-agnostic representation of one model response."""
    text: str
    tool_calls: list          # [(call_id, name, args_dict)]
    input_tokens: int
    output_tokens: int


class _ClaudeAdapter:
    def __init__(self, model: str, system: str, tools: list[Tool], max_tokens: int):
        self.model, self.system, self.max_tokens = model, system, max_tokens
        self.schemas = [{"name": t.name, "description": t.description,
                         "input_schema": {"type": "object", "properties": t.params,
                                          "required": t.required}} for t in tools]
        self.client = llm._anthropic_client()

    def init_messages(self, user: str) -> list:
        return [{"role": "user", "content": user}]

    def call(self, messages: list) -> _Turn:
        # Do not pass temperature: new claude (sonnet-5 etc.) deprecated this param, passing it 400s
        # (consistent with the claude branch of _gen.generate).
        r = self.client.messages.create(model=self.model, max_tokens=self.max_tokens,
                                        system=self.system, messages=messages,
                                        tools=self.schemas)
        acontent, calls, text = [], [], ""
        for b in r.content:
            if b.type == "text":
                acontent.append({"type": "text", "text": b.text})
                text = text or b.text
            elif b.type == "tool_use":
                acontent.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
                calls.append((b.id, b.name, b.input or {}))
        messages.append({"role": "assistant", "content": acontent})
        return _Turn(text, calls, r.usage.input_tokens, r.usage.output_tokens)

    def append_results(self, messages: list, results: list) -> None:
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": cid, "content": content}
            for cid, content in results]})


class _OpenAIAdapter:
    def __init__(self, model: str, system: str, tools: list[Tool], max_tokens: int):
        self.model = model
        self.schemas = [{"type": "function", "function": {
            "name": t.name, "description": t.description,
            "parameters": {"type": "object", "properties": t.params,
                           "required": t.required}}} for t in tools]
        self.extra = ({"extra_body": {"max_completion_tokens": max_tokens}}
                      if model.lower().startswith("gpt-5")
                      else {"max_tokens": max_tokens, "temperature": 0.1})
        self.system = system
        self.client = llm._client

    def init_messages(self, user: str) -> list:
        return [{"role": "system", "content": self.system}, {"role": "user", "content": user}]

    def call(self, messages: list) -> _Turn:
        r = llm.next_client().chat.completions.create(model=self.model, messages=messages,
                                                tools=self.schemas, tool_choice="auto",
                                                **self.extra)
        msg = r.choices[0].message
        messages.append(msg.model_dump())
        calls = []
        for tc in (msg.tool_calls or []):
            try:
                args = json.loads(tc.function.arguments)
            except json.JSONDecodeError:
                args = {}
            calls.append((tc.id, tc.function.name, args))
        tin = r.usage.prompt_tokens if r.usage else 0
        tout = r.usage.completion_tokens if r.usage else 0
        return _Turn(msg.content or "", calls, tin, tout)

    def append_results(self, messages: list, results: list) -> None:
        for cid, content in results:
            messages.append({"role": "tool", "tool_call_id": cid, "content": content})


class ToolLoop:
    """Tool loop executor. run() returns (final_answer, usage, trace, wall_time_s)."""

    def __init__(self, model: str, system: str, tools: list[Tool],
                 max_iter: int | None = None, max_tokens: int | None = None,
                 ctx_chars: int | None = None):
        self.model = model
        self.system = system
        self.tools = {t.name: t for t in tools}
        if SUBMIT.name not in self.tools:
            tools = list(tools) + [SUBMIT]
            self.tools[SUBMIT.name] = SUBMIT
        self.tool_list = tools
        self.max_iter = max_iter or config.AGENT_MAX_ITER
        self.max_tokens = max_tokens or config.AGENT_MAX_TOKENS
        self.ctx_chars = ctx_chars or config.AGENT_CTX_CHARS
        self.max_total_tokens = config.AGENT_MAX_TOTAL_TOKENS   # per-question cumulative token cap (guard against non-convergence blowup)
        self.max_wall_s = config.AGENT_MAX_WALL_S               # per-question wall-time cap

    def _adapter(self):
        cls = _ClaudeAdapter if self.model.lower().startswith("claude") else _OpenAIAdapter
        return cls(self.model, self.system, self.tool_list, self.max_tokens)

    def run(self, user: str) -> tuple[str, dict, list, float]:
        t0 = time.time()
        ad = self._adapter()
        messages = ad.init_messages(user)
        tin = tout = 0
        log: list = []
        final = ""
        for it in range(self.max_iter):
            # per-question total budget guardrail (audit P2-1): stop when cumulative tokens / wall-time exceed limits, record giveup, same rule for all models, prevent runaway
            if self.max_total_tokens and (tin + tout) >= self.max_total_tokens:
                final = f"[ERROR] Agent loop stopped: total-token budget {self.max_total_tokens} exceeded"
                break
            if self.max_wall_s and (time.time() - t0) >= self.max_wall_s:
                final = f"[ERROR] Agent loop stopped: wall-time budget {self.max_wall_s}s exceeded"
                break
            _shrink_messages(messages, self.ctx_chars)
            try:
                turn = _retry_call(lambda: ad.call(messages))
            except Exception as e:
                final = f"[ERROR] API call failed at iteration {it}: {e}"
                break
            tin += turn.input_tokens
            tout += turn.output_tokens
            if not turn.tool_calls:
                final = turn.text or ""
                break
            results = []
            for cid, name, args in turn.tool_calls:
                if name == "submit_answer":
                    final = args.get("answer", "")
                    log.append({"tool": "submit_answer", "iteration": it})
                    results.append((cid, "Answer submitted."))
                    break
                tool = self.tools.get(name)
                if tool is None or tool.fn is None:
                    res = {"content": f"[ERROR] Unknown tool: {name}",
                           "next_action": "Check available tools."}
                else:
                    res = tool.fn(args)
                log.append({"tool": name, "args": args, "iteration": it,
                            "result_chars": len(res["content"])})
                resp = res["content"] + (f"\n\n[next_action]: {res['next_action']}"
                                         if res.get("next_action") else "")
                results.append((cid, resp))
            ad.append_results(messages, results)
            if final:
                break
        if not final:
            final = "[ERROR] Agent loop ended without producing an answer"
        usage = {"input_tokens": tin, "output_tokens": tout}
        return final, usage, log, time.time() - t0


def run_loop_answer(model: str, system: str, tools: list[Tool], question_text: str,
                    approach: str, max_iter: int | None = None):
    """Convenience wrapper: run the loop and pack it into an AnswerResult."""
    from .base import AnswerResult
    loop = ToolLoop(model, system, tools, max_iter=max_iter)
    final, usage, log, wall = loop.run(f"Please answer the following question:\n\n{question_text}")
    return AnswerResult(final, approach, tokens=usage, cost_usd=compute_cost(usage, model),
                        wall_time_s=wall, trace=log)
