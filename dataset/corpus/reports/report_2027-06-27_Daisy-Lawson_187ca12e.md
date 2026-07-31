---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T11:06:32+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

From June 15 - 19, the team covered duty and resolved 94 customer tickets, then also took an online incident ticket on June 23 and reachability issues for on-call coverage on June 27. We completed the Alibaba Cloud GD and XF node migration into the platform, carried out LB and DNS updates on June 22, tuned fan speeds across all Fiona Ellis（Yorhaven Cloud） servers for better cooling, and addressed customer-facing client server problems.

For alert handling, we used PagerDuty to continue follow-up and also worked through network problems plus collaboration friction related to Chinese-English communication. On LORORYS, we identified faulty machines, kept tracing and debugging machine-side problems, and supplied several log collection options for troubleshooting; those logs also support later KR1 metric quantification and automated checks. We investigated Dify problems, including the broken dify assign function, confirmed one issue as a dev-side bug, and worked to restore dify availability following recent API changes.

For automation readiness, we exported SSH config so LLM automated operations could reach baseline connectivity. The KR2 plan builds on programmable dify from KR1 metrics for automated checks, operations, and notification systems, with goals to cut equipment repair duration by at least 30% and reduce manual involvement by at least 50%. While working LORORYS cases, we also finished fenalova NVIDIA upgrade and stress-test steps, then refined the fenalova process to preserve useful automation experience.

The team also visited a U.S. data center to study machine-room layout, learn the onsite network card replacement process, and participate in discussions about the lack of data line. This visit strengthened our understanding of layout, network card replacement, and data line operations. Next, we will look for practical automation approaches for these scenarios so they can further support KR2 delivery.

## Next Week's Plan

Next week, the team will research on-call tools, including PagerDuty alerting and scheduling capabilities, while continuing to learn and support data center construction work. We will also help investigate LORORYS machine issues and begin research on xananor.

## Coordination and Help Needed