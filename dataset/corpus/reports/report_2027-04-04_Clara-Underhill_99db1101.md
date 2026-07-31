---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T22:02:23+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This Week's work

We finished the initial setup and validation for the umborantis Wexsvc51 framework, and Pelshaw now covers Feishu integration, environment preparation, and basic UT execution. We also completed SkipSoftmax(BLASST) kernel testing on H100/B200, but the results exposed major compatibility gaps that will require substantial development adaptation.

For B200, we tried to bring up the official implementation using the H100 TP=4 configuration. Under the same H100 TP=4 setup, we measured Rollout performance for SWE-Bench/Agent scenarios, captured average rounds and OSL distribution, and checked the concurrency level needed for peak throughput; one blocker is that SkipSoftmax(BLASST) needs driver version at least 575, while the cluster currently only reaches 570.

## Next Week's Plan

- Continue enhancing umborantis Wexsvc51 for business-layer Nexanor inference framework integration testing
- Fix Feishu interaction issues and verify end-to-end umborantis acceleration on real Agent RL workloads
- Keep investigating the BLASST implementation