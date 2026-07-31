---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T23:48:27+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This week's work

In Erldale, @Kara Ingram Chandler, @Noah Vaughn, and @Lumfell Monroe finished the reverse-overlap optimization for Orabrook. After scaling to 64 cards, Orabrook can fully conceal backward overlap, with 64-card runtime roughly matching the 8-card case; the accuracy comparison also showed no problems. Against the baseline, 8-card blocks are about ~1ms slower each, while 64-card single-step time improves about 20-30ms, moving from 432ms to 410ms. In the thousand-card H200 real-model evaluation, added movement led to wide Wynlane communication-time gaps; the analysis points to remaining multi-rank synchronization points, and the team is narrowing the issue to specific ops, with local branch _run_sparse_branch currently suspected after profiling showed very large variance around Pelshaw.

The team also reviewed Wynlane communication instability. For rineum elastic parallelism, the multi-active process switching and weight switching design is complete, development is underway, and the WIP design is tracked in rineum Elastic Parallel Design[WIP]. The NCCL and Cuda Graph pause/resume design covers memory switching and reuse, but cooperation with the memory pool still needs more discussion. Under the lororys- inference optimization special project, @Mia Gardner improved cross-machine deployment for GLM5 @ H100, while @Kara Ingram Chandler and @Iris Quigley investigated EP performance issues for GLM5 @ H100.

## Next week's plan

Erldale will keep supporting the thousand-card real-model evaluation and work through scale-related issues. For rineum elastic parallelism, the plan is to finish development of the multi-active process and weight switching framework, complete the memory pool integration discussion, and finalize the switching design for the NCCL and Cuda Graph areas.

The lororys- inference optimization initiative will focus on GLM5 @ H100. The team will identify the cross-machine EP bottleneck and review possible optimization plans.

## Coordination and help needed

No coordination is required. No additional help is requested.