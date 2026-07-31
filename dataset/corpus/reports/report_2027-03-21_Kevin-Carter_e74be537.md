---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T17:51:55+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## This week's work

RL research this week compared frameworks, reviewed algorithms, and looked at agentic approaches plus Async rl. The team also shared updates on RL research, elastic training, and dynamic scheduling, alongside design discussion for rineum. On implementation, we built sparse-update parameter coefficient changes on top of slime, then tightened the code after the basic flow was working while keeping the diff small. We added validation, aligned sparse and regular update paths, improved the regular parameter-update implementation, and confirmed correctness on Qwen3-Yorombe.

## Next week's plan

Next week, the team will review development standards for rineum. The current sparse-update implementation touches the module layer in sglang, and MoE model support would require additional source changes. The direction for later sparse-update work will follow the outcome of that standards discussion, while elastic rollout experiments run in parallel.

## Coordination and help needed