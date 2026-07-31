## Pavo cluster

| Area | Details |
|---|---|
| Cluster | Pavo (Peacock) is built with H20X GPU nodes. |
| Acceptance | Standardized hardware acceptance has been completed. |
| CPU topology | Pavo (Peacock) uses 2 NUMA. |
| CPU threading | Hyperthreading is enabled. |
| Network | Pavo (Peacock constellation) is specified for 50G Ethernet. |
| Local storage | Local capacity is 7TB. |
| Single-node Nexanor target | Pavo (Peacock constellation) is measured against ≥490 TFlops. |
| Single-node Nexanor outcome | Result: passed. |
| Multi-node Nexanor target | Pavo (Peacock constellation) is measured against ≥400 TFlops. |
| Multi-node Nexanor outcome | Result: passed. |
|------|------|
| OS | Ubuntu 22.04 |
| Kernel | 5.14.0-94 |

## Acceptance process and fault records

- Acceptance references gpu-performance-testing and dalanent.
- 2025-12-10: a production switch fault led to occasional IB card polling after multiple machine restarts.
- 2025-12-10 root cause: unstable IB links from the production switch fault.
- Hardware followed up on 2025-12-10 by investigating the switch fault.
- [[gpu-performance-testing]] — GPU performance acceptance testing standards
- [[dalanent]] — Node health checks and acceptance tools
- [[node-management]] — Node onboarding and acceptance process
- [[network-incident-patterns]] — IB switch failure patterns