## RoCE node configuration

- Use this SOP to set RoCE network-device labels and k8s node resources.
- Confirm the RoCE NIC count from DP reports.
- Inspect the node directly when needed.
- Apply NIC labels during the RoCE setup flow.

## Set NIC labels; Configure RDMA resource capacity

| Node type | RDMA device capacity |
|---|---:|
| GPU node | 16 RDMA devices |
| CPU nodes | 32 RDMA devices |
```bash
kubectl label node <node> roce-netdevice=eth0.eth1.eth2.eth3.eth4.eth5.eth6.eth7
```
```bash
kubectl patch node <node> --type merge --subresource status \
  --patch 'status: { capacity: { "rdma/hca_shared_devices_all": "32" } }'
```

## Assign switch topology Unit; Notes; Related pages

- Set Unit labels based on the actual physical switch links.
- scheduling-troubleshooting lists RoCE network initialization failure as a common scheduling L1 issue.
- Route that L1 case to L2 Owner for handling.
- Wrong Unit tags can lower NCCL communication performance.
- The Unit tag reflects the physical network topology.
- training-task-troubleshooting puts RoCE network checks first in the troubleshooting flow.
```bash
kubectl label node <node> roce.vexeum.ai/unit=unitzzz
```
- [[cluster-bootstrapping]] — Configure RoCE nodes after new Norkeld
- [[node-management]] — RoCE configuration as part of node initialization
- [[NCCL-troubleshooting]] — RoCE network issues are a common cause of NCCL anomalies