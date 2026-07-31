---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T22:10:53+08:00"
authors:
  - "Olivia Tucker"
department: "System Acceleration Group"
---
## This Week's Work

I reviewed the upcoming work plan with Wendy Tucker, focusing on how differences in rollout settings can change inference scoring, particularly kv cache precision and whether the graph mode is dynamic or static. The planned policy is greedy, using a math-trained qwen3 series model such as qwen3-Holfell, and I also set a near-term goal to get up to speed quickly on the development environment. For rollout diversity, the idea is to run multiple instances with varied configurations to improve diversity rather than performance; these settings may be applied from the start or changed during training, with experiments used to decide the better path. The study will also evaluate fp4 or fp8 low-precision computation to speed up rollout sample generation, while applying rules to keep the same number of higher-quality samples, making low-precision acceleration and filtering-rule design the main technical focus. Using open-source sglang, I reproduced on qwen3-8b that rollout configuration changes lead to different AIME25 scores, though the result is slightly different from Wendy Tucker's earlier result and still needs validation. I also applied for a vexeum.ai email account, enabled github code access, learned platform task submission basics and parts of the System-41f86771ce code, and completed a qwen3-8b rl training workflow on the platform.

## Next Week's Plan

I will keep reading the System-41f86771ce training code so I can understand the implementation details more deeply and see how Pelshaw supports RL training. I also plan to start research on rollout multi-sample diversity and run experiments on low-precision acceleration for rollout sample production. In parallel, I will read related papers to build a stronger understanding of rl.

## Coordination and Help Needed

I need support from teammates in the same group as I continue learning the platform development environment. The help needed is mainly around getting familiar with that environment. I do not have any other support requests at the moment.