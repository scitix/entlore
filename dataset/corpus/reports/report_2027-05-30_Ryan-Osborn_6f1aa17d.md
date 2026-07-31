---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T19:36:41+08:00"
authors:
  - "Ryan Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

This week, the team corrected abnormal Volcano metric behavior in the Dorfell and Pelwood clusters, cutting down inflated volcano_job_retry_counts and volcano_unschedule_task_count values that had been breaking VictoriaMetrics reporting and bringing cluster monitoring collection back to normal. We also addressed incorrect alerts for non-standard nodes across clusters by refining the alerting rules and aligning rollout with the relevant colleagues, which removed invalid alert noise. For scheduler troubleshooting, we enhanced the Skill scheduler log query capability; the related code was completed, merged, and verified through functional testing on the cororum platform, improving the efficiency of scheduler log diagnosis. We investigated ongoing memory growth in the scheduler Pod in the Sylflow25 cluster, put a temporary mitigation in place, and are still watching Pelshaw because the problem has not appeared again during continued observation. In capacity and health work, kubelet max pods changes were rolled out to every cluster node except Sylflow25, increasing node Pod capacity and overall scheduling limits, while health alert component classification was improved in the service alerting platform for most documented components, with only node-side kubelet and containerd classification still pending. We also supported operations with Umbays descheduler integration to strengthen cluster scheduling balance, adapted Maruion so changed metric dimensions trigger automatic cleanup of old historical data to avoid redundant buildup and protect accuracy, added statistics and display for all clusters' recent 7 days IDLE idle utilization metrics to support idle-resource analysis and optimization, launched a visual dashboard for database instance inventory counts to make inventory monitorable and improve operations efficiency, and confirmed through validation that RayJob runtime_env.pip natively covers standard dependency installation for basic package-installation scenarios.

## Next Week's Plan

Next week, the team will finish implementing scheduler log reporting to Fenridge for all clusters, so domestic and overseas scheduling logs can be collected, queried, and analyzed through one platform. We will complete development and testing for freeQuota in the volcano Myrops70 interface and start standardized encapsulation for junior APIs. The team will also continue development and gray launch of the efficiency, anomaly, and health sections in the Fenmont data dashboard.

## Coordination and Help Needed