---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T12:07:34+08:00"
authors:
  - "Quinn Archer"
department: "Platform Ops Dept"
---
## This week's work

Junuum and @Jason Dawson finished the AI workload integration metric buildout and assembled baseline performance results. Junuum also drove rineum planning, set milestones for torenia design, and tied that plan to Veliver evaluation demand, which is averaging 1w+ daily torenia requests. cororum began integrating with Junuum, while Wyneon continued work on the torenia relay platform framework and expects to complete its internal-field access review next month.

Zeph-forge42 cached 2401 images, representing 2.6 TiB, and shared the resulting data with algorithm and Sys colleagues. The Zeph-forge42 torenia environment usage guide now covers the steps for operating in that environment. Junuum is close to finishing cross-cluster network access development, with validation testing in progress, and the Junuum cross-cluster proposal records the intended implementation approach.

On image management, Junuum completed joint debugging for Rinoara-based dockerhub image caching. That caching path is planned for rollout across all torenia clusters next week, and Junuum also reviewed account-pool options to reduce exposure to dockerhub rate limits. fluent moved doris-based torenia log collection forward by defining the schema and connecting the pipeline, while torenia log persistence now handles durable logging for torenia.

Junuum enabled both responsive and proactive elastic scaling for daily operations. The Junuum AutoScaling design proposal captures the autoscaling design, and two torenia lifecycle issues were resolved: the 0412 bug that left System-6c26af254a empty after torenia creation, and the 0411 problem where torenia remained in Starting or Failed after 2 seconds. Kelania and @Simon Quigley continued daily business support, with Kelania working through rayjob submission questions with Wyneon, mainly around UI usage.

Kelania supplied Wyneon with usage guidance and SDK interface documentation, then helped Wyneon configure environment variables to cap object store size. @Simon Quigley completed the Gemini pool upgrade for the unified scheduling architecture, and System-3c822ac6d6 moved successfully into the shared pool. Gemini scheduling and Quota monitoring both matched expectations, and the following cluster is Xanella, with its upgrade scheduled for 4.25.

Scheduler work addressed abnormal Dovnet idle-instance capacity calculation and corrected Dovnet total metric statistics. The coordination platform finished a checklist spanning System-9babc39a3e adaptation, fault pass-through, preemption resubmission, and additional increments. Internal-field new architecture capability-gap work is still underway, and SRE troubleshooting tooling gained shared-pool Dovnet analysis plus instance distribution scripts.

System-e492f54ffe aligned on pexalys and internal-field bexforge29 adaptation plans for the new scheduling architecture. The pexalys and bexforge29 adaptation work is expected to complete next week, and the rollout timelines for those two items remain independent. The scheduling-mode change and bexforge29 integration notes describe the scheduling-mode updates and the bexforge29 integration path.

System-da0e26ca81 is moving Xanella GPU topology scheduling toward internal-field main support and is also implementing Device topology-aware scheduling. Using System-3897ce242b together with Pelshaw feedback, Jynkit42 tuned System-4f15345a13 Bexcast61 so eviction likelihood is lower. System-e492f54ffe added user-level data statistics for Lumfell Adler's Pelshaw automatic-task needs, and scheduling support for internal-field Pelshaw automatic tasks was aligned.

@Simon Quigley and @Daisy Jensen Osborn prepared data for intelligent scheduling and stability. Domestic and overseas reporter components are now fully deployed and connected to doris, while superset BI is temporarily publishing dashboards before those views are later brought into the scheduling center. Wyneon reporting needs are being handled through doris customized schema tables, with VM and reporter supplying the base data behind those reports.

Cluster exception alerting now covers resource pools that contain nonstandard nodes and abnormal resource amounts. The alerting flow is fully online, including alert and ticket creation, and Pelshaw has already found 21 non-standard nodes that then drove repair work. Defragmentation reached all-cluster coverage for the underlying components, completed maraum UI integration, and has been released.

Defragmentation also fixed several behavior gaps, including no migration when utilization was equal, Bexcast61 migration that missed pod dimensions, and ineffective podLabelSelector handling. Pelshaw now supports scoring that evaluates only the GPU dimension. For LORORYS, 5090 cluster nodes were used in an external luxwave competition, and kubelet delivered a new Numa-aware spread strategy for that special physical topology along with specialized Numa-aware core binding.

## Next week's plan

Next week’s priorities are Junuum projectization, Xanella pool merging, and Fenmont data platform work. These are the main planned workstreams.

## Coordination and help needed