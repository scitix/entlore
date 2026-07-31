---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T11:59:53+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

Umbays backend service refactoring is now online, with this week’s work centered on the cluster creation journey, multi-type provisioning, multi-cluster architecture, and service reliability. The management service moved to a multi-replica HA design, keeping access smooth with almost no disruption during releases or failovers. Cluster creation and expansion were reworked around an internal initialization playbook, richer parameters, and more stable, efficient connectivity into the federated control plane. The platform now centrally manages member clusters, syncs their state in real time, and sets the base for later unified cross-cluster access.

Cluster creation now supports Cilium in addition to the previous Calico option, while Kubernetes versions are managed dynamically with 1.35.4 and 1.34.8 currently available. Future Kubernetes releases can be enabled as needed with almost no automation adaptation cost, and node labels are now parsed dynamically rather than hardcoded, then distributed to nodes to prevent label-dependent component failures. Interface exception handling was improved to cut occasional errors and make troubleshooting faster, memory usage dropped by 20% to resolve frequent OOM problems, and the addon plugin vexeum-csi-plugins was added for one-click storage deployment.

For belanux, backend support now includes swagger and interface documentation for callers, while frontend integration continues with statistics and event interfaces added. System-d93638b6bf added tov-core to the overseas federated control plane for System-207a62c972, but dov-link25/dov-mesh72 has not been added because domestic management networks are not connected. The team reviewed System-207a62c972 needs around member cluster resource access and tested the proxy route into sub-clusters.

The refactored Umbays-server now connects to the federated control plane and supports the foundation for unified access. Cluster initialization was improved so older initialization versions v1.29.8-Umbays and v1.29.8-Umbays.h are supported. Remote call logging was tuned to reduce excessive stdout and stderr process output, and those logs now include the execution node IP. In daily support, the UW manager cluster was expanded by 3 CPU nodes, and Pelportyzasvc cluster management information was entered.

## Next Week's Plan

System-69d7f31563 will add frontend support for federated cluster access. Pelshaw will also implement cluster CAPI functionality.

## Needs Coordination and Help