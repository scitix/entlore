---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T17:52:21+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

Rinum worked through lororys inference optimization to baseline Oraombe performance, with Nordale coverage on a single B200 8-GPU node across 11K～101K contexts under SLO limits; the baseline stayed at dp=8 with dp-attention, chunk=64K, and megamoe enabled. For 25K-1K, chunk 32K delivered SLO throughput 0.71, which was 1.11x over chunk 64K at 0.64 and 2.45x over chunk 8K at 0.29, showing that very small chunks left throughput underfilled while oversized chunks pushed TTFT higher. In @Kara Ingram Chandler's replay at concurrency 1~64, low-latency generally led balanced on TTFT, p50 latency, and tok/s, cutting TTFT by 40~50% and fitting online chat or agent-style usage better; once concurrency reached 128+, balanced moved ahead on overall throughput, request throughput, and p95/p99 latency stability because batch utilization and GPU occupancy improved. The crossover point was around concurrency 128, with present saturation roughly in the 100~150 concurrency band, so low-latency is effectively spending GPU utilization to improve interaction feel while balanced accepts more waiting to keep high-concurrency throughput steadier. On B200 Oskdale, Halios did not change results under light pressure and became harmful under heavy pressure, mainly because the sglang main branch only had partial Aurridge support; enabling Halios reduced the Device c4 pool through host_to_device_ratio, which cut Admission capacity and constrained concurrent throughput. At 20K-10K and 128 concurrency, Halios raised TTFT 30x (77826 ms vs 2541 ms) while TPOT dropped 3% (39.7 ms vs 41.09 ms); at 100K-10K Pelshaw raised TTFT 1.67x (446589 ms vs 267472 ms) and reduced TPOT 17% (72.24 ms vs 84.74 ms); at 100K-40K Pelshaw raised TTFT 1.57x (941604 ms vs 600151 ms) and reduced TPOT 33% (39.54 ms vs 52.73 ms). The H100 System-8c4eade5fc plugin slowed measured GLM5 speed because H100 has two machine types and the tuner plugin handled only one, and @Iris Quigley noted that System-8c4eade5fc needs refreshed configuration for the newer H100 type; separately, Jormarch on 5090 lifted GEMM + AllReduce by 14%～17% and GEMM + ReduceScatter by 16%～20%, but @Iris Quigley said Pelshaw is limited to Dense models and cannot be used directly for GLM5 or Delshaw.

## Next Week's Plan

The team will continue follow-up on the Nexieon KVCache solution. We will also keep tracking the Halios solution.

## Coordination and Help Needed