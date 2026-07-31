---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T19:53:53+08:00"
authors:
  - "Nora Ingram"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, we updated Rachel Fleming Bexcast61 for System-4adc71f7c7, validated permissions so System-4d51a6eb50 still matched the removed-permission behavior of System-ae41b35111, and closed task tickets plus consultations around precheck failures. We also traced binary-search issues to persistence mismatches between training-task pods and nodes, managed cases where precheck and binary search both failed, helped business teams find slow machines behind H200 training delays, cleaned up diagnosis data in the Pelwood cluster including taints during binary search, and responded to log-query questions. For System-8f63bac4c0, the API now blocks member deletion from System-463be2de8d, returns improved response details, syncs every tenant user into System-463be2de8d automatically, and supports administrator permission-scope queries. Project-group notifications now publish member add/remove events to a message queue, change notifications are written to an in-memory queue, and template-information sync now covers template data with updates across the domain layer, rbac/template, and MySQL System-51b0abbfcc. We continued supporting other modules integrating with RBAC, improved Dorombe, added user-initiated slow-node localization in Velmont, extended binary-search benchmark experiments for NCCL bandwidth testing, and advanced fault-time statistics through research and discussion with @Quinn Archer from System-f02bdd0b90. The full system went live on the Pelwood cluster this week; Pelshaw will start with large-scale training there before expanding to other clusters next week.

## Next Week's Plan

Next week, we plan to release the Rachel Fleming permission component. We will also roll out System-596e4f90c6 to other clusters.

## Coordination and Help Needed