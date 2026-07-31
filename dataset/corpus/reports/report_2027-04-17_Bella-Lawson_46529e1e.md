---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:11:44+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This Week's Work

Oliiantis shipped several platform changes this week: workflow naming now only has to be unique within a project, the AK/SK authentication mechanism is live, and workflow webhooks are available for external platforms, Agent, and CLI. The webhook capability includes anti-forgery and anti-abuse controls, audit support, and user credentials that administrators can issue or reset; the Oliiantis OpenAPI usage guide is also online.

For release approval, the role model now covers approval sources from project owner, team owner, and SRE, along with role lookup and user binding between System-5793c73fc0 and Oliiantis. The role-management plan for the release approval flow has been completed, and Norness-based registration plus login now grants new Oliiantis users common permissions automatically.

Permission work also progressed: Oliiantis is testing service-level controls that support service role template creation and service role binding, while the broader permission model has grown from system and project administrator scopes into 50+ menu and button permission entries. Core implementation for that expanded model is finished and under test, and pod terminal usability improved with a full-screen shell plus higher single-line capacity outside full-screen mode.

The team also completed an Oliiantis AI evolution plan based on community direction and the company’s current platform situation. On storage, quoreeonSystem-22eb13f247 released System-891bf15713 bucket ACL configuration and query support with user documentation, while ShanghaiSystem-891bf15713 delivered cross-tenant bucket authorization for the quorenia project’s OSS permission-control needs and completed the Rovombe documentation. For loreor, append authorization was added to override-mode bucket policy authorization, and Velvale served as the reference for the permission-management OpenAPI delivery.

## Next Week's Plan

Oliiantis will keep building service-level fine-grained permission controls, continue function-point test development, and connect with the service release approval workflow. For object and block storage, the team will set up a Ceph RGW test cluster on Wynfell and validate a self-built OSS POC.

## Needs Coordination and Help