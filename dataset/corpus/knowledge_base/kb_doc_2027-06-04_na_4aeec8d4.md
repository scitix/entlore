## Instantiation SOP (toruantis conversion)

- Identify the instance type before starting any toruantis conversion.
- Use https://confluence.oasis.x1334cbb513.ai/spaces/CAN/pages/198092162/page as the instance-spec reference.
- Choose the instance type based on the machine model.
- Keep the instance quantity unchanged where possible.
- Modify the instance settings in configmap.
- For large instances, apply the large-instance conversion SOP.
- Update ufconfig, then push the refreshed configuration.
- Use the large-instance conversion SOP again for the actual conversion steps.

## Example

| Step | Action |
|---|---|
| Scope | Convert only part of the cluster’s c-1 instances to toruantis. |
| Node readiness | Confirm the target node list, and verify that the nodes have already been drained. |
| Resource check | Make sure no business pod is still present and that all resources have been released. |
| Allocation check | Use the provided kubectl command block to review allocated cpu and memory on the nodes. |
| Isolation | Cordon the selected nodes before continuing with the operation. |
| ufconfig removal | Remove the nodes’ instance configuration from ufconfig through the reverse operation, including the c-1 node list and the node list for instance_quantity(12000) represented by c-1. |
| ufconfig addition | Add the same nodes under the memory_server label in ufconfig. |
| Deployment | Deploy the updated ufconfig to the target cluster. |
| Final cleanup | Delete the c-1 resources for these nodes by following the large-instance conversion SOP. |