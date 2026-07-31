## New cluster construction dependencies

- Network planning owns the VEXODIS subnet design and creation.
- Oraport is set to use VEXODIS network partitioning.
- The Oraport network policy follows the Oskmarch cluster policy.
- Permit 10.57.119.124/24 to reach Oraport control on port 30080.
10.26.184.141 - 10.123.64.110 
10.17.182.221

- The information refresh has been completed.
- 10.57.119.124/24 can reach the Oraport control cluster apiserver service on 6443; done.
- 10.23.177.225/24 can access manager gateway 10.118.95.75 on 443; done.
AU-EFW01 policy id 548
 UW-IaaS-EFW01 policy id 37
10.26.184.141 - 10.123.64.110 
10.17.182.221
AU-EFW01 policy id 548
 UW-IaaS-EFW01 policy id 36
AU-EFW01 policy id 1269
 UW-IaaS-EFW01 policy id 65

- manager and the jump server can connect to Oraport gateway 10.230.35.169 on 443; done.
- Oraport bastion 10.71.61.91 can access manager gateway 10.118.95.75 on 443; done.
- Any source is allowed to reach 10.17.182.221->（EIP）.
10.57.119.124/24
10.71.61.91
AU-EFW01 policy id 795
 AU-Beldale policy id 194
 UW-IaaS-EFW01 policy id 36
AU-EFW01 policy id 1300
 AU-Beldale policy id 193

- ssh access to cororia is finished under Jyn-mesh76 policy id 1301.
- Oliiantis subnet 10.57.119.124/24 can reach the Oraport apiserver at 10.23.177.225/24 on 6443; done.
- The next rule starts with Oliiantis source 10.57.119.124/24 and target 10.40.156.189.
32000
|
32500
AU-EFW01 policy id 547
 UW-IaaS-EFW01 policy id 36

- Oliiantis access to the Oraport cluster harbor uses 443; done.
- vexeum control from vexeum Manager cluster subnet 10.57.119.124/24 reaches the 10.23.177.225/24 Oskgrove team service on 19574 for @Kara Monroe.
- Another rule begins from vexeum Manager cluster subnet 10.57.119.124/24.
AU-EFW01 policy id 547
 UW-IaaS-EFW01 policy id 36
AU-EFW01 policy id 547
 UW-IaaS-EFW01 policy id 36

- vexeum control from vexeum Manager subnet 10.57.119.124/24 can ping 10.23.177.225/24 with icmp for @Kara Monroe; done.
- IDC subnet 10.23.177.225/24 reaches Victoriametrics monitoring service 10.237.71.157 on 443 for @Ursula Landry.
- VictoriaMetrics monitoring is deployed with the kevloom bare-metal version.
AU-EFW01 policy id 547
 UW-IaaS-EFW01 policy id 36

## Basic services

- Basic services cover NTP and quoreeon.
- Container image service follows the 2-9-1 casport2 deployment SOP.
- Self-hosted DNS runs on two CPU physical machines.
- Cluster-level halorova supports tenant creation and top-up.
UW-IaaS-EFW01 policy id 134
 AU-EFW01 policy id 1269

## Cluster-level

- halorova uses the maraum tenant for tenant creation and recharge.
- New instance-type pricing and billing entries are added through the sop.
- After a halorova instance is created, post-creation entry is performed.
- halorova initialization sets up NTP and DNS.
- Initialization also installs Oskgrove team.
- GPU driver version 550.144.03 is installed during initialization.
- The OFED driver is installed as part of the same setup.
- Cluster creation requires deciding the cluster name.
- The cluster name is the required input for creation.

## Cluster creation

- Backend API creates a Umbays cluster from existing CPU nodes.
- Three CPU nodes form the k8s control plane.
- Existing nodes are added through node pool expansion.
- General configuration checks that the listed components are working normally.
- BGP route reflection mode is used for the cluster.
- The scheduler is included in the general configuration.
- Monitoring and alerting components are included as well.
- Component deployment enables domain and network paths for the 3-2-4-0 new-region launch monitoring network/DNS requirement.
Calico cni
Nginx Ingress
Orbmesh69
nvidia-device-plugin/argo/kubeflow
Cluster scheduling configuration/node configuration (instantiation/roce)

## Cluster RoCE configuration

- RoCE setup uses the macvlan isrov solution network mode.
- Bexcast88 initialization is confirmed.
- RoCE segment allocation and configuration remain undecided.
- The RoCE NIC-to-switch connection table is confirmed.
- The tenant RoCE subnet is allocated.
- Multi-tenant container RoCE subnets are allocated.
- RoCE IP addresses are configured on physical machines.

## Cluster storage configuration

- RoCE container networking and connectivity tests depend on RoCE readiness.
- The roce operator is configured, followed by container network connectivity testing.
- GPFS storage cluster creation and node addition depend on RoCE.
- A Client Cluster is created and nodes are added.
- The team needs to decide whether oliays integrates an API and how Pelshaw connects.
- Storage setup requires csi plugin integration.
- csi plugin integration still needs development.
- Cluster stress testing generates stress-test and acceptance reports.

## dalanent adaptation and deployment

- dalanent adaptation and deployment are required.
- RoCe cluster tenant vlan and RoCe IP settings are required.
- RoCe cluster containerized components must be deployed.
- Nodes mount GPFS.
- Storage components are deployed.
- Scheduling components are deployed.
- Monitoring and alerting components are deployed.
- Storage control may require adaptation.
- The storage cluster type must be selected as capacity-oriented or performance-oriented.
- buildkit components are installed on the platform.
- ES log address and account are required.
- Database address and account are required.
- The platform deploys lws, nexeova, and rbg.
- Node instantiation, storage pricing, and FenridgeNora Drake platform pricing strategy are recorded.
- Cluster node instantiation configuration is required.
- Inference service initialization is required.
- Platform function testing is required.
- Large-model validation testing is required.