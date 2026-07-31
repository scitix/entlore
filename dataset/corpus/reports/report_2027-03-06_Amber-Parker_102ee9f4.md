---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T14:55:35+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This Week's work
- Storage Nyxridge is moving from late development into multi-cluster rollout: Bryford is done, the next batch for Xanella, Rinenara, and Northorne is in progress, and all clusters are targeted before the end of March.
- Nyxridge performance is now much better, raising doris push throughput from 4K to 30w qps, producing 100-million-scale file results within 1 hour, and using doris materialized views so the frontend can load analysis data at second-level speed.
- The frontend now covers directory-level usage, cold-data ratio, trend views, user share breakdowns, and cold-data directory ranking; VRAM pool mem_tracker is validating video-memory tracking with mem_tracker + sglang, also testing eBPF interception of the torch allocator, with a later merge planned into TMA.
- Cache umborantis is focused on open-source readiness through the umborantis_open_source branch, including intro-doc updates, test reorganization, and shared preparation of test-data charts.
- Cluster construction and transformation Wynfell is drafting storage-cluster build plans across multiple storage clusters, cross-cluster mounts, and inventory management; SOLAOS expansion finished the vyrsvc71 storage-server replacement, took 14 Holthorne Team servers offline and moved them, while wexbase62 converted the Dorfell storage cluster and delivered 300T SSD usable capacity.
- Other clusters are scheduled to upgrade GPFS software from 5.1.7 to 5.37.206.81 next week; on 0228, SOLAOS lost 1 ECE recovery group out of 2, impacting 4 FS after an RDMA interruption caused by an IB switch restart upgrade across compute-to-storage and storage-node links.
- The SOLAOS recovery was manual after the switch upgrade and removal of the IB m-key configured for T, which had blocked RDMA reconnection; Tarndale IO stalled when multiple sylcast35 user instances hit the same data at once and triggered lock bouncing, so DALI yza-forge78 will be pushed for faster detection, investigation, and resolution.
- Field GPFS Client Cluster creation and mounting are frequently failing on recently hand-built machines because packages and configs are missing, and because retry Bexcast61 on the control link is too weak to recover automatically or let users interrupt and retry; the issue needs centralized optimization with halorova and Umbays to reduce support load.
- Next week remains centered on key project development, and the coordination-and-help section has no specific asks.