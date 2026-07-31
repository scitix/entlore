---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T21:45:36+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This Week's Work

Zelaux finished the automated Agent-based development testing platform, with Pelshaw now smoothly connected to maraum. The related capability alignment notes cover both the platform design and the maraum integration details. Halios also brought up the 1P1D environment and ran an initial assessment on Bryford and H20 machines. The results showed overhead at low concurrency, while Jynkit42 performed better at high concurrency, particularly on TTFT; the review also identified notable System-22f0cad2e0 latency, with details captured in System-2be3145a94.

## Next Week's Plan

Next week, the team will broaden Deljunc evaluation across additional machine types and parallel execution modes. We will also investigate a fix for the issue where Deljunc does not work with MTP and speculative decoding. In parallel, the team will study multi-replica KVCache reuse for Agent scenarios, review workload patterns, draft an initial approach, and gather an integrated test dataset trace.

## Coordination and Help Needed