---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T15:04:02+08:00"
authors:
  - "Olivia Reyes"
department: "Platform Ops Dept"
---
## This Week's Work

For the Pelportroce network ipvlan solution, the Pelport cluster finished validation of the ipvlan roce approach: gpu containers receive ipvlan subinterfaces built on ovs vf, and the ipvlan case handles device_all semantics so 8 devices can be requested together. The team also completed adaptation work for the open-source rdma device plugin, built the roce operator, and delivered an aggregated cni in place of the open-source ipvlan cni so multiple NICs can be created in one step. For the Pelportroce network sylgrid67 solution, the Pelport cluster completed validation, added ovs flow tables for mac-address-based forwarding under multi-vf conditions, enabled multiple vf initialization on pf0 across 4 planes for container vf passthrough, and completed container creation plus connectivity tests. The sylgrid67 validation path starts on its own; from the current single vf network architecture, an overlay script can switch directly to 16vf and finish all NIC and flow table setup, while device_all semantics allow 8 vf passthrough devices for all gpu to be requested at once; the solution needs both device plugin + cni changes, with device plugin development complete, Corworth development complete, and open-source sriov cni plus rdma cni combined into System-7b5b3359bd. For PelportLuxlink monitoring, Luxlink added ovs metrics for the Pelport cluster ovs network solution to track core node ovs status and keep roce links healthy, added anomaly signals for forwarding issues including pmd utilization and packet-drop statistics, added ovs monitoring views in the grafana dashboard, and sends key alert metrics to the alerting platform.

## Next Week's Plan

Next week, Pelportswichdev will work on the multi-tenant solution design. The same effort will include validation.

## Coordination and Help Needed