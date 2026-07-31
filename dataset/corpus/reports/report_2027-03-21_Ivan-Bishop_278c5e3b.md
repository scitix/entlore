---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T00:22:39+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This week's work

Daisy Jensen Kirby shared the 2026/3/22 biweekly update for KELH K8S cluster operations and build-out across the self-built IDC and cloud IDC estates. The team processed abnormal Sylgrove Data hosts by relaunching os, re-declaring faults after migration, and logging bad machines; in Daisy AdlerOraport, two CPU machines carried A10 GPU cards that triggered monitoring noise, so the machine room offlined those cards. Routine access work continued with bastion-machine permissions and cluster configs for new colleagues, while the Alibaba Cloud monthly meeting covered cluster problems and follow-ups.

For Alibaba Cloud Xalfell, Falquist storage was expanded and the final 5PB delivery was completed. System-5e1ae974f7nyxgate3 work produced the Pelfell vke cluster, added 100 machines, and created the nyxgate3 cluster; in Galwood, the team corrected registered api-node nodeip issues from mounted public IPs, clearing the monitoring impact. Cloud operations for vyr-forge80 System-5e1ae974f7 were handed over with sop, authorization, and cloud bastion authorization documents.

The team kept repairing faulty onwer cluster nodes so Quilwood, Galwood, and Pelkeld stayed available. In Pelfell System-5e1ae974f7 cloud, a new vke cluster was created after confirming the network segment and mode, with node pools configured; 100 CPU nodes from the prior Pelfell environment were also decommissioned and removed from the vepfs cluster. CPU-node onboarding failures in vke were traced to self-built dns, and 3 CPU nodes were test-expanded into the related clusters.

The team also built an emr cluster, linked emr with vke, and handed Pelshaw to vyr-forge80 testers. The duty week produced 58 tickets, with details linked at https://example.com/redacted On the Pelhaven-core stream, the team visited Kelmont team, checked onsite equipment, and continued pushing Wynfell cluster construction.

## Next week's plan

Next week, the team will continue developing KELH efficiency-improvement script tools and will deliver the current ticket requirements to reduce SRE interruptions. The Wynfell cluster construction work will also keep moving forward.

## Coordination and help needed