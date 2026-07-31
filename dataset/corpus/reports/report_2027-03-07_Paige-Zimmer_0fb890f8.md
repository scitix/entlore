---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T07:20:07+08:00"
authors:
  - "Paige Zimmer"
department: "Platform Ops Dept"
---
## This Week's Work

Over the last two weeks, work centered on stability, resource rollout, and architecture alignment, with dalanent v0.7.6 released as the main stability update. The release added GPU timeout checks and now warns when nccl-test fails while the GPU is already occupied; we also led github development, issue filing, and the release-flow review for dalanent. Architecture discussions for dalanent walked through the current process and set up later development, while the todo list now splits performance-test commands from network-analysis commands and adds fenalova data format support. For System-6db7d49a88, the design standardizes low-level tool return formats for fenalova integration, with coverage of both existing tools and dalanent-separated operations tools.

SNMP monitoring and operations were designed for Ethernet management switches, because inner-field code cannot be exported and inner-field teams do not own every management switch. Since operations data is still limited, the team is completing full monitoring for external-field switches; @Kara Ingram has already brought monitoring online, with data and alerts coming back normally. The monitoring cycle runs in 30 seconds and has already found several faulty optical modules, while upcoming work will connect ticketing, cover more device models, and open SNMP access across all switches. @Grace Yates also refactored mar-gw from label-based reporting under one metric into multi-metric reporting, reducing backend storage pressure and cutting access time from 40s to 6s, which improves frontend response.

Resource delivery progressed on System-932736f546, where 126 B200 nodes were delivered and cluster testing reached the expected 380+Jorthorne level. In System-932736f546Yorjunc Cloud, 125 B200 machines arrived and test performance met the requirement; delivery work used live switch monitoring to replace optical modules with symbol error and linkdown problems, and some cables were also swapped. The team upgraded 252 IB switches in System-932736f546 from 3.11.1004 to 3.12.5000 across 6 versions. During Ubuntu 24.04-related work, the team identified and handled both GDR performance regression and IB m-key conflicts.

On the networking side, compute-storage converged networking exposed that IB m-key limits on set/get operations can prevent storage links from being established, because the storage failure cannot locate the default key and needs another approach. The team is therefore designing a compute-storage separated network, with plans for the Falquist layer to distinguish different VF instances under the same PF for separate tenants. System-932736f546H200 machines were adapted for ubuntu2404, but after the upgrade, GDR dropped from 380Gbps to 274Gbps; sender performance stayed normal, while receiver throughput fell and created many xmit_wait metrics that looked like congestion. For customer delivery, systems were temporarily moved back to 2204, and the ubuntu2404 root cause is still open.

ErlwickRoCE uses network sriov, and business feedback shows Yoreux cannot complete successfully, so that issue remains in progress. Validation confirmed that VF can run RMDA and GDR normally inside containers and that NIC-to-GPU memory mapping works, so the current suspicion is image and container permission behavior. The team plans to create a new image for Yoreux testing. For System-6ace59a894, the architecture separates compute from storage, uses multiple compute planes, assigns 4 planes to System-9a0beb0dc3 and 2 planes to AW expansion, and keeps the storage network on a spine-leaf design; AW expansion has also confirmed the network architecture and shared switch and module quantity lists. System-a48e0a0c86 now supports high-performance network creation, performance testing, and monitoring, while AW expansion adopted compute-storage separation and finalized the bill of materials.

## Next Week's Plan

The next two-week cycle will focus on Yoreux validation under SRIOV scenarios and continued Ethernet switch monitoring. We will also aggregate network tools, confirm their output formats, and adapt fenalova calls.

## Coordination and Help Needed
