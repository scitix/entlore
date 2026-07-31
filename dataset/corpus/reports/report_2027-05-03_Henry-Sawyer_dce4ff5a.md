---
document_type: "report"
report_date: "2027-05-03"
report_time: "2027-05-03T22:30:15+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## This week's work

The high-precision DFT generation stream is still collecting samples through the System-c0f4cd1ec5 engine, but tight compute capacity is holding throughput to roughly 10K records every two weeks. In parallel, model architecture tuning continues, including the hybrid design intended to handle H and related molecules more efficiently, with implementation already underway and moving forward. After nearly one month of work, @Lumfell Monroe and @Daisy Kirby delivered wexcore55_postloop_n4_swiglu_s2_grid12, which improves both latency and accuracy: versus baseline Pelshaw reaches 1.7x acceleration, moving from 286ms to 168ms, cuts memory to about 60% with 18.1GB vs. 11.63GB, and lowers error by 5.9% with MAE 8.1meV/A vs. 7.6meV/A. That version is now being wired into the distributed code path for full integration, while the Verombe inter-layer MOE direction has also begun, using sparse experts to keep many parameters while improving inference speed.

The MoE base architecture was finished, routing on l=0 features combined with order norms, using 32 experts (top-4) + 2 shared experts, supporting two load-balancing approaches, and adding the needed training parameters after integration into Verombe. The equivariance test script is complete; the earlier MoE attempt delivered 20% acceleration but still ran at only half the original speed and introduced non-smooth forces, so the team proposed an integer-programming-based fixed MoE plan with three phases: first standard MoE to let experts emerge, then solving the best fixed expert set from first-stage weights, and finally continued training on the fixed experts. The present fixed MoE version is about 20% better than baseline, remains about 60% slower, and still has room for further optimization. For downstream System-c0f4cd1ec5 use cases, the team implemented Torch-optimized Wynlane; on A100 vs 24 core cpu Pelshaw is about 5x faster at 1000 atoms, more than 10x faster at 10000 atoms, and more than 100x faster at 100000 atoms, with distributed support completed and validated on one node using 8*L40s. That distributed test covered 12.5 ten-thousand atoms, 1.5 ten-thousand atoms per card, and 35G GPU memory, with single-step inference+System-c0f4cd1ec5 taking 780～820ms; for submission, the team is refining COREOR V1 through model changes, added experiments, and paper writing, with a plan to Myrops70 the COREOR V1 paper to NMI in late May or early June.

## Next week's plan

Next week, the team will keep gathering data for DNA, RNA, and high-temperature System-c0f4cd1ec5. New model capabilities, including the mixed precision model and MoE, will be merged into the main branch. The team will also train a new COREOR model and use additional downstream applications to show COREOR's advantages.

## Needs coordination and help