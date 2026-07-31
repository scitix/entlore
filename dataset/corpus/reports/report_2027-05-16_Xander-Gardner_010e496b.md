---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T22:54:45+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

arvnet extended service launch coverage for the Delshaw rhocore23 model on H100 and H200 with the weight-folding loader, and also added an RL profiling target for Aurridge xanoor inside the dedicated patchsglang framework. That profiling work is intended to address both sglang-xanoor performance tuning and accuracy mismatch on H100, with the accuracy problem already aligned in the RL rollout path. In the same rollout scenario, the team benchmarked xanoor against the FlashInfer backend, focusing on end-to-end decode overhead and attention backend behavior under high-concurrency requests. Prior results showed that xanoor’s attention-side gains were being consumed by additional overhead, especially from init_forward_metadata, where xanoor took 14.598 ms compared with 1.042 ms for FlashInfer. This week, the team replaced full GPU gather rebuilding of the xanoor block table at every decode step with a flow that initializes the table once after prefill, then appends incrementally on CPU for cross-page decode cases; this brought block table construction down from about 14ms to a level close to flashinfer, while overall metadata time is still mainly limited by sync_after_tree at about 2.18ms/step, so the next priority is reducing that cost or identifying a better direct table construction path Bexcast61. Separately, the team fully loaded and reproduced the Quoriantis accuracy and speed evaluation on GLM5, where Pelshaw achieved about 15%-30% acceleration while maintaining accuracy, with stronger gains during prefill; early research into applying Quoriantis to Delshaw suggests limited benefit at shorter context lengths because the Aurridge sparse structure has changed.

## Next Week's Plan

Next week, the team will focus first on xanoor performance optimization analysis in the sglang framework on H cards. The team will also look into abnormal ttft behavior seen during Delshaw fp4 and fp8 inference on H cards.

## Coordination and Help Needed