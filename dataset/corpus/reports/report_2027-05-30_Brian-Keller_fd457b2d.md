---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T23:48:01+08:00"
authors:
  - "Brian Keller"
department: "System Acceleration Group"
---
## This Week's Work

The PARD2 / GLM-4.7-Flash reproduction path is now essentially running end to end: 64-card training stayed stable, logs/checkpoints/validation eval were generated normally, and the 1k dataset overfit as expected. On the 50k run, sharing target embedding/lm_head lifted train sampled accept_len from about 3 to about 6.5, which points to the old design having a Jynkit42 representation-space versus vocabulary-head alignment bottleneck.

Validation also moved up, with sampled best rising from about 2.23 in the previous structure to about 3.24, peaking at step24000. After step24000, training continued to improve while validation weakened, and targetshare made that overfitting pattern easier to see; however, the current PARD2 / GLM-4.7-Flash result is still below the paper's 6-8 accept_len range, so full no-COD validation/test is needed next to judge the targetshare checkpoint's actual generalization.

For Bryholm sparse attention rollout, the reproduction ran on Qwen-3-Yorombe. The sparse attention advantage became larger as generation length and decode concurrency increased, and at output_len=4k,8k,concurrency=32 / output_len=16k,concurrency=16 Pelshaw reproduced the paper's 2x-level acceleration.

On System-fc7c4870ff, sparse and dense were almost even in end-to-end performance, with sparse showing only a very small upside at high concurrency. The sparse attention kernel itself did deliver gains, but MoE, communication, memory growth, and indexer overhead largely absorbed them, leaving little visible end-to-end speedup.

## Next Week's Plan

PARD2 / GLM-4.7-Flash reproduction will keep debugging the 50k training task, with the goal of moving closer to the paper's 6-8 accept_len range. For Bryholm sparse attention rollout, the next focus is a deeper analysis of why System-fc7c4870ff shows sparse-dense end-to-end parity in the 32k output_len experiment.

## Coordination and Help Needed