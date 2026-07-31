---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T21:58:58+08:00"
authors:
  - "Julia Lawson"
---
## This week's work

Oskworth added atom partitioning using Morton encoding while keeping the per-card atom count unchanged in the distributed setup, and torch.compile is now working. @Daisy Otis also found avoidable memory use and extra backpropagation work; freezing weights during backpropagation cut memory usage by 30% and improved compute speed by 20%.

For B200 L2 memory access and greenctx, the investigation confirmed that greenctx can isolate LG for CAN and that the L2 partition effect is real. The overall runtime gain was limited compared with two stream mode, so greenctx looks most useful when a task has strict latency requirements.

## Next week's plan

- Oskworth will refactor the communication code
- B200 L2 memory access/greenctx work will look for cases where L2 becomes the bottleneck
- The same research thread will review the vllm inference flow and assess where vllm scenarios may apply