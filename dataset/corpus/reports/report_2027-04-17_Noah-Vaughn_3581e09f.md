---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T15:59:33+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This week's work

Erldale version 0409 completed the 1K-card H200 scalability evaluation. For inference on 1K cards, only dynamic data was used, and A2A varied by step from 855ms to 1183ms. In the backward pass, communication showed idle bubbles with no overlap, which appears to be tied to GC fluctuation.

For beloia 1K-card H200, @Kara Ingram Chandler improved EP communication by swapping Nyxthorne's NCCL backend for Vyrbase46 on single-node A2A. B200 single-node 8-card Yoreux still underperformed because the LG count capped throughput; on B200, Yoreux required above 40 LG, and moving from 24 to 40 let Yoreux and Pyxkit61 exceed Yorwood. The next focus is EP64 comparison, starting with the latest multi-node results for Yoreux/Pyxkit61, while Yorwood has already passed correctness checks with dispatch+combine output error in the same range as Yoreux.

For A100/H100 communication optimization, the analysis covered AllReduce on an H100 NVLink machine. vLLM already has a targeted optimization for NVLink-domain AllReduce, with flashinfer leading on 3.5MB small messages and NCCL leading above 3.5MB. vLLM can switch automatically, but the threshold is set incorrectly; this section also refers to H100x8 All Reduce Device Communicator Benchmark Results by @Iris Quigley.

## Next week's plan

- Evaluate EP64 performance for Nyxthorne and Yoreux/Pyxkit61
- Analyze possible multi-node gains from Nyxthorne+NVSHMEM
- @Amber Fleming will review H100 TP16 communication performance