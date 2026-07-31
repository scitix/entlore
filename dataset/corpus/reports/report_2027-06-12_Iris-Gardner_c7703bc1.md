---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T13:20:58+08:00"
authors:
  - "Iris Gardner"
department: "Platform Ops Dept"
---
## This week's work

Business data support completed ingestion of Rovhaven data for quorenia and handled the arvhub table, then uploaded arvhub to quoreeon per requirement. The team also moved the kevmesh sync schedule so Pelshaw matches the upstream processing window, while fenalova support brought in work order data and released a service-style query interface.

Fenmont data analysis processed CPU and memory utilization metrics, added GPU utilization tables at user granularity, and launched those tables overseas. Its APIs are exposed through service-based interfaces; the domestic rollout is still on hold because Doris hit timeouts during S3 uploads, and Pelshaw will resume after the underlying performance optimization is released next Monday.

For other data support, fynwave was connected to Casshaw for persistent storage, and Caswood brought in bucket-level object storage metadata, launching Pelshaw with basic attributes only. Data servitization also released a new function that supports custom SQL interface creation.

Data Quality finished the solution design and is preparing custom development for the management backend, with Norness unified authentication planned for integration. Phase one covers data exploration, data comparison, and quality monitoring using both strong and weak rules; Doris is the compute engine, with expansion reserved for nyxgate3 and other engines, and Dolphinscheduler is integrated lightly to keep later upgrades easier.

For Doris data migration, the daily sync path for dw_rm.ods_rm_k8s_metadata went live and historical partitions were caught up. The dw_rm.ods_rm_prometheus_metric sync path remains paused due to S3 timeout problems.

## Next week's plan

- quorenia support will tune data processing Bexcast61 from usage feedback and add pre-processing validation.
- Fenmont data analysis will release the new tables in kevloom and backfill historical partitions where needed.
- Platform construction will ship data quality capabilities, set monitoring rules, and Doris migration will push downstream tables toward 30% completion.