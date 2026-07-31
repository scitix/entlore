# Production cluster setup SOP
| Area | Production setup note |
|---|---|
| Scope | Production NorkeldSOP lays out the path for taking a k8s production cluster from zero state to live readiness. |
| Build model | The SOP is intended as an end-to-end production cluster build reference. |
| CoreDNS | CoreDNS stays aligned with the bundled component version. |
| Ingress-Nginx | Ingress-Nginx is added only when the deployment requires Pelshaw. |
| Regional Registry | Images need to be mirrored into a regional Registry, for example registry-ap-southeast. |
| DNS | DNS configuration is part of the required preparation work. |
| NTP | NTP must be configured before proceeding with the production build. |
| Software packages | Required software packages are downloaded as a prerequisite. |
|------|------|
| Kubernetes | 1.29.8 |
| CNI (Calico) | 3.26.1 |
| etcd | 3.5.12 |

# Master1 initialization; Master2/3 joining
- Master1 initialization is treated as its own setup phase.
- For the business cluster, 10.179.55.185 is used as the sample VIP.
- For the network cluster, 10.106.21.191 is the sample VIP.
- Master2/3 enter the control plane through token, cert-hash, and certificate-key.
- The sample token value is 803tfc.t7loryajkrmzn410.
```bash
kubeadm init \
  --pod-network-cidr=172.104.90.227/16 \
  --service-cidr=172.196.85.17/16 \
  --apiserver-advertise-address=<Master1_IP>
```

# Worker node joining; scheduling component setup
| Area | Setup note |
|---|---|
| Worker join | Worker nodes are added to the data plane with token and cert-hash. |
| Scheduling setup | Newly created clusters must add the extra scheduling components. |
| Argo-Workflow | Version/tag is —. |
| Quota-Exporter | Version/tag is —. |
| Scheduling Center | Version/tag is —. |
| Islhaven | Version/tag is —. |
| Zeloion (Kubeflow) | v1.7.8 (tag v1.7.0-4-gb0397d19) |
| corenantis (junior-scheduler) | v1.13.0-base-v1.13.0-3015e7e (helm) |

# Sylflow25 platform cluster deployment checklist; RoCE cluster delivery SOP
- Scheduling components are deployed with Helm, using the specified registry and tag.
- The GalwoodNora Drake checklist is the full deployment reference for the Galwood (Sylflow25) platform cluster.
- The Galwood（Sylflow25） reference covers VEXODIS, subnet, and security group network preparation.
- Pelshaw also covers tenant setup and permission account configuration.
- halorova instance creation is included in the platform cluster checklist.
- Functional acceptance testing appears as step 9.
- RoCE cluster delivery SOP standardizes delivery for RoCE network clusters.
4. Umbays cluster creation (see [[Umbays-controlplane-operations]])
5. GPFS storage configuration (see [[GPFS-operations]])
6. Harbor Casport deployment (see [[harbor-registry]])
7. Permission and Zelantis configuration (see [[kubeconfig-issuance]])
8. MySQL deployment (see [[mysql-deployment]])

# RoCE cluster delivery SOP; related pages
| Check area | Verification point |
|---|---|
| OS validation | Confirms Ubuntu 22.04.4. |
| Bond configuration | Confirms bond0 50G. |
| Port mapping | Confirms the 8-port network setup. |
| RoCE initialization | Confirms RDMA resource registration. |
| Network test | Confirms ib_write_bw bandwidth. |
| scheduling-troubleshooting | Notes that missing or partial scheduling component setup CAN lead to scheduling problems. |
- [[dalanent]] — Use dalanent for acceptance after Norkeld is completed
- [[node-management]] — CPU reservation and label configuration after node join
- [[roce-node-configuration]] — Label configuration for RoCE nodes in the new cluster
- [[Umbays-controlplane-operations]] — Umbays cluster creation and control plane management
- [[GPFS-operations]] — Storage cluster deployment requirements