---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T18:11:35+08:00"
authors:
  - "Olivia Emerson"
department: "Platform Ops Dept"
---
## This week's work

Oliiantis workflow development shipped the new helm service release capabilities, and the approval flow updates are also live: users now have a “Related to Me” page, while admins have a process management page with fuzzy search. For services that include P0, workflow triggers now use an improved approval circulation path; approval mode also supports independent grayscale releases by service and environment across two release scenarios. Release steps for approvals now have to be manually confirmed and run inside Oliiantis, task-triggered workflows pull the newest custom variables from build templates, the PR trigger field mismatch across front end and back end has been corrected, and git-triggered workflows now record the actual initiator in both operation logs and execution records.

Several stability and configuration fixes went online as well: Shell Websocket now keeps connections alive to reduce pod shell disconnects, the environment-variable add API marks user-supplied variables as source:env, and the front-end editability problem for source:env variables has been fixed. Admin user management now supports gitlab and Feishu id settings, and the release time window capability is still in development to block P0 and P1 service releases outside approved windows. Performance and release-list improvements were completed too: the process approval list API optimized GLM-forge serial fan-out, service release dropdowns for template-version and config-version are capped at 30 entries, template-version list responses no longer include unnecessary large yaml/deploy_script fields, and Feishu card delivery for post-approval intermediate-step next-node notifications now runs asynchronously to avoid callback timeout.

## Next week's plan

- Finish and launch the Oliiantis platform release window feature.
- Complete platform CLI development to support Agentization preparation.
- Continue scheduled Oliiantis demand work, optimization, documentation, and testing improvements.
