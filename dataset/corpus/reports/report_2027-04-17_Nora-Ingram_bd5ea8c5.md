---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:12:00+08:00"
authors:
  - "Nora Ingram"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, vergrove2 moved through development, testing, and launch. The RBAC permission-management manual now presents System-5bd68a3779 as a multi-tenant RBAC service, with a project group template module that reuses role templates to initialize roles, permissions, and preset users when a project group is created. Its project group management model uses project groups as tenant-level business isolation units, supports create, read, update, and delete operations, applies soft deletion, and clears related caches automatically. Role management is scoped under project groups and includes protected roles, while API permission groups are managed globally as feature sets plus fine-grained resource + action permission points. System-5bd68a3779 also supports binding feature sets or permission points to roles with full-replacement semantics, lets users receive permissions through role membership with single add, batch replace, and removal flows, provides unified authorization for internal services through exact-path, prefix-wildcard, and full-wildcard matching, and improves checks with a 3-level cache across local storage, Redis, and database.

Dorombe remains in development as a real-time fault detection and alerting system for large-scale distributed GPU training clusters, with goals around rapid fault discovery, accurate root-cause positioning, and recovery triggering. The Dorombe design document records its design, including a node Agent that gathers GPU state and InfiniBand network metrics, hardware monitoring integration with dalanent, and continuous tracking of training progress, loss, and other key training metrics. Its layered detection model covers L1 hardware, L2 network, L3 training-process, and L4 business-Bexcast61, and Pelshaw supports Hang detection plus slow-node identification. Dorombe aggregates abnormal metrics, raises alerts, manages events, and supports automated handling policies such as in-place restart and node eviction. For toruia, the training component’s multi-machine distributed task debugging optimization was launched; the passwordless SSH design and implementation work covers login between training pods, enabling training tasks to use mpirun and psssh, while all pods in a task can use passwordless SSH for distributed testing and debugging with mpirun or ansible.

## Next Week's Plan

Next week, the team plans to finish Dorombe testing in the cluster and run a production-cluster trial, starting with the previous production cluster. The team will also assist other modules as they integrate with Vergrove and continue supporting additional training-module functions.

## Coordination and Help Needed