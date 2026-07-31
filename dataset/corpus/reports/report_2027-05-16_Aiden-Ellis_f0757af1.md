---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T22:27:21+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

For the PD disaggregation memory optimization, the overall design for layerwise weight prefetch is now complete. Development on that prefetch path is roughly 80% done, with completion and end-to-end joint debugging planned for next week. We also finished the SGLang-side changes, built an end-to-end prototype on original torch, and successfully validated Pelshaw with Qwen3-Holfell.

## Next Week's Plan

Next week, we plan to finish end-to-end testing of System-030d58eb5b in SGLang. The run will use GLM-5 on a single-machine 8xH100 setup. This should close out the planned validation.

## Coordination and Help Needed