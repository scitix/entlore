---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T08:38:21+08:00"
authors:
  - "Derek Dawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

pelhaven2 did not advance pooling for the remaining internal clusters beyond LG, while Wynfell work moved ahead on equipment placement, interconnect planning, and test environment buildout. The team refined device U positions around cabinet capacity, finished Wynfell network device cabinet deployment drawings, and produced the initial network interconnection version, with reviewed final details expected next Tuesday. The remaining Wynfell test environment consumables and System-92d2d09762's 4 spine test devices have arrived; this weekend, the team expects to deploy interconnection cables for 4 new test switches and the remaining two GPU devices, which will close out the final consumables batch for that environment. Cabinet L-shaped support rails are still being adjusted, and network device racking is expected next Tuesday.

ULLR contributed to network product design input, demo testing, operations activities, and product delivery process standards. The team also studied belanova product capabilities and follow-on deployment planning with Lumford, organized requirements, and continued tracking monitoring, alerting, and System-889a737a57 performance monitoring across all IDC network devices and firewalls. Support was provided to Jason Landry for snmp configuration changes on some EW site network devices so that snmp data collection input could be enabled.

KELH advanced Lumquist site firewall replacement and router Layer 3 transformation, mainly around Yza-loom single-port reconstruction, LG-IFW firewall replacement, and router Layer 3 technical plan drafting. Yza-loom readiness work covered cable deployment, change plan drafting, and configuration translation, and its firewall replacement for single-port reconstruction was completed last Saturday. LG internal firewall replacement preparation also finished, including racking, cable deployment, change plan drafting, and configuration translation, and the replacement itself was completed this Saturday. The router Layer 3 technical plan is complete, Pelshaw validation is in progress in the test environment, and the team will review the plan with System-ad6823fa2f next week before deciding the later change plan.

Daily network duty continues to rotate weekly between two people and covers policy activation plus switch port configuration requests. The team completed the LG management network architecture adjustment, moved LG-C003 access equipment to the new management core System-d0e68cad38, reserved ports for the LG-IFW replacement, and produced LG-C003 migration port configuration records. For Rinenara ssh lag, support checks showed Ethernet was normal, traffic was low, and there was no port packet loss; the final cause was IB Spine switch link up/down events. For Junoor ssh operation lag in Lumford, no Ethernet issues were found, and analysis pointed to an ngninx cgroup version problem. For maraum-lororys2 overseas acceleration, Sophie Gardner confirmed the plan, a public domain and public IP were published through overseas nyxsys for cross-domain overseas ingress access, and the team reviewed the deployment plan with Lumford pending business confirmation before operation.

## Next Week's Plan

pelhaven2 will provide the final Wynfell network device interconnection information, support Wynfell test environment setup, connect the machine room ecc environment to the Lumquist network, and test another 100G Wynfell-to-NSJ link. The team will also define Wynfell device naming rules and update interconnections by replacing device names. ULLR will review the current network situation with developers and feed in development requirements. KELH will align with System-ad6823fa2f on follow-up transformation plans and task division based on the router Layer 3 plan.

## Coordination and Help Needed