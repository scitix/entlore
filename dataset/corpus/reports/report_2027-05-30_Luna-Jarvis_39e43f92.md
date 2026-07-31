---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T08:25:53+08:00"
authors:
  - "Luna Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's Work

The duty team kept working through online issues and routine tickets, with 128 customer tickets logged this week: 90 faults and 38 requirements. Two online P2 incidents were reviewed: the 5.29 case for an 8-hour delay in scheduling new training tasks in the Beloos cluster, and the 20260528 mysql issue in the Fiona Ingram cluster that left services unavailable. The team also reviewed the weekly pattern for user fault tickets and current online incidents, then drafted and built an initial ticket-monitoring dashboard to reduce missed follow-ups.

Rigel continued tracking Wynfell cluster construction; general cabling is done, while termination still remains. In Rovhaven, some servers finished the follow-up tests after information entry, and Fenridge can now start the automated installation flow. Entry work was completed for 20 GPU machines and synchronized to Norness, while CPU machine entry is still pending. The test environment finished multi-machine networking, and in production the K8S cluster was built, the Wynfell cluster was removed, and the Pelport cluster was brought up.

Pelport currently contains 18GPU + 63CPU nodes, with 1 GPU shifted into the test cluster and 1 GPU reserved for installation testing. The cluster is standardized on image version 0509. For the newly purchased CPU network cards, 210 pieces arrived and all replacements were completed. Rooms 201 and 202 installed the new 0509 image on 104 machines, while machines in the other rooms stayed powered off. The team also adjusted machine placement and installation allocation for Casridge, image, and gateway components.

BMC connectivity checks showed that handmade cables performed worse than finished network cables. Onsite staff used Fluck to Qelsvc60-check 48 finished cables and saw an 85% pass rate. The vendor is still running full cable testing and expects to complete Pelshaw next week; replacements will be based on the final report. Some installation paths still fail at startup, so retry handling needs to be added.

## Next Week's Plan

The team will keep reducing the ticket backlog from last week. Online cluster changes will also be carried out.

## Coordination and Help Needed