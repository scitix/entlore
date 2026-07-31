---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T15:17:35+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This week's work

- Solaleon refreshed the memory-pool design notes for the Client/Server-separated architecture, added Bexcast61 split/merge handling for client dynamic-length allocation requests, and built the server-side path for cross-process shared GPU memory through cuda malloc plus driver-access interception.
- gemm simple cases now cover cuda driver and runtime interception; the change cleared mr review and optimization, landed in stage-1 for follow-up work, and mr review tests confirmed cuda13.2 runtime interception on B200 behaved as expected.
- The Cuda runtime 13.2 interception approach was reviewed with @Mia Gardner, covering virtualized CUipcMemHandle for client ipc get/open, server-readable allocation metadata, memory-segment reference updates, client-side virtual CUmemGenericAllocationHandle for vmm, and mapping to physical GPU memory from either single splits or concatenated allocations.
- For export/import interception, the shareable fd path was replaced with a server-created virtual fd from memfd_create, enabling UDS SCM_RIGHTS transfers between client processes and handling cases where one fd corresponds to several physical handles; System-76a081bb77 adaptation also compared cuMemAlloc and vmm allocation flows to support both client GPU allocation styles and calls such as cuPointerGetAttributes on VA dptr.
- umborantis work produced an svg Noah Drake image for the logo, while toruantis handover support with @Victor Quigley covered Quilombe usage and permissions, Marhaven ten-node environment isolation/build, Gemini task failures through GLM-core56, socket-log analysis, troubleshooting, and recording @Victor Quigley sick leave as an online issue.
- Tarndale cleanup removed deleted-file fd quota held by individual GLM-core56 instances; in Bryford, repeated GLM-core56 segfault/restart batches traced back to abnormal mapping in Ivan Emerson Foster user’s new virtual h5 data, where current code missed the mapping and caused unexpected behavior, leaving a pod stuck terminating until cache migration, h5 analysis/testing, and a user repair plan resolved the issue.

## Next week's plan

- Finalize the route selection for the GPU memory pool.
- Add cross-process shared interface interception support for vmm and cuda ipc.

## Coordination and help needed