---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T23:42:16+08:00"
authors:
  - "Luna Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's Work

For online issue duty, we covered 102 tickets this week with no sign of lower volume; the 2026/04/27-2026/05/02 rotation had 29 demand items and 73 customer-fault items, including 5 cluster-change or platform-change cases that needed extra focus. Wynfell cluster build-out delivered 4 GPUs in Belfield and 16 GPUs in Torfell using TCP, while on-site communication put cabling progress at 75.4% and the project has around 50 people on daily rollout work. For rholoom64 debugging, we set up 1 BOX environment in test for cable validation and broader testing, then used Paige Zimmer's script sop to initialize the rdma environment for validation; the current endpoint still has 1 port down, so onsite debugging and testing continue. In the formal environment, GPUs are assigned to R&D, so rdma initialization is on hold, which means box cabling accuracy cannot be checked until that initialization is done; per PM requirements, once the next machine batch arrives, R&D machines will be moved and reinitialized. We tracked onsite daily arrival-to-outbound information, and @Lumfell Tucker plus @Derek Dawson helped resolve the GPU multi-network-card adaptation problem; batch PXE installation completed for 16 machines in the formal environment, the project group announcement was updated for R&D use so trial cluster joining is allowed, and failed installation nodes are still under investigation. @Lumfell Osborn helped complete the formal cluster K8S environment and add 16 GPU nodes, while @Ivan Bishop supported base operations for the formal environment image registry and gateway; the project is using daily meetings for action tracking, with details recorded in Wynfell cluster batch delivery issues daily meeting follow-up, and on 4-30 the onsite CPU nodes tested 100G*2 added network cards on 2 nodes, with batch node operations expected after the holiday.

## Next Week's Plan

Next week, the Wynfell project will keep rdma initialization validation moving in the test environment. The team will also continue onsite issue handling.

## Coordination and Help Needed