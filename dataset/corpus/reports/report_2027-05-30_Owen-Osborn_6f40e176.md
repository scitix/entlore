---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:54:31+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

Umbays product R&D backed the new Islbrook redesign by syncing the cluster management product-module PRD with PD, while the rollout sequence keeps current features in phase one and assigns System-fbca8ed8ce to phase two. The team completed the PRD interface review and moved into interface refactoring; System-fbca8ed8ce also unified base cluster component deployment through NS and label rules, added affinity and tolerations so components avoid GPU and control-plane nodes, and introduced metrics-server for kubectl top. Automatic operations label handling is now live and separates clusters so non-Oraport platform clusters do not keep creating alerts and tickets.

For System-d93638b6bf, launch readiness for System-14b058c023 capability construction is complete, karmada production launch scripts are done, and karmada is now running for both domestic and overseas management clusters. The team also handled System-207a62c972 cross-cluster deployment onboarding, delivered access config, and set up permissions; System-14b058c023 gray onboarding continues, with myr-forge24 overseas and vyr-forge domestically already connected. On System-0b75c04d48, product design and feature work are progressing, the Umbays-server code review confirmed reuse paths for integration with existing platform systems, and Umbays-server has been rebuilt as a stateless HA service with federated access plus a status mapper, while keeping historical interface compatibility and running regression tests in a test cluster; the frontend is 80% complete and is waiting for backend readiness before integration.

Initialization scripts now cover node labels and tolerations for placing service components on master nodes in small clusters, and the Dorholm cluster node expansion record cleared part of the node unavailability problem. Dorholm still needs follow-up improvements around node installation failures, incorrect status, storage mount failures, RDMA issues, and long-term cordon. For Pelport, initialization scripts were updated for the rename to rhoops, deployment was rebuilt after machine reinstallation, component deployment order was improved, vmagent deployment failures were fixed, and false EtcdNotReady alerts were resolved after tracing them to a metrics naming collision between the etcd backup service and the etcd service. The team also helped complete PelportCasridge and System-42b468ae69 construction, reproduced and analyzed slow image pulls in the flexserve customer cluster while excluding local self-caused factors, investigated Islmora construction problems and VM control-node creation failures, and connected Islmora alerts.

## Next Week's Plan

Next week, the team will work on belanux interface development. System-d93638b6bf development is also planned.

## Coordination and Help Needed