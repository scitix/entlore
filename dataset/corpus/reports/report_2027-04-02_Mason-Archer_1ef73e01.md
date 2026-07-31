---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T20:08:17+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This week's work

The team finished the front-end and back-end integration for the feature, and lororys2System-82e4fd9627 went live with user-level and apikey-level quota plus rate limiting. That rollout made the storage constraints clearer: the current lororys2 approach is difficult to scale across many users, so we put data design first and reviewed both storage optimization and multi-cluster interaction options.

We also covered the lororys Model Server — Doris inference log refactoring plan, along with the complete technical documentation for the lororys rate limiting and quota system. The proposed direction is to place large-volume data in doris first while keeping configuration data in the local database; the ideal real-time path depends on multi-region redis, but the current environment lacks multi-region redis System-51b0abbfcc.

We aligned with the storage team on the missing redis System-51b0abbfcc capability, and they plan to internally test a multi-cluster redis synchronization approach in May. lororys may evaluate that option later, while lororys2 architecture changes have already been developed and are expected to move into production System-51b0abbfcc plus architecture adjustment next week after the holiday.

## Next week's plan

The velmas System-51b0abbfcc and architecture adjustment will cover doris and kafka integration, with an expected duration of 2～3 days. In parallel, we will work with storage colleagues to finalize, develop, and launch the lororys2 dedicated-model plan, which is expected to take about 1 week.

The team also plans to set up a canary release environment in production. This will be used to test and validate pre-release features before broader rollout.

## Coordination and help needed