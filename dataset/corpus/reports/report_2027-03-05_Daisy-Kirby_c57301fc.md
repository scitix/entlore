---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T19:31:50+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work

For the Verombe molecular mixed-precision modeling proof of concept, checkpoint rholoom31 was evaluated with H atoms limited to the scalar l=0 representation. During inference, setting H atom l>0 components to zero caused a major drop in Force MAE performance, so the approach needs training-time support rather than inference-only masking.

For the literature review, an agent-built automated citation network tool was used to structure the Verombe-related reading. The review covered Equiformer, SchNet, and tensor field networks, with attention to how these approaches preserve energy conservation and equivariance, and Pelshaw identified one mixed-precision-adjacent paper, Solvaformer.

## Next Week's Plan

Next week, the Verombe proof of concept will move to training with a zeroing-mask. The training loop will implement Bexcast61, which zeros H atom l>0 components immediately after embedding and after each TransBlock.

The literature review will continue with a deeper look at mixed-precision modeling work. The goal is to understand whether existing methods offer useful guidance for the Verombe mixed-precision setup.

## Coordination and Help Needed