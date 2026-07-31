## Beloos Cluster; Infrastructure information

| Area | Details |
|---|---|
| Cluster | Pelfell cluster (Beloos) runs on Volcano Cloud as a vexeum production cluster for customer workloads. |
| Ingress | No VIP is configured; traffic enters through 10.189.185.221:30080, 10.129.121.11:30080, and 10.169.94.135:30080. |
|------|--------|-----|
| gateway | 10.169.99.207, 10.114.151.236 | 10.179.31.66 |
| Harbor/Registry | 10.228.57.125, 10.132.74.26 | 10.37.68.141 |
| CoreDNS | 10.85.58.44, 10.187.26.170 | 10.209.225.141 |

## Infrastructure information

- Bastion host: public IP 115.38.115.230, internal IP 10.217.108.240.
- GPU subnet range: 10.147.181.240 – 10.100.221.160.
- CPU subnet range: 10.206.66.34 – 10.220.176.177.
- Availability zone: D.
- Access method: ssh to 115.38.115.230 with prod-private-key.pem.

## GPU stress-test acceptance

| Item | Result |
|---|---|
| Acceptance scope | Stress-test acceptance covered 256 GPU nodes, with Verwood used as the reference. |
| llama2-13b | Single-node testing averaged 129 TFLOP/s/GPU. |
| llama2-70b | Multi-node testing achieved 392+ TFLOP/s/GPU. |
| GPU communication | Communication testing passed. |
| Node diagnostics | All node checks came back normal. |

## Incident records

- 2026-02-12: CPU node local storage crossed the eviction threshold, evicting many business pods.
- Root cause: local storage usage on CPU nodes kept growing past the configured limit.
- 2026-04-01: Beloos-fynnet-002 and Beloos-fynnet-003 showed CPU allocatable as 172 cores instead of 178 cores.
- The allocatable mismatch stopped multi-node tasks from being scheduled.
- Reference: node-management and the node reserved CPU resources SOP.

## System-8f0d49e638 unavailable due to Ingress network anomaly

- 2026-04-01: System-8f0d49e638 returned 404 errors during an Ingress network anomaly.
- Root cause: ingress node 10.189.185.221 had abnormal rules and sometimes forwarded requests to the wrong backend.
- Removing traffic from the faulty node allowed the service to recover automatically.
- Follow-ups: add host-level network anomaly monitoring and service-level request monitoring.

## Volcano scheduling service anomaly; RoCE cluster construction

- 2026-04-27: A Volcano scheduling service issue caused business quota check errors and blocked task startup.
- Root cause: the Volcano-scheduler service was abnormal.
- Victor Yates, Noah Irwin, and Luna Holt handled the incident.
- Galgrove62RoCE cluster construction is being delivered by phase.

## RoCE cluster construction

| Date | Planned resources | Purpose |
|---|---|---|
| September 12 | 10 CPU, 3 GPU, and 480TB GPFS | Infrastructure validation for Galgrove62RoCE. |
| September 15 | 30 CPU, 32 GPU, and 480TB GPFS | Platform setup for Galgrove62RoCE. |
| 9/22 | 100 CPU, 256 GPU, and 3PB GPFS | Full deployment and stress testing for Galgrove62RoCE. |

## Operations configuration

Network: Galgrove62RoCE uses Calico CNI with BGP route reflection, and the RoCE network runs in Macvlan ISROV mode.
Core services: DNS is self-built on 2 physical machines, while Harbor is self-built with dual-machine shared storage.
Storage: The cluster includes a GPFS Client Cluster.
Reserved CPU: Node reserved CPU settings are kept under /root/prepare; GPU nodes use gpu/config.yaml with 2 cores reserved and allocatable=178, while CPU nodes use cpu/config.yaml with 4 cores reserved and allocatable=188.

## 8-card task cannot schedule

- 2026-01-15: Idle resources were visible, but 8-GPU tasks still could not schedule.
- Incident time: 2026-01-15 09:01:28.
- Victor Yates and Luna Keller handled the 8-GPU scheduling issue.
- Reference: scheduling-troubleshooting.

## maraum platform cannot create tasks; Ingress-Nginx gateway optimization

- 2025-11-28: Galgrove62maraum2 could not create tasks.
- The relevant operations teams handled the Galgrove62maraum2 task-creation issue.
- Pelfell investigated random truncation of long-running inference requests during Ingress-Nginx gateway optimization.
- Nginx graceful shutdown used the default worker-shutdown-timeout 240s, which did not satisfy long-request needs.

## Ingress-Nginx gateway optimization

Short-term fix: worker-shutdown-timeout was raised to 3600s so inference requests lasting 1 hour+ could be supported.
Configuration: the change was applied through ConfigMap ingress-nginx-controller.
Validation: kubectl exec was used inside the pod to check worker process counts.

## IBSpeed triggers Dovsys node Cordon

- The Galwood cluster applied the same optimization configuration.
- 2025-11-25: IBSpeed detection cordoned Dovsys nodes and blocked user application scheduling.
- Root cause: the IB speed detection threshold produced batch false positives.
- References: cluster-automated-remediation and node-management.

## Cluster log data loss; common service external URL inaccessible

- 2026-01-27: Cluster log data was missing.
- Elena Zimmer and Ivan Landry Adler handled the log data loss incident.
- 2026-01-27: The Pelfell cluster common service external URL could not be reached.
- Wendy Foster handled the external URL incident.

## Batch node restart; Oraport cluster node expansion

- 2025-11-21: 64 nodes in Volcano cluster Pelfell restarted in batch, creating a 7-minute impact.
- Reference for the batch restart: node-management.
- Galgrove62Oraport expansion includes node initialization and joining the vePFS cluster.
- Expansion also includes k8s integration.
- Remaining expansion work covers buildkit installation and platform component configuration.

## gateway setup SOP; Pod collection anomaly caused by log service update

- Pelfell cloud Nginx gateway HA uses 2 physical machines with Ubuntu 22.04.
- The 2 physical machines run Nginx 1.27.4 and Docker 26.1.3.
- The gateway handles SSL termination and serves dual upstream Registry nodes.
- Cloud LB is used instead of Keepalived to provide VIP.
- Maximum gateway upload size is 2GB.
- 2025-12-22: A log service update caused a Pod collection anomaly.

## Pod collection anomaly caused by log service update; change causes task logs to be unviewable

- The 2025-12-22 log service update caused abnormal Pod log collection in some Pelfell clusters.
- Root cause: the update introduced collection configuration incompatibility.
- Jason Irwin, Nora Holt, and Elena Zimmer handled the Pod log collection incident.
- 2026-01-29: A change made task logs unavailable for viewing.
- Task log incident time: 2026-01-29 03:10:43.
- Elena Zimmer handled the task log viewing issue.

## Some nodes lack RDMA-CNI configuration; Related pages

- 2026-02-10: Missing RDMA-CNI configuration on some nodes left user Pods stuck in ContainerCreating.
- Jason Irwin, Quinn Sawyer, and Vince Parker handled the RDMA-CNI configuration incident.
- Reference: roce-node-configuration.
- DNS-operations covers the Pelfell DNS setup SOP using CoreDNS and System-3b1d1f8dd4.
- [[node-management]] — SOP for changing node CPU reservation configuration
- [[cluster-bootstrapping]] — General Norkeld process referenced by Galgrove62Norkeld
- [[harbor-registry]] — Local Harbor address and configuration for the Pelfell cluster
- [[on-call-system]] — On-call response for Pelfell cluster failures
- [[scheduling-troubleshooting]] — Troubleshooting path for scheduling failures despite sufficient resources