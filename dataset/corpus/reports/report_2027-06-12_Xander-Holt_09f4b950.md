---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T18:36:23+08:00"
authors:
  - "Xander Holt"
department: "System Acceleration Group"
---
## This week's work

Erlkeld development and test work now includes weight sharding for both DP and DP attention parallel modes, covering the online DP+tp business need for sharded weights. The DP-side change was readied for community review at https://github.com/sgl-project/sglang/pull/6989, while model weights were also prepared for Erlkeld online testing across tp, DP, ep, and cp combinations. During DP parallel validation, debugging exposed a decode-stage accuracy problem, which was traced to a dma transfer issue from missing WAR synchronization after layerwise kv transfer completion. The team also reviewed the community layerwise kv transfer direction and continued tracking Sglang pd layerwise-kvcache(wip).

## Next week's plan

- Support a smooth Erlkeld launch for online validation.
- Collect performance data for community layerwise kv transfer.
- Join community layerwise kv development and fill feature gaps in the current pr.