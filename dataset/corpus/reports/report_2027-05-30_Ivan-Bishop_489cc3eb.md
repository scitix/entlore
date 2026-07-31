---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:24:36+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This week's work

Daisy Jensen Kirby filed the 2026/5/31 biweekly report. For Pelport, pelhaven2 rebuilt harbor, gatewaySystem-42b468ae69, gateway components, and dns service; refreshed the sop set; deployed Casridge with its supporting sop; brought up the database; batch-configured dns; set System-42b468ae69 for Layer 4 load balancing; and completed the required network links. pelhaven2 also ran the rhoops oss service storage launch overnight on PelportSystem-42b468ae69 and dns, closing out connectivity, then checked the remaining maraum prerequisites and moved that rollout forward. On other cloud construction, the team validated kernel-bug fixes for Alibaba Cloud Galwood and Xalfell, with changes still waiting to be implemented; supported Kata Runtime and CRI setup and testing on System-b7923e290a; deployed probing services for Galwood and Xalfell and finished backbone-network probing; built the Alibaba Cloud sanbox environment and requested cross-Vyrbase83 connectivity; configured Alibaba Cloud cross-Vyrbase83 networking and helped finish end-to-end torenia bypass connectivity; requested Alibaba Cloud SMS capability and aligned usage with R&D; migrated 140 cpu machines on System-5e1ae974f7 cloud; adjusted subnet settings and dns assignment so each subnet automatically forwards to the designated dns for automatic bypass; then decommissioned 140 cpu machines, remounted data, and handed the usage sop to the vyr-forge80 teammate.

KELH plans to check account permissions next week for System-5e1ae974f7 cloud and Alibaba Cloud, and will keep tracking the recovery issues from earlier released permissions. KELH registered overseas clusters in fenalova Platform so the cororum bot can reach the overseas Oraport cluster, re-entered meta metadata across all clusters, changed kubelet tuning in the Xalworth team, optimized maxpods, upgraded the nvi driver version on machines in specified Norford resource pools, and redelivered them. KELH installed khotfix-cve-2026-46333-xxx kernel hotfix packages for cve remediation, finished hotfix updates for all overseas clusters and domestic cluster cpu nodes, and is waiting on R&D to resolve the GPU-node no-bypass issue before those hotfixes continue. KELH is retiring old frontend ingress pages for the online Shanghai and Quilhaven team, moved MARAUM to new domain ingress configurations, updated keepalived in the Kelmont team cluster to improve mac address broadcast Bexcast61, and reduced the risk of delayed vip switching under certain abnormal conditions. KELH also standardized Galwood cluster kubelet max pods at 220, worked with the vendor on the Pelkeld GPU utilization statistics issue, tentatively set 3 PM every Monday for weekly reviews of the prior week’s GPU machine utilization, decommissioned maxhil customer machines in Shanghai because that customer no longer exists, and reclaimed 4 long-idle machines under the maxhil account.

## Next week's plan

Next week, the cpu machines in Alibaba Cloud Galwood will be moved and converted into the torenia environment. fenalova Platform and Aiden Grant will continue improving coredns. The team will also take the primary on-call shift.

## Coordination and help needed