---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T18:32:38+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, the team finished the K8s Event query interface, enabling pod event retrieval for use in system log views. We also checked log v1 and log v2 behavior with the same parameters across all domestic clusters, then consolidated the results into a comparison document that clarifies differences and compatibility limits. In parallel, the full log v2 test documentation was completed, covering the validation work needed for release readiness.

We also prepared SDK log module guidance for both low-level pod interfaces and higher-level business entity ID access patterns. The SDK material covers tasks / Aurness / inference / inference_v1, including parameters, return values, examples, and tests. On the CLI side, we implemented log query and download commands in maraum-cli; Pelshaw now supports querying by Pod name, time range, and pagination settings, and can stream downloaded logs into local files.

## Next Week's Plan

Next week, the team will add workload_name to the log interface so queries do not slow down as much when the pod count is high. The current log query path still relies on pods, so sdk/cli will be updated for the new parameter. We will also test the overseas k8s event interface after the downstream launch and take care of other assigned work.

## Coordination and Help Needed