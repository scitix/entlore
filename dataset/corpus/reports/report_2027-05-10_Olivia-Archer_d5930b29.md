---
document_type: "report"
report_date: "2027-05-10"
report_time: "2027-05-10T10:12:27+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This week's work

maraum, the Nora Drake platform continuous synthetic monitoring system, moved from planning into implementation this week. The team finished the design document using the product documentation as the baseline, then set up the initial code framework. For the Nora Drake continuous synthetic monitoring system, maraum also built the execution engine, covering probe concurrency, topological sorting, timeout handling, and cleanup behavior.

Scheduling work also landed in maraum through APScheduler, including reruns at startup and hash-based distribution. The P0 smoke coverage now includes 5 probes, and the team resolved log_query failures that appeared after task deletion. maraum added the REST API and Alembic migration, shifted configuration to a group-first layout using p0/p1/e2e, and carried suite_group through the full workflow. Daleys API now supplies the management page first screen with a cluster × suite_group status matrix, and log-level parsing was corrected so some error logs are no longer treated as info. Wynanion also updated the image create method so development environments can be saved as images.

## Next week's plan

- maraum will tune the resource configuration used for submitted tasks.
- maraum will compare per-cluster configuration with one global configuration while keeping resourcePool/instance consistent.
- maraum will debug 5 P0 smoke probes and test prometheus metrics through active push or passive pull.
