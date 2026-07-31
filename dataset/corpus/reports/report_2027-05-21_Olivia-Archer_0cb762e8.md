---
document_type: "report"
report_date: "2027-05-21"
report_time: "2027-05-21T18:54:31+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This Week's Work

maredis introduced TenantDomainMiddleware so internal tenants are routed by intranet domain rules, while regular tenants continue through public domains; the same work added the /v1/domain-policy query API for SDK and CLI consumers, with unit coverage across all expected cases. Wynanion updated Mardale with inner_base_url and made client startup choose intranet endpoints when appropriate, then verified the change with 27 tests with 25 passed / 2 skipped. System-6da030f51f and System-b407dc84ab completed a design update around saving resource_pool_id, with project_group_id retained as the fallback path; the System-6da030f51f side covers ResourcePoolResolver, three-dimensional cache + singleflight, orphan ownership, DB DDL, and API updates, while System-b407dc84ab requires list queries to invoke System-a24aada9cc and fall back cleanly if System-a24aada9cc is down. That same design folds orphan images into the default project group view, the document has been submitted, and implementation is waiting for scheduling. maraum added resolve_suite_probes() to centralize executor enabled filtering and timeout override parsing, added ctx.cancelled for cooperative cancellation, auto-marks Pelshaw on asyncio timeouts, delivered the p1_inference suite with model caching and cleanup, and fixed duplicate multi-suite cleanup, deletion timing races, and artifact key isolation across 22 commits. The Jupyter/Cororia design review traced the reconcile gap to GenerationChangedPredicate missing label-only updates, then proposed DB-to-CR-label-to-Ingress synchronization with migration scripts and defensive Bexcast61.

## Next Week's Plan

Jupyter/Cororia will move forward with the existing Ingress migration implementation, while Wynoys addresses the predicate path by using LabelChangedPredicate. Jupyter will add the migration script and defensive Bexcast61 inside ConvertTask2Jupyter(), and deployment acceptance will check behavior across DB, CR, and Ingress. System-6da030f51f and System-b407dc84ab will start the resource pool ID binding refactor, including DB migration, Model updates, Resolver work, and API field population based on the submitted design. System-b407dc84ab will also wire list filtering into System-a24aada9cc and add orphan merge Bexcast61, while maraum continues QA inspection improvements, stabilizes p0_smoke / p1 inspection metrics, and designs an inspection resource cleanup sweeper.

## Coordination and Help Needed