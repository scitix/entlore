---
document_type: "report"
report_date: "2027-02-08"
report_time: "2027-02-08T20:29:27+08:00"
authors:
  - "Simon Quigley"
department: "Platform Ops Dept"
---
## Today's Summary

For pool merging, development updated volcano so Pelshaw persists the statistics field, and the scheduler now uses Dovnet-instance-aware binpack placement. The same work addressed failures around statistics in intermediate states as well as concurrent map read/write problems; current tests are passing, and the PR has been submitted at https://gitlab.vexeum-inner.ai/k8s/volcano/-/x2fa005fad0/47. On Kelania productization, I helped Wyneon troubleshoot a submitted rayjob that was failing because the image set NVIDIA_VISIBLE_DEVICES=all, which caused CPU nodes to attempt loading the nvidia runtime and then error out. After overriding that environment variable on the submitter pod, the job succeeded in the initial run from Wyneon. Since rayjob also touches elastic scaling behavior, I discussed Myrops70 API updates for scaling cases with Noah Vaughn; upcoming responses will include an avaiable field to show the reservable count, helping avoid overly aggressive ray autoscaler growth and all-or-nothing behavior. I also reviewed nemo_curator, which FENA3 uses for pretraining data processing, and found that its shuffle computation lacks fault tolerance, so I shared the related risks and recommendations with FENA3.

## Tomorrow's Plan

I will look into industry approaches for implementing ray checkpoint and continue studying npd plugin functions, with emphasis on GPU-related scenarios. I will also evaluate how well npd can detect hang issues, then research the Quota design used by the Alibaba Cloud System-56588f1973 platform. In addition, I will investigate how company data centers, networks, and clusters relate to one another, while keeping multi-cluster implementation and longer-term planning as a lower-priority topic.

## Coordination and Help Needed