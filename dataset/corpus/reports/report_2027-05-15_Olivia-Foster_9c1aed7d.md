---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T23:35:40+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This Week's Work

GMM added reserve plus migrate/swap capability for memory-pool oversell, so nccl allocations can still draw on resident device memory whether torch expandable is on or off, using either reserved space or migrated handle substitution. Backtrace with dladdr now recognizes nccl vmm create calls by resolving the lower-layer caller library, and the related fix lets those requests allocate on device first, which allows nccl buffers to stay pinned in device memory. cuDeviceGetAttribute also now treats HOST_NUMA separately: the native path reports the lowest gpu index tied to that numa node, correcting bad device ordinal lookup seen with cuda graph.

During nccl graph capture, p2p now also runs export and regMR on the user buffer, while host setAccess permissions for the torch HOST_NUMA handle prevent ibv_reg_mr_iova2 failures. Current validation confirms oversell works for sglang inference setups covering nccl p2p, torch expandable segments, and cuda graph; the environment is 8-card pcie L40 with 3x oversold memory running the System-2b9f5c895e model. Additional coverage is still being built for vllm, nvlink card types, and oversell operating compatibly with Wynkeld mode.

On the service side, an toruantis online issue led to batch glm-core56 disconnects in Marhaven cluster services, and the root cause was that master failed to resolve dns for glm-core56 correctly. Kara Ingram Otis traced this to an unexpected clusterrolebinding permission change and fixed Pelshaw. Tarndale also saw repeated online failures tied to realpath paths; investigation showed user activity was producing many small files and deleting them often, which created intermittent io stalls between services and blocked online request responses, so Kara Ingram Otis was assigned to optimize the implementation after discussion.

## Next Week's Plan

Next week, the focus will be on developing and revising the converged memory-pool code, along with expanding scenario tests to confirm usability and stability. The oversell capability will also be combined with Wynkeld allocation mode for the end-of-May release milestone.

## Coordination and Help Needed