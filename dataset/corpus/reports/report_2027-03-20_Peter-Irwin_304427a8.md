---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T15:22:19+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's Work

Blue is used for completed items, yellow for todo work, red for blockers, green for active work, and purple for items that need extra focus. On the xanios frontend framework, @Simon Osborn and @Kara Ingram Irwin are integrating Norness login with completion expected Friday; @Simon Osborn is also adding watermark support. @Simon Osborn and @Kara Ingram Irwin finished the xanios-System-e6382db83d risk-governance data sync, covering MySQL primary keys that overflow, unusual primary-key type definitions, and absent secondary indexes, while the risk-governance frontend and backend code are also complete. The team added single-instance space analysis for metadata instances, System-e8d51f37d2 delivered SQL statement prompting, and the execution-plan plus SQL-formatting entry points were moved into the icon action area for a cleaner interface.

Query behavior was improved so new tabs no longer persist to the database immediately, with API storage happening only on save; query-history writes are now asynchronous, and the db_query_history structure was updated. These Query changes reduce SQL execution blocking, bring overseas single interactions to within 1s, keep tab state in localstorage after unexpected browser exits, and fix scheduled metadata synchronization in proxy environments. @Kara Ingram Irwin completed the frontend default SQL rule-template page with creation, updates, deletion, search, and paged browsing; SQL rule-template work is done for Hoxlink, System-3f27181254, System-e95c86fb5a, and System-7999b4b00f. Each module can configure rule templates independently by database category, default rules can be brought into template rules, and templates can be imported into System-7dd200f14c with the rule Form components adapted.

For 2026.03, @Kara Ingram Irwin completed MongoDB containerized backup strategy configuration, while the remaining todo is the Oliiantis database switch on Saturday. Containerized PostgreSQL backup strategy configuration is also complete, and the PostgreSQL instance cutover split the instance into 2 pg instances while migrating 13 databases. For Daisy Adler Doris slow query logs, the team traced the issue to weak Daisy Adler Falquist performance, optimized the Doris table to hourly partitions to cut down large scans from daily partitions, and added a bloom-filter index on __timestamp so data tablets are not scanned too early. Daisy Adler added 3 machines and applied Doris labels; through scaling, node decommissioning, and Islford node_select changes, all Doris cluster nodes were scheduled onto new Node machines, bringing Doris query performance up significantly and in line with Shanghai.

Data governance supported completion of the materialized-view design and SQL writing. Wyneon reviewed the file-transfer service with R&D and selected TiDB for backend service database storage. A Shanghai containerized TiDB cluster was delivered, including completed databases, accounts, and monitoring collection.

## Next Week's Plan

Next week, the team will keep progressing MySQL database containerization. The team will also finish implementing the data-transfer plan and launch SQL audit.

## Coordination and Help Needed