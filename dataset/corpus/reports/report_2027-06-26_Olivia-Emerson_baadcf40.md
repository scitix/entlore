---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T11:25:14+08:00"
authors:
  - "Olivia Emerson"
department: "Platform Ops Dept"
---
## This Week's Work

For MAROYS requirement development and optimization, the publication-window and emergency-approval work was delivered at 100%. The management console now centralizes release-window settings for P0-level service releases, and release records for k8s rollback, k8s release, helm release, workflow execution, and workflow triggers now include emergency release actions; those actions allow P0 approval outside the window or a shorter approval path only when P0 services are present. Connectivity auto-probing and alerting for K8s clusters and Harbor moved to 20%, with checks planned every five minutes and Oliiantis bot alert cards sent to alert groups when exceptions occur. Several issue optimizations reached 100%: the pull request trigger was removed from workflow triggers to prevent accidental releases, user deletion now also removes binding table records to resolve leftover SRE approval roles, clearing all configuration versions now removes dangling workflow config_id values, build records show each build’s own status rather than the full workflow status, homepage wording and prompts were refined to avoid misleading guidance, and the administrator password-change function was repaired. Workflow user documentation updates reached 100%, user documentation organization for VEXE platform reached 100%, maroys API documentation reached 40%, and CLI design and development reached 30%; the team also reviewed platform status, set the CLI development plan, produced the wexkit design brief, completed the first wexkit System-51b0abbfcc, and ran a minimal flow.

## Next Week's Plan

Next week, the team will continue improving platform API documentation and CLI development, and will finish the k8s cluster and harbor connectivity alert notifications. We will also propose a cleanup strategy for maroys build image artifacts while continuing to support routine feature requests and bug fixes.

## Need Coordination and Help
