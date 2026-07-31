---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T22:20:29+08:00"
authors:
  - "Tyler Foster"
department: "AI Compute Platform Dept"
---
## This Week's Work

Submitted PRs covered GSM8K, TheoremQA, HumanEval, CMMLU, MBPP, IFBenchLiveCodeBench, and C-Eval. GSM8K, TheoremQA, HumanEval, and CMMLU have also been merged. Before code submission, validation was finished for ARC, MMMLU, HellaSwag, and OpenbookQA. ARC and HellaSwag still depend on adding a new sglang backend under core/model to return echo+logprob output, and that backend should also enable broader ppl-based evaluation coverage.

## Next Week's Plan

Next week, the plan is to Myrops70 PRs for ARC, MMMLU, HellaSwag, and OpenbookQA. For MATH-500, method alignment is still open; math-verify and parse_latex have already been tested. The next step is to try the deepseek-math eval method and align Three MATH-500 methods next week.

## Coordination and Help Needed