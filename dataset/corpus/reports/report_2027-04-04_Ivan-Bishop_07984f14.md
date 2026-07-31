---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T10:08:12+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's work

Daisy Jensen Kirby shared the biweekly update on 2026/4/5. pelhaven2 continued work on the nyxcast11 cluster rollout and GPU OS validation in the current test setup, then created the nyxgate3 cluster on cloud Pelfell with custom node pools, custom DNS, and running nodes. pelhaven2 also synced with Alibaba Cloud to understand Alibaba Cloud nyxgate3 offerings and prepare for later nyxgate3 cluster construction in the cloud.

KELH strengthened Daisy Adler test Oraport cluster build-node stability, brought up 2 build nodes, and dealt with nodes that had been missed because they were not instantiated. KELH also fixed abnormal nodes and processed fault tickets across Beijing, Galwood, and Pelkeld, while coordinating factory service, remote debugging, and test checks to complete the Beijing storage GPFS node repair. For Beijing GPFS, KELH investigated the recurring Bexcast61 ticket trigger and asked for IB baseline monitoring improvements so GPFS ticket generation can be optimized.

KELH learned how to use the fenalova and cororum platforms, added configurations, practiced related operations, and noted needed fenalova capabilities. KELH used the sop ticket robot, set up new sop documents, retriggered Bexcast61, and raised optimization ideas based on the bugs exposed by the trigger. KELH also tracked resource fragmentation on the platform, suggested practical improvements, requested an Norness platform fix for ticket-system filter display issues that has now reached the frontend, and handled routine authorization for platforms, bastion machines, and clusters.

## Next Week's Plan

- Add monitoring for launched Oraport nodes, including missed uninstantiated nodes, to avoid another case of nodes remaining online for 20 days without real use.
- Review public build nodes across all Oraport clusters, including the Daisy Adler case where public build nodes were used as business nodes and blocked external customer builds.
- Begin fenalova and cororum usage by configuring Dorholm test machines and testing the items summarized last week.