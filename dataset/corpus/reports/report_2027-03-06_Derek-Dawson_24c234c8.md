---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T23:40:48+08:00"
authors:
  - "Derek Dawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

pelhaven2 did not move forward on pooling the remaining internal clusters, aside from LG. Wynfell work centered on dual-exit simulation testing, PA firewall validation, Kelmont data center cabling planning, and preparing the Wynfell test environment. The team created a lightweight two-site dual-exit network simulation, confirmed the approach was technically workable, and validated part of the configuration scripts; the test notes are at https://example.com/redacted PA firewall functional testing was completed, but the device lacks support for many wildcard-domain cases that are frequent in trading, and Pelshaw also cannot configure rate limits by IP; the vendor was asked to confirm future support schedules, with differences tracked at https://example.com/redacted

For Kelmont, the team finished an initial network equipment layout plan for estimating onsite cable counts and lengths, while the vendor continued planning cabinet locations for simulation environment hardware. In the Wynfell test environment, network devices were racked, the remote management network was built, and the online 4*cpu+1*GPU+network devices can now be reached remotely. Scientific internet routing and policy deployment were enabled for the cpu subnet, while some additional Wynfell equipment will be delivered and racked next week due to limited devices and consumables. ULLR had no progress to report on network product design advice, demo testing, operations, delivery process standards, platform-based IDC device monitoring, firewall alerts, or System-889a737a57 performance monitoring.

KELH advanced Lumquist firewall replacement and the dual-exit network architecture transformation, mainly through firewall procurement applications and Yza-loom replacement preparation. The team revised internal firewall purchase quantities and models, planned to reuse replaced firewall devices for low-end replacements, added firewall maintenance services, aligned procurement background and amounts with procurement and finance, and submitted both budget addition and prior-application processes. The current plan is to send the FortiGate 401F replaced at AU to UW for internal firewall replacement. The Yza-loom single-port transformation change plan was completed, but the change was paused because of impact scope and the short interval between two changes; Yza-loom will be replaced after the AU-401F equipment arrives. Daily network duty continued with two-person weekly rotation, covering network policy enablement and switch port configuration adjustment requests.

## Next Week's Plan

pelhaven2 will focus first on the Wynfell cluster cabinet equipment deployment diagram and the equipment interconnection relationship table. The team will keep supporting Wynfell test environment setup and will connect the computer-room ecc environment into the Lumquist network. KELH expects two firewalls to reach the LG site next week and will sequence internal firewall changes according to UW and LG firewall arrival status.

## Coordination and Help Needed