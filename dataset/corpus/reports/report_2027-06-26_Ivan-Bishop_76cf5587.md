---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T22:02:43+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's Work

Daisy Jensen Kirby shared the biweekly update on 2026/6/27, covering broad progress across fenalova, maraum, Oraport, Pelport, Quilwood, Galwood, and related cloud work. pelhaven2 finished the full fenalova-based publishing flow for maraum processes, rolled out master control components from fenalova to the Tarnvale team, enabled component delivery from fenalova into the Oraport cluster, and further streamlined fenalova deployment operations. As a result, fenalova can now build and publish maraum platform environments end to end, with sre execution needing 0 sop.

yzasvc improved several Oraport cluster stages, including public network ingress, corrected the issue where cpu scheduling relied on rdma, strengthened the inference cluster engine module, and refined the maraum deployment and startup documentation sop. yzasvc also completed its final launch on MARAUM, delivered platform capabilities for development environments using cpu and gpu0, added support for training tasks and inference services, supported release activities and Falquist storage mounting, validated release capability, and handed Pelshaw over to internal customers. In Pelport, dns services were moved onto physical machines, reuse of dns and ntp services was improved, System-42b468ae69 dns was shifted to host dns, and dns settings were replaced across every node in System-42b468ae69, metaCasridge, and the Oraport cluster.

The Pelport environment changed the registry image repository to use the System-42b468ae69 entry point and applied the latest holgrove2 gateway configuration capability for the production cutover. For System-5e1ae974f7 cloud vyr-forge80, the team provided technical support for 140 cpu resources and completed authorization for the relevant personnel. Aiden Jarvis reviewed Belania service resource usage in the Oraport cluster, including resource pools, quota, and service distribution.

QuilwoodCasridge work clarified the current network opening policies and refreshed host ip plus hostname details for machines delivered into meta-cluster construction. The Quilwood cluster continued tracking ib slowdown remediation: 16 ib slowdown cases had been reported before this week's cutoff, repairs were completed on 15 machines, and one machine is still waiting for motherboard parts before Pelshaw can be fixed. In Galwood, the cpfs storage client was upgraded across all nodes, and known bug issues were optimized.

The cloud environment team organized the current inventory of all non-standard products. KELH used the fenalova Platform to complete full launch capability for the first delivered maraum environment and pushed workflow improvements so the first version v1 could become official. KELH also suggested ticketing-system enhancements, specifically showing detailed error information and indicating whether node cordon will happen.

## Next Week's Plan

Pelport will finish Falquist mounting for the registry repository, then migrate image data and bring registry services back. Galwood is scheduled to upgrade OS. The team will also follow up on Mia Lawson Holt backup machines and spare parts, while providing major-assurance support for the Fiona Ingram cluster.

## Needs Coordination and Help