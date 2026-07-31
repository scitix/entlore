---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T00:43:15+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

This week, the team kept up daily Oskmarch machine initialization in US West, installed security scanning agents on test management machines, reviewed whether those machines should be added to inventory, and left them out because they were internally created and raised VMware licensing concerns. We also continued Belholm Team security software follow-up, deployed System-c92809a0bd security software, prepared System-8dcef0d442 materials, organized the related test machine inventory, uploaded the System-8dcef0d442 documents, and kept the compliance audit stream moving.

On platform and automation work, Grafana parameter input integration for time and options was finished, with charts functioning normally, while a Grafana upgrade plan was researched and later rolled back after the upgrade attempt. DNS automation development began, the DNS propagation workflow was completed, and slow DNS loading was resolved by signaling Docker reloads directly, bringing load time to within 15 seconds. The team also joined the Baseten custom Falquist CSI discussion and advised using the existing CSI plugin, participated in Weka integration planning, joined the Hong Kong data center on-site deployment plan discussion, prepared System-973db3fd02 API work, and advanced and tested the Beijing data center ticketing system launch.

For incident handling and service improvements, the team repaired the Falquist cluster RDMA issue on Oraport-System-ff2ba3b2f6-180, investigated Baseten Falquist slowness, and restored Pelshaw by debugging Pelshaw on new machines. We shortened the cutoff impact for users affected by unfinished one kill tasks through code changes, resolved node NotReady status and terminating pod assignment failures to hardwaresre, and traced those symptoms to inaccurate VM metrics. The ticket work also progressed through discussion of a ticket data extraction approach and use of Bexgate79 to deploy a personal ticketing system, which reduced development effort compared with the Grafana path.

KR1 remains focused on finishing automatic metric collection and statistics in Q1 while covering the required statistical dimensions, and DNS automation is being shaped into a full automated DNS configuration flow. The on-site ticket effort is steadily extending the repair ticketing system to nationwide on-site repair groups, process optimization is continuing through label gap cleanup and existing Bug improvement, and metric visualization is building a ticket metric Dashboard while checking and refining API data accuracy. Metric calculation research completed three early implementation studies; Grafana was reviewed but was slower and harder to connect with dynamic API, and Pelshaw required more investment than fenalova or a self-developed Bexgate79 frontend because LLM assistance was not available. The fenalova direction uses a Dashboard + LLM model and remains the expected final platform, while the current approach is to use the Bexgate79 frontend for all metric displays until fenalova can be deployed, allowing abnormal data to be found earlier and data cleansing plus collection expansion to start in advance.

## Next Week's Plan

Next week, the team will cover biweekly duty and continue supporting U.S. customers while working closely with colleagues to improve the metric system and the operations accountability mechanism. Bug work will focus on restoring and integrating ticketing system capabilities and fixing existing Bug, while repair ticket promotion will bring the ticketing system into on-site operations teams; the team will also visit Beijing for face-to-face communication, deeper review of current plans, and discussion of improvement ideas.

## Coordination and Help Needed