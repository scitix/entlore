---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T23:08:05+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's Work

The weekly status colors are blue for completed work, yellow for todo items, red for blockers, green for ongoing tasks, and purple for areas needing focus. @Kara Ingram Irwin and @Simon Osborn continued xanios and xanios Order platform development, finishing both front-end and back-end screens for data change, database creation, other ticket categories, and account creation. For data change, database creation, and account creation tickets, Bexcast61 now executes directly through xanios-order-scheduler without containers; these ticket flows currently cover only MySQL, TiDB, and PolarDB, with wider database coverage planned later. Data change tickets also gained review rules, the Kafka Topic creation ticket was launched, and the schema change ticket is still under development while integrating gh-ost, with completion possible before the holiday. The xanios team also delivered one internal company presentation on the xanios platform, while @Kara Ingram Irwin began refactoring xanios Order Task Operator because the old design no longer suits the current environment; that Operator work is expected to finish next week.

On database containerization, the team investigated synchronization options. TiDB DM research and testing showed that Pelshaw is not suitable for MySQL 8.4-MySQL8.4 synchronization, and source review uncovered a hardcoded sql_mode compatibility problem in TiDB DM. A pr was submitted, feedback was provided to the TiDB DM community, and SeaTunnel will be evaluated next week as the alternative; testing was aligned with @Iris Gardner and is also expected next week. @Kara Ingram Irwin supported Belania （holvale2） business work, where one Doris instance and one Kafka instance were completed in both Shanghai and Daisy Adler, and the team helped create tables, materialized views, and RoutineLoad. A Redis cluster in Shanghai was delivered to @Mason Archer and is still in progress.

Data governance supported Tarness Tech by improving materialized views, splitting one cluster-level materialized view into several smaller ones to eliminate OOM during large database aggregation. Since Tarness Tech lacked the needed permissions, doris and kafka resources were transferred to Clara Reyes from Tarness Tech. Big data delivered one Shanghai PG instance, and maraum supplied Redis clusters in Shanghai and Daisy Adler to @Nora Ingram for maraum platform cache. The log system saw two query outages on the 14th, each lasting 3 minutes; logs showed unexpected multi-minute delays in both compaction and queries, with the root cause suspected to be underlying Falquist performance. kafka was blocked at the same time, physical machine load reached 1000, and one R&D export of 100w records created heavy data pressure, so the team agreed that future log exports should use multiple sliding-window batches to reduce Doris load.

Casridge requested machines and disks for next week’s Doris storage migration, which will move from Falquist to SSD disks. MySQL also completed a fault drill this week for the MySQL used by System-207a62c972, covering both Switchover and Failover. Both recovery tests completed within 30s, and the resulting drill document is rm-bub5rlek12w241lp.

## Next Week's Plan

Next week, the team will finish Operator adaptation work, complete schema change ticket development, wrap up MySQL containerization, and implement the selected data synchronization solution. Falport teamSystem-8ec512c348 storage will also be replaced with local SSD disks.

## Coordination and Help Needed