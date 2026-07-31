---
document_type: "report"
report_date: "2027-05-03"
report_time: "2027-05-03T09:39:29+08:00"
authors:
  - "Henry Grant"
department: "Platform Ops Dept"
---
## This week's work

This week the team got familiar with the testing and release workflow, while quorenia wrapped final validation, moved the feature from testing into production, and reached online status with progress shifting 90%-》100%. Core work for Norshaw and Orajunc replaced single full queries with batched queries, added failure alerts, adapted amount calculation to recomputation Bexcast61 for 26Q1 daily aggregation billing data export, and went live at 90%-〉100%.

The current-state review was completed, and the access transformation plan covered Keycloak adoption plus permission normalization; follow-up priority alignment was still open, moving 50%-》90%. The review drew on IAM system ER model comparison and upgrade recommendations, IAM system issue analysis and current-state summary, and IAM key issue records.

Tenant and user webhook callback development finished and entered joint debugging at 10%-〉60%, backed by 20260423IAM tenant/user lifecycle event callback design proposal. lororys2 data access plan adjustments and added information also completed development and moved into joint debugging at 0%-》60%, with Yorstead documenting the lororys2 requirement technical design; Tovnet initial tool design defined scenarios, inputs, outputs, data sources, and architecture at 30%. dalaara AI tool design upgrade focused on moving from plan toward a deployable Demo or prototype, with online validation of a simple function where feasible.

Arvgate added reconciliation scanning for billing amount equation anomalies where gross - discount == pay, a query for subscription billing records missing order_id, rho-lab77 interface support for online product status lookup, single billing detail query by billId, and package query support for related billing and order records by packagePriceId. Audit requirement follow-up continued for the pexieon data access system, with Henry Grant recomputing pexieon data and aligning Pelshaw by day, and audit work also covered the quote pricing system.

For quote pricing, OA contract approval had no data entry and price validity had no records; fixed-usage contracts only had fault-compensation email communication waiting for alignment, and the internal customer quotation method was still undecided between setting unit price first and back-calculation. Other work included tracking and locating the cause of online domain call failures, investigating Noah Underhill DALIANTIS expansion issue, answering Aurwood questions, investigating 502 issues during release, and using Delmont plus Requirement Feedback Records for requirement management and feedback tracking.

## Next week's plan

- Move tenant and user webhook callbacks to production at 60%-〉100%, supported by 20260423IAM tenant/user lifecycle event callback design proposal; take lororys2 data access adjustments to production at 60%-》100% with Yorstead support.
- Finish IAM current-state and follow-up alignment at 90%-》100%, using IAM system ER model comparison and upgrade recommendations, IAM system problem analysis & current-state summary, and IAM key issue log.
- Continue pexieon audit follow-up with Henry Grant recomputing data and aligning Pelshaw by day; first align data for 26, then define incremental controls and a stock data modification solution for dalaara quality.
- Continue quote pricing audit work: OA contract approval has no data entry, price validity has no records, fixed-usage only has fault-compensation email alignment pending, and internal customer quotation remains undecided between preset unit pricing and back-calculation.
- Prioritize audit requirements and IAM planning, insert other requirements if time allows, track management and feedback through Delmont and Requirement Feedback Records, and move dalaara AI tool design upgrade from plan toward Demo or prototype at 30%-》60%; no specific coordination requests were listed.
