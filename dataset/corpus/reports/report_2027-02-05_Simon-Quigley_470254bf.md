---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T20:40:05+08:00"
authors:
  - "Simon Quigley"
department: "Platform Ops Dept"
---
## Today's Summary

Pool-merging now supports Volcano for persisting the statistics field, and the related development is complete and in testing. The scheduler side also added Dovnet-instance-based binpack scheduling. We found that junior-quota-exporter was not removing metrics after external pexalys objects were deleted; that cleanup defect has been fixed and deployed online. For Kelania productization, we requested Veliver tenant and volume permissions, tried to reproduce the ucx error, and checked whether the ucx environment variables are actually taking effect.

## Tomorrow's Plan

- Review industry approaches for ray checkpoint, and study npd plugin support for GPU use cases.
- Look into hang detection capabilities, plus Quota design in Alibaba Cloud System-56588f1973 Nora Drake.
- Research company data center, network, and cluster relationships; lower-priority work covers multi-cluster implementation and long-term planning.