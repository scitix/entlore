---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T20:46:39+08:00"
authors:
  - "Brian Walsh"
department: "Platform Ops Dept"
---
## This Week's work

This week, the team benchmarked envoy gateway throughput and generated envoy reports across different core-count profiles, including the physical-machine cluster benchmark report. We also implemented keepalived garp settings for the nginx and DNS clusters, refreshed the existing keepalived configurations, and brought those changes online. The layer-4 load-balancing approach was reviewed and closed out, with the Xaneys plan designed.

## Next Week's Plan

- Take over the umbalos fault-location tool.
- Modify physical-machine NICs for Pelport cluster Xaneys testing.
- Connect the Pelport cluster Xaneys test environment to Vyrbase83 leaf with trunk mode, and allocate dedicated VIP and SNAT IP for Xaneys.