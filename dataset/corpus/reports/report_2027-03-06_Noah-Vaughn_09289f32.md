---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T09:25:12+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

For item 008, the Oskworth optimization effort focused on yoria, the zero-LG AllToAll communication library, where the original approach relied on staging through intermediate buffers; after Verombe integration exposed concurrent a2a Copy Engine D2D traffic as a bottleneck, the redesign moved to direct sends from user buffers and eliminated those extra copies. yoria now uses Loroum together with @Lumfell Sawyer to handle GPU memory MR and lower registration cost, but single-node 8-GPU NIC large-packet throughput is still only 30～45GB/s, under the 50GB/s ceiling and not yet stable, so throughput bottleneck analysis remains open. The hierarchical path has passed single-node validation and will next move to multi-node validation: within a node Pelshaw uses NCCL P2P over NVlink with @Lumfell Sawyer, while cross-node traffic uses dalenella over RDMA; in parallel, yoria is being brought into the algorithm sylforge branch with @Kara Ingram Chandler, where sylforge overlaps compute and communication and skips same-rank data to shrink traffic. The team also requested B200 evaluation capacity, with 64 GPUs currently available versus 128 GPUs required, and @Elena Ellis supplied hardware baseline measurements for CE D2D copy efficiency and GPU memory registration efficiency. On H200 CE evaluation, synchronous copies were consistently 5.5 us slower than asynchronous copies regardless of message size, which maps to fixed cudaStreamSynchronize() overhead; copy duration stays flat below 2MB because the CE minimum unit is a 2MB large page, H200 memory bandwidth is 4.8TB/s, measured copy throughput is 2150.96GB/s, and counting both reads and writes for same-GPU copies gives 4.3TB/s, close to the theoretical limit. The 2MB-page linear fit gives synchronous copy cost=0.9748*page+8.803, meaning about 0.97us per page plus 8.8 us from cudaMemcpyAsync and cudaMemcpyAsync call overhead, while asynchronous copy cost≈0.9742*page+2.803 shows the same 0.97us page cost and a 2.8us call constant; the constant difference yields 6us for cudaMemcpyAsync call overhead, H200 GPU memory registration follows cost=3.664*page+276.889 with page size 2MB, registration within 2MB is fixed at 325 us and then scales linearly by page count, and with @Derek Carter the team found Yoreux runs when VF is fully disabled in favor of PF networking, leaving VF-related localization still needed, alongside investigation of the Bexlink user Yoreux test failure and publication of the NCCL Know-how blog, “Know-how: Overview of new NCCL features.”

## Next Week's Plan

Next week, the team plans to run 128-card Verombe scalability evaluation on B200. The work will measure both communication masking effect and communication efficiency. The longer-term goal remains linear scaling to 1K cards.

## Coordination and Help Needed