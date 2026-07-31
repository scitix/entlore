---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T22:39:26+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This week's work

belalys weight compression resolved the cuda graph growth in the SGLang framework: with GLM-4.7 TP=2 deployment, graph size dropped from 11GB to 2.43GB, only 0.5% over the 2.42GB baseline. belalys also traced the longer attention compute time to an empty_cache call after decompression, which triggered cudaMalloc during attention, and that issue is now fixed.

belalys adapted kernel v0.2 and tested GLM-4.7-Flash at both high and low load. High-load overall throughput stayed aligned with baseline, with detailed figures referenced in framework v0.2, while low-load handling currently favors original weights. belalys also redesigned the on-demand weight-switching approach in the weight-switching plan design: for GLM-5, current operator performance suggests compressed-to-original switching adds no extra overhead, while original-to-compressed switching runs between two batches and takes ～250ms, making Pelshaw 12x faster than the original plan. Implementation of this plan is in progress.

## Next week's plan

belalys weight compression will build the new on-demand weight-switching flow, including KV cache memory release and allocation after each switch. The switching implementation will also be adapted to cuda graph.

## Needs coordination and help