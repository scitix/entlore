#!/usr/bin/env bash
# Minimal end-to-end smoke test (~10 chat calls + ~10 judge calls, a few cents).
#
# Verifies your environment is wired correctly BEFORE spending money on a full run:
#   1. build_indexes  -> bm25 index builds offline (no embedding endpoint needed)
#   2. run_eval       -> closed_book (model creds) + bm25 (retrieval) over 5 questions
#   3. score          -> deterministic gates + LLM judge (JUDGE_MODEL) produce a mean
#
# Uses only closed_book + bm25, so NO embedding endpoint is required (rag/graphrag/okf do).
# closed_book is expected to score ~0 (parametric floor) — a nonzero bm25 mean means it works.
#
# Usage:
#   cp .env.example .env    # fill in API_BASE/API_KEY + ANTHROPIC_* + JUDGE_MODEL
#   scripts/smoke.sh [MODEL_UNDER_TEST]      # default: gpt-4o-mini
set -euo pipefail
cd "$(dirname "$0")/.."

MODEL="${1:-${EKWB_SMOKE_MODEL:-gpt-4o-mini}}"
QS="dataset/smoke.json"
OUT="runs/smoke"

if [ ! -f .env ]; then
  echo "[smoke] no .env found — copy .env.example to .env and fill in credentials first." >&2
  exit 1
fi

echo "[smoke] 1/3 building bm25 index (offline, no LLM)..."
python scripts/build_indexes.py --baseline bm25

echo "[smoke] 2/3 running model=$MODEL over 5 questions (closed_book + bm25)..."
python scripts/run_eval.py --models "$MODEL" \
    --pipes closed_book,bm25 \
    --questions "$QS" --out "$OUT" --workers 4

echo "[smoke] 3/3 scoring (deterministic gates + LLM judge)..."
python scripts/score.py --root "$OUT" --models "$MODEL" \
    --pipes closed_book,bm25 \
    --bank dataset/golden_packets.jsonl --questions "$QS"

echo
echo "[smoke] OK — pipeline is wired. See $OUT/score_summary.json"
echo "[smoke] (a clean pass writes score_summary.json; score_summary.incomplete.json means some calls failed)"
