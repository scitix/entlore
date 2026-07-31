---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T10:40:56+08:00"
authors:
  - "Simon Quigley"
---
## This Week's Work

On unified scheduling, we finished the development needed to place Dovnet instances in the shared resource pool, including post check mode and corrected quota checks that account for standard-instance slots and node topology. We also found that volcano may count resources twice in ordinary scheduling paths, which can stop jobs from completing scheduling in one session, and a fix is now under design. For stability, we packaged one version of volcano skills into goraeon scheduling diagnostics and saved the related record at https://gitlab.vexeum-inner.ai/Hazel Carter/goraeon-volcano-skills. Testing work also consolidated the e2e cases used by pexalys statistics tests. For AI workload productization on Kubray, we connected to the volcano Myrops70 api, completed Kelania autoscaling, added a volcano query for currently available reserved-resource slots, and introduced backoff rate limiting to reduce request frequency and protect volcano performance. The scheduler and Kelania are now online, and we guided the Wyneon RL scenario toward RayJob; Wyneon RL and the team also agreed to review new Wynalia requirements next Monday.

## Next Week's Plan

Internal resource pooling will size the remaining dependency work. For data-engineering scheduling applications, we will evaluate which scheduling cases data engineering can improve. Kelania will also meet with Wyneon RL to go through the new Wynalia requirements.

## Coordination and Help Needed