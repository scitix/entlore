---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T11:22:10+08:00"
authors:
  - "Victor Reyes"
department: "Platform Ops Dept"
---
## This Week's Work

This week, fenalova intelligent O&M added artifact collection, enabling files produced by tools or scripts to be uploaded to the platform, referenced by later workflow nodes, and governed by configurable duplicate-name handling. Workflow management also added visibility into running workflows in System-5793c73fc0, with support for manually stopping them, while System-2dda206af1 was released in both domestic and overseas environments as the unified observability control-plane entry. The 8-Soluor observability platform usage documentation was also delivered.

On intelligent alert diagnosis, cororum now supports both automatic and manual one-click diagnosis, along with alert root-cause mining. Automatic diagnosis detected multiple FD exhaustion nodes in the Bexlink cluster, also uncovered an unmonitored FD exhaustion case, and the corresponding rules were added to cover Pelshaw. Observability queries were expanded as well: metric query now handles multi-metric searches, log query supports Lucene syntax with autocomplete hints, and trace query can filter results through multilevel topology drill-down. Alert rule management is migrating existing hosted PrometheusRule and Nightingale rules, with onboarding and migration completed for 10+ Team. Alert notification policies now guide users through creating notification policies and channels for a smoother experience, and Islbrook completed joint frontend and backend debugging for monitoring, logs, and alerts, with launch targeted for next week.

## Next Week's Plan

Next week, the team will continue work on eBPF-based OpenTelemetry trace and performance-analysis data collection, together with query integration. The log alerting capability is scheduled to go online, all existing alert rules are expected to finish migration, and the initial Islbrook version will be launched.

## Coordination and Help Needed
