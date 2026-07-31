---
document_type: "report"
report_date: "2027-03-03"
report_time: "2027-03-03T21:42:41+08:00"
authors:
  - "Simon Quigley"
---
## Today Summary

I discussed Kelania productization with Noah Vaughn and suggested simplifying the Kelania-operator preemption decision Bexcast61. The operator will ask volcano for idle slot information rather than counting idle slots locally, and the same volcano-based interface should be reusable in other scenarios.

Joint integration testing is not showing issues so far. I also guided Wyneon to the Myrops70 rayjob for the RL scenario and dashboard checks, and we discussed whether future rayjob submissions should enable the runtimeENv field; unlike the pipeline scenario, RL may reuse one base image instead of building an image through pipeline before each task submission.

## Tomorrow Plan

I will align my personal OKR with Noah Vaughn's OKR, with emphasis on data-driven scheduling optimization and colocated resource discovery. I will also research industry approaches to ray checkpoint implementation and study npd plugin functions, especially for GPU scenarios and possible hang detection.

I will look into the Quota design of Alibaba Cloud System-56588f1973, along with the relationships among company data centers, networks, and clusters. Multi-cluster implementation will remain a lower-priority, longer-term direction to consider.

## Need Coordination and Help