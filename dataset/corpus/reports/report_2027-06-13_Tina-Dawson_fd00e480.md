---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T18:37:15+08:00"
authors:
  - "Tina Dawson"
department: "System Acceleration Group"
---
## This week's work

The team investigated Corthorne long-text optimization for the new speculative inference path and reviewed additional directions with Aiden Holt, drawing on mimo open source plus prior long-text speculative inference work. For long-context training, the current plan covers long-context data and SWA window attention, while SWEBench per-turn acceptance-rate shifts confirmed degradation in Corthorne long-text capability. We also used Draft OPD as the starting point for Corthorne post-training and examined how Dovsys user speculative decoding data can improve speculative draft models for both a single version and multiple versions. Early single-version optimization results are available from Corthorne and MTP post-training; in post-training settings, OPD performs better than SFT and raises Corthorne accepted length by 14%. The team is now applying past speculative inference data to newly released speculative inference models, has gathered cross-version data for Qwen 3.5 and Qwen3.6, and analyzed similarities such as rejection positions and rejection entropy given their broadly similar architectures.

## Next week's plan

Next week, the team will use historical old-version user speculative decoding data to improve new-version speculative decoding performance. This work depends on similarity across model versions. We will also collect and review MTP post-training papers.

## Coordination and help needed