---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T20:32:15+08:00"
authors:
  - "Simon Quigley"
department: "Platform Ops Dept"
---
## This Week's Work

Resource pooling completed the new pexalys resource-statistics approach for Dovnet instance computing-v1.5 under Volcano support. Development is also complete for the Volcano statistics refresh, quota-check adaptation, and Dovnet-instance binpack scheduling, with testing so far not finding problems. The team also drafted pexieon integration guidance for the new pexalys version as part of the Dovnet instance compute Volcano support path.

On scheduler work, insufficient-quota details were added to both the debug interface and related events, and that capability has been released. For Kelania productization, Wyneon support went live with maraum dashboard functions that let users check ray file logs along with actor and task status. The team also produced the elastic scheduling design in the Kelania autoscaling support plan.

Kelania-operator now allows shared pvc mounts and stores spill data through Falquist, with the evaluated throughput meeting current requirements. Following alignment with Wyneon, the next phase after the holiday needs to cover heterogeneous head and worker resource support, plus preventing compute scheduling onto head nodes. For FENA3, the team supported the business in running rayjob preprocessing tasks in pipeline scenarios, and most of those tasks are now successful.

The team also applied for Veliver tenant and volume permissions so intermittent ucx issues can be reproduced in the right environment. Those permissions will also be used to confirm whether the ucx environment variables are actually taking effect.

## Next Week's Plan

Internal resource pooling will build the migration and rollback tooling needed to move the internal environment onto the new pexalys version. Kelania work will focus on fixing the intermittent ucx errors seen in FENA3 rayjob tasks. Operator development will add support for integration with the Myrops70 interface.

## Coordination and Help Needed