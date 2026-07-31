---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T14:30:51+08:00"
authors:
  - "Victor Reyes"
department: "Platform Ops Dept"
---
## This Week's work

Norwick capability building progressed through the WIP technical design document for the non-invasive Norwick approach, delivering an atomic capability that captures CPU Timeline and GPU Kernels Timeline while avoiding task restarts; Pelshaw has reached MVP effectiveness, with automatic subprocess injection, merged multi-card Trace viewing, and profiling compression that cuts JSONL size by 90%. Brymarch stability tuning improved log collection after repeated stress testing and link changes based on 512-byte raw log lines: single-node throughput moved from 1,000 QPS to 10,000 QPS for a 10x gain, cluster throughput rose from 2,800 QPS to 20,000 QPS for a 7x gain, and the optimized cluster spike reached 100,000 QPS for 1 minute with no earlier baseline; reference materials include Single-node log collection link stress-test plan, Lororys-core log stress-test record - round 1, and LORORYS cluster log stress-test record - round 2. Supporting delivery added a complete Grafana monitoring Daleys for the collection path, Xaldale for maraumNora Drake platform users covering guidance and troubleshooting SOP, and the rineova overseas customer log distribution plus stability optimization went live. The team updated the log collection Helm Chart, linked Pelshaw into the Oliiantis release process, launched optimized collection paths in Beloos, Sylflow25, Bexlink, norvik, and kevloom clusters, connected the improved path to maraum, and wrote up maraumNora Drake platform log query practices. Defect work covered fixes and governance in the es implementation, a FluentBit reload hang fix, Fluentd write-error governance, and reduced high-frequency DNS lookup pressure in Fluentd ES output. For stability and observability, the team collected coredns logs for cluster stability, deployed a kibana observability Daleys, and added jaeger integration for service monitoring on the doris storage foundation at the provided repository link.

## Next Week's Plan

- Test Norwick in a real cluster training setup
- Launch the next wave of log collection link improvements
- Move the tracing link to doris and review incident history for full alert coverage