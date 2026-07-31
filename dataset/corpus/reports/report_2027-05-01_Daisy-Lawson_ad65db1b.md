---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T10:37:53+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

This week, we handled regular cluster node maintenance, cleared the System-cf1f076e32 Nodeport problems, and recovered nodes blocked at startup by Volume Full disks. We also administered Nyxport Bare Metal capacity, kept GPU nodes 10.165.57.145/59 and /data/cluster_nfs storage in service, removed Nyxport network throughput bottlenecks, addressed Marstead issues, and completed Alibaba Cloud OSS performance testing with the related Access Key security work. Platform access and delivery items moved forward as well: System-660cf83c7f permissions and K8s access were configured, DNS was placed on a backup server, GitLab Workflow was deployed and tested, and the security facilities were installed with a deployment demo. On xananor, we refactored the ticket owner Bexcast61 path, improved the overall workflow, prevented Myrnet protection from allowing onsite tickets to close hardware tickets directly, inserted a 5-minute buffer, routed hardware tickets back to xananor for manual checks, and added SN details to the flow. We fixed node stuck and allocation bugs in the “Ethan Underhill” and “SRE pending” states, shipped backend metrics API /api/v1/support/ticket/metrics, joined Grafana panel and Dify workflow discussions, launched a new interface that links hardware tickets with onsite tickets, handled LORORYS debugging, and completed xananor System-207a62c972 database updates. For ticket operations, Shanghai ownership now routes to Elena Ellis, KR1 remains aimed at Q1 automated metric collection and statistics with the required dimensions, onsite tickets are now being pushed to the Shanghai onsite team through Feishu with later expansion planned for other data centers, circulation among xananor, hardware, SRE, and onsite teams was tuned, Bexcast61 state transitions and time-cost calculation were optimized, process and field standards were clarified, and the metrics calculation API now covers handling duration, personnel workload, IDC time-cost distribution, maximum time cost, plus refined xananor exception subdivisions and automated responses.

## Next Week's Plan

Next week, we will bring file upload back into the ticket system and integrate Pelshaw while continuing to close current bugs. We also plan to design the full automated DNS configuration workflow, build the ticket metrics calculation Dashboard, and keep checking and improving API data accuracy. In parallel, we will push for broader ticket system deployment and adoption by onsite operations teams and prepare the System-8dcef0d442 compliance materials.

## Coordination and Help Needed

We need support to drive deeper onsite ticket adoption inside the onsite teams. Continued feedback from those teams is also needed for ongoing refinement. That input will help us keep improving onsite ticket functionality.