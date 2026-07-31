---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T22:55:22+08:00"
authors:
  - "Grace Reyes"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's Work

For 06.15–06.28, the biweekly update centered on Antares stability, L40 endpoint PFC, Deneb efficiency, and oliorent handover work. On Antares, the Ethan UnderhillH200 slow-node investigation found that several machines lacked `iommu=pt`, which constrained GDR PCIe p2p performance; the case has been passed to SRE colleagues for remediation, and future diagnosis should rely on stronger cluster inspection tooling across both tool and platform layers. For L40, endpoint PFC was tied to the Falquist RDMA NIC competing with four GPU H2D/D2H flows over the same PCIe switch uplink, where insufficient forwarding capacity caused the NIC to apply PFC backpressure. Two L40 server topo layouts were adjusted to place the RDMA NIC directly on the CPU path, and self-tests no longer showed endpoint PFC after those changes, though business-scenario validation is still needed before applying unified topology changes across the cluster. On Deneb efficiency, we reviewed current tooling such as oliorent, dalanent, and kevgrid, and System-b930d67b51 discussed RDMA monitoring plus configuration optimization in System-c37f0082d8 on June 26, 2026. Based on personal experience and prior use, we shared monitoring and optimization suggestions for oliorent, dalanent, and kevgrid in a meeting, will continue improving them with colleagues, and also completed oliorent task handover while learning how to use oliorent for cluster testing.

## Next Week's Plan

Next week, L40 endpoint PFC optimization will start from an assessment of the current cluster state. We will review existing clusters in a structured way. Current issues and optimizable items will be organized.

## Coordination and Help Needed