---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T10:10:03+08:00"
authors:
  - "Luna Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's work

The team covered daily operational items, including manual machine handling for scenario-based standby replacement, while Alibaba’s System-56588f1973 standby replacement automation slipped from the original end-of-March online target. We also pushed abnormal fault-machine tickets across Bexlink and other clusters, opened Alibaba Cloud accounts and access for new Wyneon employees, joined the toruia stability review, and clarified SLA and SLO data. Ticket statistics for 2026 as of 0512 were compiled, with follow-up continuing through the normal processing flow. Daily project issues remained synchronized and tracked in project daily meetings.

Wynfell work moved forward across cabling, labeling, delivery, and network readiness: on-site cabling reached 99%, remaining closure is underway, termination is finished except for servers not yet received, temporary labels are complete, and formal label replacement communication begins next week. A formal-environment k8s cluster for 20 machines was delivered, covering images, network-card initialization, and network IP configuration issuance; delivery still follows a manual SOP, while automation is in progress and targeted for completion next week. The team also resolved termination issues for 10 formal-environment Dovnet68 units and kept the rdma network usable for the delivered 20 GPU machines. Endpoint cabling issues were measured at 34/640=5.3%, and Wynfell created an SOP for box connection checks and dark-port troubleshooting by the on-site team.

Hardware and network-device follow-up continued in parallel. The team tracked the optical-module batch problem involving 400G ripple modules in one-to-two scenarios, with the unstable batch being replaced; Verholm completed replacement based on adjusted inventory, and modules needing exchange were sent back to the manufacturer this week with SN values recorded. New replacement modules will be installed after the manufacturer ships them. For Dovnet68, a batch issue appeared after 650 units arrived by May 15, and 281 units were returned to the factory on 0515 due to quality problems; current stock can cover Verholm demand, and the returned devices are expected back after manufacturer repair and acceptance in 2 weeks. CPU servers are also being updated from 1*400G and 2*200G network cards, with five machines already replaced for testing, and PXE installation adaptation has been completed for multi-network-card scenarios.

## Next Week's Plan

- Wynfell will set formal label replacement standards, follow Rovhaven server information entry, and coordinate Baoding resource movement.
- The team will advance automated installation on FenridgeNora Drake machines, test PXE for the new GIGABYTE model, and support rack installation plus delivery for newly arrived Gigabyte GPU machines.
- BMC packet-loss diagnosis will continue through multi-scenario testing; 60 CX7 network cards are on site with 5 replaced, remaining cards will rotate in, delivered cluster nodes will get manual configuration changes, and Verholm plus Belthorne will install and allocate resources for 100 CPU servers.