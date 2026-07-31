"""Baseline CLI: build (offline prepare) / run (answer a question set, producing the same answers/tco/trace as run_answers).

  python -m src.baselines.cli build --baseline rag
  python -m src.baselines.cli build --baseline rag
  python -m src.baselines.cli run   --baseline rag,agentic_rag,okf \\
         --questions dataset/questions_official_v2.json --out eval_export/v3_eval --workers 4
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src import config as _cfg          # noqa: E402
from src.baselines import get_baseline, REGISTRY  # noqa: E402
from src.baselines import config as bcfg          # noqa: E402
from src.baselines.corpus import Corpus           # noqa: E402
from src import llm                                # noqa: E402


def _safe(s: str) -> str:
    return re.sub(r"[^0-9A-Za-z一-鿿_.-]+", "-", str(s)).strip("-")


def cmd_build(args):
    corpus = Corpus()
    if not corpus.exists():
        raise SystemExit(f"[build] corpus does not exist: {corpus.root} (first run scripts/export_dataset.py)")
    for name in args.baseline.split(","):
        name = name.strip()
        bl = get_baseline(name, corpus=corpus, model=args.model)
        if not hasattr(bl, "prepare"):
            continue
        print(f"[build] {name} prepare() ...", flush=True)
        bl.prepare()


def cmd_run(args):
    corpus = Corpus()
    questions = json.load(open(args.questions, encoding="utf-8"))
    if isinstance(questions, dict):
        questions = questions.get("questions", [])
    approaches = [a.strip() for a in args.baseline.split(",")]
    out = Path(args.out); (out / "answers").mkdir(parents=True, exist_ok=True)
    bls = {a: get_baseline(a, corpus=corpus, model=args.model) for a in approaches}
    # oracle pipelines: testable-set filter + pointer-purity hard assertion (abstention/oracle_excluded removed, refuse to run if unresolvable)
    qsets, skipped_all = {}, {}
    for a in approaches:
        if hasattr(bls[a], "filter_questions"):
            qsets[a], skipped_all[a] = bls[a].filter_questions(questions)
            print(f"[run] {a}: testable {len(qsets[a])} (excluded {len(skipped_all[a])})")
        else:
            qsets[a] = questions
    if skipped_all:
        (out / "oracle_skipped.json").write_text(
            json.dumps(skipped_all, ensure_ascii=False, indent=1), encoding="utf-8")

    def _one(job):
        ap, q = job
        qid = q["id"]
        try:
            r = bls[ap].answer(q)
        except Exception as e:
            return {"id": qid, "approach": ap, "error": repr(e)[:200]}
        (out / "answers" / f"{_safe(qid)}__{ap}.md").write_text(r.answer, encoding="utf-8")
        tk = r.tokens or {}
        rec = {"id": qid, "approach": ap, "model": args.model, "cost_usd": round(r.cost_usd, 5),
               "tokens": int(sum(tk.values())),
               "tokens_in": int(tk.get("input_tokens", 0)), "tokens_out": int(tk.get("output_tokens", 0)),
               "wall_time_s": round(r.wall_time_s, 2), "context_chars": r.context_chars}
        if r.trace is not None:
            rec["_trace"] = r.trace
        return rec

    jobs = [(a, q) for a in approaches for q in qsets[a]]
    print(f"[run] {len(questions)} questions x {approaches} = {len(jobs)} generations (model={args.model})", flush=True)
    tco_f = open(out / "tco.jsonl", "w", encoding="utf-8")
    trace_f = open(out / "trace.jsonl", "w", encoding="utf-8")
    done = 0
    for rec in llm.pmap(_one, jobs, workers=args.workers):
        done += 1
        tr = rec.pop("_trace", None)
        if tr is not None:
            trace_f.write(json.dumps({"id": rec["id"], "approach": rec["approach"], "trace": tr},
                                     ensure_ascii=False) + "\n"); trace_f.flush()
        tco_f.write(json.dumps(rec, ensure_ascii=False) + "\n"); tco_f.flush()
        tag = "ERR:" + rec["error"] if rec.get("error") else f"${rec.get('cost_usd')} {rec.get('tokens')}tok {rec.get('wall_time_s')}s"
        print(f"[{done}/{len(jobs)}] {rec['approach']:6} {rec['id'][:34]:34} {tag}", flush=True)
    tco_f.close(); trace_f.close()
    print(f"\nanswers -> {out/'answers'} | TCO -> {out/'tco.jsonl'} | trace -> {out/'trace.jsonl'}")


def main():
    ap = argparse.ArgumentParser(description="EKWB self-contained baseline CLI (bm25/rag/agentic_rag/okf/graphrag)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="offline preparation (bm25/rag build index / agentic_rag validate / okf / graphrag compile)")
    b.add_argument("--baseline", required=True, help="bm25 / rag / agentic_rag / okf / graphrag (comma-separated)")
    b.add_argument("--model", default=bcfg.SUT_MODEL,
                   help="answering model (Baseline.model); does NOT affect the compiled index — "
                        "okf/graphrag build enrichment uses CHAT_MODEL from .env")
    b.set_defaults(func=cmd_build)
    r = sub.add_parser("run", help="answer a question set")
    r.add_argument("--baseline", required=True, help=f"comma-separated, options: {sorted(REGISTRY)}")
    r.add_argument("--questions", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--model", default=bcfg.SUT_MODEL)
    r.add_argument("--workers", type=int, default=4)
    r.set_defaults(func=cmd_run)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
