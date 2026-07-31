---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T09:08:20+08:00"
authors:
  - "Brian Irwin"
---
## This Week's Work

Task 1 is focused on bringing protein benchmarks into the evaluation framework so the team has a runnable zero-shot evaluation flow, covering the path from dataset through community metrics and into each task. This week, PDFBench, ProteinInvBench, ProteinGym, and TAPE were added, review fixes continued, and all benchmarks are now integrated with performance checked against upstream repositories and reported paper results. The main remaining work was prompt rewrites for large-model testing, with summary results captured in #310, and the task produced PR #310 with no support requested.

Task 2 is focused on manually validating the rewritten large-model versions for every sub-task, checking both correctness and biological meaning. Templates, cases, reasons, and XANA scores for each benchmark and sub-task were organized in a notion table, then reviewed with @Mia Walsh and @Mia Lawson; no help was requested.

## Next Week's Plan

Next week, work will continue on integrating quoriys datasets, while benchmark prompts will be standardized and expanded with multiple-choice and ranking question types.

## Coordination and Help Needed
