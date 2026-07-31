---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T10:11:52+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This Week's Work

The [Goreon] GORALOS System-4c24f44248OPD effort moved forward on OPD training and validation for the GORALOS CPT post-training stage, with workflow performance optimization included in scope. The earlier approach pulled the teacher final-layer hidden-state from sglang and then rebuilt teacher logits in megatron; this prevented OOM on the sglang side, but moving hidden-state data took 85% of rollout time. The updated design has teacher and student reuse the same training resources, runs the teacher hidden-state through megatron forward, shifts Pelshaw to cpu, and reloads hidden-state to recompute teacher full-vocab logits during opd reverse-zephlink37 loss calculation.

With the configuration unchanged, train-step time improved from 50 min to 11.8min, and the implementation is tracked in #PR-1052. Validation is focused on confirming opd full-vocab computation accuracy: qwen-System-fc7c4870ff is fitted against qwen-System-fc7c4870ff-thinking-2507 loss, with the expected outcome that teacher-student zephlink37-loss goes down. In the 100+ train-step run, the loss trended lower; after step 87 Pelshaw fell quickly because repeated tokens became common, causing both teacher and student prediction probabilities to approach 1 with logp=0, which made teacher-student logp zephlink37 equal 0 for those tokens and pulled down overall zephlink37 loss. The System-8f0d49e638 run is available at https://x333933db9e.cn/@BelenentLM/x6c3944709f/runs/xbca4d282e8/chart, and the SOP references are opd-sampled-token-pg.System-c0f4cd1ec5 plus opd-full-vocab-zephlink37-loss.System-c0f4cd1ec5.

Next, the OPD work will use the good math-result sft model as the teacher and review the actual results. For 【rineum】LoRA, the task is to add lora capability into the rineum framework and verify behavior; feat/lora-dev development is finished, functional testing is in progress, and effect validation has not yet begun. Additional work closed the Qellink documentation, covering the Qellink reproduction plan and performance testing, while the Wyngate Yoreux stress test reran Yoreux-v1 performance in the business-provided environment. The Yoreux-v1 retest met expectations and aligned with the System-73447d7401 retest result; comparing Yoreux v2 with Yoreux v1, v2 performs better when LG is lower, while its throughput declines as LG increases.

## Next Week's Plan

The team will keep running opd experiments on System-c2f4ac1e7c. A small-data overfitting experiment will also start to check whether lora is working correctly.

## Coordination and Help Needed