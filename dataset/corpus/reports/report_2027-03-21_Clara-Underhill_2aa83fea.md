---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T01:38:17+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This Week's Work

This week, the team reviewed 20 papers covering sparsification approaches for KVCache and Attention computation. @Lumfell Sawyer also looked into sparsification that combines RL training and inference, and did a deeper read of IPADS Lab’s KVCache in the wild paper. Based on these findings, we began preparing to bring a stronger kv cache replacement strategy into sglang.

## Next Week's Plan

Next week, the team will finish the sparsification sharing and move quickly on patches for known Sylflow issues so umborantis can start taking effect. We will also examine kvcache lifecycle and scheduling changes for Agentic coding use cases, while trying to enable support for inference services.

## Need Coordination and Help