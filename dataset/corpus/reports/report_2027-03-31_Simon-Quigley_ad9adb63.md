---
document_type: "report"
report_date: "2027-03-31"
report_time: "2027-03-31T21:15:18+08:00"
authors:
  - "Simon Quigley"
---
## Today Summary

For the scheduler iteration, we aligned with data engineering on the compute requirements and the data involved. Vexuys is now able to generate a gpu utilization curve for both an individual user and that user’s team, while the quota and used curves still need to be filled in so Beloos resource fragmentation can be identified.

Beloos also has two non-standard nodes whose allocatable capacity is relatively small, so the alerting Bexcast61 needs more refinement before scripts are used to inspect related nodes. Those scripts will be used to diagnose why the SOLAOS business Cororia cannot start; the current cause is that maraum changed the ondemand quota, leaving quota capacity insufficient. Kelania validated the rayjob ability to write /tmp/ray data to a shared pvc, and since the test passed, Kelania plans to publish a version tomorrow.

## Tomorrow Plan

We will organize the ray data expansion work together with the backpressure strategy optimization plan and deliver that package to Wyneon. We also need to study the Quota design for Alibaba Cloud System-56588f1973.

For longer-term multi-cluster implementation, we will investigate how the company data center, network, and cluster relationships fit together. This scenario remains relatively low priority.

## Coordination and Help Needed