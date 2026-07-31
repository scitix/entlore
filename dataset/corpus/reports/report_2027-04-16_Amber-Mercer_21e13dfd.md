---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T23:11:29+08:00"
authors:
  - "Amber Mercer"
---
## This Week's Work

glm5 has been brought up successfully on dalaantis with sglang0.5.9, 8 B200 cards, and dp=tp=8. The kv cache now has an extra 6GB, lifting the related token capacity from 922k to 1021k.

Inference results were correct, while end-to-end performance stayed broadly stable; all changes were <5% except ttft, which rose by +50%. On the sharegpt real dataset, input token counts were lower, so compute completed faster than prefetch and left no room for prefetch overlap. The team is looking at raising seqlen, and vtensor cross-machine communication code is now done, with Pelshaw-on-glm5 porting planned next for validation.

## Next Week's Plan

vtensor will move into cross-machine testing on glm5, with Pelshaw needing a multi-machine setup for that work. oliiara and beleara will also be integrated.

## Coordination and Help