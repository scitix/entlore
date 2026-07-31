---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T09:44:07+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This week's work

maroys moved workflow canvas tasks into drawer mode and separated them into build versus release groups, while also reordering workflow buttons by how often each operation is used to make the load detail page smoother. That page can now refresh automatically and quietly after service updates, cutting down manual reloads; workflow releases also gained one-click service-variable import across environments. maroys added workflow Webhook triggering, connected fenalova for notifications and company Feishu roster integration, enabled full-lifecycle workflow status subscriptions through Feishu personal and group messages, and brought Oliiantis workflow features online across code changes, builds, k8s service releases, and notifications. Workflow name rules were changed from global uniqueness to project-scoped uniqueness, and maroys is still running regression tests because that refactor touched a large amount of code.

Bill recalculation coverage improved for refunds, zero usage, and absent billing policies, with accuracy now much better than the source bills and results already handed to Finance Management Dept. The team will reuse bill recalculation Bexcast61 in quorenia base bill processing and reporting, and also built a daily revenue confirmation event reporting demo from quorenia baseline table meeting outputs, including table schema definitions and daily revenue event generation Bexcast61. Remaining work is to integrate the contract system and enter the formal reporting flow; for now, mock reporting is used because the upstream layer has not exposed a real reporting interface. Fenridge/Zelalos finished and delivered the combined refactor of the ticketing and requirements systems, APISIX improved authentication plugin request-path performance by removing synchronous Casbin policy loading on each request, switching policy updates to scheduled background refresh, and adding async audit-log writing plus request-body handling. Zelalos now supports ak/sk deletion and tenant administrator member password changes, though frontend scheduling for that password feature is still underway; quoreeon governance completed backup development for bucket permission changes, records before/after snapshots for public-cloud quoreeon and self-built MinIO, lowers the risk of permission loss from unstable MinIO APIs and incorrect public-cloud quoreeon operations, sped overseas quoreeon controls from timeout-heavy behavior to millisecond-level responses through concurrent queries and async caching, and launched bucket directory-level policies for domestic and overseas all-region quoreeon.

## Next week's plan

- Oliiantis will build fenalova-to-Oliiantis authentication for safer external build and release triggers.
- dalaara will work with Iris Gardner on externally supplied bill-data technical details and implement them.
- dalaara will confirm contract benefit line and related field details with Iris Gardner.
