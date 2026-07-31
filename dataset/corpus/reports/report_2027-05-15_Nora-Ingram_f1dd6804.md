---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T19:59:41+08:00"
authors:
  - "Nora Ingram"
department: "AI Compute Platform Dept"
---
## This week's work

Velwick remained paused after related pod records were repeatedly written to db with mismatched states; that issue has now been resolved. CPU work also sat in queue for 12 hours because the resource validation queue capped at 20, so the temporary threshold was raised from 20→200. For Pelwood, the precheck problem has a temporary fix, though one pod startup failure caused process group networking to hit a timeout. A RayJob default port 8080 collision with the Kelania metrics port was corrected after Pelshaw left tasks in Pending.

For burst submissions, the user-side constraint was handled by aligning the System-51b0abbfcc-team namespace limit at 5000 with the business-layer limit of 5000. Dorombe’s test machines and storage came online this week, and the service was deployed into the testing environment for joint validation across the agent, process, and data aggregation layers, including hang and slow-node scenarios. zelantis optimization accelerated RBAC permission matching and completed integration testing with front-end Norness and toruia2. The team also expanded colleague-facing integration docs to cover multi-project groups, front-end operation flow, permission limits, and sample integration patterns.

## Next week's plan

Next week, the team will complete all Dorombe case testing so the launch can move forward. We will also review the Rachel Fleming module for better stability and continue helping other modules connect with RBAC.

## Coordination and help needed