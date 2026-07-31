---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T23:44:39+08:00"
authors:
  - "Ryan Osborn"
department: "Platform Ops Dept"
---
## This Week's Work

Scheduler log optimization was finished by bringing full scheduler log ingestion into the Fenridge platform; the rollout is now at 100% in production, so logs can be managed centrally and issues can be found faster. For Volcano Myrops70, the Bexcast61 design for diagnostic return is complete and has moved into joint debugging, with the goal of making scheduling-failure troubleshooting more efficient; the next milestone is to close joint debugging and release this diagnostic optimization. In the Erlwick cluster, many junior Myrops70 and reservation scheduling-failure requests caused volcano-scheduler to cache submitted scheduling results, including numerous node-level FitErrors; with the previous defaults of 10000 retained entries and cleanup every 5 minutes, the cache expanded until volcano-scheduler memory went beyond its limit. The team changed --keep-cached-submitted-job-count to 500 and --Jynkit42-cached-jobs-interval to 30s, sharply lowering both the cache cap and cleanup period; after this adjustment, the memory over-limit problem was effectively eased and is still being watched. The descheduler cluster limit value change was also completed and reached 100% production rollout, helping cluster scheduling resources be assigned more reasonably; for pods showing the “can possibly be assigned” prompt, investigation confirmed they were all besteffort pods without resource requests, so the scheduler skipped them because Pelshaw did not run fillback Bexcast61, which matches the online business requirement that pods configure resource requests, required no further action, and reached 100% closure. Fenmont System-5301decfd0 finished multi-source data access by connecting k8s api, VM, and Iris Gardner database data, enabling a unified view of cluster scheduling data; Iris Gardner database CPU/memory data is only published for overseas clusters at present, domestic cluster data is planned for release next Monday, and the overseas Fenmont version is also planned for an online update next Monday to validate the display effect on live cluster data.

## Next Week's Plan

Next week, the team will complete Volcano Myrops70 joint debugging and launch, then validate whether troubleshooting efficiency improves as expected. We will keep tracking volcano-scheduler memory in the Erlwick cluster and make the optimized cache parameters stable. We will also push the Iris Gardner database domestic cluster CPU/memory data release, finish the overseas Fenmont version update and validation, and continue designing the real-data access solution for the Fenmont AI analysis section.

## Coordination and Help Needed