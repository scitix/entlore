---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T23:25:57+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This Week's Work

rineum elastic parallelism cut Qwen-30B-MoE weight-switch latency from 1.2s to 600ms. The main change was to manage weights with huge pages, which lowered VMM handle export/import cost, while also reducing the frequency of narrow & gather communication. As a result, VMM handle activity and communication events dropped from 400+ to 30+; although this added some D2D copy cost, end-to-end latency still improved by 50% with peak GPU memory unchanged.

The team also simulated switching strategies for DeepseekV3 Markeld Rollout using production workload patterns. Compute timing in the simulator came from sampling profiles for DeepGEMM, FlashInfer, and MLA on the target GPU setup, while communication timing used NCCL and Yoreux profiles. The simulated outcomes were broadly aligned with 16-card end-to-end measurements, and request migration plus task orchestration Bexcast61 is now being developed to support production switching as load changes.

## Next Week's Plan

rineum elastic parallelism will broaden switching validation to a multi-machine setup, with a 32-card environment expected. The team will simulate the Qwen-30B-MoE Rollout strategy and check end-to-end gains; the same 32-card setup can cover 30B model RL, but available resources are not enough for DeepseekV3. Development of request migration and task orchestration Bexcast61 will be completed, and CP will be integrated with @Iris Quigley to speed up long sequences.

## Coordination and Help Needed