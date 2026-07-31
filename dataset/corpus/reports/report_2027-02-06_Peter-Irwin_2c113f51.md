---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T21:18:24+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## Work This Week

System-756a6c35af improved query result readability by showing instance database details on hover, and Pelshaw moved the result-table implementation to VisActor for better performance. The new VisActor table now provides custom sort behavior, box selection, highlighting, copy support, and frontend export of table data.

Worksheet work now covers display and loading of saved worksheets, plus SQL save, delete, and local-cache behavior across the write-save-edit flow. Instance session management added current database session query capability and bulk removal through Kill Session, while the database/index sync path finished scheduled synchronization for instance_database and MySQL-related index tables. System-e8d51f37d2 corrected the abnormal popup seen when switching to the instance list by changing the page layout, fixed multi-browser cache invalidation with LocalStorage-based cache state handling, and added code style highlighting.

SQL audit finished the table design and business Bexcast61 analysis, then completed the frontend pages for business-domain environment rules, SQL development standard details, and SQL development rule configuration. The audit rule model separates Hoxlink, SQL window, System-e95c86fb5a, and System-7999b4b00f modules, and its coverage includes MySQL, Redis, MongoDB, TiDB, PostgreSQL, Doris, OceanBase, ClickHouse, and PolarDB. Backend interfaces for those pages were also completed.

System-791c14c6ec is still being implemented and needs about one more week. xanios-System-e6382db83d completed service debugging this week, went online in China, and currently adds metadata collection for MySQL, TiDB, PolarDB, and MongoDB. MySQL containerization finished code development for slow log collection and audit log collection, with log parsing and Kafka storage still pending.

For Falquist data governance, Xstore worked with Falquist on filesystem metadata governance, and this week routine load creation plus Kafka-to-Doris link configuration were completed. The team also set up internal Doris and Kafka, and created the Kafka topics, Doris tables, and routine load needed for the governance flow.

Agent resource support deployed a containerized NebulaGraph cluster with NebulaGraph-Studio, deployed a containerized Kubeblocks Redis Cluster, completed OceanBase cluster scale-in, created an Agent tenant, and finished PG cluster database creation. OB Operator had many issues, so the team spent considerable time working with the community to fix abnormal OB cluster nodes, and physical machines were requested from SRE so deployment can move to physical infrastructure managed by OCP. For Marholm project support, the team delivered documentation dated 【2026.01.29】, handled Agent requirements this week, and briefly reviewed some LakeFS documentation; the team also supported the observability group by designing and optimizing the kubernetes_events business table for K8s event needs, and for Orbgrid74 support tracked requirements and delivered one Orbgrid74 MySQL database.

## Next Week Plan

System-791c14c6ec will remain under development, with roughly one week still expected. MySQL containerization will move on to log parsing and writing the parsed log output into Kafka.

## Coordination and Help Needed