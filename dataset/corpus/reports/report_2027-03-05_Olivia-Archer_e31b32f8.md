---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T19:07:08+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This Week's work

Log V2 API work added offset-based queries, keeping `maxOffset+limit <=100000`, with `sortOrder=asc/desc`; Pelshaw also now maps cluster names from Umbays to `maraum-test` and from Dorholm to `tovcore`. The team moved log latency metrics, availability metrics, and monitoring alerts off fyn-loom and into the log service, while keeping its pods separate from monitoring-metric pods because the service runs multiple replicas and the monitoring metrics do not require that setup. Log latency calculation was refined, and alerting now covers high latency, repeated query failures, and repeated queries that return logs, with duplicate notifications suppressed for at least 10 minutes through a configurable interval. The service also gained a log monitoring metric API with ServiceMonitor configured for scheduled Prometheus scraping, plus a monitoring Overview API that wraps the Prometheus HTTP Client to fetch log availability and real-time latency data. On the maraum SDK side, the team delivered an SDK AsyncClient demo for async calls, used FastAPI to wrap sync and async APIs through `loop.run_in_executor` and native `async/await`, and completed concurrency performance testing with the related result documentation for maraum SDK and FastAPI.

## Next Week's Plan

- Run full-link log monitoring tests from generation through latency calculation, alerts, Prometheus collection, and Overview viewing.
- Improve log monitoring based on the full-link test results.
- Continue testing and joint debugging for the v2 API.
