"""Unified evaluation runner (P1.3): model x pipeline x question set x concurrency, reproducible from a single command in the repo.

  python scripts/run_eval.py --models gpt-5.5,glm-5.2 --pipes rag,agentic_rag,okf \
      --questions dataset/questions.json --out eval_export/myrun --workers 32

- Outputs are split per model: <out>/<model>/answers/*.md + tco.jsonl + trace.jsonl (same convention as cli run);
- oracle_* pipelines automatically filter to the testable set (abstention/oracle_excluded removed); the filter list is written to oracle_skipped.json,
  with a hard pointer-purity assertion at startup (refuse to run if it cannot be parsed);
- Paths (dataset/index/bundle) all go through the single EKWB_* env-var table in src/baselines/config.py.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

_QPATH = None   # question-set path (used for the hash recorded in run_manifest; assigned in main)
# F8: key source files frozen at runtime (hashes written into run_manifest to distinguish uncommitted changes). Filled out to cover the files actually involved in the run (review P2-1).
_SRC_FILES = ["scripts/run_eval.py", "scripts/score.py", "src/baselines/loop.py",
              "src/baselines/oracle.py", "src/baselines/rag.py", "src/baselines/graphrag.py",
              "src/baselines/toolkits.py", "src/baselines/config.py", "src/baselines/_gen.py",
              "src/baselines/bm25.py", "src/baselines/agentic_rag.py", "src/baselines/okf.py",
              "src/baselines/base.py", "src/baselines/corpus.py", "src/corpus_index.py",
              "src/corpus_construction.py", "src/metrics.py", "src/operators/operator_registry.py",
              "src/evidence_anchors.py", "src/evaluator.py", "src/validators.py",
              "src/llm.py", "src/config.py"]
_SRC_HASHES_AT_START = None   # snapshot at process start (not read from disk at the end; review P2-1)
_INPUT_HASHES_AT_START = None # snapshot of the input surface (bank/questions/corpus/index) at startup (review P1-4)

from src import llm                                      # noqa: E402
from src import evaluator                                 # noqa: E402
from src.baselines import get_baseline                    # noqa: E402
from src.baselines import config as bcfg                  # noqa: E402
from src.baselines.corpus import Corpus                   # noqa: E402


def _sha(p) -> str | None:
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:16]
    except Exception:
        return None


def _input_hashes() -> dict:
    """Hash snapshot of the input surface (bank/questions/corpus manifest + each index's meta and **data files**; review P1-4)."""
    def h(*parts):
        return _sha(Path(*[p for p in parts if p]))
    b, r, o, g = bcfg.BM25_INDEX_DIR, bcfg.RAG_INDEX_DIR, bcfg.OKF_BUNDLE_DIR, bcfg.GRAPHRAG_DIR
    return {
        "questions": _sha(_QPATH), "bank": _sha(os.environ.get("EKWB_BANK")),
        "corpus_manifest": h(bcfg.CORPUS_DIR, "_manifest.json"),
        "bm25": {"meta": h(b, "index_meta.json"), "chunks": h(b, "chunks.jsonl")},
        "rag": {"meta": h(r, "index_meta.json"), "chunks": h(r, "chunks.jsonl"),
                "embeddings": h(r, "embeddings.npy")},
        "okf": {"manifest": h(Path(o).parent, "okf_manifest.json"),
                "vindex_emb": h(str(o) + "_vindex", "embeddings.npy"),
                "vindex_chunks": h(str(o) + "_vindex", "chunks.jsonl")},   # the data surface read online (review P2-4)
        "graphrag": {"manifest": h(g, "graphrag_manifest.json"),
                     "entities": h(g, "entities.jsonl"), "relationships": h(g, "relationships.jsonl"),
                     "communities": h(g, "communities.jsonl"), "text_units": h(g, "text_units.jsonl"),
                     "reports": h(g, "community_reports.jsonl"),
                     "entities_emb": h(g, "entities_index", "embeddings.npy"),
                     "entities_chunks": h(g, "entities_index", "chunks.jsonl"),
                     "reports_emb": h(g, "reports_index", "embeddings.npy"),
                     "reports_chunks": h(g, "reports_index", "chunks.jsonl")},
    }


def _git_rev() -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"],
                                       text=True).strip()
    except Exception:
        return None


def _safe(s: str) -> str:
    return re.sub(r"[^0-9A-Za-z一-鿿_.-]+", "-", str(s)).strip("-")


def load_questions(path: str) -> list[dict]:
    qs = json.load(open(path, encoding="utf-8"))
    return qs.get("questions", []) if isinstance(qs, dict) else qs


def run_model(model: str, pipes: list[str], questions: list[dict], out: Path, workers: int,
              allow_incomplete: bool = False, no_clear: bool = False):
    corpus = Corpus()
    # P0.3: by default forbid implicit reuse of old answers -- clear the output directory each run, to avoid contamination from same-named answers of the previous round.
    # Patch mode (--no-clear): keep reused answers, only overwrite this subset (used only when running specific question ids).
    ans_dir = out / "answers"
    if ans_dir.exists() and not no_clear:
        for f in ans_dir.glob("*.md"):
            f.unlink()
    out.mkdir(parents=True, exist_ok=True)
    ans_dir.mkdir(exist_ok=True)
    bls, jobs, skipped_all = {}, [], {}
    for p in pipes:
        bls[p] = get_baseline(p, corpus=corpus, model=model)
        qset = questions
        if hasattr(bls[p], "filter_questions"):           # oracle: testable-set filter + purity assertion
            qset, skipped = bls[p].filter_questions(questions)
            skipped_all[p] = skipped
            print(f"[run] {p}: testable {len(qset)} (excluded {len(skipped)}: abstention/oracle_excluded)")
        jobs += [(p, q) for q in qset]
    # oracle exclusion list: in patch (no_clear) mode **merge** with the existing one, to prevent a single-pipeline subset patch from clearing other pipelines' skips (review P0-1)
    sk_path = out / "oracle_skipped.json"
    merged_sk = {}
    if no_clear and sk_path.exists():
        try:
            merged_sk = json.loads(sk_path.read_text(encoding="utf-8"))
        except Exception:
            merged_sk = {}
    for _p, _sk in skipped_all.items():          # qid-level union (not a top-level overwrite; review P0-1)
        merged_sk[_p] = {**(merged_sk.get(_p) or {}), **_sk}
    if merged_sk:
        sk_path.write_text(json.dumps(merged_sk, ensure_ascii=False, indent=1), encoding="utf-8")

    def _one(job):
        ap, q = job
        try:
            r = bls[ap].answer(q)
        except Exception as e:
            return {"id": q["id"], "approach": ap, "status": "exception", "error": repr(e)[:200]}
        # F2: API failure (loop returns [ERROR] ...) counts as generation_infra, **do not write an answer file** (leave a gap to be patched later);
        # agent giveup (budget/loop exhausted) = a real task failure, write the file and score 0; everything else is normal.
        if evaluator.is_infra_error(r.answer):
            return {"id": q["id"], "approach": ap, "status": "generation_infra",
                    "error": r.answer.strip()[:160]}
        status = "agent_giveup" if evaluator.is_agent_giveup(r.answer) else "ok"
        (ans_dir / f"{_safe(q['id'])}__{ap}.md").write_text(r.answer, encoding="utf-8")
        tk = r.tokens or {}
        rec = {"id": q["id"], "approach": ap, "model": model, "status": status,
               "cost_usd": round(r.cost_usd, 5), "tokens": int(sum(tk.values())),
               "tokens_in": int(tk.get("input_tokens", 0)), "tokens_out": int(tk.get("output_tokens", 0)),
               "wall_time_s": round(r.wall_time_s, 2), "context_chars": r.context_chars}
        if r.trace is not None:
            rec["_trace"] = r.trace
        return rec

    print(f"[run] model={model}: {len(jobs)} generations (workers={workers})", flush=True)
    # P0.4: as_completed writes to disk in real time; P0.2: tally by F2's four classes (ok/giveup/generation_infra/exception)
    from collections import Counter as _Ctr
    cnt = _Ctr()
    # patch (no_clear) mode: **append** to tco/trace (do not overwrite, keep cost/trace of all rounds; review P0-2)
    _mode = "a" if no_clear else "w"
    with open(out / "tco.jsonl", _mode, encoding="utf-8") as tco_f, \
         open(out / "trace.jsonl", _mode, encoding="utf-8") as trace_f, \
         ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = {ex.submit(_one, j): j for j in jobs}
        done = 0
        for fut in as_completed(futs):
            rec = fut.result()
            done += 1
            cnt[rec.get("status", "ok")] += 1
            tr = rec.pop("_trace", None)
            if tr is not None:
                trace_f.write(json.dumps({"id": rec["id"], "approach": rec["approach"], "trace": tr},
                                         ensure_ascii=False) + "\n"); trace_f.flush()
            tco_f.write(json.dumps(rec, ensure_ascii=False) + "\n"); tco_f.flush()
            tag = ("ERR[" + rec.get("status", "?") + "]:" + rec.get("error", "") if rec.get("error")
                   else f"${rec.get('cost_usd')} {rec.get('tokens')}tok {rec.get('wall_time_s')}s")
            print(f"[{done}/{len(jobs)}] {rec['approach']:18} {rec['id'][:32]:32} {tag}", flush=True)

    n_ok = cnt["ok"]; n_giveup = cnt["agent_giveup"]
    n_gen_infra = cnt["generation_infra"]; n_exc = cnt["exception"]
    n_ans = len(list(ans_dir.glob("*.md")))
    # conservation = all questions land in ok or giveup (no generation_infra, no exception); gen_infra/exception are gaps to be patched
    conserved = (len(jobs) == n_ok + n_giveup + n_gen_infra + n_exc) and n_gen_infra == 0 and n_exc == 0
    manifest = {
        "model": model, "pipes": pipes, "mode": "patch" if no_clear else "full",
        "planned": len(jobs), "generated_ok": n_ok, "agent_giveup": n_giveup,
        "generation_infra": n_gen_infra, "exception": n_exc, "answer_files": n_ans,
        "skipped": {p: len(s) for p, s in skipped_all.items()},
        "conserved": conserved,
        "hashes": _INPUT_HASHES_AT_START,     # snapshot of the input surface (including data files) at startup (review P1-4)
        "src_hashes": _SRC_HASHES_AT_START,   # F8: snapshot at process start (not read from disk at the end)
        "run_config": {   # review P1-2: key run config goes into the manifest to guarantee reproducibility
            "agent_max_iter": bcfg.AGENT_MAX_ITER, "oracle_max_iter": bcfg.ORACLE_MAX_ITER,
            "agent_max_total_tokens": bcfg.AGENT_MAX_TOTAL_TOKENS,
            "agent_max_wall_s": bcfg.AGENT_MAX_WALL_S, "agent_ctx_chars": bcfg.AGENT_CTX_CHARS,
            "oracle_max_chars": bcfg.ORACLE_MAX_CHARS, "rag_top_k": bcfg.RAG_TOP_K,
            "bm25_top_k": bcfg.BM25_TOP_K, "bm25_k1": bcfg.BM25_K1, "bm25_b": bcfg.BM25_B,
            "search_top_k": bcfg.SEARCH_TOP_K, "gen_max_tokens": bcfg.GEN_MAX_TOKENS,
            "lc_oracle_max_chars": bcfg.LC_ORACLE_MAX_CHARS, "max_context_chars": bcfg.MAX_CONTEXT_CHARS,
            "group": bcfg.GROUP, "chunk_size": bcfg.CHUNK_SIZE, "chunk_overlap": bcfg.CHUNK_OVERLAP,
            "agent_max_tokens": bcfg.AGENT_MAX_TOKENS, "embed_model": bcfg.RAG_EMBED_MODEL,
            "graphrag_report_topk": getattr(bcfg, "GRAPHRAG_REPORT_TOPK", None),
            "graphrag_local_topk": getattr(bcfg, "GRAPHRAG_LOCAL_TOPK", None),
            "graphrag_level": getattr(bcfg, "GRAPHRAG_LEVEL", None),
            "graphrag_max_glean": getattr(bcfg, "GRAPHRAG_MAX_GLEAN", None),
            "graphrag_max_cluster": getattr(bcfg, "GRAPHRAG_MAX_CLUSTER", None),
            "judge_model": getattr(__import__("src").config, "JUDGE_MODEL", None),
        },
        "git_rev": _git_rev(),
    }
    # patch runs write a dedicated patch name, not overwriting the full-run manifest (review P0-2); closure is proven by the driver's closure_manifest
    mf_name = "run_manifest.json" if not no_clear else f"run_manifest.patch.{'-'.join(pipes)[:40]}.json"
    (out / mf_name).write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[run] {model} conservation: planned{len(jobs)}=ok{n_ok}+giveup{n_giveup}+gen_infra{n_gen_infra}"
          f"+exc{n_exc} | answers={n_ans} | conserved={conserved}", flush=True)
    if not conserved and not allow_incomplete:
        raise SystemExit(f"[run] completeness gate failed (model={model}): {n_gen_infra} generation_infra + "
                         f"{n_exc} exception to be patched; add --allow-incomplete to override")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--models", required=True, help="comma-separated models under test")
    ap.add_argument("--pipes", required=True,
                    help="comma-separated: rag,agentic_rag,okf,oracle_rag,oracle_agentic_rag,oracle_okf")
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out", required=True, help="output root directory (split into per-model subdirectories)")
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--allow-incomplete", action="store_true",
                    help="override non-conserved runs / runs with model_fail (default is nonzero exit)")
    ap.add_argument("--only-ids", default=None,
                    help="patch mode: run only these question ids (comma-separated, or @file with one id per line)")
    ap.add_argument("--no-clear", action="store_true",
                    help="patch mode: do not clear the answers directory (reuse existing answers, overwrite only this subset)")
    args = ap.parse_args()
    global _QPATH, _SRC_HASHES_AT_START, _INPUT_HASHES_AT_START
    _QPATH = args.questions
    _SRC_HASHES_AT_START = {f: _sha(ROOT / f) for f in _SRC_FILES}   # freeze source hashes at startup
    _INPUT_HASHES_AT_START = _input_hashes()                         # freeze input/index data-surface hashes at startup
    questions = load_questions(args.questions)
    if args.only_ids:
        raw = args.only_ids
        ids = (set(l.strip() for l in open(raw[1:], encoding="utf-8") if l.strip())
               if raw.startswith("@") else set(x.strip() for x in raw.split(",") if x.strip()))
        questions = [q for q in questions if q["id"] in ids]
        print(f"[run] patch subset: {len(questions)} questions (--only-ids)")
    pipes = [p.strip() for p in args.pipes.split(",")]
    for m in [m.strip() for m in args.models.split(",")]:
        run_model(m, pipes, questions, Path(args.out) / m.replace("/", "_"), args.workers,
                  allow_incomplete=args.allow_incomplete, no_clear=args.no_clear)


if __name__ == "__main__":
    main()
