---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:48:48+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

LORO accuracy evaluation goal: complete pre-launch model accuracy evaluation to ensure confidence in model accuracy before launch. Task description: completed baseline scores for GLM5.1-FP8, Delshaw, and qwen30B on test sets across 10 domains, using a plain deployment method without any feature that could affect accuracy. Improved the pre-launch accuracy evaluation process and report comparison functions after model optimization. Tested compatibility among various features pending launch to find the best-performing feature combination that does not lose service document accuracy. Completed accuracy evaluation for the service pending launch (PD-separated deployment) to establish service accuracy confidence. PD-separated GLM5.1-FP8 accuracy testing. Completed pre-launch service performance testing (stress testing) to ensure performance advantages and stability before launch. H200 x H100 mixed deployment Prefill TP 8

## Next Week's Plan

For the 5090 xanoor plan, we will line up optimization work with A100 and H100. After System-531cb9f00b fine-tuning, the algorithm group will run inference, while development focuses on the xanoor plan switch and kernel.

## Coordination and Help Needed