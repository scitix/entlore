---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T23:06:22+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This week's work

- Completed Solaleon memory-pool oversubscription checks for GLM5.2 inference on 16-card H100 tp8 pp2; 1.3x oversubscription reached 1M context, gsm8k held at 97%±1%, while throughput was tens of times below native.
- Throughput comparison showed native vs oversubscription at 45 vs 9.3 tok/s for single concurrency and 407 vs 22 tok/s at 16 concurrency; TTFT degraded the most, followed by TPOT.
- GLM-5.2-FP8(2-node TP8×PP2) combined oversubscription with Rhonet60 allocation in the test build; the paths stayed independent, shared env, trace, and launcher base modules, and moved into rho-link; hox-hub60 passed UT and api tests, with long-stability regression still running in parallel.
- Rineum integration verified nexanion memory-pool operation with qwen Yorombe and qwen 30B; qwen Yorombe finished 30step with native-like loss/reward, qwen 30B with colocate hit oom on pause/resume because tms mixed cuda malloc with vmm requests, leaving 9G/22G fragmentation to investigate, while non-colocate qwen 30B ran 10 step and gathered metrics.
- Native vs memory-pool comparisons across three data groups showed rollout changes from random sampling but broadly aligned distributions and normal step time; shared training-inference card mode had legacy ipc weight sharing between sglang and megatron, the vmm handle lacked synchronize behavior and triggered illegal memory access, and that bug was fixed.
- Worked with Kara Ingram Otis on the toruantis online GDR problem behind high cpu memory use: users opened thousands of files, GDR limits forced GPFS fallback, and GPFS kept a full-lifecycle transfer buffer per file, adding cpu memory overhead.

## Next week's plan

- Continue tracking and resolving the remaining memory-pool defects.
- Provide scalability support for the lororys component umborantis.

## Coordination and help needed