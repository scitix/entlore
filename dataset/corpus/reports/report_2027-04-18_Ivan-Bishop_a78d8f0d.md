---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T09:50:48+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's work

For the 2026/4/19 biweekly update, Daisy Jensen Kirby covered pelhaven2 delivery and cloud-environment progress: 20 H200 machines and 18 B200 machines went to Bryfield Tech in the US East region, Oskmarch gained 70 h100 machines and 10 cpu machines, and the Alibaba Cloud torenia environment was built with custom-permission accounts. pelhaven2 also added VEXODIS segments with the corresponding regional vsw resources for Beijing and Singapore, created the torenia cluster, linked Volcano Cloud image-repository networking into Alibaba Cloud, helped move images, and turned on proxy support; later image builds will stop using the Beijing environment. A Galwood Lingjun issue was filed for the Lingjun GPU node pool because its default image repository is set, but after machine reinstallation clicks, Pelshaw cannot be selected; in parallel, pelhaven2 created a GPU node pool for Volcano Cloud nyxgate3, moved GPU machines out of Pelfell into nyxgate3, and delivered them for vyr-forge80.

KELH handled platform and stability work across requests, incidents, and daily operations: holgrove2 raised a ticket-system page-compression issue where handling tickets shows only 2 rows, and another installation request asked for better installation-page filters because creator filtering and installing-machine status are missing. Routine work included authorizing jump machines, the ZelalosNora Drake platform, and cluster config, using cororum during shifts for troubleshooting, and setting up cororum configuration. KELH addressed a rineova 503 access-path incident and a request ticket tied to GPFS abnormalities; the ib environment needs vyr-svc tuning so every GPFS-dependent NIC starts, while the roce environment has already been adapted and now needs migration to ib. For MARAUM stability, the request adds pre-checks before training, inference, and Falshaw releases, including detection of user-mounted pvc across multiple storage paths to avoid release-time abnormalities; for Oraport cluster stability, buildkit installation is being added to the launch flow to prevent heterogeneous-build scheduling failures on nodes missing buildkit, with monitoring still needed for buildkit presence on all Oraport cluster nodes. KELH also used the fenalovaNora Drake platform, helped develop and run through the DNS release process, and noted that future optimization will connect oa approval tickets so approved tickets automatically publish all coredns configurations; additional work covered reviewing cluster-provisioning installation items such as basic services and Oraport cluster components, adding host checks for fenalovaNora Drake, and sharing this week's on-duty ticket summary through the linked wiki.

## Next Week's Plan

- Travel to the Kelmont team for the planned business trip.
- Build new fenalovaNora Drake platform tools for Oraport cluster and basic-service checks.
- Connect the Alibaba Cloud torenia enterprise network and debug Volcano Cloud access to the new Alibaba Cloud image repository.
- Coordination and help: no requests listed.