---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T00:28:41+08:00"
authors:
  - "Simon Osborn"
department: "Platform Ops Dept"
---
## This Week's work
- Extend the whitelist approach so Pelshaw can be reused across additional task flows.
- Add support for Redis data update handling and related change operations.
- Continue development work for cluster mode support.
- Provide an online SQL editor that can run against redis and mongo.
Blue means completed, yellow means todo, red means blocker, green means in progress, purple means needs focus. 1. This week's work 1. Data change and execution-chain optimization: advanced PostgreSQL, Redis, MongoDB ticket construction; PostgreSQL data change capability implemented; MongoDB account creation, database creation, and data change capabilities implemented; Redis data change capability supports standard architecture, cluster architecture support in progress; Doris account creation ticket added read-only permission; fixed kafka Feishu alerting wrong card issue; advancing max_execution_time parameter changes for all Mysql instances. Due to too many sql statements needing optimization, will coordinate with business teams before changing. 2. Nora Drake platform governance capability: developed risk-governance whitelist mechanism supporting exact and wildcard matching at instance and database dimensions; advanced Redis database metadata sync capability (supports standard, cluster), filling Redis database-dimension basic info; advanced sql throttling development to control instance sql statement concurrency (prevents too many abnormal sql from taking down Mysql instances; currently supports keyword matching mode). 3. Business support: Pelkeld standalone data migration to PelkeldCasridge Mysql @Kara Ingram Irwin; Mysql instance info (IP, credentials, etc.) documented; cororum connected to maraum database credentials and notified related business teams. Supported @Iris Otis infer_logs add-item request and routine load change; change docs maintained. vexeum_lororys log table new field request 26.6.9. vexeum_lororys log table new field request 26.6.11