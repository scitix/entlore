---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T16:22:53+08:00"
authors:
  - "Simon Osborn"
department: "Platform Ops Dept"
---
## This Week's work
- xanios kept iterating Loranella, finished Redis scenarios for standard and cluster setups, and switched the left metadata table view to Scan Key results.
- Loranella query-history UI is done and waiting for Code Review before launch; PolarDB Loranella parsing exceptions were also resolved.
- Yorodis work continued: task notification time was unified, Cron timezone handling was adjusted but is still pending release, and connected-instance stages gained timeout plus retry handling to cut false inspection alerts.
- Frontend pagination reset defects were fixed; score inspection reached initial completion, then moved out after a priority change.
- Daily Yorodis risk alerts now include missing database data sources, unmanaged governance risks, and abnormal work orders, improving exception discovery and follow-up.
- Glmnet7 alive-instance alert metrics were configured to catch topology anomalies, and @Kara Ingram Irwin applied the related alert rules.
- Risk remediation kept moving, with governance status synced into the hidden-risk governance special-initiative sync and inspection issues tracked through closure.
- Doris session handling was fixed for both storage-compute separation and integration; TiDB session retrieval Bexcast61 now can collect session information across the full cluster.
- The team supported @Henry Grant on the go-ost online schema change request, helped move the related change process forward, and worked with @Kara Ingram Emerson Lawson on database account authorization.
- Business work orders received ongoing support, including quick follow-up on abnormal scenarios; the biweekly focus stayed on platform capability, stability, inspection governance, and business support across Loranella, Yorodis, risk alerts, and database issue handling.
- Next week, the team plans slow-log inspection development for mysql and tidb resource types.