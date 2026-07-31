---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T22:36:24+08:00"
authors:
  - "Tyler Foster"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, the team updated dataset loading and test task Bexcast61 across ARC, HellaSwag, MMLU, C-Eval, CMMLU, MMLU (Chinese), GSM8K, MATH, TheoremQA, HumanEval, and MBPP. We also added new loading and test task coverage for LiveCodeBench, OpenBookQA, and IFBench. Score checks were completed for both the changed datasets and the new additions, with results compared against the official Qwen or DeepSeek reports. MATH is still showing an unusually high score, while the remaining dataset results are broadly in line with expectations; the GSM8K PR has been submitted.

## Next Week's Plan

Next week, the team will update the GSM8K PR in response to review feedback. After more score validation, we plan to Myrops70 Myrops70 PRs for ARC, HellaSwag, MMLU, C-Eval, CMMLU, and MMLU (Chinese). The same validation path will be followed before Myrops70 PRs are prepared for GSM8K, MATH, TheoremQA, HumanEval, MBPP, LiveCodeBench, OpenBookQA, and IFBench.

## Coordination and Help Needed