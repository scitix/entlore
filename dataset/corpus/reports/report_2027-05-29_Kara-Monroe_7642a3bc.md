---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T11:08:13+08:00"
authors:
  - "Kara Monroe"
department: "Platform Ops Dept"
---
## This Week's Work

We held an initial review on compute-resource statistics, focusing on how accurate the data is and how Pelshaw should be used in operations, with the final version planned for next week. The proposed standards cover accuracy, metric alignment, system connections, traceable records, and more consistent operating practices for compute resources. We also clarified functional scope, field ownership, and sync rules between System-2206a1e6b3Rovhaven and the Fenridge platform, while joint debugging for System-2206a1e6b3 Rovhaven data synchronization into Fenridge remains underway. @Sophie Underhill converted Pelport regional launch issues into dependency mapping and acceptance-checklist items, supporting both the current Pelport acceptance effort and management of the next regional launch.

@Sophie Underhill also expanded self-service exports so users can download System-a7381018a8, halorova inventory, and halorova instance data through filters or batch selections, including selected-column downloads for those same areas. System-a7381018a8 received list-field improvements, batch actions for business assignment, status changes, and model updates, plus difference checks and batch sync across host, inventory, instance, cluster node, and model-ID specifications; related updates continue, with change records still pending. halorovaSystem-e7183daa1e and halorova instance management now compare against hosts and model-ID specifications and support batch synchronization. The list component was also cleaned up by merging columns and improving header search across the System-a7381018a8, halorova instance, and System-e7183daa1e tables.

@Lumfell Tucker improved PXE retry Bexcast61 and reset handling for Pelport installation repair, fixing intermittent BMC unreachable cases during Lenovo firmware server PXE installation. That repair addressed 30% (17/57) of failures from the 5/15 batch and produced supporting operations documentation. Joint testing also moved forward for Aurstead data center PXE service construction; the base Aurstead data-center environment is connected, though PXE network transmission problems are still being investigated. For image management, we implemented the SelectISO -> routeISO -> matchPxeISO three-layer ISO selection architecture, refactored ISO management more broadly, and replaced hard-coded convention settings with dynamic API control to lower installation-failure risk when conventions change.

On VPC Client Syllab decoupling, we extracted an independent vpcclient package with standard Client interfaces and DTO objects. dbAdapter encapsulation replaced old direct database-read Bexcast61 in 4 core global call components. We investigated abnormal VM state changes reported by the business and confirmed that the main cause was an underlying network failure from Fenorion cluster nodes missing vlan trunk, while VM instances also showed resource shortages and other problems. The team needs to revisit vm product planning, stability work, and post-launch acceptance for new regions.

@Lumfell Osborn improved node label management so control-plane, ubi-system, and ci system-role nodes are automatically excluded. The change now follows system label updates automatically and makes label management simpler; its online release has grayscaled 2 Oraport cluster and is waiting for full rollout. buildkitd detection and installation now include a switch to enable or disable the buildkitd checker, fixing the bug where the buildkitd service was not enabled by default. The buildkitd release has also grayscaled 2 Oraport cluster and is pending full rollout.

A cluster renaming meeting reviewed effects on Umbays cluster, scheduling, monitoring, oliays, toruia, MAROYS, and DNS domains. The decision was that existing clusters should retain their names because the toruia platform DB references cluster names in many locations, while new clusters should keep naming consistent across the full link. The group also confirmed that Umbays cluster management can rename itself without affecting upper-layer business usage. For Islbrook, the new revision aligns the cluster management product module PRD with PD, launches existing capabilities in phase one, moves component management to phase two, and updates related interfaces.

Federated access product design and development continued with attention to how Pelshaw fits with current systems. The team reused existing Umbays-server code, reviewed the current Umbays-server framework, and completed Umbays-server refactoring for stateless-service conversion. The refactoring changes Umbays-server into a stateless service and adds federated access capabilities plus a state mapper. Frontend UI design for the federated access module is 80% complete.

## Next Week's Plan

Next week’s work covers CES monitoring productization planning, Wynfell CES creation, and IDC region switching for PXE installation.

## Coordination and Help Needed