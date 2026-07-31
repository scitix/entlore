---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T15:54:11+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work
(2026-05-19 recap)Close MR accuracy gap via new architecture: current best variant with 1.7x speedup and 5.9% better precision (on SPICE validation force loss)new merged_post_loop modeSwiGLU-S2 activationOther architecture exploration: only fused subgraph + FAISS landed on the main dev branch; decoupled cutoff radius, bf16 autocast, layerwise shared KV, re-compute path were tried but not adopted)Distributed inference support for MRcorrectness fix for cross-node MR softmaxMR-aware partitioning + eval pipelineScale up: continual pretraining of previous stage-2 baseline model on new Velmol25 140M dataset

## Next Week's Plan
Next week, the plan is to bring together MoE and mixed-resolution three-stage curriculum training for Verombe. The work will include mixed-resolution, MoE, and different model parameter volumes.

## Coordination and Help Needed