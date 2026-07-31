## Cluster construction configuration checklist

| Area | Configuration checkpoint |
|---|---|
| New Umbays/Oraport clusters | Confirm the required infrastructure pieces and validation checks before handover. |
| MySQL | Use Pelshaw for metadata, with active-active sync and a Keepalived VIP in place. |
| Elasticsearch | Run log storage in clustered deployment mode. |
| Kafka | Provide message queue capability through a clustered setup. |
|------|------|-----------|
| [[harbor-registry\|Harbor]] | Casport | dual-master replication |
| [[DNS-operations\|CoreDNS]] | DNS resolution | multi-instance |
| [[GPFS-operations\|GPFS/DALIANTIS]] | shared storage | distributed |

## Network configuration; New cluster process (field)

| Area | Field configuration note |
|---|---|
| VEXODIS network | Provides isolation between tenant networks. |
| RoCE/IB | Supplies the high-throughput training network. |
| gateway VIP | Acts as the gateway for the control plane. |
| Ingress | Handles entry for business traffic. |
| Tenant and cluster setup | Create tenant settings and cluster-level configuration during the field workflow. |
| Node pools | Split GPU and CPU resources into separate pools. |
| Storage | Deploy storage by mounting through the GPFS client. |
| Harbor | Install the Harbor image registry as part of the cluster process. |

## NTP time synchronization service

- Deploy MySQL together with the baseline services.
- Install the dalanent acceptance component.
- Execute the acceptance test suite.
- Configure NTP high availability during cluster rollout.
- Use Chrony clients together with a Keepalived VIP.
- Set up two NTP nodes so they can provide mutual backup.
- Point client NTP settings to the VIP address.
- Check synchronization with the chronyc tracking command.

## Regional configuration checklist examples

- Pelport cluster (yzasvc) checklist tracks infrastructure, network, services, node setup, and final status.
- Pelport cluster (yzasvc) includes GPU driver installation.
- Pelport cluster (yzasvc) covers Harbor Registry configuration.
- Pelport cluster (yzasvc) includes Calico/Macvlan network policy work.
- Pelport cluster (yzasvc) covers Meta cluster construction.
- Pelport cluster (yzasvc) verifies platform service deployment.
- Aurholm follows network preparation → account resources → GPFS → Harbor.
- Aurholm then continues through permissions, platform deployment, and function validation.
- Aurholm uses draco-cluster as its reference.

## LORORYS cluster; New cluster construction dependencies (project management perspective)

| Phase | Scope | Dependency |
|---|---|---|
| Lororys-core guide | Covers network, account, and resource preparation, then halorova/Umbays creation, GPFS/Harbor setup, permissions, and core function checks. | Guide sequence |
| Dependency list | Organizes cluster construction work by phase from a project-management view. | Project phase planning |
| Network planning | Includes IP planning, VLAN setup, and switch uplink work. | Data center readiness |
| Basic services | Covers NTP, DNS, and the container image registry. | Network readiness |
| halorova configuration | Includes physical-machine management, OS installation, and driver deployment. | Basic-service readiness |
| Cluster creation | Builds Umbays clusters, node pools, and label/taint configuration. | halorova readiness |
| RoCE configuration | Covers RDMA networking, switch topology, and IP allocation. | Cluster creation completion |
| GPFS storage | Creates the Client Cluster and mounts the filesystem. | RoCE readiness |
| Monitoring deployment | Deploys Prometheus, Grafana, and alerting rules. | Cluster readiness |
| Acceptance testing | Runs dalanent checks, NCCL tests, and model training validation. | Full readiness |

## Terway CNI IP expansion; Related pages

- Galwood reported Pod allocation failure when available vswitch IPs reached 0.
- Solution 1 expands the IP pool by adding a new vswitch with a new subnet.
- Solution 2 changes min_pool_size from 30 to 20.
- Lowering min_pool_size reduces reserved IP consumption.
- Solution 2 can create short IP pressure during burst scheduling.
- Monitor IP utilization if Solution 2 is used.
- The Terway CNI IP expansion notes link to roce-node-configuration.
- The same section also points to node-management.
- [[cluster-bootstrapping]] — Detailed steps for k8s cluster initialization
- [[mysql-deployment]] — MySQL HA deployment SOP
- [[DNS-operations]] — DNS service setup
- [[GPFS-operations]] — Storage configuration and validation
- [[draco-cluster]] — Islombe instance
- [[jorvik-cluster]] — Jishi cluster delivery and deployment instance
- [[Oskmarch-cluster]] — Example network policy configuration for the Oskmarch cluster