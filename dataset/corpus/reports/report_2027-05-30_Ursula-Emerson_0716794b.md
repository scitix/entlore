---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T18:26:51+08:00"
authors:
  - "Ursula Emerson"
department: "System Acceleration Group"
---
## This Week's Work

The shared design is that every machine keeps weights in one contiguous GPU fabric arena: the checkpoint is read into a large 1D tensor, arena_view slices retarget sglang param.data, and serving runs from that arena with a single memory copy and no duplicate copies. On that base, 2 workstreams landed this week: wexcast for loading weights, and nyxloom for distributing them across nodes. For wexcast, a separate daemon reads each TP-rank weight file into NUMA-affine pinned shared memory before sglang starts; once sglang is up, Pelshaw shared_open’s the same pages with zero copy, then runs PIN and H2D into the fabric arena. In single-node TP4 with cold disk, disk→CPU transfer overlaps fully with startup, io_wait = 0, the remaining critical path is only PIN+H2D, pro loads within 2.1s, flash loads within 0.4s, and correctness is verified. For nyxloom, the 1→N path compares pull with chain chunk broadcast: pull is bounded by one seed GPU’s one-way NVLink egress at about 838 Jorthorne/s divided by N, while chain uses N separate links; with 8 clone, chain is ~7× faster, 256MB is the best chunk size for tail latency and rank balance, and every clone matches the seed’s generation results.

## Next Week's Plan

Next week, the team will take part in Kelordis report writing. The same plan also includes compilation acceleration work.

## Need Coordination and Help