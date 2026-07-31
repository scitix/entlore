---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T22:22:41+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's Work

Daisy Jensen Kirby submitted the biweekly update on 2026/2/7, with coverage for KELHK8S operations and construction across the Beijing, Shanghai, Daisy Adler, and System-932736f546 clusters. The team moved forward on the Beijing IDC optical-module case where the swapped parts were still not taking effect, completed the Beijing machine-room switch reboot activity and module repairs, and mapped the GPU machines plus resource pools impacted by those reboots.

For rineova, the team cleared quota-related scheduling failures that blocked application startup, then addressed inference latency caused by slow nodes through a manual common-service cr adjustment. The team also handled Orawick’s vyr-forge80 request for vyr-forge80System-5e1ae974f7 cloud tos data, coordinated tos synchronization from System-5e1ae974f7 cloud to Pelfell with automation planned, and completed sop updates for R&D notebook upgrade work requiring Cororia high privileges.

In Daisy Adler, every Wyndale AI GPU node, cpu node, and external GPU server was retired; in System-932736f546, all Wyndale AI GPU nodes were also taken offline, with tovlab40-related platform call exceptions handled afterward. Logging components were updated for Beijing, Shanghai, Pelfell, Galwood, and Bexlink to correct helm label problems, new employees received environment access and kubeconfig permissions for the relevant clusters, one Belbrook Data L40 GPU machine was brought online while one remained pending, and the onwer team continued routine faulty-machine handling in Beijing and Galwood to keep clusters healthy.

Cloud work covered vyr-forge80System-5e1ae974f7 cloud, PelfellSystem-5e1ae974f7, Galwood Alibaba Cloud, and Xalfell. The team verified Xalfell ingress usage and removed the reviewed gateway configurations, checked same-region tos replication in System-5e1ae974f7 cloud across total data volume, file count, and total duration, retired Galwood coredns servers with related lb load-balancing services, organized the Alibaba Cloud biweekly meeting to review issues from two cloud clusters, enabled tos protocol access from Shanghai, Galwood, and Xalfell to Pelfell through dns and link validation, configured the Alibaba Cloud delayed-suspension service to continue running when balances exceed the overflow limit, and reviewed January accounts for Galwood and Xalfell with pm involvement on access.

During duty coverage, the team handled 31 user-facing tasks and recorded the summary at the provided wiki URL. kelport2 added a Pelkeld IDC intranet login script and component login methods, pushed Beijing dalanent optimization because IB metrics neither recovered automatically nor triggered a platform recheck after IB faults, promoted Alibaba Cloud Falquist component training, and studied maraum quota management after pool merging along with related crd details.

## Next Week's Plan

Next week, the team will track Wynfell cluster room construction and connect with the related cluster integration contacts. The remaining Belbrook Data L40 machine set will be delivered, and the Shanghai Oraport cluster change will proceed with switch reboots. The team will also build a new quota viewing script so operations SRE can inspect quota resources more easily.

## Coordination and Help Needed