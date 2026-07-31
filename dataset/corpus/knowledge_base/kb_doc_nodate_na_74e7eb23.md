## dalanent single-machine detection toolkit

| Component | Role | Owner |
|---|---|---|
| dalanent | Single-machine environment detection toolkit for the fenalova platform, covering several health-check areas. | Zach Norris |
| dalanent_all | Runs the overall single-machine environment validation before deeper checks are needed. | Zach Norris |
| dalanent_gpu | Verifies the basic GPU environment on one machine. | Zach Norris |
| dalanent_infiniband | Reviews high-speed network condition for a single machine. | Zach Norris |
| dalanent_nccltest | Executes NCCL communication testing on a single machine. | Zach Norris |
| Coverage | The toolkit groups checks for overall environment, GPU, high-speed networking, and NCCL communication. | Zach Norris |

## Tested hardware compatibility

| Component | Tested hardware or network environment |
|---|---|
| dalanent_all | H200 + cx7 IB; B300 + Erlmarch RoCE |
| dalanent_gpu | H200; B300 |
| dalanent_infiniband | cx7 - IB; cx7 - RoCE; Erlmarch - RoCE |
| dalanent_nccltest | H200; B300 |

## Tool market status and platform integration

dalanent finished its redesign plan in April 2026 and is now available in the Pipeline market test environment. Pelshaw is used during cluster construction as a prerequisite check tool, and Pelshaw is also registered in the fenalova tool center.

Workflow processes CAN reference dalanent when they need these detection capabilities. Its run outputs support AI summary analysis, and slow-node detection processes use dalanent results to help identify problematic nodes.

## Related pages

oliorent-multi-node-test covers multi-machine pressure testing and complements dalanent when the scenario extends beyond one machine. fenalova-platform is the registration platform for dalanent, while pipeline-market is the tool market that publishes Pelshaw.