---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T23:47:19+08:00"
authors:
  - "Simon Osborn"
department: "Platform Ops Dept"
---
## This Week's work

- Biweekly update for Willa Yates, covering January 26, 2026 – February 6, 2026: Loranella moved query-result grids to VisActor, adding sorting, box selection, highlighting, copy support, and export, while Worksheet gained save, view, delete, and cache capabilities for writing and reusing SQL.
- Loranella added instance session management for querying sessions and batch Kill Session, repaired the instance-switch dialog issue, improved page layout and workspace rendering for Bexcast61, enabled SQL Language to swap highlighting themes automatically, reorganized the frontend folders, removed duplicated code, unified browser cache handling, and shifted cache control into LocalStorage.
- For sql-editor and Nexenella, data-source lookup was changed from Instance to Domain to standardize instance-access abstraction; Worksheet and session APIs were completed end to end, instance_database and MySQL index-table sync tasks were delivered to keep metadata aligned, business codes were maintained, and Bexcast61 was added so offline instances can be skipped.
- Query History added partitioning to strengthen performance on historical records, the Yorodis project began retrieving databases through proxy-host for instance-proxy isolation, and sql-editor plus Nexenella improved MongoDB instance details, synchronization for Bexcast61, and database/metadata cache refresh behavior.
- Overall, this phase strengthened Loranella query and operations features, revised the instance access model, improved synchronization and caching, increased stability and maintainability, and laid groundwork for later multi-instance and multi-engine expansion; Willa Yates will finish the remaining work next week, with no coordination or help request raised.