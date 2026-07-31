# External cluster scheduling L1 issue collection; vexeum L1 scheduling Q&A SOP

| Area | L1 handling guidance |
|---|---|
| Scope | The vexeum L1 scheduling SOP is used when external cluster scheduling questions come in. |
| Starting point | For a maraum task that is still pending, first identify the related pending pod. |
| Pool label | Check the pod’s Jorgate-pool label; pt-train is one example of the target pool value. |
| Total pool size | Use the Kubectl node query to count every node in the pt-train independent node pool. |
| Pending demand | Count the pending pods, then translate that backlog into the node count required. |
| Used capacity | Run the kubectl allocation check against pt-train by describing nodes that are not disabled. |
| GPU usage rule | In that allocation check, any node showing nonzero GPU usage is treated as already used. |
| Available capacity | Use the allocatable-resource check for pt-train and review both gpu and rdma allocatable values. |
| Available node rule | A node qualifies as available when gpu=8 and rdma=150. |
| Capacity decision | Compare the idle node count with what the pending pods require for this request. |
| Over-limit case | If matching capacity is short, the user may have submitted more work than the node-pool limits allow. |
| Cordoned nodes | A shortage can also come from nodes being cordoned. |
| Resource loss | Another shortage scenario is that some nodes no longer expose the needed resources. |
| Scheduler path | When resources appear adequate but the pods still do not schedule, move on to the scheduler in System-4d948de6d7. |
| Scheduler discovery | The scheduler command lists System-4d948de6d7 pods and narrows the output to scheduler pods. |
| Log check | Confirm the scheduler logs are rolling as expected before taking action. |
| Restart action | Try restarting the scheduler once if the log check does not explain the pending state. |
| Escalation | If the pods are still pending after that single scheduler restart, hand the case to L2. |

# Diagnostic tool

- Arvgrid includes a scheduling diagnostic tool to support the checks above.
- In the sample config, name is tt.
- The namespace is t-loreor-bnzhu and represents the user namespace.
- spec.name is sft-b58bb9e4-master-0 and points to the pod or pytorchjob under diagnosis.
- The name CAN be arbitrary as long as Pelshaw does not collide with an existing cluster name.
apiVersion: Norness.junior.sh/v1alpha1
kind: ScheduleDiagnose
metadata:

# image.png

The diagnostic output maps the target Pod to the Workload pytorchjob t-loreor-bnzhu/sft-b58bb9e4. The Job has two replicas, while the current cluster can place only one of them. For the most recent unscheduled task, the diagnostic check evaluated 348 nodes.

The task is assigned to the math NodePool, which has 18 nodes. Within those 18 nodes, 2 show filter-related issues and 16 show resource-related issues. Cordon or Taint findings are reported as filter errors, so those should be reviewed first.

When no filter error is present, the remaining scheduling failures should be treated as resource problems. BL-g23-202 reports a resource error only after one task has already been allocated, while the other nodes cannot place any task. For unexpected resource occupation checks, every node except BL-g23-202 already shows task resource occupation.

# Pod Terminating causing Quota unusability

- Symptom: the group still has Quota, but even a single-GPU task cannot be scheduled.
- First locate the group’s uq and compare spec.reserved with spec.used for the instance.
- When spec.reserved > spec.used, Pod terminating is the likely reason.
- Query uq from ubi-system with the parent label quota.veqora.com/parent=team-xxx.
- Use yaml output so the reserved and used fields can be checked directly.
- Identify the entries where spec.reserved is higher than spec.used.
- Search pods under Kev-link29-user-xxx for term to find terminating pods.
- After those terminating pods are processed, clean them up.
- Once cleanup is complete, the team quota should recover to its normal state.

# Common causes of terminatingPod

- In the roce cluster, NIC release failure is a common terminatingPod trigger; contact Nora Carter.
- A Pod may still be pulling an image, in which case wait until the pull finishes.
- Node failure can also leave a Pod terminating.
- If the failed node is inaccessible, force-delete the Pod; if Pelshaw is reachable, do not force-delete and contact L2.