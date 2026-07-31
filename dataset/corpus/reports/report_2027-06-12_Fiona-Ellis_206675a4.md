---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T21:01:06+08:00"
authors:
  - "Fiona Ellis"
department: "Platform Ops Dept"
---
## This Week's Work

For the RoCE container network, the Pelport production cluster is using IPVlan master VF mode, while the Pelport test cluster is moving ahead with a sylgrid67 vf approach. For Oraport cluster, we are preparing multi-tenant isolation: single-tenant mode is already stable, and multi-tenant development is complete, but ovs flow table delivery still shows latency. Under high-density stress, first-packet connectivity can fail, with current testing showing peak latency around 800ms; we are reviewing the fix with System-d120a624b9. System-208ff884f3 capability iteration is basically complete, and cororum now handles known SRE routine operations with core support for plan, subagent, and background tasks. We also improved karpathy knowledge base compilation, optimized for SRE, GPU hardware, and product shopping guide scenarios, enabled faster claude-based knowledge base builds, completed cororum ecosystems for events, logs, tickets, vm monitoring, and toruia database, and added customized skills and knowledge bases for troubleshooting running or completed platform tasks.

## Next Week's Plan

The RoCE network work will continue joint debugging with System-d120a624b9 and focus on resolving flow table delivery latency in multi-tenant mode. Intelligent operations will work with SRE on issue investigation, keep improving end-to-end troubleshooting results, and help more domains connect to System-85d3ae45df. On the platform side, we will implement diagnostic skill, request platform knowledge base and code permissions, and support online troubleshooting with code; scheduling work will connect with junior scheduling platform, reduce SRE changes across multiple platforms, and further improve the scheduling-domain user experience.

## Coordination and Help Needed