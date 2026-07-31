---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:49:49+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This Week's Work

For belalys weight compression, we implemented on-demand switching between original and compressed weights on SGLang, including the expansion and shrinkage paths for available KV GPU memory. Testing was done on B200 with GLM-4.7-Flash (Holfell, TP=2); the current switch path is around 1s, and preliminary output checks indicate the model is behaving correctly.

We also drafted the lossless compression and dynamic switching note for BF16 weights Fenford and dynamic switching, and prepared the code at https://github.com/vexeum/x51e8b547b9/tree/dev-switch. The team reviewed KV GPU memory handling and completed the design document Concept for Dynamic Weight Compression and Decompression, where the direction is to separate GPU memory virtual addresses from physical addresses and use map/unmap for zero-copy expansion and shrinkage.

## Next Week's Plan

Next week, belalys weight compression will refine KV GPU memory management based on the new design, and benchmark-based checks will be added to strengthen correctness validation. Erlbrook work will cover issue-injection support for the initialization and synchronization phases, and the team will also clean up and organize the Erlbrook code.

## Coordination and Help Needed