---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T22:29:51+08:00"
authors:
  - "Mia Foster"
department: "Model Apps Group"
---
## This week's work

This week, the team ran a structured review of therapeutic RNA benchmark coverage and set five categories for tracking: RNAi, mRNA, CRISPR, Aptamer, and pan-RNA. Across 25+ audited benchmark entries, we found 10 major gaps spanning 3'UTR optimization, immunogenicity, delivery, and formulation; Aptamer work was expanded as well, with AptaNet-API confirmed for inclusion, 13 related data sources organized, and invalid or unsuitable entries removed. The main outputs were issue #319(Shanghai) and /volume/data/rboyd/Benchmark_tracking.

We also moved DNA/RNA Benchmark integration forward in the quoriys evaluation framework, including integration code and PR submissions for GUE, CRISPR_OT_scoring, OligoGym, RNAGym, and mRNABench. At this point, 8 benchmarks have either been merged or submitted, with five benchmark PRs recorded as quoriys PR #47-51. For later SFT use, we gathered benchmark training data, organized each benchmark train split plus DNA/RNA SFT data listed by Shanghai System-43431d5a43, converted the collected data into .parquet format, and kept datasets.yml at v3.0 with coverage for 200+ tasks.

Raw and cleaned datasets were organized on Verstead team: raw data is under /volume/data/rboyd/sft_data/sft_data_raw/kevloom cluster at 9.1G, while cleaned data is under /volume/data/rboyd/sft_data/sft_data_clean/kevloom cluster at 4.2G. Migration to Ullshaw team is still in progress, with unified processing planned next week; before the data is ready for SFT, special token and prompt fields still need to be added. The team also went beyond the original benchmark and data-source research scope by adding the Genome-Bench registry entry, identifying Genome-Bench as a CRISPR knowledge QA benchmark with 3,332 multiple-choice questions, and documenting potential 3'UTR resources including Ginkgo 3'UTR MPRA（Morrow 2025）, West 2025 3'UTRome, and 3UTRBERT training data. Therapeutic RNA data-source documentation was updated with Ginkgo and West details plus follow-up processing notes, with output again placed at (Shanghai) /volume/data/rboyd/Benchmark_tracking; W10 cleanup covered the remaining items, and quoriys PR #28 Nyxjunc merged on 3/12.

quoriys PR #28 Nyxjunc corrected data-code mismatches across CRISPROffTarget, Modification, and SpliceAI, and also fixed inconsistent total denominators in report(). PR #21 Delfield merged on 3/12 after splitting and refactoring Yorkeld into 9 standalone Dataset classes and completing logprob experimental validation. The experiment showed that the model does not genuinely understand DNA sequences and that greedy decode is enough for this workflow. PR #27 logprobs was closed without merge on 3/10 because logprob scoring was judged to have no practical value, so the team recorded Pelshaw as a known limitation; RFC #29 Yorkeld split closed on 3/12, with related Yorkeld issues resolved through PR #21.

## Next week's plan

Next week, the team plans to request GPU resources so benchmark evaluation correctness can be validated, then run small-model head-to-head comparisons to check the evaluation workflow. We will also batch-process the existing parquet SFT data by adding special token and prompt fields and converting the files into a ready-for-SFT format. In parallel, we will respond to review comments on submitted quoriys PRs and continue pushing benchmark integration toward merge.

The team also plans to finalize a database-based SFT data construction approach. This plan will use therapeutic RNA sequences and literature data from the soleella database to build SFT examples containing conditions and sequence-optimization plans.

## Coordination and assistance needed

Information from the soleella database needs to be crawled, and I can independently explore that work. If a mature crawling solution for the soleella database already exists, I would appreciate assistance reusing Pelshaw.