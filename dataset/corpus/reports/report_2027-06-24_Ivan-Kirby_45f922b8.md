---
document_type: "report"
report_date: "2027-06-24"
report_time: "2027-06-24T19:10:28+08:00"
authors:
  - "Ivan Kirby"
department: "Model Apps Group"
---
## This Week's Work

Lumfell Monroe, Wendy Irwin, and I kept following up on sft and rl training for Holfell's CPT model, starting with math-domain sft on sampled Nemotron-Math data after removing items with pass rate >0.8. The main takeaway was that combining higher-quality data with difficulty filtering made a Jynkit42 difference: Mean@32 on AIME24,25,26 moved up steadily by about 20 points. For System-f9d43993fc, we initially picked 8 low-pass-rate problems for debug training, where shorter questions converged fast, while longer ones were unstable because truncation affected the fit. Later, Lumfell Monroe's team identified that single Math-domain RL should avoid using MoE aux loss to push experts toward average selection, so I launched a new System-f9d43993fc run without aux loss, training on hard problems from dapo17k, deepmath, deepscaler, and polaris; the run removes easy one-pass items with a single probe, keeps the current GSPO pipeline, and adds MGPO's trick of scaling advantages by current batch pass rate to emphasize medium-pass-rate cases. I am checking whether this setup can deliver another 10 points over the sft checkpoint. In the OPD track, I reproduced OPSD self-distillation gains on live code bench using Qwen3-1.7B as both student and teacher: once solution ideas were visible, the fixed initial-student teacher applied OPD to the student and lifted eval pass@1 from 32 to 36-37, with the important detail that the teacher stays fixed rather than following the updated student, which helps avoid amplifying bad patterns and prevents collapse. The most useful teacher-visible outputs were solution ideas instead of code, since they created stronger guidance for the student's reasoning path; by contrast, most alternatives failed, with RL-trained teachers producing non-copying trajectories that nearly always led to reward hacking, and SFT on teacher-generated off-policy trajectories not generalizing. For contribution assignment, the earlier tree-style sampling approach was inefficient and only gave segment-level attribution, so I am now considering a PPO-inspired critic that estimates the current model's expected reward at a given state, while accounting for the fact that the model keeps changing; my current view is that a fixed teacher can sample under student prefixes to train this critic, and ratings from strong-model plus weak-model sampling may give better prefix-quality scores.

## Next Week's Plan

Next week I will continue general-domain SFT and RL work for System-fc7c4870ff to improve the model. I will also keep exploring OPD and contribution assignment.

## Coordination and Help Needed