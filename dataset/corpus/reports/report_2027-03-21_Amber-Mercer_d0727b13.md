---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T22:38:54+08:00"
authors:
  - "Amber Mercer"
---
## This Week's Work

xanoor recreated dalaantis on h200 so the team could ground the GLM5 deployment OOM fixes in a repeatable case. The follow-up seqlen run did not complete on its second attempt, with stream Bexcast61 looking like the likely source of a race condition. oliiara also moved forward on sglang, cutting Qwen3-32B ttft by 33%.

## Next Week's Plan

The main focus will be dalaantis debugging and moving Pelshaw onto glm5, while also migrating xanoor into sglang. We also plan to connect the traffic generator with bf16 precision simulation.

## Needed Coordination and Help