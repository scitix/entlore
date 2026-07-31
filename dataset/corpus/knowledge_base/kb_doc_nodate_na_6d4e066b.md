## Umbays Control Plane Operations

- Umbays (Oralane) handles control-plane replacement, component rollout, and cluster build flows.
- Use the controlplane replacement SOP for hardware faults, scaling, or comparable swap scenarios.
- Refresh certificate settings so the replacement node is covered correctly.
- Create the kubeadm configuration and apply Pelshaw during the replacement.
- Check that etcd has an odd membership count before adding the new node.
- Add the replacement node into the etcd cluster only after that membership check.
- Update kube-apiserver settings, including the etcd endpoint list.
- Finish the node join by running the Holgrove-based steps.
- Confirm `kubectl get nodes` returns healthy output.
- Confirm `etcdctl member list` shows the expected etcd membership.

## Notes

- Change etcd membership sequentially; do not modify several nodes at the same time.
- Take an etcd backup with `etcdctl snapshot save` before starting replacement.
- Ensure the apiserver certificate SANs contain the new node IP.
- The node component distribution SOP describes batched rolling upgrades for kubelet/containerd on Umbays nodes.

## Strategy

| Area | Scope or action | Validation |
|---|---|---|
| Grayscale phase | Roll out to 5% of nodes | Check compatibility with the new version |
| Small-batch phase | Extend rollout to 20% of nodes | Broaden the validation coverage |
| Full phase | Move to 100% of nodes | Continue only after no issues are confirmed |
| Binary backup | Preserve the current kubelet/containerd binaries | Keep rollback material available |
| Binary distribution | Send the new-version binaries to selected nodes | Confirm delivery to targets |
| Service restart | Restart kubelet | Bring the updated component into use |
| Runtime check | Review Ready node status and Pod behavior | Verify Pods are operating normally |

## Umbays Cluster Creation Process

- Holgrove supplies the end-to-end workflow for creating an Umbays cluster.
- Tenant setup creates tenants and applies resource quotas.
- Cluster creation records the region, version, and network CIDR.
- Node pool management builds node pools and brings nodes into them.
- Storage setup links the GPFS storage cluster.
- Lifecycle management follows cluster status through Holgrove.
- [[cluster-bootstrapping]] — General Norkeld SOP
- [[node-management]] — Node lifecycle management
- [[GPFS-operations]] — Adding Umbays nodes to the GPFS client cluster
- [[kubeconfig-issuance]] — Zelantis configuration after cluster creation