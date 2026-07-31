# EntLORE: A Graph-Grounded Benchmark for Latent Organizational Reasoning in Enterprise Question Answering

<p align="center">
  <img alt="License: MIT" src="https://img.shields.io/badge/Code-MIT-blue.svg">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg">
  <img alt="Documents" src="https://img.shields.io/badge/Corpus-2%2C341%20docs-success.svg">
  <img alt="Questions" src="https://img.shields.io/badge/Questions-907-success.svg">
  <a href="https://arxiv.org/abs/XXXX.XXXXX"><img alt="arXiv" src="https://img.shields.io/badge/arXiv-XXXX.XXXXX-b31b1b.svg"></a>
</p>

<p align="center">
  <b>Official code &amp; data repository</b> for the paper<br>
  <i>EntLORE: A Graph-Grounded Benchmark for Latent Organizational Reasoning in Enterprise Question Answering</i>
</p>

<p align="center">
  Akrin Zheng<sup>*</sup> &nbsp; Alexander Wu<sup>*</sup> &nbsp; Alaia Liu<sup>*†</sup> &nbsp;—&nbsp; <b>ScitiX.ai</b><br>
  <sub><sup>*</sup> Equal contribution &nbsp;·&nbsp; <sup>†</sup> Corresponding author: <a href="mailto:alaia.liu@scitix.ai">alaia.liu@scitix.ai</a></sub>
</p>

> **TL;DR.** Enterprise answers often depend on *organizational relations* that no single
> document states. EntLORE reconstructs an **audited enterprise truth graph** from routine
> documents, authoritative tables, and operational records, then releases an anonymized
> document world whose gold answers and proofs are computed from the graph — while the target
> derived relations are **withheld from evaluated systems**. Across 8 models × 7 knowledge-access
> conditions, **how the released world is organized matters more than how much retrieval
> machinery is applied to it** — and even perfect evidence leaves latent-relation questions
> unanswered.

📄 **Paper:** [arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX) &nbsp;·&nbsp; 📊 **Data & code:** this repository

---

## Overview

Enterprise question answering is usually framed as *retrieve relevant internal documents, then
generate a grounded answer*. But routine enterprise records are produced as **by-products of
work**, not self-contained descriptions. Many questions therefore cannot be answered from an
explicitly stated fact or a fixed chain of passages — their answers depend on relations that
connect local activities, internal terminology, project hierarchies, and ownership across
heterogeneous sources. We call this task **implicit enterprise process question answering** and
the missing capability **latent organizational reasoning**.

EntLORE is a **graph-grounded construction framework** that:

1. **Reconstructs an audited truth graph** from real enterprise documents, authoritative
   organizational tables, and operational records — separating *native*, *metadata*, *heuristic*,
   and *certified derived* relations.
2. **Derives only human-authorized relations** through versioned, organization-specific convention
   cards, yielding complete **golden answers and proof certificates**.
3. **Releases aligned, anonymized views** — the document corpus — while **withholding private
   structure and the target derived relations** from the systems under evaluation.

The released benchmark contains **2,341 documents** across **three enterprise source types**
(1,194 weekly reports · 794 knowledge-base pages · 353 incident tickets) and **907 questions**
spanning explicit lookup, cross-source composition, latent organizational reasoning, exhaustive
aggregation, evidence acquisition, and answer generation. The full evaluation matrix is **56
configurations** (8 answer models × 7 knowledge-access conditions).

## Key findings

- **Access *organization* beats retrieval *machinery*.** All five deployable conditions read the
  same corpus and differ only in how they index and present it. They split into two far-apart
  tiers: **BM25 (0.529), GraphRAG (0.522), LLM Wiki (0.509)** on top, **Agentic Retrieval (0.365)
  and flat dense RAG (0.360)** ~15 points below (tier-weighted overall).
- **Even perfect evidence leaves latent relations unanswered.** Supplying the gold documents
  (Oracle) still leaves **30.4% of latent (L3) questions unanswered**, versus **12.6%** for
  explicit (L1) and **6.2%** for compositional (L2) — the residual is *reasoning*, not retrieval.
- **Flat dense retrieval falls *below* a plain lexical index.** Released documents identify their
  organizational region through sparse anchors (project aliases, module names, ticket terms) that
  BM25 ranks first and a single dense space washes out.
- **Where documents stop helping, the ranking inverts.** 70% of L3 items resist flat retrieval (the
  target relation is stated in no released document). On that subset **GraphRAG leads (0.310)** and
  BM25 falls to 0.251 — GraphRAG answers with a relation it *materialized offline*, not by
  retrieving better. This is the sense in which EntLORE measures **relation recovery, not recall**.
- **A mismatched harness burns the budget reasoning would have used.** On non-retrievable L3 items,
  30-step agentic retrieval scores **0.088 — below the no-corpus closed-book floor (0.077)**.
- **The gap concentrates in hierarchy attribution.** Department attribution: lexical retrieval
  **0.02** vs. the induced graph **0.53**, on items the oracle answers 84% of the time.

## Main results

Overall answer accuracy by level, **averaged over 8 answer models**, for each knowledge-access
condition. Every deployable cell uses the full bank (L1 469 / L2 204 / L3 234); Oracle Ω is the
perfect-evidence ceiling (18 L3 items without a complete gold packet omitted, *n*=216). See the
paper for the full per-model table.

| Access condition | L1 | L2 | L3 |
|---|---:|---:|---:|
| Closed-book *(parametric floor)* | 0.006 | 0.000 | 0.079 |
| BM25 *(sparse lexical)* | **0.624** | 0.514 | 0.340 |
| RAG *(flat dense)* | 0.461 | 0.325 | 0.189 |
| Agentic Retrieval | 0.485 | 0.356 | 0.135 |
| LLM Wiki *(compiled offline KB)* | 0.617 | **0.525** | 0.277 |
| GraphRAG *(induced entity graph)* | **0.632** | 0.453 | **0.362** |
| Oracle Ω *(ceiling, excluded from ranking)* | 0.874 | 0.938 | 0.696 |

*Bold marks the best **deployable** condition per level (closed-book and Ω excluded). No single
condition owns a level; structural access leads L2/L3, lexical access is strongest on some L1.*

## What's in this repository

| Path | Contents |
|---|---|
| `dataset/corpus/` | 2,341 markdown documents (1,194 reports · 794 knowledge-base · 353 tickets) |
| `dataset/questions.json` | 907 questions (`{id, question}`) |
| `dataset/golden_packets.jsonl` | 907 gold packets — required facts, evidence pointers, proof/scoring mode |
| `dataset/SCHEMA.md` | field-level schema for the dataset |
| `src/baselines/` | the 7 access conditions + oracle upper bounds (self-contained) |
| `src/evaluator.py` | deterministic gates + LLM-judge scorer |
| `scripts/` | `build_indexes.py`, `run_eval.py`, `score.py`, `smoke.sh` |
| `third_party/` | vendored GraphRAG (MIT) and OKF (Apache-2.0) |

**Question tiers.** L1 (explicit fact, 469) · L2 (compose across facts, 204) · L3 (derive a latent
relation, 234). 62 operators (question types); 18 verified-unanswerable questions (abstention).
The truth graph behind construction holds **1,153 entities and 3,784 typed relations**.

**Access conditions** (paper name ↔ baseline id):

| Condition | Baseline id | Measures |
|---|---|---|
| Closed-book | `closed_book` | parametric-memory floor (no retrieval) |
| BM25 | `bm25` | naive sparse lexical retrieval |
| RAG | `rag` | flat dense top-*k* single-turn retrieval |
| Agentic Retrieval | `agentic_rag` | multi-turn autonomous tool loop over the dense index |
| LLM Wiki | `okf` | navigation loop over an LLM-compiled offline knowledge base |
| GraphRAG | `graphrag` | dual-tool loop over an induced entity graph + Leiden community reports |
| Oracle Ω | `oracle_rag` / `oracle_agentic_rag` / `oracle_okf` | perfect-evidence ceilings (gold packet fed directly) |

---

## Getting started

```bash
pip install -r requirements.txt
cp .env.example .env          # fill in your API endpoint(s) + model names
```

Model calls go through `src/llm.py`: point `API_BASE` at any OpenAI-compatible endpoint and
`ANTHROPIC_BASE_URL` at Anthropic (or a compatible relay). Endpoint routing is by model-name prefix
— `claude*` uses the Anthropic native protocol, everything else uses the OpenAI-compatible endpoint.

### Smoke test first (a few cents)

Verify credentials and the build→run→score wiring end-to-end on the 5-question subset
(`dataset/smoke.json`) before spending budget on the full run. It uses only `closed_book` + `bm25`,
so **no embedding endpoint is needed**:

```bash
scripts/smoke.sh <your-model>   # ~10 chat + ~10 judge calls
```

A clean pass writes `runs/smoke/score_summary.json` with `"complete": true`. A nonzero `bm25` mean
means retrieval + scoring work; `closed_book` is expected near 0.

### Full evaluation

```bash
# 1) build retrieval indexes (bm25/rag are fast; okf/graphrag are heavier, many LLM calls)
python scripts/build_indexes.py --baseline bm25,rag        # add okf,graphrag for the structured conditions

# 2) run a model over the access conditions
python scripts/run_eval.py --models <your-model> \
    --pipes closed_book,bm25,rag,agentic_rag,okf,graphrag,oracle_rag \
    --questions dataset/questions.json --out runs/main --workers 32

# 3) score (deterministic gates + LLM judge; set JUDGE_MODEL in .env)
python scripts/score.py --root runs/main --models <your-model> \
    --pipes closed_book,bm25,rag,agentic_rag,okf,graphrag,oracle_rag \
    --bank dataset/golden_packets.jsonl --questions dataset/questions.json
```

All paths and parameters are overridable via `EKWB_*` environment variables (single table in
`src/baselines/config.py`).

<details>
<summary><b>Configuration notes (build model, concurrency, thinking models)</b></summary>

- **`okf` / `graphrag` build model.** `bm25` uses no LLM and `rag` only calls the embedding endpoint
  (`EMBED_MODEL`); the `okf`/`graphrag` compilers run an LLM per document using **`CHAT_MODEL` from
  `.env`** (recorded as `build_model` in their manifests). `build_indexes.py --model` /
  `EKWB_SUT_MODEL` set the *answering* model and do **not** change the compiled index. An
  OpenAI-family `CHAT_MODEL` builds fine — routing is by name prefix.
- **Concurrency.** `run_eval.py --workers N` (default 32) sets question-level fan-out.
  `LLMWIKI_MAX_CONCURRENCY` (env) governs index build, embedding, and the judge. A comma-separated
  `API_KEY=k1,k2,k3` round-robins across keys to raise the effective rate limit. **Single-key
  users:** keep `--workers` ≈ 4–8 and `LLMWIKI_MAX_CONCURRENCY` low to avoid rate-limit errors.
- **Thinking models.** Set `EKWB_NO_THINK=1` to inject `enable_thinking=false` for open "thinking"
  models (Qwen/GLM) that otherwise burn their token budget on hidden reasoning and return empty
  completions. It is a no-op for `gpt-5*` and `claude*`.

</details>

### Bring your own system

Your system only needs to read `dataset/corpus/` and the question text in `dataset/questions.json`,
then emit one answer per question. Score it with `scripts/score.py` against
`dataset/golden_packets.jsonl`. To add it as a baseline, subclass `Baseline` and register with
`@register("name")` (see `src/baselines/`).

## Citation

If you use EntLORE, please cite:

```bibtex
@article{entlore2026,
  title   = {{EntLORE}: A Graph-Grounded Benchmark for Latent Organizational
             Reasoning in Enterprise Question Answering},
  author  = {Zheng, Akrin and Wu, Alexander and Liu, Alaia},
  journal = {arXiv preprint arXiv:XXXX.XXXXX},
  year    = {2026}
}
```

<sub>The arXiv identifier and paper link will be filled in once the preprint is posted.</sub>

## License and data statement

Code is released under the **MIT License** (see [`LICENSE`](LICENSE)). The corpus is **fully
synthetic and anonymized** (English): an audited real enterprise world is reconstructed into a
fictional organization, with persons, projects, aliases, and dates mapped through a shared identity
map and private metadata never verbalized into the documents. See [`NOTICE`](NOTICE) for the full
data statement and the licenses of vendored components (`third_party/`).
