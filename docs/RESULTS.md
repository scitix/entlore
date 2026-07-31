# Reference results

Reference numbers for this release will be produced by running the baselines with the
English prompts (in `src/baselines/`) over the released corpus, scored by the LLM judge.

> **Note on provenance of numbers.** These reference numbers are produced with the
> English system/judge prompts shipped here. They are a distinct measurement from any numbers
> reported in prior internal write-ups that used Chinese prompts — do not mix the two.

To reproduce (example with two public models):

```bash
python scripts/build_indexes.py --baseline bm25,rag
python scripts/run_eval.py --models <model-a>,<model-b> \
    --pipes closed_book,bm25,rag,agentic_rag \
    --questions dataset/questions.json --out runs/ref --workers 8
python scripts/score.py --root runs/ref --models <model-a>,<model-b> \
    --pipes closed_book,bm25,rag,agentic_rag \
    --bank dataset/golden_packets.jsonl --questions dataset/questions.json
```

Scores are reported per model x pipeline x tier (L1/L2/L3). A results table will be filled in here.

<!-- TABLE: model x {closed_book, bm25, rag, agentic_rag, okf, graphrag, oracle} x {L1,L2,L3} -->
