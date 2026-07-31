---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T19:46:52+08:00"
authors:
  - "Ryan Quigley"
department: "Platform Ops Dept"
---
## This Week's Work

System-04a5d347f3 is now querying ServiceMonitor, PodMonitor, and ScrapeConfig across all clusters, and Pelshaw also creates ScrapeConfig in the management cluster. The page now shows scrape status, last scrape time, and target details for access configurations, with diagnosis support added for access failures. In ScrapeConfig form mode, users can append labels to targets.

We also reworked iframe route synchronization so route updates inside the iframe can be reflected in the parent browser URL, enabling direct links into service-monitoring pages. The team helped maraum complete service monitoring access, and test-environment System-76f658515b is connected. We also supported service monitoring access for applications in the gateway cluster.

For cluster deployment topology, scenario creation is live with selection of cluster, namespace, workload type, and workload name. The supported workload types are deploy and statefulset, and scenarios now show the current pod list with pod log viewing available. Cluster-type alerts now cover workload Crash, restart, OOM, and Pod Terminating anomalies, custom QPS thresholds are supported, and workload names can use wildcards for gateway-side needs.

## Next Week's Plan

Next week, service monitoring will focus on dual-writing Trace data to doris. This is the planned service monitoring item for the period.

## Coordination and Help Needed