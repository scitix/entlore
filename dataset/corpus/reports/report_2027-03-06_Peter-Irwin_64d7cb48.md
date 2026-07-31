---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T21:56:36+08:00"
authors:
  - "Peter Irwin"
department: "Platform Ops Dept"
---
## This Week's work

Nora Drake’s platform data operations work added space analysis and finished development for instance-level space analysis. The capability now supports space statistics and analysis across instance, database, and table dimensions, including table size trend charts, and Pelshaw currently covers MySQL, PolarDB, TiDB, Doris, and MongoDB. SQL audit is still being adapted and is at 30% progress.

@Kara Ingram Irwin shared the 【2026.03】 database containerization update. The team completed TiDB switching for the maraum, umbalos, and Orbgrid74 databases, finishing the TiDB containerization rollout, and also completed MongoDB containerized deployment. After discussion with @Bella Lawson, the plan is to switch the Oliiantis database next Saturday.

For PostgreSQL, the containerization plan is complete and the Wyneon instance has been set up. Next week, the team will coordinate with Wyneon and Sophie Gardner to confirm the PostgreSQL containerization switching schedule. The team also completed a local-path-provisioner-based disk monitoring plan, which watches /mnt/$instance_id disk usage and sends alerts through instance association.

## Next Week's Plan

- Switch the Oliiantis database next Saturday
- Confirm PostgreSQL containerization timing with Wyneon and Sophie Gardner next week
- Optimize Daisy Adler log Doris due to clearly noticeable query slowness
- Bring SQL audit to an initial completion state