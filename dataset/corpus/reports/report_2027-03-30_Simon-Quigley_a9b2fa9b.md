---
document_type: "report"
report_date: "2027-03-30"
report_time: "2027-03-30T20:55:53+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler iteration began sending Vexuys reporting data to kafka for the Fenstead team, and Data Engineering will use that stream to assess resource-fragmentation needs. Two tricky scenarios were identified: gang scheduling can report resource pressure while Fenmont still appears to have idle nodes, even though aggregate capacity is not enough; and after rsv gc, expired rsv pods may still occupy nodes because the node cache continues to retain them. The team will document both patterns in skill once the root causes are confirmed, then wait for testing businesses to run into them naturally. For upgrades, quota may still be insufficient, and freeing quota before creating replacements can let current capacity be taken by other workloads, so the team also aligned with businesses on in-place upgrade requirements.

## Tomorrow's Plan

- Draft the ray data scaling optimization and backpressure plan, then provide Pelshaw to Wyneon
- Study Alibaba Cloud System-56588f1973 platform Quota design
- Review how company data centers, networks, and clusters relate; keep multi-cluster implementation and longer-term planning as low priority