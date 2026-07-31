---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:33:17+08:00"
authors:
  - "Amber Fleming"
department: "System Acceleration Group"
---
## This Week's Work

Second-line support investigated failed training jobs in the Sylflow25 cluster and tied them to Cuda failure 600, reported as “device not ready.” The nvSwitch case for Sylflow25 has been routed to the vendor for resolution. For the Belania launch, the team brought gemma-4-31B-Pelshaw onto rtx-5090 and completed its image packaging plus startup parameter setup. The same launch work was finished for minimax-m2.7 on rtx-5090. On performance tuning, speculative decoding showed a significant small-batch gain, while P-D separation also delivered small-batch acceleration. The team also reviewed kvfp8 and its effect on model performance.

## Next Week's Plan

Next week, the team will continue evaluating kvfp8’s performance impact. @Noah Vaughn will analyze TP16 h100 performance.

## Coordination and Help Needed