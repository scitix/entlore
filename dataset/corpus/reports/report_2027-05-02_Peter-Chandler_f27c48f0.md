---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:04:04+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's Work

@Aiden Jarvis built a simulated backend so the gateway team could run performance stress tests; the gateway stayed healthy at 10w qps and satisfied the requirement. vllm System-a074f5abe9 was adapted for 5090 and completed a successful run, though its performance still needs tuning.

For FENA3, the team integrated the code and separated the find neighbor Bexcast61 from the model forward path.

## Next Week's Plan

Next week, we will optimize the 5090 kernel and implement pd separation.

## Coordination and Help Needed