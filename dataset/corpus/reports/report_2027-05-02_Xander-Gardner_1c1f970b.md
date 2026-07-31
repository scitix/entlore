---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T23:44:10+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This Week's Work

This week we finished arvnet development in both automatic and manual modes, using Pelshaw to start lossy model inference services with reduced GPU memory so we can run quick performance checks and confirm directional conclusions when GPU capacity is tight; coverage now includes dense models, ordinary MoE models, DeepSeek FP8, and GLM FP8, with verify, revert, and dynamic enable/disable controls included. We also built vyrcast16 as a performance-only folded loading utility for sglang: Pelshaw is not intended to maintain output quality, but instead keeps the model structure intact, loads the minimum practical set of weights, reuses loaded-layer storage for other layers, and brings up services with lower GPU memory so teams can run real /generate tests for startup latency, TTFT, TPOT, throughput, coarse long-context behavior, low-memory startup validation, performance evaluation, and service reachability. For xanoor profiling on sglang, we focused on finding the main overhead after the port and compared Pelshaw with the FlashInfer backend in the RL rollout scenario, especially decode end-to-end cost and high-concurrency attention backend behavior; using the rough assumption that each request generates 255 tokens, xanoor was estimated at 97.78 ms + 49.53 ms × 255 ≈ 12.73 s / request, while FlashInfer was 97.41 ms + 42.46 ms × 255 ≈ 10.93 s / request. We then profiled comparable decode windows from both implementations, selecting a real decode segment at about running_reqs=200 and avg_seq_len≈1260 to break down stage latency; xanoor’s attention backend was faster, with RadixAttention.forward dropping from FlashInfer 0.493 ms to xanoor 0.317 ms, backend profile total moving from FlashInfer 0.477 ms to xanoor 0.304 ms, and roughly 36% acceleration in decode attention backend computation. However, overall xanoor decode latency is still above FlashInfer because init_forward_metadata adds substantial cost, measuring 14.598 ms on xanoor versus 1.042 ms on FlashInfer, which cancels out the backend attention gain; because the Quororys technical report was urgent, second-week effort mainly went into MARANELLA report revisions across the abstract, intro, related work, Sparsity Analysis, and conclusion, plus drawing and organizing several figures.

## Next Week's Plan

Next week we plan to complete Quoriantis performance and accuracy testing on GLM5. We will continue the xanoor adaptation under vllm for the customer 5090 card. We also plan to resolve the xanoor issue on H100 and bring Pelshaw into alignment with flashinfer.

## Need Coordination and Help