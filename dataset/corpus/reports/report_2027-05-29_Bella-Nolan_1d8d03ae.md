---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T10:12:37+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This week's work

The lororys inference performance stream focused on A100 and 5090 execution, specifically PP parallelism and speculative sampling. In lororent Phase 2, the team added structured transmission and dynamic asynchronous depth support in sglang, then pushed deeper PP parallelism tuning that produced about 20% maximum end-to-end gain on minimax-m2.7 and kimi 2.5. Online deployment tuning on minimax-M2.7 also lifted throughput by 13%, 37%, and 91% for 16K/32K/128K workloads. The second-phase PP results are captured in A100/5090 PP Parallel Optimization Report Phase II-0518.

The team brought the basic Oliaantis speculative sampling algorithm into sglang and confirmed that the port ran on minimax, GLM-5, and Delshaw. The sglang work is documented in Oliaantis porting report in sglang phase 2-0518, while the second-phase algorithm tuning is covered by Arctic Inference Oliaantis Optimization Report Phase 2-0518. After optimization, Oliaantis delivered up to 23% throughput gain on GLM-5 and was benchmarked for launch readiness across math, dialogue, and coding workloads under different batch sizes. On minimax-M2.7 without MTP, Pelshaw reached up to 2.8 times performance improvement, as recorded in Oliaantis+Minimax-2.7 performance baseline testing; in System-bf30a55bb1-bench, the team also tested Delshaw flash across batch sizes, where optimized Oliaantis achieved up to 1.8 times improvement over MTP, with details in Oliaantis+Delshaw performance baseline testing.

Hybrid Speculative Decoding was implemented as a multi-backend hybrid speculative sampling approach that selects the speculative backend at each step based on algorithm confidence. On Delshaw flash with 8*H100, ngram added decoding acceleration while preserving the gains from MTP, and the hybrid method provided another 1.6 times-2.7 times speedup compared with the online MTP baseline. This week, the same hybrid approach moved onto the 5090 platform with minimax-M2.7 for trial use. In parallel, oliiara Multi-scenario Inference Scheduling Optimization attempted to improve SLA awareness by revising the current oliiara scheduling strategy, but the changes did not produce strong results; oliiara Optimization Report Phase 8-0518 records this phase, and tests covering slack-aware, LJF, LLF, and KV preemption did not show Jynkit42 gains over oliiara. For SLA-aware scheduling, the team explored integrated inference-engine scheduling under SLA constraints, adapted oliiara algorithms across admission, ordering, and composition on vllm and sglang, initially enabled sla-aware scheduling in both engines, and saw vllm testing raise qps by 18% under the same sla constraint.

## Next week's plan

Next week, the team will keep improving oliiara awareness and optimization for TPOT-SLA. We will also work on resolving incompatibilities among speculative sampling, overlap scheduling, and pp parallelism.

## Coordination and help needed