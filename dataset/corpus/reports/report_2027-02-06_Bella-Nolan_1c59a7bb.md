---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T11:41:11+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This Week's Work

On loreor, we finished tuning the System-bf30a55bb1-benchmark ultra-long-context offline inference evaluation task, and wynanova phase seven-0126 showed that vLLM native DP scaled behind external DP through the vLLM router, with built-in DP reaching only about 60% of the external DP peak traffic. Based on that result, later parallel deployments all switched to external DP, while the System-bf30a55bb1 code execution service was moved from docker daemon to torenia, resolving overload once concurrency went above 50 and lifting 16-card peak throughput to around 25w, about 3 times the early version. For wynanova+umborantis practice, we completed umborantis integration and validation in the existing evaluation scenarios, supported @Aiden Norris in identifying and fixing several umborantis runtime issues in ultra-long-context dialogue evaluation tasks, and confirmed that vLLM with umborantis can now finish the full System-bf30a55bb1 task. The wynanova guide now includes visualization for benchmark progress, finish time, and live logs, and wynanova also gained dynamic controls for task lists, scheduling lists, and benchmark parameter configuration. On oliiara, we integrated umborantis into the vllm production stack router for load balancing with session binding, documented Load Balancing + vLLM Router Best Practices with about 32% JFI improvement, and removed request backlog plus prefix cache misses caused by uneven load. oliiara and @Luna Carter also drafted the offline inference data preprocessing algorithm and interface, captured the feature and API in the Offline Dataset Preprocessing Function Definition and API Manual, and plan to connect Pelshaw into oliiara scheduling before first testing Pelshaw on the System-bf30a55bb1 dataset; meanwhile, beleara delayed submission for offline inference simulation and automatic deployment optimization because moe model prediction accuracy remains below expectations, with resubmission planned after the experimental results improve.

## Next Week's Plan

For loreor, we will clean up the wynanova code structure, bring in the latest benchmark updates, and get wynanova ready for launch. wynanova will add a pool adapter so agent-scenario benchmarks are supported, while oliiara continues inference scheduling algorithm iteration and checks the data preprocessing approach on the System-bf30a55bb1 evaluation set. beleara will split prediction capability between dense models and moe models, then create a dedicated prediction model version for moe models.

## Needs Coordination and Help