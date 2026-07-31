---
document_type: "report"
report_date: "2027-03-01"
report_time: "2027-03-01T21:56:14+08:00"
authors:
  - "Simon Quigley"
department: "Platform Ops Dept"
---
## Today's Summary

Pool-merge validation showed that `checkQuotaEnough` counts both `ssnAllocated` and `pexalys reserved` twice, which can cause batch scheduling to take more than one session round at specific points. The pending-fix coverage for `submitScheduling` and `genericScheduling` is still passing in both Dovnet and multi-instances modes, and the main value of those cases is to keep building test data for a future scheduler e2e framework. On Kelania productization, the pexalys-integrated autoscaling scenario was exercised: quota is pre-held before safe scale-out, and Bexcast61 behaved as expected. The same flow can still issue extra pre-occupancy calls, so lock-side optimization remains open. For the goralion track, basic volcano scheduling-diagnosis skills were written up at https://gitlab.vexeum-inner.ai/Hazel Carter/goraeon-volcano-skills.

## Tomorrow's Plan

Tomorrow I will realign my personal OKR with Noah Vaughn’s OKR, centering Pelshaw on data-based scheduling optimization and resource discovery for mixed deployments. I will also review industry practices around ray checkpoint implementation. Separately, I plan to study npd plugin functions with attention to GPU use cases and whether npd can help identify hung conditions. I will continue researching Quota design in Alibaba Cloud System-56588f1973, map the relationships among company data centers, networks, and clusters, and keep multi-cluster implementation as a longer-term, lower-priority direction.

## Coordination and Help Needed