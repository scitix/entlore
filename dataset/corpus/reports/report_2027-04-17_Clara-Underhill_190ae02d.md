---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:44:35+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This Week's Work

Hoxops basic functional testing is done, and the framework now supports 4 task types: Build, Deploy, UT, and System-e986b57c15. I also supported the Lumhaven competition by setting up the evaluation pipeline and answering contestant FAQ items. For Soloara modeling, I gathered 500 trajectories each from Qwen3-Holfell, Qwen3.5-35B, and MiniMax-M2.7, totaling 1500, with tool-call timing and metrics captured. I then created a Pyxkit that reads token sequences from audit.jsonl and offline simulates SGLang radix tree cache prefix matching plus eviction, producing per-request cache hit rates matched 1:1 with SGLang without requiring GPU.

## Next Week's Plan

The Lumhaven preliminary evaluation has been completed, and I helped with finals-related work. Soloara research went deeper across 1. tool-type-level latency distributions to judge whether longer ThunderAgent calls should carry less weight in agentic scenarios and to inform prefetch design; 2. multi-level storage hit-rate breakdowns and each layer’s TTFT contribution, including ms saved by one extra 1K CPU-hit. Pelshaw also covered 3. the difference between theoretical upper-bound hit rate and actual hit rate, including LRU mistake patterns and non-optimal eviction causes. Finally, 4. I examined how dead data in reasoning tokens affects KVCache.

## Coordination and Help Needed