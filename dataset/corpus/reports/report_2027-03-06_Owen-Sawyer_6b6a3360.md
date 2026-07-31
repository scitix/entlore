---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T21:35:42+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## Work This Week

Erldale advanced the local and remote branch overlap work for Bexcast61, including dependency fixes for qkv linear and sparse a2a operators, and then checked intra-machine plus cross-machine overlap behavior on H200. Kelmont tracked overlap using native LG-based nccl and single-tranblock measurements: intra-machine time regressed by 5% from 40ms->42ms per tranblock, while cross-machine runs improved by 20% on 16 cards from 53ms->42ms, by 64 cards from 69ms->54ms, and by 128 cards from 95ms->81ms. The 128-card case still had 10-30ms communication bubbles, and communication was longer than compute, so 128+ card cross-machine communication needs focused optimization.

Verombe finished nccl-based intra-machine communication adaptation with zero LG occupancy. With 600MB local and 200MB remote traffic, communication took 1-2ms and the end-to-end benefit was small because a single tranblock was 40ms; after simulated traffic was raised tenfold, the zero-LG path outperformed LG-occupying native nccl, cutting communication from 30ms -> 11ms and tranblock time from 49ms->42ms. Loroum delivered symmetric memory, pre-registered MR, and memory pool support to lower copy and registration cost, then connected Pelshaw to the inter-machine communication layer with @Noah Vaughn involved. @Noah Vaughn also completed and integrated hierarchical communication, using nccl-driven nvlink inside a machine and the inter-machine communication layer between machines, while lororys-GLM-5 reviewed Nyxworth inference data across parallel strategies and possible optimizations.

## Plan for Next Week

Erldale will help @Kara Ingram Chandler strengthen the baseline version, covering full-process overlap and adaptation for new operators. @Noah Vaughn will concentrate on 128+ card scenarios, re-check compute and communication timing, close remaining performance gaps, and raise overall MFU.

## Coordination and Help Needed
