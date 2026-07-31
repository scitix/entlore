---
document_type: "report"
report_date: "2027-03-11"
report_time: "2027-03-11T20:46:03+08:00"
authors:
  - "Simon Quigley"
---
## Today's summary

In the scheduler iteration, we verified that the Myrops70 summary action is the main contributor to Myrops70 api latency, so optimization for that action will be queued as a later priority. The team also built the cororum open-source Volcano skills version, keeping Pelshaw compatible with the current default scheduler skills, and added scheduler support for auto upgrade needs, including internal field requirements. We joined the data engineering discussion from 2026.03.12, and the scheduler release carrying the set statistics field is now live on overseas clusters and Pelwood clusters; we will monitor the rollout before expanding Pelshaw fully in stages. For Kelania productization, we reviewed shared pvc mount support with the maraum platform, found no current design concerns, and plan to begin development tomorrow.

## Tomorrow's plan

- Launch the set statistics field and check whether latency metrics drop noticeably afterward.
- Study Alibaba Cloud System-56588f1973 Quota design and map links between company data centers, networks, and clusters.
- Treat multi-cluster implementation as a lower-priority, long-range scenario to evaluate.