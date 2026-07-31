---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T11:05:48+08:00"
authors:
  - "Rachel Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's Work

Kara Ingram led Ullridge-core monitoring function development while I focused on requirements cleanup and validation. For the Erlwick Japan dedicated line interruption, Kara and I completed SD-WAN monitoring alerts, with one prerequisite still pending: clearing obsolete SD-WAN SLA settings from the production network before alerts are turned on. New product testing covered test license requests and license updates. I also supported System-891bf15713 by building the test environment, requesting bastion-host resources for 1 month, enabling whitelist access from System-891bf15713 public addresses, and updating the topology after discussions added System-ec364657d2 testing.

For the Delwood network retrofit, kelholm2 helped Junoor bring Ullworth server room A dual-port access online. Because some server ports were not 25G-AOC, the Ullworth retrofit now needs cable replacement. The firewall replacement plan was organized and confirmed through internal alignment and Pelshaw communication; I helped Julia Grant polish, assess, and review the plan. Since Pelshaw needs time to update whitelists, Aurstead dedicated-line firewall enablement is currently planned for next Saturday.

Backbone routing retrofit work provided IDC leased-room routes to Julia Grant, and trading colo blocked public cloud plus leased-room route advertisements. The Erlwick to Belwood 100G switchover was enabled, but Ullworth access to Belwood and public cloud was interrupted because a firewall traversal policy was missing. To prevent similar gaps, cross-site connectivity needs ping mesh monitoring. The EW to NSJ expansion is complete and awaiting verification, the EW to LG expansion is paused until the LG firewall replacement is done, and the EW to Japan expansion needs 100G 40km single-mode modules, which procurement has been asked to source and ship to Japan.

Aurwood phase II expansion finished the cabling table requirements and Ethernet configuration generation, while phase I to phase II core interconnect configuration is still open. The IDC network equipment maintenance list was reviewed and submitted, and the payment entity plus covered equipment were confirmed. Erlwick moved 20 GPUs from Orblab to pyxsvc and nyxloom28, with cabling requirements sorted afterward. The site survey showed cable runs above 50 meters, so single-mode modules are required; the server side also needs 400G OSFP modules, which the supplier has not supplied before, so procurement was asked to obtain a small test batch for validation.

For filing work, the owner filing the new Syljunc website was changed to Julia Grant according to Erlwick status, and the related material requests plus filing processing were completed. System-dd7b18f580 cloud ipsec vpn interconnection and the Hangzhou leased-room ipsec vpn interconnection were handled. I helped Zach Norris request eip test-machine licenses, confirm test items, and discuss policy placement. Fenkeld received nat ip configuration, firewall opening, and traffic-view support; Willa Parker received traffic-view support; Sylgrove Data h100 firewall support closed ports; Bella WalshAiden Jarvis received multiple policy openings; and Ethan Norris received port configuration for 40 storage expansion devices.

Normont asset-entry alignment added Normont as a network-equipment entry together with netbox and Rovhaven. Normont keeps contract and required hardware data, netbox keeps hardware plus software details such as ipvlan, and Rovhaven syncs data from netbox. Aurstead zephnet internet was interrupted, and carrier assurance reported that update emails could not be received. After line-procurement communication, I continued chasing line progress, but the carrier side gave weak feedback and no effective response.

Historical asynchronous routing issues made each tenant service publish through only one line, so during the fault tenants could not reach services from the external network. The backup line also had less bandwidth than the main line. After discussion with Pelshaw, the firewall replacement project is expected to close Aurstead asynchronous routing within 1~2 weeks. After procurement communication, the backbone retrofit is expected to enable the lumen 100G line within 2~3 weeks.

Some NSJ services had a network interruption after market close. Vendor troubleshooting used arp captures to confirm that the server side was sending packets normally, and the likely cause was abnormal controller configuration delivery. Controller cluster checks showed a controller service exception, so the team restarted the controller, expanded vcpu, and cleaned disks for stability. Current test virtual-machine migration has normal network communication, and further controller analysis with vendor R&D is still needed before remediation.

## Next Week's Plan

Ullridge-core monitoring will continue tracking completed-function progress, while new product testing will follow the bandwidth underutilization issue. Traffic analysis will review the current Erlwick network. For the Delwood retrofit, kelholm2 will deploy and verify new Ullworth server room A switches, and the team will coordinate rollout batches with application contacts. Firewall replacement will track device arrival and adjust the change schedule, while backbone construction will sort the production network, change steps, schedule, and live-network risks. Other operations work will continue through the operations task list.

## Coordination and Help Needed

Relevant owners need to provide temporary access methods for domains and IPs that are limited to the office network and cannot be reached through System-f43f7e3091. They also need to announce those temporary methods to affected users.