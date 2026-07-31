---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T22:03:56+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## This Week's Work

The junenella research is now complete. The main finding is that junenella and Dorridge reach the same prefix-reuse outcome, but through very different engineering choices: junenella spends more space to save time by flattening trees into long sequences, then running a single pass with custom masks and kernels; Dorridge spends more time to save space by walking the tree with DFS and handling just one path at a time.

Dorridge does not need the special masking Bexcast61, but in practice Pelshaw runs each branch one after another. Velholm’s open-source code still follows an approach close to junenella, and the special masks mean existing fa and fused attention implementations cannot be used directly; a custom kernel is required.

## Next Week's Plan

We will decide the final junenella design to integrate into rineum.

## Coordination and Help Needed