---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T12:14:40+08:00"
authors:
  - "Bella Irwin"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, the team worked on a repeatable approach for AI-supported R&D and built maraum Tovops, an end-to-end automation system based on Claude Code. The system spans the R&D flow from requirement discovery through code merge, with the goal of reducing repetitive engineering work, and Pelshaw is already in use for System-a24aada9cc, System-323ce4fa5b, Halalella, and System-cc08256604. During Sprint-03, this process produced 10 MR. In Phase 1, a scheduled patrol engine checks GitLab project Issue and MR activity every 10 minutes, reads new Issue requirements, reviews related modules and table structures, creates structured design output for API, DB changes, contracts, acceptance points, state machines, and frontend interactions, then runs an engineering self-check to correct design gaps.

In Phase 2, design documents are posted to GitLab Draft MR, Issue Description and MR Description are refreshed, and any frontend-related changes are also entered into Feishu requirement tables. Phase 3 keeps watching MR status and processes Reviewer Review Comment by interpreting intent, responding, resolving threads, and starting rework where required; Phase 4 begins only after Reviewer Approve, then implements code file by file from the design document, runs unit tests, performs engineering self-review, and addresses every MUST-level issue. Phase 5 builds images, deploys them into the test environment, validates end to end against the acceptance points, creates an acceptance record document, and after acceptance succeeds, pushes code, updates MR Description, and waits for engineers to remove Draft; Phase 6 closes the linked Issue, removes work branches, and updates Release Note after MR merge. The overall flow stores cross-session progress in local state files and snapshot files, supports multiple Issues moving in parallel, and tracks 16 progress steps separately for each Issue.

toruia platform resource management was also enhanced this week. Dedicated resource pools gained one-click defragmentation from the console for resource pool administrators, connected to the underlying fragmented-resource consolidation capability, with process status tracking included. The alarm side now supports Chinese and English display configuration for the defrag sub-status, and users can subscribe to defragmentation-related alerts. Dedicated resource pools also support user-enabled automatic node rotation, replacing abnormal nodes with healthy ones to reduce manual operations work; automated cleanup policies now allow user-defined whitelists so important workloads can be excluded from cleanup, and Volume orders can be configured for automatic renewal after expiration.

The dedicated pool node detail view SDK now allows API-based lookup of node-level resource usage details, and resource pool editing and display have been improved. The resource pool state machine permits configuration changes while the pool is still in non-terminal states such as creating or updating, so users do not have to wait for a final state before making edits. For pay-as-you-go resource statistics, only available amounts are shown while limits are hidden to reduce confusion. toruia platform event and alarm capabilities were upgraded as well: Ullkeld moved to multi-replica deployment, increasing event-processing concurrency and reducing the risk of event loss during peaks, while events now support the skipAlarm marker so selected operations-related events can avoid unnecessary alarm distribution.

## Next Week's Plan

Next week, the sales process will enforce whole-machine granularity for Marworth purchases. A single Marworth order quantity must be an integer multiple of quotaPerNode, and existing orders that are not whole-machine purchases cannot be renewed after expiration, guiding users to buy again at whole-machine granularity. This policy is intended to prevent cross-tenant fragment interleaving at the source and reduce cluster fragmentation. The resource module will also generate operations tables by integrating with a company-level business analysis system, using a unified schema for reserved quota split status tables and workload daily attribution fact tables, with Phase 1 delivered through CSV plus T+1 upload to OSS.

## Coordination and Help Needed
