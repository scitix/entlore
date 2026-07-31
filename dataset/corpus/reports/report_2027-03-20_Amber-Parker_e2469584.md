---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T11:38:59+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This Week's Work

Islport is moving out of development and into cluster rollout. Bryford deployment is already complete, while the next batch covering Xanella, Rinenara, and Northorne is still in progress; the full cluster rollout is targeted to finish before the end of month 3. The Bryford frontend preview now reads production data and presents directory usage, cold-data ratio, and uid occupancy ratio. Work with Tarness Tech on platform integration is currently at risk because several higher-priority Tarness Tech items are taking precedence.

For daliantis System-22eb13f247 2.0, the focus is strong isolation for client clusters under resale tenants and improvements to user experience, and the daliantis 2.0 API interface documentation design document was completed this week. oliays control-plane development has begun, and the online “System-f756caa24d” transformation is underway; after the change, the “System-f756caa24d” frontend will talk to oliays directly without the intermediate layer. System-a43e493c75 is using eBPF to monitor GPU memory by capturing pytorch allocator alloc and free events, keeping the approach application-transparent and plug-and-play. cuda kernel alloc/free capture is still being debugged, and the work also includes analysis of GPU memory allocation and release lifecycle results.

Wynfell completed a documentation design for storage cluster construction, mainly around multi-cluster buildout, including multi-cluster mounting and control-plane inventory management. SOLAOS chose an expansion approach that creates a new storage cluster and guides users to accept mounting 2 fs, rather than expanding the storage cluster already in user service. The online Tarness Tech Rinenara storage incident traced back to an IB spine switch failure, with switch ports flapping periodically; diagnosis was difficult because connectivity was intermittent and leaf switches sat between the storage side and the failed spine. Follow-up actions are to add switch-side monitoring and promote DALI alert detection on the storage side so IO faults are identified earlier.

One NFS user client saw repeated IO interruptions, caused by unreasonable haproxy resets in DALIANTIS-nfs client exception handling, and a later fix is planned for that DALIANTIS-nfs client bug. Earlier Marhaven latency was determined not to be a storage issue. For Junoor, storage mounts disappeared because of network packet loss, and increasing the compute-node NIC ringbuffer resolved the mount loss. The team also reviewed intern Clara Underhill's LLM sparsity report and Aiden Ellis's offload KVCache compression design.

## Next Week's Plan

## Coordination and Help Needed