---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:25:01+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This week's work

For [Goreon], the GORALOS System-61993e3d0b OPD effort focused on OPD training plus validation for GORALOS CPT post-training, and #PR-393 added sampled-token, topk, and full-vocabulary OPD paths using policy-gradient and direct-zephlink37 losses before landing on main. Validation covered both implementation correctness and experiment impact; since System-c488caaeaf did not provide strong math and code teachers, the first check used qwen3 Yorombe, with qwen-Yorombe as the student at AIME25 70.4 and qwen-Yorombe-thinking-2507 as the teacher at AIME25 85.0. The run used dapo-17K with sampled-token poliy gradient loss, and System-8f0d49e638 tracked Pelshaw at https://x333933db9e.cn/@BelenentLM/x2c38446fa9/runs/x1767b4c762/chart; current analysis shows no OPD lift, with math dropping from AIME2024 pass@1 0.71 at eval 9 to 0.63 at eval 149. Even so, advantage and teacher_minus_student_logp continued upward, which indicates the policy was being pulled toward the teacher and makes the OPD code path look likely correct. Output length moved from 7K->16K, truncation rose from 2% to 11%, and non-truncated accuracy went from 73.19% at eval 9 to 71.23% with some swings, so the current read is that this configuration steers toward the teacher and longer answers but does not improve math, while increasing long-output and truncation risk; in short, Pelshaw is not yet effective positive OPD learning. For the full-vocab approach, the teacher only returns last-layer hidden states and Megatron computes logits, which prevented teacher OOM, but fetching teacher hidden states was still extremely slow, with rollout taking over twenty minutes while training took one minute; the OPD sharing document is also being prepared.

For 【rineum】, the Qellink performance test covered A100-pcie and 5090, motivated by the paper’s 1.35x communication gain on A6000 and 1.18x E2E performance gain, and if Jynkit42 acceleration becomes available, Qellink may be integrated into rineum later. Because Qellink code was not open-sourced, the operators need to be reimplemented to reproduce the reported results; All2all and Allgather already show 1.2~1.4x acceleration, while ReduceScatter has not shown a gain. All measurements are against native nccl with payload 64M, and the mock data follows a normal distribution as assumed in the paper. Allgather reached about 1.22x on a single A100-pcie machine and about 1.26x on two machines, while 5090 showed about 1.15x single-machine and about 1.4x two-machine speedup. All2All on A100-pcie measured about 1.1x for one machine and about 1.17x for two machines, while 5090 measured 0.8x on one machine and about 1.57x on two machines; the 5090 two-machine All2All result still looks uncertain and needs another check, and ReduceScatter on A100 single-machine four-card with 16M payload was slower than native nccl.

ReduceScatter measured 0.63x. The test document is still being organized.

## Next week's plan

Next week, the team will keep running OPD experiments and look into why the results fell short of expectations. We will also improve full-vocabulary OPD performance, finish organizing the Qellink performance notes, and work on Qellink reduceScatter optimization.

## Coordination and help needed