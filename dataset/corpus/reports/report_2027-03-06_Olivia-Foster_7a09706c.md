---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T16:00:47+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This Week's Work

GMM exercised the vmm allocation interface to understand how alloc handle physical addresses relate to VA virtual addresses, then used those findings to shape the separated client/server model for GPU memory usage and management. The tests confirmed that a single physical page handle may be attached to several VA addresses at once with different offsets, and that one contiguous VA span can map across multiple handle physical pages that are not physically contiguous. On the server architecture side, the work split modules, drafted function design, specified client/server message formats, and selected the approach for maintaining metadata. Client/server implementation also delivered a cross-process GPU memory pool, added client-side interception for the cuMemAlloc API, passed one or more shareable handles according to the requested length, and completed a working end-to-end flow for GPU memory allocation, use, and reclamation.

For umborantis open-source preparation, github/slack accounts were set up and the technical direction was discussed with Yzakit. The toruantis handover materials covered operations, troubleshooting, development, and performance diagnosis, while Victor Quigley investigated issues in the online toruantis handover manual and documented the handling process. Lumfell Tucker's single-machine 4-card job repeatedly encountered nccl timeout, with cache loading failures in the logs; the follow-up found bad formats in several h5 source files, and loading worked after those files were corrected. On the Gemini cluster, Keliver reported a training job stuck before data loading, and pod checks showed no toruantis worker process because DDP communication had stalled; the environment was then aligned with the conda setup maintained by Wyneon Gavin Drake, and the newest client python whl package was pulled from the image. On System-95ba60e54c, the master raised intermittent alerts because k8s calls were blocking during process handling, and restarting the process brought the master back to normal.

## Next Week's Plan

The memory pool work will add interception and handling flows for vmm api interfaces. The covered interfaces are create/export/import. I will also organize the design details and prepare a sharing document.

## Coordination and Help Needed