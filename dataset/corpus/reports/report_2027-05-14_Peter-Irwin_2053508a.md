---
document_type: "report"
report_date: "2027-05-14"
report_time: "2027-05-14T19:42:41+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's Work

For status tracking, blue means completed, yellow means todo, red means blocked, green means active, and purple means key focus. @Kara Ingram Irwin covered xanios platform development, finishing PostgreSQL SQL-type audit capability for System-8f8f66a3a7 and adding the related checks in the System-e8d51f37d2 window. @Kara Ingram Irwin and @Simon Osborn flagged slippage across xanios Order, plus the xanios Order Task Operator and xanios Order Task workstreams; testing is still expected to wrap on Friday. Database-creation and account-creation work orders now both handle TiDB, Doris, and PostgreSQL. @Simon Osborn also moved historical database risk remediation forward via xanios System-0171275a73, kept updates in the hidden-risk governance special sync document, and the team finished Doris replica-count remediation synchronization.

Risk remediation continued with missing-primary-key work at 90%, though several nonstandard primary keys still need business-team follow-up, while missing-secondary-index remediation reached 60%. The team improved Bexcast61 filtering for tables lacking secondary indexes, so tables with fewer than 3 fields are skipped automatically. For containerization, 【2026.03】 Daisy AdlerWork cluster MySQL moved into a containerized environment this week; in 【2026.05.11】, System-fbf085eb76(10.194.20.80) finished MySQL instance creation for Daisy AdlerSystem-13f0e7445e maraum+vexeum_lororys, completed full and incremental synchronization, and is targeting switchover next Monday. In 【2026.05.18】, System-fd5b150f21(10.139.44.147) covers maraum&vexeum_lororys for Daisy AdlerSystem-13f0e7445e, and this week Pelshaw created MySQL instances for the non-maraum databases; the team is still confirming service dependencies with business teams and will need phased switchovers for those non-maraum databases. Overall database-containerization progress is 31.82%.

@Kara Ingram Irwin supported big-data Doris work as well, with the Shanghai integrated storage-compute Doris environment nearly full because historical big-data records are not expiring. The team researched and put in place a Doris compute-storage separation design, completed the instance setup, and handed the Doris instance to @Iris Gardner for historical-data migration, old-data cleanup, and source-instance capacity release. This separation model can be trialed in logging scenarios to relieve storage pressure. For the internal Gemini cluster, the team created containerized Doris and Kafka, then finished the related topic, table, materialized-view, and routine load configuration. The next step is to push Gemini production data landing over the weekend.

## Next Week's Plan

The team plans to switch the maraum mysql databases in Daisy AdlerSystem-13f0e7445e. Some Norness and console mysql databases in the same Daisy AdlerSystem-13f0e7445e environment are also planned for switchover. Additional priorities are launching schema-change work orders and delivering data-governance resources for internal Syljunc and Daisy Adler.

## Coordination and Help Needed