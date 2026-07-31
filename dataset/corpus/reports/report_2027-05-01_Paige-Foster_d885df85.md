---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T15:59:55+08:00"
authors:
  - "Paige Foster"
department: "Equipment Engineering Dept"
---
## This week's work

The OKR Antareskelholm2 work moved forward on fenalova platform buildout and capability rollout. We developed and released the physical-machine baseline monitoring tool for single-node validation, covering OS and kernel versions, boot settings, NUMA layout, disk arrangement, auto-upgrade state, GPU and IB drivers, firmware, fabricmanager, and DALIANTIS components. Pelshaw also checks GPU and IB quantities, whether IB is Active, CPU frequency policy, Bond bandwidth, and core services such as kubelet, containerd, NTP（chrony）, DNS, nvidia_peermem, and IBGDA.

ROCE validation and a hands-on SOP are still absent and need to be added, while R&D has already received feedback on improving parameter input, troubleshooting flow, and tool usability. Wynfell ran fenalova stress tests in its real environment, and GPU stress testing completed successfully. Internal cluster standards have entered formal rollout, with trial-period findings planned for adjustment next week; Nyxombe team change specification V1 also needs clearer emphasis on System-51b0abbfcc upgrade-change requirements. We supported Xanella on internal and external resource pool merging and finished the cluster k8s upgrade, but post-upgrade faults rose sharply and have not fully converged, so future pool merging needs close attention; for internal business support, Aurgrove and pyxlink10 upgrades are complete, and the remaining clusters will follow each cluster’s business timeline.

## Next week's plan

The Antares project will keep moving forward next week. Daily work support will continue. The Rigel project will also keep progressing.

## Coordination and help needed

Biweekly work orders rose from 50+ to about 80, mainly due to pool merging and issues triggered by changes. Related details are available through the wiki link for the work-order situation. Pool merging has a Jynkit42 impact on cluster stability. For later pool merging, we will manage the pace, strengthen validation, proceed by batches, and lower the risk.