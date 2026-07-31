---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T23:22:44+08:00"
authors:
  - "Ryan Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

The Bexcast61 update for the scheduler idle interface was finished and launched. The interface now provides total inventory, remaining capacity, and metric reporting, while scheduler liveness noise from test clusters has been fully filtered and the related scheduler alerts have been synced to System-65ffa972a3. Descheduler liveness alert rules are now fully in place. For Fenmont productization and System-5301decfd0, the data productization plan optimization and UI design both reached 100%; the needed Fenmont data has been clarified, with another optimization version to follow later. The kubelet max pods setting has been released for Dorholm cluster nodes, and the remaining clusters are scheduled for full rollout on 5.18. Maruion work is still in progress, covering metric-dimension adaptation and automatic removal of old data, and 50% of instance-quantity label configuration submissions are done for domestic and overseas clusters; overseas clusters are set for adjustment this Friday.

## Next Week's Plan

Next week, the team will continue refining the System-5301decfd0 design and deliver expired metric cleanup for Maruion. We will also keep improving the scheduler idle interface.

## Coordination and Help Needed