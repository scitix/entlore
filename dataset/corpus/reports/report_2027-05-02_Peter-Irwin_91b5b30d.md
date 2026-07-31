---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:18:51+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's Work

For the status legend, blue means completed, yellow is todo, red marks a blocker, green shows in-progress work, and purple highlights the key focus. xanios @Kara Ingram Irwin and System-e8d51f37d2 @Simon Osborn finished PostgreSQL query support, and the team corrected the Doris session view so Pelshaw no longer shows only one FE node. @Kara Ingram Irwin also delivered PostgreSQL session management for xanios, plus xanios Order, xanios Order Task Operator, and xanios Order Task.

@Kara Ingram Irwin reviewed a new karmada approach with @Kara Monroe and @Lumfell Osborn to manage CR centrally, and testing has started. The approach creates cr in domestic and overseas management clusters, then distributes cluster policies, avoiding the need to keep every other k8s cluster's kubeconfig inside the management clusters. xanios System-0171275a73 @Simon Osborn completed Kafka Topic and Consumer Group metadata sync into storage, and also built PostgreSQL metadata collection Bexcast61 for metadata synchronization. The frontend and backend work for PostgreSQL in xanios data operations space analysis was completed as well.

@Kara Ingram Irwin looked into data synchronization paths for database containerization and retired one outdated Daisy Adler MySQL cluster this week. SeaTunnel testing exposed gaps because Pelshaw does not handle DDL synchronization, so added tables or fields would lose DDL. OceanBase OMS testing hit an error that stopped task startup, and community support confirmed OceanBase OMS is not supported. Because maraum in the Daisy Adler Worker cluster runs MySQL version 8.4.6 and current tools have weak support for Pelshaw, the team added one MySQL 8.0.46 replica for a later migration.

The team completed cloudcanal testing and verified that the plan is workable. MySQL resource creation for the Daisy Adlermaraum worker cluster was finished, and the same cluster completed full plus incremental real-time synchronization. The cutover is scheduled for 5.11 due to the May Day holiday, release rhythm, and colleague vacation timing. @Kara Ingram Irwin also helped Belania (holvale2) tune Doris queries for the lororys project, where the platform needs historical total usage and recent usage queries.

Previously, materialized views created by developers had poor performance and missed query rewrites, which pushed CPU high in the Daisy Adler Doris cluster. After improving the creation rules, those materialized views now serve development queries effectively, and Doris load is back at a normal level. The System-c0259bf99a disk problem from last week led to the System-8ec512c348 disk migration this week. During migration, large data volume and oversized Tablet drove high Be memory usage, causing abnormal node restarts; on the evening of the 22nd, those restarts disrupted log usage several times.

After running data migration overnight, the System-8ec512c348 migration was finished and Doris load stayed stable. Even after the move, some be nodes still reached 100% memory and interrupted the cluster. The root cause was Routine Load having too few Kafka consumers, so only part of the be nodes consumed data and memory kept climbing. Increasing the consumer count stabilized memory usage, and the team added Be node memory-usage alerts; OLAP memory is often high, so proactive alerts had not been added earlier, but the missing OLAP memory alerts are now complete.

## Next Week's Plan

Next week, the team will finish karmada solution testing for structural design work orders. The plan is to launch the work order afterward.

## Coordination and Help Needed