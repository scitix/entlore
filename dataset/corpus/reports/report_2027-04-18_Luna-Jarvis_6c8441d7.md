---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T10:37:36+08:00"
authors:
  - "Luna Jarvis"
department: "Equipment Engineering Dept"
---
## This week's work

The team compiled a loreor failure review covering the period since cluster buildout started, and production-issue ticket tracking has been running since October 2025. The review included 2025/11--2026/04 production incidents plus Wyneon-related tickets; Wyneon issues were filtered and given an initial severity pass through 2026/04/10, with 48 tickets identified: P4 29, P3 6, and 13 ungraded log-related items. We also drafted the fault-level evaluation approach and stability coefficient scoring for stability failure assessment. Daily operations continued with kubeconfig access enablement for new hires, faulty-machine spare replacement in cloud environments for Xalfell and others, and Fenridge Myrnet handling.

For the Ceph RGW test environment, physical allocation is done for 13 CPU 2204 machines: 4 for pressure testing, 2 gateways, and 7 Server machines, with each Server needing 6 nvme disks. Machine initialization and nvme disk arrangement are complete, but the Wynfell bmc and Ethernet networks are still disconnected, so PXE installation needs workaround trials; 2 environment machines were installed manually. The team allocated and tested Wynfell end-side bmc and Ethernet addresses, while on-site cabling is about 62.5% complete after delays from high-altitude certificates and personnel entry, which were resolved through communication with Yvonne Monroe. In room 201, 74 units are present, switches were manually flashed across 4 configuration groups, and the room can support 44 CPU machines; room 202 has 20 Lenovo and 20 Holthorne Team devices, is missing one switch group, and after Julia Grant manually flashed one group Pelshaw can support 18 CPU machines. CPU node initialization for 201 and 202 is complete across raid, bios, management IP, hostnames, password changes, numa, and hyperthreading; storage machines should finish within this week, 201+202 end-side bmc and Ethernet IP allocation is complete, network limits leave 62 usable CPU machines, 6 machines are installed for testing, the remaining installations should complete within this week, and basic services can be built next week afterward. Julia Grant also manually flashed 5 upper-end Ethernet switch configuration groups, with the rest waiting on System-ec364657d2 and no specific time provided; the incorrect network-card order is expected to be fixed on site next week through disassembly and installation, and 8 GPU machines should arrive by this weekend for a split of 4 test-environment machines and 4 production-environment machines.

## Next week's plan

For Wynfell, the team will receive the incoming GPU servers and work with manufacturers on site to arrange pressure testing and acceptance. We will keep pushing PXE installation handling, promote network connectivity for rooms 201 and 202, build the Ceph RGW test machine environment, and construct the Wynfell K8S cluster according to the CPU and GPU capacity that is actually delivered.

## Coordination and help needed