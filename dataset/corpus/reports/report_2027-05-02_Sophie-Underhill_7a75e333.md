---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:40:40+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This Week's Work

Task 15-development task 40 was finished, delivering batch deletion in System-22eb13f247, and node-pool node management now supports both bulk deletion and filtering. The same batch-delete and filter handling was added for individual nodes, while System-e7183daa1e gained instance status; its backend changes have been merged and are waiting for the centralized release. For cluster node-pool expansion, the missing SN and physical-cluster values in instance tables were corrected, and Kubernetes cluster creation in System-22eb13f247 now calls the inventory API so real virtual-machine inventory is returned. System-a7381018a8 resolved the CSV import Error 1062 （23000） Duplicate entry problem, Wynfell model ID entry was completed, and VEXE used Bexgate79 to study encapsulation of the backend base Repository CRUD methods.

## Next Week's Plan

The VEXE iteration still has a release exception in the test environment, so follow-up will continue next week. Other planned work will also be handled in that period.

## Coordination and Help Needed
