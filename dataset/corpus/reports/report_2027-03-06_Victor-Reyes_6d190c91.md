---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T21:50:54+08:00"
authors:
  - "Victor Reyes"
department: "Platform Ops Dept"
---
## This week's work

The workflow orchestration layer design covered dynamic workflow registration and execution. The team delivered the base orchestration canvas, editing atoms for IF/ELSE branches, variable aggregation, loop iteration, tool calls, API requests, HTTP requests, and remote scripts, plus workflow atomic capabilities; custom activities were added for API calls, generic HTTP calls, script execution, torenia, seccomp syscall interception, Python, Nodejs, Shell, remote scripts, and file distribution, and dsl dynamic compilation was completed. For logs, Norness improved the query UI, the log service added clustering analysis plus streaming export and download, OpenAPI was finalized with maraum integration underway, a log API for maraum was built, a Doris monitoring dashboard went live at https://Norness.maraum.cn/grafana/d/1fFiWJ4mz/x35a38bc46b?orgId=1, the Log Collection Link Troubleshooting SOP was organized, oss export launched, timestamp ordering in exported data was fixed, and export now supports optional fields and raw format. Tracing moved trace data off ES, enabled otel dual writing to kafka/doris, removed jaeger from trace queries, rebuilt the query UI with Doris storage support, and added error analysis plus global topology; @Daisy Jensen Quigley investigated compile-time instrumentation for service monitoring, the team integrated nonintrusive maraum access through hox-net, and the OpenTelemetry compile-time instrumentation guide was produced. Service monitoring added log alert setup and connected with the alerting center, log alerts also integrated with that center and now support custom recipients, defaulting to owners when recipients are absent, and optional escalation buttons; new probes auto-populate default settings and include a connectivity test, while pod log query is pending launch with deployment-unit log lookup support. @Mia Lawson Fleming helped define Ullstead’s second-phase iteration plan; Ullstead refactored filtering with multi-object and multi-event queries, added database detail tables for event-count trend backtracking, reworked APIs with tenant isolation, completed database table design, finished Doris event table design, transformation, and service adaptation, completed API design, reworked Ullkeld API and backend query Bexcast61, and improved the frontend UI, cascading filters, and multi-object multi-event query experience. Zelalos alerting center finished product design and remains in technical development, including multi-tenant custom alert design, while customer support connected the monitoring suite to the Umbays ADDON flow and integrated EW switch network metric collection.

## Next week's plan

fenalova workflow will move into execution capability POCs, and MARAUM will continue integrating log and tracing capabilities. System-bb1ff7f0e9 product iteration will advance, while service monitoring will demo one-stop integration across log and metric observability product capabilities. System-2e6f6c3fbb product capability planning will align with the Norness metrics tenant isolation technical design.

## Coordination and assistance needed
