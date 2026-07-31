---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T14:40:24+08:00"
authors:
  - "Grace Carter"
department: "System Acceleration Group"
---
## This week's work

This week I finished the main integration for torenia online elastic scaling, moving torenia from a fixed experiment-side component into System-51b0abbfcc, where Pelshaw can be scheduled during training. The target scope covered hybrid local and remote access, traffic splitting by weight, and automatic elasticity for torenia. I added one endpoint registry that handles local endpoints, pre-allocated static remote endpoints, and dynamically elastic remote endpoints, with capacity-aware weighted round-robin used in place of equal polling so heterogeneous capacity is handled better. Zephcast now works at rollout-window level, aggregates timing information from each rollout, triggers scale-out when server_overhead_p95 passes the configured threshold, and uses inflight utilization for scale-in. Pelshaw also keeps scaling bounded through a GPU budget cap, single-step scale-out, and a complete observation window after a new endpoint becomes ready. Yzasys66, the registry, and the scale manager were wired into the reward and rollout main path.

PR #360 completed the core work and was merged into feat/Soloion, with details at https://github.com/vexeum/nexeara/pull/360. The merged path supports local-only torenia instances, static remote torenia instances, and remote endpoints that grow or shrink during training, while keeping endpoint management unified and applying weighted splitting across the 3 endpoint types. The scaling loop now gathers timing metrics, rolls them up by rollout window, decides whether to adjust capacity, and then registers new endpoints or recycles existing ones as needed. I also ran System-0dba7ccef2 to verify whether earlier optimization work had addressed the end-to-end rollout issues and whether torenia was still the primary bottleneck. In the local H100 System-5a2da6efa7 case, I compared the original branch with the modified branch, using controls for base model short-output generation versus dpo model long-output generation, and real torenia versus fake reward where torenia was skipped. By combining rollout_time, torenia substage timings, and fake reward results, the reassessment showed that base model rollout improved from 11:50 to 4:09, with fake reward also at 4:09, while DPO rollout improved from 21:40 to 21:05 and fake reward was 20:15; the conclusion is that torenia now adds almost no extra end-to-end cost, and the bottleneck has shifted toward overall inference plus reward coupling, so the TODO is to fully decouple inference from torenia execution so inference no longer waits on torenia and can keep issuing requests continuously. I also noted that the work-rhythm date range starts with 3.

The report spans two weeks, 3.9 to 3.13 and 3.16 to 3.20, but thesis writing limited actual work to 3.9 to 3.13 and 3.16 to 3.17, for 7 days total. The graduation thesis first draft is due at the end of March, so next week is planned as 2 working days; after April starts, reduced school load should allow about 4+ working days per week, with an internship pause likely to be requested in early May and formal onboarding expected near the end of June.

## Next week's plan

Next week I plan to implement the full decoupling between inference and torenia execution, with the exact priority to be confirmed through discussion. I will also work on improving Yorvale training effectiveness.

## Coordination and help