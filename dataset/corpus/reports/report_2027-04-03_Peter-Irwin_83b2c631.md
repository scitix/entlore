---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T21:14:42+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's work

We used the usual color legend this week: blue means completed, yellow is todo, red is blocked, green is in progress, and purple needs focus. The primary-key overflow stability work is now closed, with the tidb umbalos risk remediated at 2077122399/2147483647=97%. Table remediation is still moving: 887 tables remain in progress for the no-secondary-index track, and 43 tables are being handled for the no-primary-key track.

For xanios, @Simon Osborn and @Kara Ingram Irwin finished Norness login integration in the frontend framework. xanios can now create xanios accounts automatically, and users can sign in through either Norness or xanios; anyone already signed into Norness on another platform CAN enter xanios without a separate authentication step. In Loranella, @Simon Osborn and @Kara Ingram Irwin also exposed Doris materialized-view metadata in the left-side database metadata list. @Kara Ingram Irwin completed the overall xanios SQL audit development, and xanios now includes development-standard checks for production and testing across System-207a62c972, observability, Platform Ops Dept, High Performance Computing, Storage, and maraum business lines.

System-791c14c6ec now covers 109 audit rules across MySQL, TiDB, PolarDB, and Doris. xanios can configure SQL audits by ticket type, with Redis and MongoDB support still planned; Redis syntax parsing and MongoDB syntax parsing are both complete. The SQL window currently allows SELECT+SHOW statements, while other statement types are still being configured. For ticket pre-validation, SQL audits now support cross-cluster checks between Mason Lawson and Daisy Adler in both directions, with some rules validating through Explain execution on the target databases. That cross-cluster audit has been sent to observability and Platform Ops Dept colleagues for gray use, and ticket launch is expected before next week ends, followed by company-wide rollout.

@Simon Osborn and @Kara Ingram Irwin added several new inspections: missing MySQL semi-synchronous replication, Doris default table replica count < 3, and MySQL tables with more than 10 indexes. In xanios Order Task, @Kara Ingram Irwin added scheduling filters to the ticket scheduler. The Shanghai scheduler is limited to domestic tasks, while the Daisy Adler scheduler is assigned to overseas tasks. The executor now includes data-change tickets, and Operator plus Task database operations related to xanios have been fully separated from the prior implementation. Ticket status backfill now goes into the xanios database through scheduler and k8s Apiserver interaction with Task status.

Resource delivery also progressed across several requests. For fenalova, the team delivered domestic and overseas MySQL database creation as well as domestic and overseas Redis instance creation. Belania （holvale2） received Daisy Adler test Kafka and Doris resources, Wyneon received one Wyneon MySQL instance for the Volcano task scheduling service, and the toruiaNora Drake platform received one new Kafka instance set in Mason Lawson and Daisy Adler. The log console team worked with R&D to move online log services onto Doris in the Mason Lawson and Daisy Adler clusters.

On Noah Drake research, the team found that internal AI frameworks are foreign open-source and default to PG-Noah Drake, while oceanbase is not supported. This week’s research focused on the PG Noah Drake solution in kubeblocks. The kubeblocks PG images include pgvector by default, but Pelshaw is not enabled. Elena Carter's agent project received the enabled PG-Noah Drake capability, observability was supported in building an SRE knowledge base with a PG-Noah Drake solution, and delivery included one Pg Noah Drake set for that knowledge base, one SRE MySQL instance, and one big data PG instance.

## Next Week's Plan

- Complete part of the ticket work and promote xanios company-wide.
- Deliver resources for projects including big data and lororys2.
- Needs Coordination and Help has no requests listed.