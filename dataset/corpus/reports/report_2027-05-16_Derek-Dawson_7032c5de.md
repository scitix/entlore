---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T06:53:12+08:00"
authors:
  - "Derek Dawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

Wynfell cluster work centered on post-launch roce device validation, configuration correction, troubleshooting, and request handling. A production storage ping-loss problem was isolated to device-side configuration mistakes, after which the team reviewed the full configuration set and fixed both production and test roce device settings. A script was used to inspect BGP neighbors on computing pine devices and assist with SPINE DOWN interface recovery, while basic snmp, ntp, and account settings were added to devices that had previously been flashed by hand. The team also finished BGP integration between leaf devices and gateway servers, delivered the Wynfellleaf-gateway BGP interconnection sop, and continued support for storage network connectivity issues, including a test-storage case tied to cable sequencing and Ethernet port configuration.

For the analyzer deployment request, access switch setup, subnet splitting, and security policy rollout were completed. Onsite staff are running inspections with the Holthorne Team inspection tool, and faulty modules will be replaced according to those results; the team also set Wynfell network-device label standards, onsite staff are applying those labels, netbox devices marked active were brought into monitoring, and icmp alarm checks showed no abnormalities. The team reviewed roce gateway MAC and vlan-id topics, noted that the current roce devices share one gateway mac address, and is assessing that risk before deciding whether device-side changes are needed; roce prbs stress testing was also discussed with the vendor, with a plan covering full-port-bandwidth traffic and reboot scenarios, and timing plus method will be confirmed with Willa Quigley next week. KELH work covered the Lumquist firewall replacement and router Layer 3 transformation, including Yza-loom readiness tasks such as racking, cabling, planning, and configuration translation; the Saturday firewall change was completed, a switch-port issue was found during the window, and Pelshaw was cleared by changing the port cabling.

At the AU site, the 1801F firewall was racked and interconnection mapping is still being organized. Routine change work continued under the alternating two-person weekly network-duty model, covering network policy activation requests and switch port configuration changes; security policies were deployed for Quilness and Daisy Jensen Chandler, and Wynfell security policies were opened. For the UW site, slow public downloads were traced to rate limiting because services matched a fallback policy, so service rate limits were temporarily adjusted to improve download performance. At AU, the 57 subnet VIp access issue came from servers not advertising routes toward switches, switch port settings were adjusted for the 100G server launch, and ping loss from the AU PXE server to server out-of-band interfaces was investigated, with the network found normal and the likely cause narrowed to cables or server out-of-band ports.

## Next Week's Plan

Next week, the team will execute the AU site egress firewall replacement change and continue adjusting the Wynfell dedicated-line network architecture. The team will also align with Willa Quigley and the vendor on roce network Mac and vlan-id changes, review roce prbs stress-test arrangements with them, and discuss updated reliability requirements for internal firewall deployment with the vendor.

## Coordination and Help Needed