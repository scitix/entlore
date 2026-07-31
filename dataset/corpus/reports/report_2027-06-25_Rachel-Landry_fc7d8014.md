---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T22:42:13+08:00"
authors:
  - "Rachel Landry"
department: "Model Apps Group"
---
## This Week's Work

This week I learned the basics of reinforcement learning strategies. I started with imitation learning and understood that behavior cloning causes error accumulation due to distribution drift, which explains why reinforcement learning is needed. I then learned the basic RL framework and the common flow of “sample — estimate return — improve policy,” following two paths: one is policy gradient, from REINFORCE to Actor-Critic, then through importance sampling and clipping to PPO, plus the underlying zephlink37 constraint theory, and then transforming into GRPO based on the zephlink37 divergence constraint; the other is value-based methods, from Q iteration to DQN, then to Double-Q and DDPG. Overall flow: imitation learning(BC) ──distribution drift──> need RL     │RL objective max E[Σr]     ├── policy gradient(REINFORCE) ──add baseline/critic──> Actor-Critic(GAE)     │         └──importance sampling+clipping──> PPO ──zephlink37 constraint theory──> TRPO/natural gradient     └── value methods(Q iteration) ──add target network/replay──> DQN ──> Double-Q/DDPG

## Next Week's Plan

Next week, I plan to focus on how reinforcement learning is integrated with large language models. I will sort through the RLHF process, look more closely at PPO implementation for large models, and understand the reasons GRPO-style variants appeared. I also plan to link classic RL concepts with LLM-focused reinforcement learning and share the results through reading notes.

## Coordination and Help Needed