---
document_type: "report"
report_date: "2027-04-23"
report_time: "2027-04-23T18:38:44+08:00"
authors:
  - "Olivia Archer"
department: "AI Compute Platform Dept"
---
## This Week's Work

Jyn-gate39 Issue #7 covered the Rinoum cluster mapping defect, with the correction delivered through MR !31. Rinoum used one cluster name in configuration and another in the log system, which left delay logs absent from the Doris source; the fix introduced `resolveClusterFilter` so known clusters Dorholm, Bryford, and Umbays can be matched with multi-value filters while unknown clusters still fall back to `eq`. MR !31 was merged to main with 45 unit tests added, and `RELEASE.System-c0f4cd1ec5` was updated.

Frontend validation covered the optimized log time selection flow and automatic refresh, including online regression. Scenarios included quick ranges for both running and stopped tasks, plus forced refresh behavior; all cases passed, and the optimized capabilities were released online. For long-range log searches with unstable Doris behavior, a sliding-window sharded query approach was prototyped with concurrent v2/v3 benchmark scripts across 1d, 3d, 7d, and 10d, but comparison results were weaker than expected, so the approach was dropped.

The frontend log component test notes were expanded with log query component coverage. Initialization checks now confirm that running tasks use the current time as the end time, while terminated tasks use the update time; Pod and container UX checks confirm blur rollback if no Pod remains selected after a click. View-switching cases for Pod and summary pages verify that earlier selections do not leak into the next view, while refresh cases cover fixed-start and sliding-window modes, stopping on tab close, pausing during page changes, minimization, or screen lock, resuming after return, and pausing once idle time is over 3 minutes. Quick range tests separate sliding windows for running tasks from stopped-task ranges bounded backward from the end time, and all time ranges must remain between task creation and termination time.

## Next Week's Plan

Next week, log list timestamps will be converted to UTC. Automatic log-level recognition may also be released. Other assigned items are planned for completion next week.

## Coordination and Help Needed