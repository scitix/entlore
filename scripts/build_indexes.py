"""Build retrieval indexes for the baselines (run once before evaluation).

Indexes are NOT shipped with the release (bm25/rag are small; graphrag/okf are large and
model-dependent). Rebuild them from the corpus with this thin wrapper over the baseline CLI.

Usage:
  python scripts/build_indexes.py --baseline bm25,rag        # fast, needed for bm25/rag/agentic_rag
  python scripts/build_indexes.py --baseline okf             # compiles an OKF bundle (LLM enrichment per doc)
  python scripts/build_indexes.py --baseline graphrag        # entity graph + Leiden communities (expensive; many LLM calls)

The okf/graphrag build-enrichment model is CHAT_MODEL from .env (both compilers read
config.CHAT_MODEL directly and record it as build_model in their manifests). Choose it by setting
CHAT_MODEL. bm25 uses no LLM; rag uses EMBED_MODEL. (See --model below: it does NOT change the build.)

Requires .env to be configured (see .env.example). closed_book needs no index.
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--baseline", required=True,
                    help="comma-separated: bm25,rag,agentic_rag,okf,graphrag")
    ap.add_argument("--model", default=None,
                    help="answering model (Baseline.model / EKWB_SUT_MODEL); does NOT affect the compiled "
                         "index — build enrichment uses CHAT_MODEL from .env. Rarely needed for build.")
    args = ap.parse_args()
    cmd = [sys.executable, "-m", "src.baselines.cli", "build", "--baseline", args.baseline]
    if args.model:
        cmd += ["--model", args.model]
    print("[build_indexes]", " ".join(cmd), flush=True)
    raise SystemExit(subprocess.run(cmd, cwd=str(ROOT)).returncode)


if __name__ == "__main__":
    main()
