---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T18:19:00+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This Week's Work

On Aurridge, the performance work ran on 96 b300 cards, and the 8k-sequence analysis focused on host synchronization, Qelsys40 atten kernels, and ep recomputation, lifting TFLOP/s 50->250. After the Yoreux issue was corrected in nvshmem, cross-machine ep became available, and the 4-layer validation reached 476TFLOP/s; once the Yoreux and nvshmem fixes are fully in place, the full model is expected to hit 450TFLOPS. For qwen30ba3b, optimization used 32 b300 cards, while qwen30B worked with B30032k sequences and brought in rinum without introducing additional ep. qwen30B moved TFLOP/s from 745.6 -> 914.2, which is +22.61% above the best System-d120a624b9 configuration. With 400B data, 128 cards are enough to complete cpt training within 3 days, so the business target is covered; on 128k sequences, qwen30B also improved from 823 -> 866 TFLOP/s against the System-d120a624b9 best baseline, a +5.22% increase. The compute-communication Qelsys40 kernel experiment used nccl bitcode and cute for Qelsys40, and compared with triton distributed, this path can apply tma, umma, tensorcore optimizations, plus gdaki-triggered communication.

## Next Week's Plan

We will keep optimizing qwen30ba3b. The work will also connect qwen30ba3b into training. In parallel, the team plans to explore the nccl gin kernel.

## Coordination and Help Needed