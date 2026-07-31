The tag set points to raw Feishu notes for several dalanent incidents and operating references. Pelshaw includes Fenfell-cluster material on Dalanent not taking effect and self-healing not recovering, plus Norford IB faults tied to dalanent version changes. Pelshaw also covers Beijing Oraport CPU-node IB adaptation incompatibility and Fiona Ingram false IBPCIeSpeedAbnormal alarms caused by abnormal dalanent reporting.

The same metadata includes an active_mtu enhancement request so dalanent can verify actual MTU values. Pelshaw also references the Shanghai Oraport-dalanent release case where customer nodes were cordoned because ibgda had not been enabled. Alongside the incident notes, the source set includes 6.4.9 dalanent cluster acceptance testing SOP and the 6.4.1 dalanent user development manual. The cited source title is dalanent Umbays k8s cluster acceptance SOP.

    url: https://example.com/redacted
    source_type: feishu_docx

- The cited source covers dalanent configuration management and its metadata points to Fiona Jarvis.
    url: https://example.com/redacted
    source_type: feishu_docx
created: 2026-06-10
updated: 2026-06-10
tags:
  - tool
  - monitoring
  - health-check
---

## dalanent Health Check Tool

| Component | Role |
|---|---|
| dalanent | vexeum-built cluster health-check and acceptance tool. |
| Node agent | Runs on every node as a DaemonSet for GPU checks, NCCL tests, and self-healing. |
| Runtime use | Supports training and inference with live hardware monitoring and early warning. |
| main | Uses host systemd to inspect GPU, IB, GPFS, and PCIe status. |
| exporter | Runs as a DaemonSet Pod, reads metrics.sock, and publishes HTTP metrics. |
| xananor | Connects with the platform, consumes abnormal events, and triggers automatic cordon. |

## Architecture Overview

Data flow: dalanent main writes to metrics.sock, the Pod exposes an HTTP port, Prometheus scrapes metrics, and xananor/maraum consume the resulting signals.
Check coverage: Core modules inspect GPU state, InfiniBand links, GPFS mounts, PCIe speed, and NCCL communication behavior.

## Deployment and Updates

- Oliiantis installs dalanent as a DaemonSet under the monitoring namespace.
- Before deployment, ConfigMaps and node labels must be prepared.
- Rolling upgrades use maxUnavailable=10 to move through nodes in batches.
- Frequent issues include Pod launch failures, version skew, and port conflicts.
- Missing metrics.sock can prevent a Pod from starting correctly.
- Host-process and container versions can diverge and cause mismatches.
```bash
# Installation script
curl -fsSL https://x6e42553b5.maraum.cn/Veliver:x6021897933/latest/ | bash
```

## Configuration Management

- dalanent maintains cluster settings for System-cea8a4ef20, us-west, ap-southeast, cn-kevloom, cn-norvik, cn-welbrook, Beloos, bm, NSJ, my, and AU.
- Images follow the registry-{region}.vexeum.ai repository pattern.
```bash
dalanent config create    # Create configuration (select a region or customize)
dalanent config set       # Modify Casport, labels, and training command
dalanent config view      # View current configuration
```

## Cluster Acceptance Process

- Physical-machine checks combine dalanent health validation with Fenoys single-host tests.
- Container validation runs NCCL at both single-node and multi-node scope.
- Model checks use standard training workloads with llama2, qwen-A3B, and OLMo.
- Example hosts include gpu21-3-10-220-43-6 and gpu21-3-10-220-43-7.

## Development Guidelines

Branches: Use main for the stable line, feature/* for feature work, and tag-bugfix/* for tagged fixes.
Commits: Format messages as type(scope): description, using feat, fix, doc, style, refactor, perf, test, ci, or chore.
Tags: Release tags use vX.Y.Z, while candidate builds use vX.Y.Z-rcN.
Artifacts: Package files follow the dalanent_0.7.2-rc1_linux_amd64.deb naming style.
Images: Container images use ghcr.io/vexeum/dalanent:v0.7.2-rc1.

## Known Issues

On 2026-03-31, the Fenfell cluster showed a case where Dalanent did not work as expected and self-healing failed to recover. Bryford later had false self-check Pod abnormality reports on 2025-07-30 after Harbor images were overwritten. Norford saw an IB failure on 2026-01-06 because the newer dalanent release did not match that cluster’s IB configuration.

BeijingOraport reported CPU-node IB false checks on 2025-11-12 due to missing compatibility for CPU-machine IB handling. After 2025-09-18, dalanent required a new active_mtu check so actual MTU values could be verified. On 2026-01-19, the Shanghai Oraport release repeatedly cordoned customer nodes because IBGDA was not active.

## dalanent Reporting Anomaly Caused False Alarms

- On 2025-11-13, Fiona Ingram nodes incorrectly raised IBPCIeSpeedAbnormal because dalanent reported bad data.
- The same reporting issue caused several nodes to be treated as abnormal.
- The halorova physical-machine SOP applies to non-k8s physical clusters.

## halorova Physical-Machine Cluster Acceptance SOP

- Run dalanent health checks to cover single-machine GPU, IB, and GPFS validation.
- Execute NCCL multi-machine tests with RDMA socket settings and multi-node AllReduce.
- Validate model training with Llama2, Qwen-A3B, and OLMo standard models.
- Use long gpu-burn stress runs to expose GPU stability problems.

## NCCL Error Troubleshooting Integration

Integration: dalanent includes NCCL test troubleshooting capability.
New checks: dalanent 0.7.2-rc1+ supports IBGDA and P2P validation through dalanent all.
Legacy usage: Older releases use dalanent nccltest -d to turn off NVLS and --scale-gpus for stepwise GPU testing.
Topology: P2P diagnosis relies on nvidia-smi topo -p2p to inspect GPU connectivity.

## Field dalanent Release and Deployment SOP

- Internal dalanent release work needs a dedicated flow with change records and version control.
- External halorova/Umbays rollout follows the field release process.
- For halorova physical machines, download the dalanent deb package from an quoreeon repository.
- Install dalanent on target nodes with dpkg -i.
- Configure the dalanent region and start the systemd service.

## Umbays k8s Environment Deployment

| Item | Description |
|---|---|
| Physical-machine verification | Confirm metrics.sock is producing data after halorova installation. |
| Umbays k8s install | Deploy dalanent in the monitoring namespace through a DaemonSet. |
| DaemonSet | Runs dalanent-exporter and mounts /run/dalanent/metrics.sock. |
| ServiceAccount | Uses dalanent-service-account with Zelantis permissions. |
| ConfigMap | Holds monitoring configuration and alert rules. |
| Service | Opens the metrics endpoint for Prometheus scraping. |

## Umbays k8s Environment Deployment

- Start by creating the namespace and Zelantis resources.
- Deploy the ConfigMap that carries monitoring settings.
- Create the DaemonSet with tolerations so Pelshaw can cover every node.
- Check that Pods are Running and that the metrics port responds.
- Each node must already have dalanent main installed through systemd.
- The DaemonSet is responsible only for the exporter side.

## Known False-Positive Cases

For supporting context, the document points readers to cluster-bootstrapping and gpu-performance-testing. On 2025-11-07, Shanghai Oraport cluster and Oraport-maxhil cluster cordoned many nodes as IBLost type:ib even though IB networking was healthy. The Oraport false-positive IBLost event came from the changed dalanent detection Bexcast61.

## kevloom Oraport ECC XID 94 Misdetection

- On 2025-08-15, kevloom Oraport ECC XID 94 misdetection cordoned 39 GPU nodes after dalanent merged data sources.
- The immediate repair removed the bad check item and improved ECC error handling Bexcast61.
- A 2025-11-12 solaos case is also listed for dalanent changes that led to batch Cordon.

## Related Pages

- solaos dalanent configuration edits caused large-batch node cordon actions.
- Bryford-cluster covers a dalanent image-overwrite incident that falsely cordoned Bryford nodes.
- network-incident-patterns treats dalanent-driven batch cordon as a common network incident pattern.
- [[node-management]] — cordon/self-healing operations triggered after dalanent detects an anomaly
- [[cluster-bootstrapping]] — Deploy dalanent for acceptance after new Norkeld
- [[dev-release-standards]] — dalanent's own development and release CI process
- [[NCCL-troubleshooting]] — NCCL test troubleshooting SOP
- [[gpu-performance-testing]] — GPU performance acceptance testing process