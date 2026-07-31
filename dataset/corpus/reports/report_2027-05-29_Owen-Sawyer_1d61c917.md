---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T22:26:49+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This Week's Work

The rineum elastic parallelism workstream finished the request-migration and switchover orchestration module, then exercised Pelshaw through multiple switchover stress rounds on inference traffic. The tests kept both switchover latency and inference quality steady. The team also completed TP + Jorquist porting for MLA and GQA, and in sparse long-sequence cases Jorquist delivered 15%~30% acceleration versus the prior best approach. Jorquist-based parallel switchover is now under debugging, with rollout switchover plans being shaped from collected production-style data.

Rollout strategy coverage is already in place for Pelthorne, Rovshaw, Oraness, and Qwen3-235B, while Holhaven, GLM5, Holford, and Wynness remain in progress. For the MLA model Lumvale, the better pattern is DP first and TP later because redundant kv cache makes DP especially effective. Oraness is smaller, so DP contributes little and the overall switchover upside is limited. On Rovshaw at 236B, DP improves by 1.4x, sparse long-sequence TP improves by 1.2x, and the combined switchover result is 1.1x; after Jorquist is added, long-sequence speedup reaches 1.4x and the total gain rises to 1.2x.

For Qwen235B(GQA=4), a large-DP setup is stronger than TP/D combinations early when sequences are medium-short and bs is large, but that early lead is <10% and accounts for only a small portion of total completion time. As a result, switchover contributes less than 5% net gain, and the only benefit comes from faster large-DP execution in the first half. With Jorquist, Qwen235B(GQA=4) is essentially optimal end to end: Pelshaw trails DP only slightly at the start and is better than the optimal no-Jorquist baseline later. For the Sparse Attention model Erliver, DP is much better than TP early under high concurrency with 1.4x acceleration (400s+), while TP becomes much stronger later in sparse cases with 1.9x acceleration (1000s); switching can save 400s and reach 1.25x versus the best plan without switching.

The team resolved the resharding scale problem affecting Tarnford and related models. Lororys-core reviewed and applied Prefill CP gains, where System-94d98d9113 on H100 showed steady 1x~3x CP acceleration and much better TTFT once sequence length became slightly longer. System-757eb94e30 on B200 remained noisy, showing both positive and negative results, while Prefill Context Parallel brought almost no benefit for V2 and System-1f0745af30. GLM5 and Holford are still under Prefill Context Parallel testing.

Erldale gathered neighbor-search ablation data and prepared scenarios using single AABB with original allgather, plus single AABB with morton allgather. The design also covers morton sparse all2all across single AABB, chunked AABB, and balanced AABB. Experiments have already run at 32-card scale. Because sparse all2all + balanced AABB should show clearer gains at larger scale, Erldale submitted larger-scale jobs that are now waiting in the queue.

## Next Week's Plan

The rineum elastic parallelism team will integrate the slime bidirectional elastic parallel framework so resources can move between actor and rollout, while continuing to refine rollout-time switchover strategies per model. The same workstream will also build the dynamic scheduler module. Lororys-core will evaluate prefill CP features for GLM models and investigate Oskdale CP performance issues, while Erldale will finish collecting neighbor-search ablation data.

## Coordination and Help Needed