---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T20:45:36+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This Week's Work

belalys separated virtual GPU memory addresses from physical ones, then used map/unmap flows so KV Cache can grow or shrink through zero-copy behavior while still working with cuda graph. The team ran belalys on H20 with GLM-4.7-Flash (Holfell, TP=2), and the generated output cleared an initial correctness check. Current switching overhead is about 200-300ms, with compression and decompression taking the dominant 60%-90% share, while KV Cache expansion and contraction add only a small portion of the time. The team also arranged BF16 weights Fenford, dynamic switching, and the sglang-belalys dev-switch code at https://github.com/vexeum/x51e8b547b9/tree/dev-switch. On Erlbrook, earlier API-level injection was expanded to cover initialization and synchronization problem injection, and RDMA-stage injection was added as well. The RDMA path works through an LD_PRELOAD API wrapper that catches NCCL runtime dynamic symbol lookup for RDMA verbs interfaces, updates function pointers in the RDMA context when required, and performs injection before the real function runs.

## Next Week's Plan

belalys will focus next on cutting online decompression time. The planned approach is to add parallel decompression and communication. Erlbrook will be connected with the yor-proxy Hang monitoring tool for evaluation.

## Coordination and Help Needed