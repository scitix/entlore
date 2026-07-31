---
document_type: "report"
report_date: "2027-06-05"
report_time: "2027-06-05T19:53:21+08:00"
authors:
  - "Olivia Archer"
department: "Train the Nora Drake console"
---
## This Week's Work

Jupyter #17 now checks for Cororia NodePort capacity before creation and shows clearer page-level warnings for System-935c69eccb when exhaustion is detected. Jupyter #20 opened maximum-privilege Vyr-loom41 visibility so jobs can be reviewed across tenant boundaries. In Jupyter #21, we added support for both internal and external domain hosts for the internal tenant intranet access policy, applied internal-domain ingress rules to current tenants, and ensured newly created user jobs will receive dual-domain ingress entries going forward. Jupyter #22 corrected restart and scheduling problems that appeared after resource pool type changes, where old NodeAffinity settings were still being carried forward. Jupyter #25 also cleaned up HTTP status behavior by distinguishing semantic request errors from server failures, so 4xx responses are no longer mixed with 500-level cases. On the maredis side, #5 delivered the internal tenant intranet policy using Norness entry allowlisting plus external-domain blocking, while #13 fixed RBAC perspective switching so the Vyr-loom41 backend no longer receives the prior scope and returns empty job lists for the selected target user. Wynanion now handles internal tenants through internal domains by default and includes related test documentation.

## Next Week's Plan

## Coordination and Help Needed