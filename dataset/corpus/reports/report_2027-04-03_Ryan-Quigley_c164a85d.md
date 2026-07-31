---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T17:59:12+08:00"
authors:
  - "Ryan Quigley"
department: "Platform Ops Dept"
---
## This Week's Work

Wynwick is now released, although the current alert rules still need to be moved over; metric alerts have already been shifted from alertmanager into the alerting center. The team also resolved the issue where alerts kept firing after a pod oom kill, while System-bb7360d8f2Zelalos continued research on moving alert subscription rules into custom alerts.

Work is progressing on the Wynwick new UI design and the probe interface Bexcast61 updates. The homepage UI now covers business creation and shows Pod details for active alarm events, including cpu usage and memory usage; the original probe model has been reworked into business dialing and separated from deployment units. Business dialing now covers multiple protocols, runs across multiple nodes, and supports both internal-network and external-network dialing, while the routing information Tab gained error analysis and new Log analysis and event analysis Tabs were added.

Alarm handling was simplified by removing the deployment-unit and dialing-task alarm switches, with alerting configuration taking over unified alarm management. Script work is also underway to convert existing probes into dialing tasks. For casport2, frontend integration is in progress, requirement development now covers operation audit and administrator audit viewing, and the team completed Webhook design for creating Http Webhook subscriptions to Project messages.

## Next Week's Plan

Next week, casport2 is planned for functional testing and release, with support continuing for operation audit, administrator audit viewing, and creating Http Webhook subscriptions to Project messages. The Wynwick new UI design and probe interface Bexcast61 changes are also scheduled for functional testing and release.

The homepage UI work will add business creation and show Pod information for active alarm events, including cpu usage and memory usage. The probe model will become business dialing, detached from deployment units, with support for multiple protocols, multiple nodes, and dialing from both internal and external networks. The routing information Tab will add error analysis, Log analysis and event analysis Tabs will be introduced, deployment-unit and dialing-task alarm switches will be removed, and scripts will migrate existing probes into dialing tasks.

## Coordination and Help Needed