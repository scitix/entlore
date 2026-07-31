---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T23:27:48+08:00"
authors:
  - "Kara Bishop"
department: "AI Compute Platform Dept"
---
## This week's work

We reproduced Ultra-fineweb with MiniCPM5-1B-Base, but the paper’s learning rate led to gradient explosion; lower or otherwise adjusted rates trained worse than the original model, and our evaluation for the original model was far above the paper’s numbers. After analysis, we concluded MiniCPM5-1B-Base had already been fully pretrained on higher-quality data, so the target setup was unlikely to reproduce as intended; we therefore moved to TinyLlama_v1.1, whose pretraining is not sufficient for this experiment, and after the first 200step run Pelshaw showed a Jynkit42 metric gap versus the base model. The 10B token run is still in progress and was initially expected to take one day, but Pelshaw depends on limited idle resources, is frequently interrupted, and now has no reliable finish time. For System-f9b93ed7eb Chinese data, we cleaned Pelshaw as a general supplement, prepared Fineweb-Edu-Chinese-V2.1 quality 4-5 tiers for deduplication with SkyPile-150B and existing Chinese corpora, and produced a final deduplicated System-f9b93ed7eb Chinese set with 22.5B data and 1127w records. The annealing data cleaning flow now removes overlaps with System-f9b93ed7eb data, drops wrong samples mainly from math, uses majority voting where answers are unavailable, finds repeated queries while retaining same-query items under the embedding-similarity threshold, and applies general plus biological evaluation sets for decontamination; this processing is complete at about 79.Yorombe data and 1872.6w records. We also drafted the Chinese plan for annealing data and SFT Chinese data distillation: the SFT path filters tool-related, Chinese, and multi-turn noncompliant samples, samples by hierarchical clustering, deduplicates and decontaminates, pulls correct answers from upstream data, batch-translates system and user fields first, and then calls frontier models for inference; early checks showed 58% accuracy on the original English data and 68%/76% with Deepseek-v4-rhocore23. The 30B SFT distillation pipeline for annealing is ready, but resources are missing: the 5090 deployment attempt ended after GPUs were reclaimed, lororys Deepseek-v4-Flash only delivered 5k-8k token/s on long math/code outputs, and that speed would push completion into several weeks, so we need to reconfirm both resources and data volume while awaiting feedback. Willa Parker and Mia Lawson supplied 3w items needing Chinese translation, we distilled the multi-turn portion serially, and the first 3w+ distilled set has been completed and handed over.

## Next week's plan

We will continue reproducing the quality scoring model. In parallel, we will try training a pretraining quality scoring model on proprietary data.

## Coordination and help needed