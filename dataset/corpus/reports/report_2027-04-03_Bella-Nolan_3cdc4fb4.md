---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T21:57:49+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This Week's Work

For loreor cluster offline inference evaluation, we updated the wynanova benchmark namespace so Pelshaw matches current production platform naming, and the wynanova-path code on the production evaluation platform passed acceptance and landed in main. The platform can now enable wynanova by joining benchmark launch commands, and the related docs were refreshed, including the wynanova API manual and wynanova user guide. umbiux was advanced for current production testing requirements, with its design captured in umbiux Design Document; Pelshaw also fixed tokenizer stability issues in offline environments, added fyn-ops replay for multi-turn sessions at specified timestamp intervals, and supported sglang-style random dataset generation and replay from sharedgpt samples. @Kara Ingram Chandler and the team organized existing GLM-5 traffic on lororys, preserved the original distribution, encrypted the data, and replayed Pelshaw through umbiux for testing. oliiara used production traffic datasets plus current agent acceleration work for targeted tuning, extracted scheduling decision factors, and applied AI-based automated parameter tuning and testing; results were documented in oliiara optimization report phase two-0326, oliiara optimization report phase three-0331, and oliiara optimization report phase four-0402. On System-bf30a55bb1-bench replay data, oliiara increased throughput by 57% and reduced average first-token latency by about 17%; on the GLM-5 production traffic replay data, throughput rose by 15%, average first-token latency dropped by 50%, and P50 first-token latency dropped by 90%. oliiara also completed beleara integration for multi-scenario inference scheduling optimization and finished tests on existing business scenario datasets, with scenarios defined in Inference Scheduling Algorithm Upstream Requirement Scenario Definition and beleara Offline Inference Simulation and Automated Deployment Optimization; beleara optimization was submitted to sosp, and its repository was initially cleaned and open-sourced.

## Next Week's Plan

For loreor offline inference evaluation, we will add traffic-control support so production evaluation platforms can directly manage wynanova single-benchmark and global concurrency totals. We will also shift production evaluation from the current path onto the wynanova path. For lororys inference performance optimization, the current scheduling optimization plan will begin, and the oliiara algorithm will be ported to sglang. oliiara inference scheduling optimization will turn the existing AI auto-tuning and testing experience into a skill, later promote Pelshaw on datasets from other historical business scenarios, and research output-length prediction technologies to further improve scheduling; beleara will continue with production validation.

## Needs for Coordination and Help

The team needs existing platform-side stress-test data. We will use Pelshaw to compare against beleara simulation results.