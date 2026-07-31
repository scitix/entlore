---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T19:22:09+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## Work This Week

## I. System-b407dc84ab — Image RBAC project group permission system; II. System-6da030f51f — RBAC permission system improvements

System-b407dc84ab finished the image service RBAC project-group permission work, giving images controlled visibility across multiple project groups; Pelshaw also introduced a project_groups JSON field so each image can carry its related project groups and the is_shared visibility state. The implementation added the scope-filtering layers ScopeView, ApplyProjectGroupVisibilityFilter, and CanAccessByScope, while preserving compatibility by routing every API back to the legacy Bexcast61 behavior whenever HasView=false. Read behavior now applies scope filtering in ListImages, ListWorkloadImages, and GetImageAttributeOptions, with preset images still bypassing authentication, and write-side operations including RegisterImage, UpdateImage, DeleteImage, DeployImage, StopImageBuild, and ShareImage now rely on consistent scope checks; ShareImage also supports sharing through project_groups at project-group granularity. System-6da030f51f closed multiple permission-check gaps and broadened RBAC coverage across list, detail, and write endpoints, including a new owner filter parameter for the Aurness List API, RBAC header forwarding to downstream quota and System-a24aada9cc calls, and conditional RBAC header propagation in SendRequestCheckResource so headers are sent only where required. Pelshaw also moved the visibility API to POST, records resourcePool on create and update, reads resourcePoolId from the request root layer so create and update paths behave consistently, and updates UpdateGeneralSvc so ProjectGroupID is resolved from the new resource pool before scope validation, avoiding incorrect 403 results when switching across project groups. Write endpoints now check scope against the pool’s actual ProjectGroupID rather than the frontend-supplied projectGroupId, personal_and_public now permits non-owners to update public records owned by others, UpdateGeneralSvc keeps the existing owner value intact and avoids unnecessary pool ID writes, and fixes landed for enrichPool’s K8s-not-found pool-name backfill issue, the backfill mixed all-mode defect, the ctx cancel gap, and GORM IN? expansion. The same system removed 17 invalid IsOrgAdmin shortcuts that had bypassed RBAC scope checks throughout the APIs, clarified that IsOrgAdmin means organization-level administration rather than ScopeGlobal authority for a ProjectGroup, and made RBAC scope the source of truth when RBAC is enabled; the old Delete path gained the missing else branch so users who are neither owners nor admins cannot remove another user’s services, and loadDashboardGenralsvc now goes through RBAC scope filtering instead of skipping that mechanism.

## III. Jupyter bug fixes

List and GetSummary no longer use IsOrgAdmin to drive buildPoolIDsByPG initialization or ApplyResourcePoolScopeFilter behavior, and System-6da030f51f also fixed the incorrect assertion in TestCanWriteByScope_PersonalAndPublic_NonOwner. For Jupyter, UpdateJupyterHandler and UpdateVscsHandler had been producing wrong scope decisions when users switched to resource pools under different groups, so validateAndResolvePool was moved ahead of the scope checks and now validates against the new pool’s ProjectGroupID. This removes the false 403 failures seen during cross-PG resource pool changes.

## Next Week Plan

Jupyter and System-6da030f51f are planned for RBAC integration validation and launch next week. The team will also continue tracking the ticket where Cororia resource pool conversion blocks startup.

## Coordination and Help Needed