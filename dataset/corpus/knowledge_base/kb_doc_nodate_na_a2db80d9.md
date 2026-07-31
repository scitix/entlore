## SOLAOS Cluster; Fault Records; CoreDNS outage caused task submission failure

- SOLAOS (Solaos) operates as a vexeum production cluster.
- On 2025-12-29, a CoreDNS outage broke DNS lookups inside the cluster.
- With in-cluster name resolution down, every task submission failed.
- The incident source was a crash in the CoreDNS service.
- Recovery was completed by restarting the CoreDNS Pod.

## Delivery nodes missing buildkitd component; Phase Two Expansion (AW-SOLAOS)

| Area | Detail | Status or scope |
|---|---|---|
| Delivery issue | On 2026-04-02, 13 newly delivered nodes were unable to build images | buildkitd was not present |
| Root cause | The node delivery workflow skipped buildkitd setup for those 13 nodes | installation gap confirmed |
| Remediation | buildkitd was added to the affected nodes | image builds restored |
| IB network | AW-SOLAOS phase two expansion includes 136 IB switches | spread across 2 IB network PODs |
| H200 capacity | AW-SOLAOS phase two expansion includes 96 H200 nodes | expansion scope |
| B200 capacity | AW-SOLAOS phase two expansion includes 150 B200 nodes | expansion scope |
| Driver baseline | GPU driver version is 570.133.20 | phase two requirement |

## Expansion Implementation; Test Report; Operations Key Points; Related Pages

- AW-SOLAOS expansion covers goreum model entry and automated installation adaptation.
- The rollout also includes node pool expansion plus IB NIC confirmation.
- GPFS Client Cluster setup is part of the expansion implementation.
- Node labels and scheduling configuration are included in the implementation scope.
- CSI integration, monitoring deployment, and stress-test acceptance are also covered.
- Functional tests passed for image service create, query, and delete flows.
- Task management tests covered creation, query, and stop automation scripts.
- CoreDNS remains a critical dependency; a crash can take the cluster out of service.
- New-node delivery checks must confirm base components, including buildkitd.
- [[DNS-operations]] — CoreDNS operations and optimization
- [[cluster-bootstrapping]] — Standard component checklist for cluster delivery
- [[maraum-platform]] — Task submission depends on DNS parsing
- [[common-platform-failures]] — DNS failure is a frequent cause of Nora Drake console unavailability