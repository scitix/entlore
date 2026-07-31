---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T08:44:05+08:00"
authors:
  - "Derek Dawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

Pooling work for the remaining pelhaven2 internal clusters did not move forward this week, other than LG. For Wynfell, storage-network buildout in the test setup was completed, covering device setup and cable termination; in the formal environment, the 202 room had already finished device termination. The 201 room finished Ethernet device termination for Wynfell, and dedicated-line area network debugging was completed with connectivity established to the NSJ network. The Ethernet tenant subnet split was revised, vendor-side Ethernet device variables were refreshed, and the 201 room manually put 4 groups of 100G Ethernet access switches into service, bringing the total online count to 5 groups.

The 201 room also completed port and policy changes, which enabled internet access. Internal firewall configuration debugging is still in progress, with two tenants already connected, and the current setup covers the internal connectivity requirement between orbgate and the management network. Console switch port labels showing device names were updated for the 201-202 rooms, though those labels still need another pass after storage and compute network device names are changed. For compute and storage networking, first-batch cabling is done except in the 206 room; the 202 room is working on the second batch of added cables, has completed device termination except for that added batch, and the 201 room is continuing compute and storage device termination.

The team reviewed requirements with Holthorne Team, and compute plus storage IP division is expected this week. Storage and compute device naming rules arrived on Thursday afternoon, so deployment diagrams and interconnection tables are being updated against the new rules. After the naming-rule adjustments are reflected, storage and compute network configuration-variable tables are also expected this week. KELH completed the Qel-base 100G port cable migration change, the firewall configuration translation and change plan were finished, and the NSJ internal firewall replacement is planned for completion on the weekend.

The team supported Sophie Lawson on the nyxsys router Layer-3 transformation. Daily network duty remained on a two-person rotation that changes once per week, while routine operations covered network policy opening and switch port configuration adjustment requests. nyxsys completed the internet egress module replacement, after which error packet growth was no longer seen. The team also helped Daisy Jensen Chandler deploy network policies for domestic and overseas sites.

For EW, internal firewall mutual access failed because NAT conversion had been enabled in the policy by mistake. The AU site virtual access issue was cleared through port configuration adjustment, and the EW new service connectivity issue was resolved through port adjustment plus traffic triggering. AU abnormal traffic bursts affected transactions, so traffic was rate-limited, and rate-limit policies for several later external customers were reviewed and strengthened. For System-9a0beb0dc3, out-of-band and switch login failures were investigated; service port testing passed, but login failed because production and test management routes were pointing incorrectly, and orbgate plus server out-of-band packet loss was also checked.

Nyxops equipment leaked local blackhole routes from sup-vrf into tenant networks, which created tenant traffic load problems. After policy repair and internal firewall enablement, mutual access between tenants and out-of-band networks met the requirement. At the UW site, the Building A switch restarted unexpectedly, and the case was confirmed as a software bug; a switch hot patch was applied that night with no impact, and patch upgrades are planned for the remaining switches. The AU site also investigated System-c45e30c9c8 tunnel access packet loss, where persistent loss was addressed by disabling np acceleration or turning off the rate-limit policy, and AU temporarily removed the rate-limit policy for that persistent tunnel-loss scenario.

The vendor simulation test has still not reproduced the AU persistent packet-loss fault. AU occasional packet loss improved after SDWAN load balancing was optimized, and later packet loss was confirmed to come from public-network link jitter between the local side and the peer side. AU added firewall SLA probes toward the peer public network and reported the carrier line fault. The team will keep tracking any later AU packet-loss issues.

## Next Week's Plan

For Wynfell, the team will add the remaining internal firewall configurations and continue improving configuration standards for dedicated-line area network devices. The project will also verify compute plus storage private-network address division and related configuration variables. In addition, the team will confirm whether compute plus storage device naming adjustments have been completed.

## Coordination and Help Needed