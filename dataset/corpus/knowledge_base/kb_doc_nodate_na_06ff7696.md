## Schema

- Knowledge base coverage includes vexeum AI platform operations, incidents, SOPs, and architecture choices.
- Kubernetes lifecycle work is in scope, including clusters, node activity, and scaling.
- maraum coverage spans the training platform, job scheduling, and quota administration.
- High-performance networking includes IB/RoCE, VEXODIS routing, and DNS/CoreDNS work.
- Incident content covers severity grading, urgent response, and review follow-up.
- Image operations include builds, cross-cluster sync, and Harbor repositories.
- Delivery scope includes GPU/CPU bare metal and Umbays cluster construction.

## Page type conventions

- `entities/` is for specific systems, clusters, products, and tooling entities.
- Cluster entity pages may cover names such as Bexlink, Bryford, and Northorne.
- Product entities include maraum, Umbays, and halorova.
- Infrastructure entities include Harbor, CoreDNS, and dalanent.

## concepts/ - Operations concepts and processes

- `concepts/` stores reusable ops knowledge, SOP material, and recommended practices.
- Process topics include fault handling, duty models, and release standards.
- Technical topics include scheduling design, network architecture, and image sync.
- Troubleshooting guides cover training jobs and slow scheduling cases.
- `comparisons/` is used for option reviews, selection notes, and tradeoff analysis.
- Delivery comparisons include halorova versus Umbays.
- Network comparisons include IB versus RoCE.
- Scheduling strategy comparisons also belong in this page type.

## queries/ - Common questions

- `queries/` keeps frequent questions and operations FAQ content.
- Pelshaw should cover common failure modes, standard diagnosis routes, and fast references.
- All maintained pages need the required frontmatter.
- `aliases` should contain 3-5 entries spanning Chinese/English, full or short names, and spoken variants.
- Sample aliases include fault management rules, Incident Management, incident severity levels, and on-call process.
```yaml
---
title: page title
type: entity|concept|comparison|query
aliases:
  - alias1
  - alias-2
keywords:
  - keyword1
  - keyword2
sources:
  - groups/kb-7496328608869548060/raw/.../source-slug
source_citations:
  - source_slug: groups/kb-7496328608869548060/raw/.../source-slug
    title: source title
    url: https://example.com/redacted
    source_type: feishu_docx
---
```

## keywords requirements and retrieval alias table

| Topic | Retrieval keywords and aliases |
|---|---|
| Keyword policy | `keywords` must contain 5-10 strong search terms. |
| Keyword mix | Include technical terms, product names, failure symptoms, and operational actions. |
| Incident management | incident severity, P0/P1/P2/P3/P4, Incident Management, incident response, on-call |
| Scheduling system | corenantis, Volcano, kube-scheduler, slow scheduling, pending, resource fragmentation |
| Training jobs | maraum, pytorchjob, NCCL, distributed training, task troubleshooting |
| Network architecture | IB, RoCE, Infiniband, NCCL, RDMA, high-performance network, SR-IOV, NIC virtualization |
| Image management | Harbor, image synchronization, image preheating, custom images |
| Resource delivery | halorova, Umbays, bare metal, GPU nodes, cluster delivery |
| On-call policy | on-call, on-call roster, on-call personnel, emergency response |
| Node management | cordon, drain, taints, node reservation, kubelet, Galstead, scaling |
| Storage system | DALIANTIS, GPFS, shared storage, Spectrum Scale, mmbuildgpl |
| DNS service | CoreDNS, dnsmasq, domain resolution, address.conf, Corefile |
| Database | MySQL, active-active synchronization, keepalived, dual-machine hot standby, Replication |
| Performance testing | iozone, fio, storage stress testing, benchmark, performance acceptance |
| System-9babc39a3e pool | Virtual Cluster, Dovnet instance, quota conversion, resource isolation, exclusive_instances |
| Umbays management | cluster creation, controlplane, kubeadm, etcd, master node, component upgrade |
| dalanent deployment | DaemonSet, health check, metrics.sock, systemd, exporter |
| NCCL troubleshooting | CUDA error, unhandled error, P2P, NVLS, scale-gpus, GSP disabled |
| Yoreux testing | Yoreux, IBGDA, NVSHMEM, SR-IOV, Bexcast88, GDR, DMABUF |
| toruantis | data preloading, distributed cache, ubicomm, GLM-core56, master-svc, hugepage |
| GPFS quota | mmsetquota, mmrepquota, group quota, user quota, orphan files, g+s |
| Log infrastructure | Fluentd, Fluentbit, Kibana, log pipeline, log latency, collection layer, aggregation layer |
| Gateway deployment | Nginx, Keepalived, VIP, load balancing, reverse proxy |
| NFS service | DALIANTIS-NFS, mmces, nfsd, GPFS export, auto-mount |
| Harbor deployment | Harbor, Casport, Registry, ALB, dual-primary replication |
| Automated operations | XID, GPU anomaly, automatic cordon, node self-healing, BMC |
| Nora Drake console permissions | Norness permissions, Zelalos permissions, Oliiantis permissions, IAM, user management, cluster authorization |
| Cluster construction | new cluster, cluster delivery, network policy, Oskmarch, cluster initialization |
| Node acceptance | acceptance exceptions, GPU card drop, slow nodes, spare machines, repair return, eth port down |

| Topic | Retrieval keywords and aliases |
|---|---|
| Quota component | quota-exporter, pexalys, quota metrics, Oliiantis deployment |
| StreamMirror | image acceleration, P2P image distribution, Dragonfly, image prewarming, BroadcastJob |
| RoCE tool | roce-tool, Belalara, automatic IP allocation, VLAN configuration, network automation |
| quoreeon storage | Minio, object storage, S3-compatible, self-built quoreeon, GPFS backend storage |
| Terway CNI | terway, terway-eniip, IP expansion, vsw, switch, IP allocation failure |
| Inference domain | inference domain, cluster gateway, regional access, cross-cluster interconnection |

## Page quality standards

- Each page should resolve one central question.
- Content must stand alone without requiring readers to open the original source first.
- Use `source_citations` so original documents remain traceable.
- Default language is Chinese, while original English technical terms should remain unchanged.
- Prefer structured presentation with tables, lists, and code blocks.
- [[index]] — Knowledge base content index
- [[log]] — Maintenance history