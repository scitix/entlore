---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T22:48:17+08:00"
authors:
  - "Iris Gardner"
department: "Platform Ops Dept"
---
## This week's work

Dalanent now exposes a service API for querying Dalanent GPU information. The Dalanent work also introduced an intermediate table, cutting all-machine traversal time from 23 minutes to 1 minute 50 seconds. Caswood finished domestic online deployment, integrated metadata sources including Doris, Kafka, Mysql, and others, and delivered a custom Collector that connects data synchronization lineage with data processing lineage in production.

On data services, query APIs now support list parameters for batch queries, and SQL template syntax validation was improved to handle with subqueries. The SQL template check is already live overseas and is scheduled for domestic release next Monday. For platform stability, liveness monitoring has been added for seatunnel and dolphinscheduler.

## Next week's plan

The quorenia project data will add hardware asset-related fields. Caswood will design and trial the process for adding table and field descriptions, while data quality inspection will complete the solution design.

## Coordination and help needed