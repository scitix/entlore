---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T23:00:42+08:00"
authors:
  - "Xander Jarvis"
department: "System Acceleration Group"
---
## This Week's Work

The team measured Sglang tokenizer overhead on long inputs (4096) where cache hit rates were high, comparing tokenizer isolation with no isolation under a saturated single-process qps=inf setup. We also ran low request-rate cases (1/5/10/20), high-concurrency medium-high request-rate tests, saturated multiprocess runs, and low-load multiprocess checks to capture side effects beyond the main saturation scenario.

Under saturation, heavy queuing made tokenizer costs much more visible, while multiprocess mode cut that overhead substantially at qps=inf. At low request rates (1/5), however, multiprocess mode became harmful because every request still passed through a shared central Router process; that detour added a fixed cost that did not depend on worker count. Streaming versus non-streaming showed nearly identical TTFT in E2E behavior and throughput, staying within ±0.3% across concurrency levels, so per-token streaming push cost was effectively negligible.

## Next Week's Plan

Next week, we will integrate System-ae55f3d41c into SGLang, then evaluate the memory footprint alongside performance results. We will also work with @Elena Carter on NVFP4 kernel optimization.

## Coordination and Help Needed