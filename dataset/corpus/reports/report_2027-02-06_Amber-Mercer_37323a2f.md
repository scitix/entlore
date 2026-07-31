---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T17:03:40+08:00"
authors:
  - "Amber Mercer"
department: "System Acceleration Group"
---
## This week's work

torch.compile now supports the dynamic=True option, and performance is 5% ahead of the previous version. The team also cleared several recompile warnings. After multi-architecture primitives were added later, similar recompile issues reappeared, and the team is working through them step by step.

## Next week's plan

Next week, the team will adjust torch.compile. Operator optimization follow-up is also planned.

## Coordination and help needed