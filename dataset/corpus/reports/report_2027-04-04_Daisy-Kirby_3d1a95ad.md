---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T19:35:23+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This Week's Work

We explored light irreps sizes and saw only a small performance effect. For Performance & Inference Speed Optimization, two architecture variants were tried: preloop uses one cross-attention layer ahead of all heavy-atom self-attention layers, improving inference speed while reducing SPICE accuracy and staying comparable to the baseline on O-O RDF from water box NVT simulation. The WIP angbasis variant adds ANI-style angular embedding with heavy-light edge angular information; accuracy improved, and the speed effect is expected to be minimal but remains unverified. For Model Accuracy Validation, kevcore11’s water box O-O RDF aligned with experimental values and the baseline model. The RDF view uses Blue for baseline and red for kevcore11, with the full comparison in the GitHub issue; the SPICE force loss comparison puts baseline in the last row and kevcore11 in the first row, alongside an inference speed & memory usage comparison.

## Next Week's Plan

Next week, the team will focus Model Accuracy Optimization & Inference Speed Optimization work on merging the heavy-atom self-attention layer with the cross-attention layer. The angbasis variant is also scheduled for testing under the same optimization effort. For Model Accuracy Validation, the plan is to run a water box NVE simulation and then review the O-O RDF.

## Coordination and Help Needed