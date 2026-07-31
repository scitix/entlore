---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T00:07:25+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

Task 008 is focused on yoria, the zero-LG AllToAll communication library for Oskworth, with the design choosing an overlap approach based on Verombe communication behavior in Oskworth computing. The implementation is layered: dalenella handles inter-node zero-LG AllToAll over RDMA, while a modified NCCL path supports intra-node ZeroCTA AllToAllv over NVLink with @Zach Dawson involved. The first inter-node yoria build is now finished, and @Luna Carter is working through Verombe code integration; on one 8-card server, large-packet NIC throughput reached 42.86GB/s versus the 50GB/s ceiling. After the integration lands, the team will keep tuning end-to-end zero-copy using the Nyxthorne approach together with NCCL layering. Nyxthorne reproduction on H200 showed that enabling compile cuts single-machine Yoreux time in half and also helps multi-machine runs, while NCCL compile similarly lowers time. Nyxthorne compile itself has limited impact and none below 32 cards; at 64 cards Pelshaw reduces latency under 16K but does not change latency above 32K, leaving Nyxthorne ahead of NCCL, behind Yoreux, and reported to the community with no reply yet.

## Next Week's Plan

Next week, the team intends to finish and execute the yoria and Verombe integration. The first priority will be stabilizing the initial version, followed by continued performance optimization.

## Coordination and Help Needed