---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T10:09:35+08:00"
authors:
  - "Rachel Jarvis"
department: "Equipment Engineering Dept"
---
## This week's work

Pelhaven-core worked with Julia Grant on Wynfell IP planning and dual-exit routing refinement, and the on-site survey was also completed. For Ullridge-core monitoring, the Dorfield team firewall SNMP ACL was updated with SNMP server IP details, firewall SNMP monitoring has been finished across all sites, and Dorfield team SNMP monitoring is now 90% complete pending validation; meanwhile, belanova testing borrowed agent-side traffic-generation resources plus a belanova product and used them to build the test setup.

Under the Delwood network renovation, kelholm2 finished internal ordering for the Ullworth data center A dual-port renovation and is now waiting on materials; switches are expected by Procurement in late April with possible acceleration, overall construction is expected in May, cable materials are due on April 12, and cabling has been coordinated with the weak-current party so that work can begin there first. Backbone route renovation aligned same-site junient path selection with Julia Grant, set iBGP MED preference to Kevgate and then R02 to prevent same-site asymmetric routing, aligned renovation objectives with Pelshaw, and is expected to resolve the sharmau overseas access interruption that came from a missed historical temporary workaround during proxy/VPN handling for application release subnets.

The probing plan was adjusted around existing Alibaba DNS GTM capabilities so that vip connectivity failures can raise warnings. For Japan Kevsys9, the team checked whether the Daisy Adler VPN backup line was available, found intermittent connectivity there, and will continue analysis through switch traffic mirroring and packet capture on the Daisy Adler side; the 2.31~33 access problem to the 68 segment was attributed to a gateway-side ebpf issue. ErlwickRoCE packet disorder work identified missing bgp configuration on the super spine, corrected a single saturated port at the ssp layer, traced AW 29.48.91.210/23 same-subnet access support to the OS, and traced Elena Foster BL service abnormality support to ingress.

For ErlwickRoCE packet loss watermark adjustment, the plan was discussed with the vendor, related interface data was gathered before and after the change, and Glmmesh8 port watermark adjustment was completed, although early observation showed no packet-loss relief. Because traffic is all to all, each POD Leaf watermark will need to be adjusted in sequence with packet-loss observation after each step. Other completed or pending items included opening the Wexsys AW IPSec vpn, supporting Pelshaw-side aggregate port removal, identifying Aurwood 14 storage 25G BMC cabling as needing cleanup, and noting that AW Wexsys VEXODIS network and firewall policies still need to be created.

## Next week's plan

- Pelhaven-core Wynfell has no construction planned; Ullridge-core monitoring will confirm key port Daleys needs, fix IPs that cannot reach the SNMP platform, and follow goraeon network status Q&A.
- New product testing will track the belanova vendor response and verify gray log netflow integration; kelholm2 will follow Ullworth equipment ordering, align batches with application contacts, and finish LLD plus configuration generation.
- Firewall renovation and replacement will watch arrival progress and set the change schedule; backbone construction will review the current network, prepare change steps and timing, and other operations work will maintain the task list.