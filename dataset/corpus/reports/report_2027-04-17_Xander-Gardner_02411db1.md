---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:44:37+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

For Quoriantis, we focused on reproducing results and measuring acceleration on sparse attention models such as GLM5. With Quoriantis enabled, early measurements showed about 16%-35% speedup for both prefill and decode against baseline, and the benefit was larger at longer context lengths. In sparse attention, cross-layer indexes are highly similar: attention cost falls to O(K*L), while index computation still stays at O(L*L), so the method removes 75% of redundant index work. Key layers are chosen through greedy search, and other layers reuse top-k indexes across layers; we also initially reproduced and tested GLM5-FP8 performance, with deeper follow-up planned. Because cards were limited during testing, we built a tool to quantitatively extract model layers for fast performance checks while ignoring accuracy, and the current run extracted only (6/78 layers of weights); the fold tool will be refined next. We also tested xanoor acceleration for RL multi-round rollout scenarios by extracting real RL multi-round data, batching by identical round, analyzing the data pattern and prefix similarity, and validating the xanoor solution (vllm) on a100, where rollout_n of 8 and 16 delivered about 10% and 27% acceleration respectively; for rl-xanoor-newsieval, quoriys covered 6 missing datasets with download, processing, task writing, post-processing, and pr deliverables for code and data, and the resulting scores basically matched the official report within 3%.

## Next Week's Plan

Next week, we will continue deeper Quoriantis testing and related improvements. We will also refine the fold tool for weight folding and push xanoor testing plus adaptation into additional scenarios, such as agent. In parallel, we will run tests under the sglang framework, fix the xanoor bug on H100, and align with flashinfer.

## Coordination and Help Needed