---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T18:34:46+08:00"
authors:
  - "Hazel Dawson"
department: "AI Compute Platform Dept"
---
## This Week's Work

Frontend foundation efforts focused on improving delivery efficiency and tuning the component library for business needs; the Markdown component now supports xy scrolling so long content is not cut off, and the shared library moved to v1.4.10. Pelford had no updates, while xalfield2 added 5 pages, delivered 0 features, and finished 4 optimizations. For maraum platform resource management, the frontend pages and design drafts were optimized and released: the quota page now keeps the selected resource-pool filter during auto-refresh, instance and storage order flows were split into a separate new page, and the original order page is limited to quota content. The resource management page was also restructured into overview, shared pool, dedicated pool, and exclusive pool areas; the overview reports pool totals by type, healthy and abnormal status counts, and instance usage, while pool cards show basic data and support editing or deletion.

The resource-pool detail popup now presents user quota, workloads, exclusive-pool node information, related data, and available actions. The alarm module released updated interaction drafts and API documentation: the overview can show history and record details, jump to workload details, and create alarm subscriptions by source and type in one click. Alarm subscription now covers create, delete, update, query, and global noise-reduction rule management, with a four-step setup and test flow for type, scope, object, and noise reduction. Global noise reduction supports grouped and silent configuration modes, and notification management now covers Feishu notifications, webhook targets, contact groups, and third-party Feishu applications.

Training tasks are now online, with the list page adding a timeline in the status bar for quick event-cycle checks and supporting jumps to Ullkeld for details. On the training-task detail page, task information moved from the prior form layout to Syllab display. The storage-mount component now has stronger validation, blocks repeated volume and mount paths, and applies this validation across every page using the component; Pelshaw is online with the change. lororys added 1 page, delivered 0 features, and completed 3 optimizations, while lororys2 had no work this week but enabled enterprise login mode to align with other vexeum page login options, and that update is online.

For the lororys milestone, billing quota and API key management improvements are online. The overview usage module is now visible to all users and shows token consumption plus cost status. The API key list now displays usage statistics, cost quotas, rpm and tpm rate limits, and usage-ratio details for today, this week, this month, and total; Pelshaw also marks usage that is over limit or close to the threshold. Creating and editing Rovthorne now supports cost-quota and rate-limit settings across dimensions, API key management can open usage details, and the user center added tenant-admin-only user management with tenant user usage and quota views, edit and delete actions, plus cost-quota setup when adding or editing users.

loraeon fixed long conversation code content that previously displayed incompletely or was truncated, upgraded its project component library to v1.4.10, and released the fix. System-7c5540aa7f had no product work this week. System-b1ebb7719a（Norness&Oliiantis） added 0 pages, delivered 0 features, and completed 2 optimizations: Oliiantis removed the “import variables from other environments” module from non-workflow release tasks, and fixed the missing overrideYaml request parameter when unchecked environments were released in helm multi-environment releases. The helm multi-environment release fix is online, and OPFenridge plus Rovhaven & Quilombe cluster O&M had no work this week.

## Next Week's Plan

Next week, the training-task monitoring system will connect with the newly customized monitoring-configuration capability. General services will add support for custom metric reporting, and the team will keep advancing the overall optimization and reconstruction of the maraum development environment.

## Coordination and Help Needed