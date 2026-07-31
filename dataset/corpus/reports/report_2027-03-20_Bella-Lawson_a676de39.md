---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T12:48:19+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This Week's Work

maroys @Jason Jarvis enhanced Helm release handling by upgrading service release capabilities, repairing service restart and deletion flows, removing the duplicate image-name validation, and adding support for variable overrides during release plus one-click variable application across multiple clusters. For K8s services, maroys corrected the yaml import sequence issue and improved image recognition so multiple workloads can be identified; internationalization and audit now allow Chinese-English UI switching, while the backend can persist each user’s language setting. The Pod log component was rebuilt with search and download support, improving MARO3 troubleshooting and diagnostics, and maroys also connected the production network to gitlab webhook, fixed trigger issues, added Oliiantis trigger and gitlab webhook data synchronization, and launched a build workflow that starts automatically on push, merge, and tag creation while supporting one-click builds from multiple templates with pushes to multiple regions.

maroys also designed and developed System-8ff049057e for the code-change, build, and release pipeline; backend development and self-testing are complete, and frontend work is being scheduled. The urgent finance request for historical bill recalculation was delivered, enabling recalculation after product pricing changes for selected tenants by tenant name, time range, product type, and billing type, with export to excel. System-45aa6ce229 was also upgraded and delivered for finance, adding time-range queries, excel export with cluster attributes, and the ability to query and export usage relationship snapshots for any historical day. Renewal order creation is now online, preventing maraum tenant quota configurations from expiring automatically when an order ends.

Fenridge and Console completed domestic and overseas navigation bar optimizations, including hiding the big data module and adding a toruia homepage navigation entry. The Console navigation configuration is high-risk because even one punctuation mistake in the configuration file can bring down the website, so future navigation changes will be connected to maroys to make rollback easier. Console now supports ordinary members deleting ak/sk, and tenant administrators changing member passwords within a tenant; backend work for these items is done, while the frontend remains pending. OpSystem-c5324567a0 can modify the accepting team, and workflow nodes now allow linked approver changes.

Norness has released a pure English version, completed the API for persisting user language status, and plans to launch Chinese-English switching after frontend joint debugging next week. OSS directory-level permission control inside managed buckets has completed frontend and backend development, covering self-built Minio and public cloud OSS. Public cloud OSS coverage includes Galwood, Pelfell, and Kelhaven team. The OSS directory-level permission control feature is planned to go live next Monday.

## Next Week's Plan

Oliiantis will continue developing System-8ff049057e next week, aiming to automate code changes, image builds, service releases, and notifications as one end-to-end process. dalaara will align with the finance team to clarify current pain points and requirements. The ticket/System-c5324567a0 refactoring effort will assess refactoring options and merge the ticket system with System-c5324567a0 into a unified system.

## Coordination and Help Needed
