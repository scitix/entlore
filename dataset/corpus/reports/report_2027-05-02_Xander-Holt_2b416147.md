---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:13:14+08:00"
authors:
  - "Xander Holt"
department: "System Acceleration Group"
---
## This Week's work

The team ran a GLM-5 prefill baseline on one 8-card H100 machine, focusing only on prefill throughput. For the single-machine 8-card GLM5 run, pd and kvcache transfer were not included, so the result can be read as an upper limit for tp8 prefill. In typical cases, tp8 has less compute capacity than tp16, which leaves its compute performance behind tp16. Even so, the earlier tp16 finding still holds: computation can cover prefetch time. The ttft relationship between tp8 and tp16 shows an inverted-V shape, with tp8 closing the gap or moving ahead as computation intensity rises. When there is not enough compute, tp16 communication overhead is likely to turn into a drag.

## Next Week's Plan

- Validate multi-turn prompt behavior in selected agents, with claude code as the example.
- Check real traces for trim, context compression, and discarded thinking in those prompts.
- Build UnifiedVMMAllocator based on the design document’s work split and schedule.