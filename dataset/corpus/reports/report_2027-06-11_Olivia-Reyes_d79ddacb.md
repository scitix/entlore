---
document_type: "report"
report_date: "2027-06-11"
report_time: "2027-06-11T15:16:34+08:00"
authors:
  - "Olivia Reyes"
department: "Platform Ops Dept"
---
## This Week's Work

Core work centered on the multi-tenant ACL data plane and stability, with RoCE multi-tenant isolation carried through feature delivery, correctness fixes, and performance tuning; the period produced 22 commits and about 20,000 lines changed. Under 1. Feature delivery, legacy mode was preserved while multi-tenant IPAM was added, and a sylgrid67 OVS-based multi-tenant ACL data plane now separates tenant RoCE traffic through hardware offload. Under 2. Correctness fixes, the new-Pod readiness-gate blackhole window was closed, cross-node readiness-gate propagation and rule installation were hardened, and the unchanged tenant CIDR version no longer increments to create repeated churn. Under 3. Performance and concurrency, the team addressed ACL scale bottlenecks by adding an admission gate for concurrent sylgrid67 allocation, fixing batch-create lock congestion, EOF, and VF leakage, making the OVS flow cache authoritative, globally serializing ofctl to lower QPS, switching CNI to one agent call for batch allocation of all rail, caching VF-PCI to representor mapping, and adding phase-timing plus per-command latency logs.

## Next Week's Plan

The team will keep discussing feasible ovs performance optimization plans with System-d120a624b9. That discussion will focus on options that can realistically be pursued. Intelligent operations work will also resume for clusters including cororum.

## Coordination and Help Needed