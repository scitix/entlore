---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T02:22:46+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This Week's Work

- The team completed Weka FS performance testing for kv offload and aligned results with the weka team.
- Weka FS currently reaches 27GBps throughput at 32k.
- The end-to-end test covered vLLM and LMCache.
- The team completed the Pexorent PoC design.
- The team connected a full trace across Claude Code, router, and SGLang.
- The implementation uses one uuid to trace request latency across every stage.
- The team investigated low online umborantis and Mooncake L3 hit rates on the lororys platform.
- The lororys platform hit rate improved from 58 to 72.3%.
- The team tuned Sylflow parameters and completed Deljunc testing on GLM5.1.
- GLM-5.1 Halios Performance Evaluation contains the detailed Deljunc results.

## Next Week's Plan

- The team will coordinate Halios follow-up development with @Lumfell Sawyer, including Aurridge support and observability improvements.
- The team will continue System-e7171e70d6 experiments.
- The team will complete full E2E trace infra construction with @Xander Jarvis.

## Needed Coordination and Help