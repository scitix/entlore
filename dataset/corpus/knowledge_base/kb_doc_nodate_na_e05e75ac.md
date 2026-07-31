## Oskmarch cluster (Aurstead/US West) / Basic information

| Field | Details |
|---|---|
| Cluster | Oskmarch |
| Platform | vexeum Oraport production cluster |
| Region family | Aurstead |
| Region | US West |
| Alias | Aurstead |
| Added | March 2026 |
| Onboarding note | SDK changes are required before business workloads can onboard |
| Inference endpoint | inference-Oskmarch |
| Access scope | Internal network |

## Network policy

| Policy area | Allowed connectivity | Ports and purpose |
|---|---|---|
| Overall scope | Oskmarch policies define access paths from the Oskmarch cluster to CSSDorgrove39 | Connectivity governance between the environments |
| Manager→Oraport | Manager cluster access into Oraport Oskmarch | 6443, 10250 for k8s control-plane traffic |
| gateway | Gateway nodes reaching Oraport Oskmarch | 443, 80 for service entry traffic |
| Oliiantis | maroys access to Oraport Oskmarch | Specified ports used for CI/CD deployment |
| Oskgrove team | Oskgrove team service access into Oraport Oskmarch | Agent port for remote operations |
| Monitoring | Prometheus access toward Oraport Oskmarch | Metrics port for metric collection |

## Network policy / SDK adaptation / Failure records

- Security groups and ACL are the enforcement path for these network policies.
- Cross-cluster traffic requires policy approval before enablement.
- Since Oskmarch was added on 2026-03-04, SDK work must cover cluster discovery and registration.
- The same SDK update must route task submissions for Oskmarch.
- Monitoring metric collection also needs SDK support after the 2026-03-04 addition.
- Luna Holt and Vince Parker own the SDK adaptation.
- Failure tracking includes the Aurstead machine database issue from 2025-12-09.

## Aurstead machine database failure (2025-12-09) / Related pages

- The incident impacted the machine database in the Aurstead region.
- The failure timestamp was 2025-12-09 14:08:17.
- Noah Walsh, Willa Nolan, Lumfell Dawson, Kara Ingram Otis, and Luna Holt handled the event.
- Use common-platform-failures as the reference page for Aurstead machine database issues.
- node-management documents Kubelet MaxPods configuration, including Oskmarch value 220.
- network-incident-patterns documents cross-cluster network failure patterns.
- [[rineova-inference]] — Domain access for Oskmarch cluster inference services
- [[cluster-construction-checklist]] — Dependency checklist for new cluster construction