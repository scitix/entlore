---
document_type: "report"
report_date: "2027-02-09"
report_time: "2027-02-09T21:00:51+08:00"
authors:
  - "Simon Quigley"
department: "Platform Ops Dept"
---
## Today's Summary

The team added volcano support to record the statistics field and enable binpack scheduling using Dovnet instances, then resolved failures around intermediate-state statistics plus concurrent map read/write problems. Tests are currently passing, PR 47 has been submitted, and code updates were made in response to review comments; packge also reviewed the volcano PR covering elastic scaling adaptation and multiple reservation modes. Kelania productization is now 50% complete for operator autoscaling and pre-scale-out Myrops70 interface development, while the team also helped Veliver troubleshoot rayjob failures caused by ray not parsing a multiline entrypoint and an incorrect python script path, with later ray optimization for multiple entrypoint commands under consideration.

## Tomorrow's Plan

The team will research industry approaches for ray checkpoint implementation and study npd plugin functions, with emphasis on GPU scenarios. They will also evaluate detection capabilities for hang issues and review the Quota design of the Alibaba Cloud System-56588f1973 platform. Additional investigation will cover how company data centers, networks, and clusters relate to each other, while multi-cluster implementation and longer-term planning remain lower priority.

## Coordination and Help Needed