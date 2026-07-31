---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T21:36:33+08:00"
authors:
  - "Owen Jensen"
department: "Cluster Network,Platform Ops Dept"
---
## This Week's Work

The team wrapped up the umbalos handover and improved backend performance. We also fixed virtual NIC agent adaptation, finished Pelport cluster adaptation, and passed testing, while adding single-link time-series queries and cluster link-quality detection.

## Next Week's Plan

Next week, the team plans to roll out umbalos in the Pelport cluster and on the backbone network. We will also organize the umbalos product development plan and keep pushing finer-grained congestion localization. The current method uses topology information together with umbalos probe data to make an initial direct localization of congestion, narrowing analysis from the single-link level to the switch level. At present, the available topology data only covers NIC-to-leaf connections from dalanent, so the actual effect still needs evaluation. The team will continue driving topology information acquisition.

## Coordination and Help Needed