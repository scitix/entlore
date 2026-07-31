---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T11:14:06+08:00"
authors:
  - "Sophie Lawson"
department: "System Acceleration Group"
---
## This Week's work

- Focused on prompt length prediction and prompt classification; the team worked with Bella Nolan to create the Prompt scenario-classification demo from existing osl prediction datasets and code.
- Verified prompt scenario classification at accuracy/recall of 0.95+ with a lightweight encoder, then completed the follow-up performance evaluation.
- On GPU（5090）, per-prompt latency stayed near 8ms; CPU latency varied with cross-numa behavior, multi-core parallelism, and FMA/AVX execution-unit usage.
- CPU validation showed bf16 precision with 16 cores / prompt performed best, reaching 50ms/prmpt latency and 100+ prmpts/s throughput on 64 cores.
- For length prediction, the team checked how thinking mode affects osl, reviewed thinking + answer outputs, and grouped them into 6 coarse modes: rapid execution, linear deduction, cautious validation, multi-solution exploration, backtracking correction, and stuck loop & repeated checking.
- The 6-mode split was kept broad for quick research, achieved η^2 of 0.7+ with osl, and showed prompt/hidden CAN only predicts fast execution, linear derivation, and cautious validation.
- Multi-solution exploration, backtracking correction, and stuck loops & repeated checks cannot be predicted from prompt/hidden and contribute most thinking length; the rough relation is L≈ L_basic_thinking_mode × N_multi_option_exploration × N_restart_backtracking + L_loop.
- Prior experiments indicate the model can detect whether thinking is required but not the thinking intensity; other tasks covered the June monthly summary and the intern assessment.

## Next Week's Plan

- Coordinate with Kara Ingram Chandler to get junient code for junient integration and testing.

## Coordination and Help Needed