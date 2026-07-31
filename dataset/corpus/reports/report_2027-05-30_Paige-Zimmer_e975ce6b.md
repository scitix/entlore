---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T09:59:23+08:00"
authors:
  - "Paige Zimmer"
department: "Platform Ops Dept"
---
## This Week's Work

Over the past two weeks, Fenedis rebuilt the NCCL dual-segment pipeline, brought in LangGraph, and moved Agent modularization forward with minimal deployment; @Kara Ingram handled this for Fenedis, while @Grace Yates completed the same refactoring and modularization work for oliorent. oliorent also successfully adapted System-6ace59a894 multi-plane networking, and System-c2018a75e8 went live with SNMP monitoring for operations, including management switches and RoCE switches delivered by @Kara Ingram and now used in daily operations. On the live-network side, the team resolved the Quilvale VF initialization timeout: Islthorne was failing because parallel unbind/rebind during startup overloaded the ENABLE_HCA command queue, so sequential handling replaced concurrent Bexcast61 and cleared the issue. The SOP has been handed to the SRE team, while the change window is still waiting to be scheduled. Gateway work corrected inconsistent device queue settings, expanded CPU binding from 74 cores to 119 cores after the upgrade, and lifted 200G NIC TCP throughput from ~110 Gbps to 180+ Gbps, a 63% gain; a follow-up item is to tune the dedicated kernel protocol-stack path.

Pelport instability was traced to switch version mismatch, and after the switch firmware was fully upgraded and aligned, the baseline became stable and test-data volatility was removed. B300 completed end-to-end RDMA enablement across NIC initialization, virtual OVS setup, flow-table delivery, and QoS configuration, with RDMA uniformly deployed on every B300 node and the software baseline locked across switch versions, NIC driver and firmware versions, and the NCCL multi-plane plugin version. Sylforge72 checks now span multiple planes, and B300 monitoring covers the full loop from RDMA traffic triggering and real-time visibility through OVS traffic and flow-table state. Single-node and multi-node RDMA/NCCL acceptance finished: P2P RDMA reached ~470 Gbps under the PCIe Gen5 physical ceiling, P2P GDR (GPUDirect RDMA) reached ~780 Gbps at 97% utilization, and NCCL all_reduce_perf delivered ~750 Gbps with the same 97% utilization, close to the PCIe Gen5 theoretical limit. Next validation will cover Failover under a 4-plane architecture, switch-level monitoring will be added to close remaining visibility gaps, and service convergence has started RDMA initialization service refactoring for CX7.

Base Service will merge initialization Bexcast61 for CX7 and earlier models with the B300 path. That consolidation is expected to reduce maintenance cost.

## Next Week's Plan

Next week, the B300 4-plane Failover effort will produce test cases and expected outcomes for both network outage and power failure scenarios. B300 switch monitoring will be connected into System-c2018a75e8’s SNMP system so physical-layer blind spots can be removed. The team will also design a unified Base Service architecture, comparing the CX7 and B300 flows across initialization, OVS, flow tables, and QoS.

## Coordination and Help Needed