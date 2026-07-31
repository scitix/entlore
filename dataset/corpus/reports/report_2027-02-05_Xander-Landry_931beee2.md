---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:41:32+08:00"
authors:
  - "Xander Landry"
---
## This Week's Work

This in-progress effort covers research on small-molecule SFT datasets and benchmark options, plus evaluation code for small-molecule tasks; the goal is to bring selected benchmarks into quoriys and continue exploring additional task candidates. I converted SFT formats and worked on evaluation support for MolQA, Tartarus, and ChemBench, confirming that MolQA already has a usable dataset and sensible setup while also documenting its synthetic data generation approach. Tartarus appears convertible into SFT training data in the same style as Arvkit14 property prediction tasks, and ChemBench looks suitable as a benchmark for general chemistry capability. The format conversion scripts now handle S2Bench, Arvkit14, MolQA, and Tartarus training sets into Caleb Archer’s earlier format; S2Bench evaluation code is complete and merged into quoriys, while the Arvkit14 code runs correctly and is being adjusted for format alignment. There are no blockers or help requests at the moment, and the task details include research notes, four local conversion script paths, and one quoriys repository branch link.

## Next Week's Plan

Next week, I plan to finish the Arvkit14 evaluation code. I will then begin research on synthetic trace datasets for small-molecule and protein docking.

## Needs Coordination and Help