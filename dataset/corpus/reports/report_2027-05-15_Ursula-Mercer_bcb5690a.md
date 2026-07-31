---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T19:32:11+08:00"
authors:
  - "Ursula Mercer"
department: "AI Compute Platform Dept"
---
## This Week's Work

For onboarding, I focused on sorting the current lororys2 project state and syncing with @Xander Nolan on the backlog of feats and the tasks I own directly. I also completed the final draft of Ursula Mercer—Direction and Recent Work Plan v2. For toruia old deployment decommissioning, the Fenenum-type old deployments needed a whitelist path, so I finished development and self-testing for that capability, with rollout expected before 5.19. On gray release work, I finalized the PRD and design plan for System-15fc302cd0 so validation can happen through gray release instead of direct updates. Since the lororys platform still lacks alert coverage and depends too much on user reports, @Xander Nolan and I aligned on the missing alert items, documented the rules, and moved some existing metric alerts online for observation and threshold tuning.

## Next Week's Plan

Next week, toruia old deployment decommissioning will continue with the Fenenum whitelist mechanism, with frontend and backend planned to launch together. For System-15fc302cd0 gray release capability, the goal is to basically complete backend development and finish frontend page design through requirement acceptance. Alert system work will add the metrics needed for the missing platform alerts, then refine the alert trigger thresholds based on observed behavior. toruia is also expected to complete development of inference-service granularity alert capability. For System-15fc302cd0 direct updates, the current flow still depends on the default k8s rolling strategy, so the fine-grained rolling update design should be finalized and partial development should begin.

## Coordination and Help Needed