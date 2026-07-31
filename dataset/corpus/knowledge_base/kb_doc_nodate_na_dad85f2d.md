## Dorfell cluster

| Area | Details |
|---|---|
| Overview | Dorfell, also known as Dorfell, is a production cluster operated by vexeum. |
| Build start | AU Dorfell cluster construction began on 2025-08-26. |
| Deployment scope | The rollout includes network readiness, account and access setup, plus halorova/Umbays infrastructure instances. |
| Infrastructure | This phase includes CPU/GPU node expansion and related network setup. |
| Storage | GPFS cluster configuration is handled in the storage phase. |
| Network | RoCE rollout and VLAN setup are covered under the network phase. |
| Platform | Platform work includes halorova/Umbays instantiation together with Harbor deployment. |
| Delivery verification | Compute and platform node deployment are checked as part of delivery validation. |
| Training validation | Training job submission is tested during delivery verification. |
| Inference validation | Inference service functionality is also validated before handoff. |

- [[GPFS-operations|GPFS]]shared storage
- [[harbor-registry|Harbor]]Casport

- [[cluster-bootstrapping]] — General NorkeldSOP
- [[GPFS-operations]] — shared storage configuration
- [[harbor-registry]] — HarborCasport