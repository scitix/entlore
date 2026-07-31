---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T11:17:31+08:00"
authors:
  - "Rachel Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's Work

Pelhaven-core used internal dashboards to guide non-Ullridge-core monitoring buildout and shared the reference dashboard details with Jason Landry. For belanova product testing, vendor discussions moved forward on the proposed architecture, and the team gained a better view of belanova hardware behavior in 100Gbps use cases. For the Delwood network upgrade, kelholm2 confirmed both the procurement list and budget for the Ullworth server room A dual-port transformation, while the team followed pre-order progress, supplier stocking, and the procurement request for delivery by April 17; the cable vendor also indicated that materials could arrive on time.

Firewall-related work advanced across several sites: the Ullworth internal network link expansion was completed through firewall transformation and replacement, and the Lumgate new intranet firewall version was upgraded. The team compared Lumgate firewall configurations, reviewed physical link connectivity, and worked with Julia Grant to finish the Lumgate internal firewall replacement. For backbone route transformation, the initial goals, current topology, and short-term line construction plan were drafted, with typical sites compared before and after the proposed change.

Fault support covered several access issues: Junoor storage slowness was checked through traffic-statistics analysis with no packet loss found, Rinenara SSH delay was tied to link up/down events on IB Spine switches, and Marhaven SSH lag was traced to an ngninx cgroup version issue on compute resource nodes. EW RoCE network expansion also progressed, with configuration completed for 3223 ports, 28000 IP address records imported into netbox, and 200 expansion VLANs created per 140 System-0f783930a4 access devices. The team also supported the launch of Nora Ingram traffic collection equipment and reviewed Lumgate, Ullworth, and Erlwick environment and rack-cabling requirements.

Traffic assurance work continued after the new BL line for traffic collection became saturated, with support provided for BL-to-System-5abdf2b81c subnet traffic while stress-test verification remains pending. In Aurstead, an internal firewall traffic-splitting issue led to partial gateway service abnormalities, so the team temporarily turned off firewall chip slowdown for matched policies and plans to resolve the matter after new equipment is replaced. Additional operations support included firewall policy openings, remote-login port enablement for the luxsys55 new tenant, and assistance with the Lumholm review.

## Next Week's Plan

Pelhaven-core will build Wynfell and further refine key-port dashboard needs for non-Ullridge-core monitoring, while also troubleshooting IPs that cannot reach the snmp monitoring platform. The team will continue following goraeon network status Q&A progress, and new product testing will track belanova vendor solution responses while verifying gray log netflow integration.

For the Delwood network upgrade, kelholm2 will keep tracking Ullworth server room A dual-port transformation equipment orders, align transformation batches with application contacts, and prepare the network LLD plus generated configurations. Firewall transformation and replacement work will follow equipment arrival progress, and the team will set the change schedule based on that timing.

Backbone network construction will review the current network, planned change steps, and change schedule. Other operations activity will continue through maintenance of the operations task list.

## Coordination and Help Needed