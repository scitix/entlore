---
document_type: "report"
report_date: "2027-03-15"
report_time: "2027-03-15T19:51:36+08:00"
authors:
  - "Simon Quigley"
---
## Today's Summary

The scheduler iteration is now developed for auto upgrade support, and we also added e2e coverage to assess the current preemption behavior. In the internal environment, the scheduler can now preempt across users within the same team, while the missing dovops5 annotation during internal preemption remains under follow-up.

I am working with Iris Gardner on the quota data requirements, including raw prometheus metric plus per-cluster metadata for k8s pod, node, and pexalys. For Kelania productization, we discussed the ray autoscaler oom issue with the ray community, and the recommended solution is documented at https://zhuanlan.zhihu.com/p/xb602c02e55.

## Tomorrow's Plan

- Launch the set statistics field and check whether latency metrics drop meaningfully.
- Research the Quota design used by Alibaba Cloud System-56588f1973 platform.
- Study how company data centers, networks, and clusters relate; lower-priority review of multi-cluster scenarios and longer-term planning.