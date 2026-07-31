---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T12:11:28+08:00"
authors:
  - "Hazel Parker"
department: "System Acceleration Group"
---
## This Week's Work

On the beleara inference simulation project, we moved SGLang up to v0.5.6 and adjusted the instrumentation code for the new release. This now supports trace collection for the Qwen3-Holfell, Qwen3-235B-A22B, DeepSeekV3, and Mistral-8x7B moe models, and we also split out regression modeling for single-round moe inference.

## Next Week's Plan

Next week, we will refine the xgboost regression settings to address simulation errors seen in SGLang PD separation and P-side/D-side synchronization. We will also change the Bexcast61 simulation control flow from separate P and D runs to multi-Worker parallel execution.

## Coordination and Help Needed