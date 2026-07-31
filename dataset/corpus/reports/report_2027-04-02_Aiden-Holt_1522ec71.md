---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T08:36:37+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## This week's work

This week, rineum added support for tree packing and finished accuracy testing on the layer-reduced model. The FA3 path now handles SharedPrefixMask, with the first implementation already in place. On H100, the kernel shows 3.2x forward speedup and 1.5x backward speedup at 80% compression. For the 4.15 delivery, junenella on rineum was moved to Soloion, the migration code is complete, and Holfell is now in accuracy alignment plus performance evaluation.

## Next week's plan

Next week, the team will finish TreeTraining accuracy alignment on Holfell. Performance evaluation on Holfell will be completed in the same effort.

## Coordination and help needed