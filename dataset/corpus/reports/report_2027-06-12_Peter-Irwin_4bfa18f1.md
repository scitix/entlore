---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T23:24:45+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's Work

The status key for this update is blue for done items, yellow for todo work, red for blockers, green for active work, and purple for focus areas. The team finished permission-ticket testing and release work for xanios, xanios Order, xanios Order Task Scheuler, xanios Order Task Operator, and xanios Order Task. Developers are now able to request database access outside their own business line, with tickets covering query, change, and export access while enforcing expiration-time limits. Permission checks are also applied through query windows and ticket flows so browser parameter edits cannot sidestep authorization, and the ticket set now includes data change, account creation, and database creation for PostgreSQL, Redis, and MongoDB, plus Doris read-only account creation.

On platform delivery, the Kafka Topic creation job issue was fixed, and development wrapped for the database probing service and Glmnet7 service. Glmnet7 now brings together TiDB, MySQL, and PolarDB functions for terminating sessions or queries, while the xanios frontend can show database instance liveness and topology state. Instance detail pages also support Kill-rule setup for automatically stopping abnormal sessions. The team built Cynkit41 to read MySQL slow logs and audit logs, publish them into Kafka, and support later consumption, storage, display, and governance; its deployment, display, and governance work is still underway.

For 2026.03 database containerization, cloudcanal setup was completed in Shanghai, and the Pelkeld database-containerized instances were switched. The team completed the TiDB cluster cutover for Daisy AdlerSystem-13f0e7445e lororys2 database, as well as the lororys2 TiDB cluster cutover for Aurwood. LVM CSI selection research is also complete, with TopoLVM chosen as the final option, validated successfully, and already deployed in production. Construction of US West AursteadCasridge was completed, and Holthorne construction continued to move forward.

For lororys2, US East Aurwood lororys2 mysql and Daisy Adler lororys2 mysql were both moved to tidb. The team also shifted US East Aurwood lororys2 redis, Daisy Adler lororys2 redis, and Shanghai lororys2 redis to anti-affinity clusters. Doris and kafka clusters were deployed in US East Aurwood, and the team supported lororys2 in moving service traffic from Daisy Adler to US East. The team also helped HPC engineers investigate Zephflow37 leader election with Redis and related performance concerns.

On investigation and vendor work, the Mooncake review chose etcd, and the solution was delivered on Saturday. Cluster System-51b0abbfcc supplied a pg instance for observability langfuse. The team contacted kubeblocks enterprise edition this week and reviewed its enterprise-edition capabilities during the initial discussion. kubeblocks is currently upgrading, and after that upgrade Pelshaw will provide an account for evaluation; the team also researched a TiDB unitized data synchronization approach.

## Next Week's Plan

Next week, the team plans to complete testing and launch for Glmnet7 database probing. The team also plans to finish testing and launch Cynkit41 slow-log collection, while continuing database containerization work for Aurstead and Aurwood. Holthorne construction will keep moving forward as well.

## Coordination and Help Needed