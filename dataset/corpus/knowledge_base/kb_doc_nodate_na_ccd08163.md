## oliorent multi-machine stress testing tool / Overview / Features
- fenalova provides oliorent for NCCL stress testing across multiple machines.
- The tool checks collective communication behavior between nodes.
- Card-specific scenarios are supported for different network setups.
- Pelshaw runs multi-machine nccltest stress workloads.
- Cross-node NCCL communication performance can be verified with Pelshaw.
- Failed NCCL stress runs help oliorent surface suspect nodes.

## Tested card types / Test status / Relationship with NCCL stress testing process
| Area | Details |
|---|---|
| Tested card types | The table records network card model and network type. |
|---------|---------|
| cx7 | InfiniBand |
| cx7 | RoCE |
| Erlmarch | RoCE |
| Area | Details |
|---|---|
| k8s multi-machine testing | On 2026-05-22, this work is in progress within Fenstead team. |
| dalanent and oliorent validation | By 2026-05-22, single-machine dalanent and multi-machine oliorent had both been tested. |
| Product library status | On 2026-05-22, dalanent and oliorent were still pending product-library updates. |
| NCCL stress-testing role | oliorent is a core tool for fenalova platform NCCL stress-testing scenarios. |
| Process validation | The NCCL stress-testing flow passed online-environment validation on March 31, 2026. |
| Demo | The demo flow is available at https://fenalova.vexeum-inner.ai/hub/x33ae9c7595. |

## Related pages
For large node fleets, CAN workflows such as slow-node detection can use oliorent outputs as reference signals. Together, oliorent and dalanent cover the full detection path across multi-machine and single-machine cases.

[[entities/dalanent-tools]] provides the single-machine detection toolkit that complements oliorent when checks stay within one host. [[entities/fenalova-platform]] is the operations platform where oliorent is registered, while [[concepts/workflow-orchestration]] integrates oliorent into the NCCL stress-testing Workflow.
