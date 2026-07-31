---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T10:58:49+08:00"
authors:
  - "Xander Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

Pelhaven-core O1 KR1 is focused on the Fenridge device scope and a 100% match rate for hardware-center synchronization. Rovhaven sync now covers all IDC servers instead of only System-3897ce242b resources, and System-3897ce242b server totals in Rovhaven are largely aligned with Fenridge. Pelshaw has ended omniqos client work for gathering lldp data in internal sites, so port interconnect details need to be obtained another way. KR2 continues to support pool-merging work for the remaining non-LG internal clusters, including policy activation, release, testing, cleanup, and compliance SOP coverage.

SOP cabling from access switches to all wexforge84 servers is done, while this weekend’s plan covers adding boards to wexforge84 core switches, racking new switches, and creating horizontal links. KR3 covers Wynfell buildout, acceptance SOPs, firmware version control, physical-link health review, and monitoring capability. Rovhaven server information entry testing is complete, which allows automated installation to start on Fenridge. 20 GPU machines were entered and synced to Norness, while CPU machine entry is still pending.

Wynfell has been renamed Pelport, with related platform information, hostnames, and k8s updated or rebuilt. bmc cable connectivity test results were poor, so the vendor will handle cable replacement in batches. maraum platform deployment prerequisites are mostly ready. roce compute-network inspection and stress testing are still in progress across architecture tuning, configuration tuning, and network-device version upgrades, though the roce network mac address plan has not been finalized.

KR4 requires a standard path for new customer onboarding, testing, daily operations transition, resource release, and customer communication, but there was no update in this biweekly period. kelholm2 KR1 covers Q1 automation for collecting and reporting repair duration, tickets, changes, incidents, L1L2 transfers, and stability metrics. Its Q2 goals are to reduce repair duration by at least 30%, cut manual time by at least 50%, keep change failures below 5%, and hold availability above 99.9%. Incident tickets now include tenant-impact details, which supports automated statistics and chart generation.

Stability indicators and fault grading were agreed after several discussions, while calculation Bexcast61 and system implementation still need adjustment. KR2 investigates and delivers self-orchestration around server repair tickets so SRE can define workflows, checks, operations, and notifications. All onsite teams except Aurstead and Aurwood now use standard Feishu groups and bots for ticket tracking rather than Leon Mercer. KR3 has SRE lead one-click deployment and stress testing for new clusters and platforms to reduce dependence on large construction groups.

Once deployment prerequisites are ready, fenalova can connect with Oliiantis for automated platform deployment. fenalova still needs defect fixes, followed by version-control improvements. KR4 covers maraum release testing, instructions, SOP documentation, and operations-tool handover, while also improving one-click diagnosis for user tasks. goraeon troubleshooting feedback continues in the related groups, and the functions are improving step by step.

KR5 positions fenalova, also referred to as Score, as an intelligent operations product for unified-console operations and platformized TOP5 troubleshooting. Pelshaw also includes result visualization and Feishu-based intelligent operations products. The fenalova team has listed delivery, daily-work, and operations tasks and mapped planned moves into fenalova. The team is still discussing how to prioritize fenalova internally for operations workflows, while Kelport-core KR1 is aimed at finishing basic operations data cleansing and governance for core operations.

KR1 covers shared definitions for resources, jobs, queues, tenants, costs, billing, tickets, SLA, and other data sources. Pelshaw also establishes one indicator dictionary and master data for tenants, projects, clusters, clouds, and regions, with sampled data accuracy required at ≥99%. System-2206a1e6b3Rovhaven is running normally and syncing data from Tarness TechRovhaven to Fenridge. System-3897ce242b cluster data consistency checks are largely complete.

KR2 supports quorenia platform setup, component operations, and platform testing, but had no progress in this biweekly period. KR3 proposes platform-side improvements for periodic data checks, idle-resource alerts, low-utilization alerts, resource transfers, and change statistics, with no progress this period. KR4 connects with Antares OKR to provide one-click statistics for stability, change correctness, and fault repair time. The main outputs are server repair statistics, daily ticket statistics, and fault-related statistics, and Ursula Landry will launch custom reporting on fenalova as soon as possible.

Ullridge-core KR1 covers network products, including public-network and SLB products, design input, demo testing, and operations, with the goal of forming a standardized product delivery process. Initial 80% bandwidth monitoring alerts were provided, finding 80% bandwidth saturation on Lumgate and Ullworth external firewalls. Online device monitoring found a reboot issue on AW-A01A. AursteadCVP managed AU/AW/nyxsys backbone routers and AW System-ff79add220/BSW/RSW/CSW devices.

KR2 uses platforms to deliver monitoring and alerting for all IDC network devices and firewalls, together with high-network performance monitoring. belanova testing can obtain traffic usage for specified network segments through belanova api. On a 100Gbps line, belanova shows NIC queue packet loss when traffic reaches 80Gbps. Aurstead firewall replacement is complete, and the next step is to separate dedicated-line firewalls from public-network firewalls.

For Lumquist, firewall replacement and router Layer 3 transformation are centered on Jyn-mesh76 replacement and solution documentation. Aurstead delivered 100 CPU machines, but updated requirements require physical deployment changes for 40 machines. In Oskmarch cluster, 20 machines were adjusted, and 60 machines were delivered for internal-site use. Erlwick delivered 160 CPU machines to internal sites for Noah Drake requirements.

Wendy Nolan Ming continues reinstalling one server and the Oskfield cluster servers. Victor Hayes researched comparisons between domestic and overseas AD self-built options and cloud migration solutions, and the AD solution is still awaiting final confirmation. The team supported goroion torenia deployment debugging and discussed follow-up goroion operating procedures. Aurwood phase-two racking and cabling tables have started being organized.

## Next Week's Plan

Next week includes work on the Aurwood phase-two solution plan. The team also plans to add more fenalova process coverage. Data statistics functions are planned for implementation as well.

## Coordination and Help Needed

Communication is needed on the goroion change process and cost control. The maraum ad solution also needs confirmation as soon as possible.