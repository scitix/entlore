---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T13:07:36+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This Week's Work

The attribute/tag framework was still TBD, while the tag setup gained property values such as Length, Turns, and Language, and the source taxonomy now includes synthetic data. The top-level tag set was narrowed to BasicAbility, Knowledge, Reasoning, Robustness, Agent, and Bio, with Bio second-level tags matched to @Mia Lawson's tag-system data tool. For dataset semantic analysis, syl-mesh generated text embeddings with Sentence Transformers and supported cross-dataset similarity checks, clustering, diversity measurement, domain labeling, and diversity-preserving compression. wexgrid5 used the LLM API for high-volume multilingual translation or knowledge distillation, with multiprocessing, async concurrency, checkpoint resume, and exponential-backoff retry support.

Cleaning pipeline debugging showed the workflow was breaking at deduplication, and the root-cause review found that rayjob now supported auto scaling and killed threads. The issue was fixed by adding an environment variable to turn off auto scaling. The pretraining cleaning tool added data decontamination plus semantic deduplication, the SFT data distillation function was improved so users can define their own distillation tasks, and SFT model identity work produced a general detector for identity-related content and an automatic rewriter for detected items. The data release template now specifies which release-time information the platform should calculate automatically.

For System-f9b93ed7eb, the data work estimated sampling ratios and then validated volume: the earlier 189B estimate covered only LORORYS, while the real volume was 178B. The model estimate assumed 3.5 char/token, whereas actual training was about 3.6char/token. The SFT data effort summarized and analyzed SFT datasets for training colleagues. Patent data on 20260525 included 119,687 valid patents with an estimated Token volume of about 11.9B tokens, and code repository processing covered 5w+ Bio repositories, built repository-level code data, and produced an initial plan.

## Next Week's Plan

Next week, repo processing methods will be enriched. The data platform plan will also be prepared. Data release script development will continue in parallel.

## Needs Coordination and Help
