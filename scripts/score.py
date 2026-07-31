"""Unified scorer (P1.3, subsumes the four close relatives score_mm22/score_v3/score_genreval/score_oracle22):

  python scripts/score.py --root eval_export/myrun --models gpt-5.5,glm-5.2 \
      --pipes rag,agentic_rag,okf \
      --bank dataset/golden_packets.jsonl --questions dataset/questions.json

- Scores <root>/<model>/answers/*.md by src.evaluator's current rubric -> eval_answer_only.jsonl;
- --questions defaults to the full bank; --deterministic scores only MULTI types (a judge-free smoke test);
- when trace.jsonl exists, retrieval context is automatically rebuilt for the grounded gate (get_page/get_wiki_page both accepted);
- prints a pipeline x model summary table at the end (oracle and measured runs are readable in the same table; the report side splits them into columns).
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import evaluator, llm          # noqa: E402


def _safe(s: str) -> str:
    return re.sub(r"[^0-9A-Za-z一-鿿_.-]+", "-", str(s)).strip("-")


def load_questions(path: str | None, bank: dict) -> list[str]:
    if not path:
        return list(bank)
    qs = json.load(open(path, encoding="utf-8"))
    if isinstance(qs, dict):
        qs = qs.get("questions", [])
    return [q["id"] if isinstance(q, dict) else q for q in qs]


def load_traces(model_dir: Path) -> dict:
    """(id, approach) -> [doc paths]. Agent-family uses the source-document stem; okf keeps the bundle conceptual path
    (evaluator._okf_map normalizes it to the source document). Tool names get_page / get_wiki_page both accepted."""
    tr = {}
    tf = model_dir / "trace.jsonl"
    if not tf.exists():
        return tr
    for l in open(tf, encoding="utf-8"):
        d = json.loads(l)
        paths = []
        for c in (d.get("trace") or []):
            if c.get("tool") in ("get_page", "get_wiki_page"):
                p = str((c.get("args") or {}).get("path", ""))
                if p.endswith(".md"):
                    keep_full = str(d.get("approach", "")).startswith(("okf", "oracle_okf"))
                    paths.append(p if keep_full else p.rsplit("/", 1)[-1][:-3])
        tr[(d["id"], d.get("approach"))] = list(dict.fromkeys(paths))
    return tr


def score_model(model_dir: Path, bank: dict, qids: list[str], pipes: list[str],
                deterministic: bool, use_traces: bool, eval_suffix: str = "") -> list[dict]:
    ans_dir = model_dir / "answers"
    if not ans_dir.exists():
        raise SystemExit(f"no answers directory {ans_dir}")
    traces = load_traces(model_dir) if use_traces else {}
    skipped = {}
    try:                                    # oracle exclusion set (abstention/oracle_excluded not counted as a missing answer)
        skipped = json.loads((model_dir / "oracle_skipped.json").read_text(encoding="utf-8"))
    except Exception:
        skipped = {}
    jobs, missing = [], []
    for gid in qids:
        gp = bank.get(gid)
        if not gp:
            continue
        _is_set = gp["operator"] in evaluator.MULTI or bool((gp.get("set_scoring") or {}).get("required_items"))
        if deterministic and not _is_set:   # deterministic = score only set questions (same predicate as the evaluator's routing, P2-1)
            continue
        for ap in pipes:
            if gid in (skipped.get(ap) or {}):          # legitimately excluded for this pipeline, not counted as missing
                continue
            f = ans_dir / f"{_safe(gid)}__{ap}.md"
            if f.exists():
                jobs.append((gid, gp, ap, f.read_text(encoding="utf-8")))
            else:
                missing.append((gid, ap))               # an answer that should exist but is missing -- do not silently skip
    if missing:
        print(f"[score] WARNING {model_dir.name}: {len(missing)} expected answers missing (sample {missing[:3]}); "
              f"the denominator includes the missing items and the mean may be affected -- suggest completing the run first", flush=True)

    def _score(job):
        gid, gp, ap, ans = job
        if evaluator.is_infra_error(ans):
            return {"id": gid, "operator": gp["operator"], "approach": ap,
                    "infra_error": True, "headline": None, "scores": {}, "violations": {},
                    "hard_fail": False, "diagnostics": {}}
        mo = {"answer": ans}
        docs = traces.get((gid, ap))
        if docs is not None:
            mo["retrieved_contexts"] = [{"rank": i + 1, "doc_id": d} for i, d in enumerate(docs)]
        r = evaluator.evaluate(gp, mo, track=gp.get("track", "answer_only"))
        # judge infrastructure error: handle as infra (drop from the denominator, do not score the model 0), same convention as generation-phase infra
        if (r.get("diagnostics") or {}).get("judge_infra_error"):
            return {"id": gid, "operator": gp["operator"], "approach": ap,
                    "infra_error": True, "judge_infra_error": True, "headline": None,
                    "scores": {}, "violations": {}, "hard_fail": False,
                    "diagnostics": r.get("diagnostics", {})}
        return {**{k: v for k, v in r.items()}, "approach": ap}

    recs = [r for r in llm.pmap(_score, jobs) if r]
    # P1-3: light retry on judge infrastructure failures (converges transient flakiness; <=2 rounds, only re-scores judge_infra records)
    job_by = {(gid, ap): (gid, gp, ap, ans) for (gid, gp, ap, ans) in jobs}
    for _rnd in range(2):
        retry = [job_by[(r["id"], r["approach"])] for r in recs
                 if r.get("judge_infra_error") and (r["id"], r["approach"]) in job_by]
        if not retry:
            break
        print(f"[score] {model_dir.name}: judge_infra retry {len(retry)} records (round {_rnd+1})")
        fixed = {(r["id"], r["approach"]): r for r in llm.pmap(_score, retry) if r}
        recs = [fixed.get((r["id"], r["approach"]), r) for r in recs]
    suffix = (".det" if deterministic else "") + eval_suffix
    ef = model_dir / f"eval_answer_only{suffix}.jsonl"
    # Merge-write: keep existing records for pipelines not scored this time, only update this round's records by (id, approach)
    # (historical pitfall: overwriting by --pipes would wipe other pipelines' scores; after switching to merge, scoring a subset no longer loses scores)
    merged: dict = {}
    if ef.exists():
        for line in ef.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                old = json.loads(line)
            except json.JSONDecodeError:
                continue
            merged[(old.get("id"), old.get("approach"))] = old
    for r in recs:
        merged[(r.get("id"), r.get("approach"))] = r
    ef.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in merged.values()) + "\n",
                  encoding="utf-8")
    n = sum(1 for r in recs if r.get("headline") is not None)
    print(f"[score] {model_dir.name}: this round {len(recs)} records (scorable {n}); {len(merged)} records total after file merge -> {ef.name}")
    return recs, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", required=True, help="evaluation output root (contains <model>/answers)")
    ap.add_argument("--models", required=True, help="comma-separated")
    ap.add_argument("--pipes", required=True, help="comma-separated")
    ap.add_argument("--bank", default="dataset/golden_packets.jsonl")
    ap.add_argument("--questions", default=None, help="official question-set json; defaults to the full bank")
    ap.add_argument("--deterministic", action="store_true", help="score only MULTI types (judge-free)")
    ap.add_argument("--no-traces", action="store_true", help="do not rebuild retrieval context from traces")
    ap.add_argument("--eval-suffix", default="", help="output filename suffix (e.g. .judge_gpt55), isolates different judges' scores without overwriting")
    ap.add_argument("--allow-incomplete", action="store_true",
                    help="allow scoring with missing/infra (default is nonzero exit; do not publish an incomplete mean)")
    args = ap.parse_args()

    bank = {json.loads(l)["id"]: json.loads(l)
            for l in open(ROOT / args.bank, encoding="utf-8")}
    qids = load_questions(args.questions, bank)
    pipes = [p.strip() for p in args.pipes.split(",")]
    # P2-2: independently compute the expected pair count from bank eligibility (not relying on the skip file), used to assert the task set was not silently shrunk
    _ORACLE = {"oracle_rag", "oracle_agentic_rag", "oracle_okf", "lc_oracle"}
    def _oracle_ok(qid):
        r = bank.get(qid) or {}
        return r.get("answer_status") != "unanswerable" and not (r.get("_provenance") or {}).get("oracle_excluded")
    # P2-1/P2-2: deterministic scores only "set questions"; the predicate must exactly match the evaluator's set routing
    # (op in MULTI or set_scoring.required_items), otherwise an op-only filter would match 0 questions
    def _is_set(q):
        r = bank.get(q) or {}
        return r.get("operator") in evaluator.MULTI or bool((r.get("set_scoring") or {}).get("required_items"))
    eqids = [q for q in qids if _is_set(q)] if args.deterministic else qids
    indep_expected = sum((sum(1 for q in eqids if _oracle_ok(q)) if p in _ORACLE else len(eqids))
                         for p in pipes)
    table = defaultdict(dict)
    completeness = {}
    incomplete = []
    for m in [m.strip() for m in args.models.split(",")]:
        recs, missing = score_model(Path(args.root) / m.replace("/", "_"), bank, qids, pipes,
                                    args.deterministic, not args.no_traces, args.eval_suffix)
        agg = defaultdict(list)
        n_scored = n_infra = 0
        for r in recs:
            if r.get("headline") is not None:
                agg[r["approach"]].append(r["headline"]); n_scored += 1
            elif r.get("infra_error"):
                n_infra += 1
        for p, v in agg.items():
            table[p][m] = round(sum(v) / len(v), 4)
        # F3 completeness: expected = scored (including giveup scored 0) + infra + missing
        expected = n_scored + n_infra + len(missing)
        # P2-2: compare against indep_expected computed independently from the bank; a mismatch = the task set was silently shrunk / contains out-of-set ids -> judged incomplete
        completeness[m] = {"expected": expected, "indep_expected": indep_expected, "scored": n_scored,
                           "infra": n_infra, "missing": len(missing),
                           "expected_match": expected == indep_expected}
        if n_infra or missing or expected != indep_expected:
            incomplete.append(m)
    print("\n===== pipeline x model (headline mean) =====")
    print(json.dumps({p: table[p] for p in pipes if p in table}, ensure_ascii=False, indent=1))
    print("\n===== completeness (expected/scored/infra/missing) =====")
    print(json.dumps(completeness, ensure_ascii=False, indent=1))
    # completeness not passed: write a .incomplete name, do not occupy the official score_summary.json (review P0-2: prevents an incomplete mean from being misused)
    out_name = "score_summary.json" if not incomplete else "score_summary.incomplete.json"
    (Path(args.root) / out_name).write_text(
        json.dumps({"table": dict(table), "completeness": completeness,
                    "complete": not incomplete, "incomplete_models": incomplete},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    if incomplete and not args.allow_incomplete:
        raise SystemExit(f"[score] completeness gate failed: {incomplete} has infra/missing -> wrote {out_name} (unofficial); "
                         f"re-score after patching, or add --allow-incomplete to override")


if __name__ == "__main__":
    main()
