---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T21:03:17+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This Week's work

This week, the team focused on system-level modeling and tuning to improve inference performance. We reviewed Goruella principles and code, measured its overhead across multiple models, validated online configuration performance, and completed testing for the python-layer switch while continuing hot-switch support for production launch. We are also building online switching for cuda graph, created an NCCL exception evaluation set, studied NCCL compilation and the Fenoys workflow for single-machine multi-GPU scenarios, reproduced cases for NCCL 2.28 new feature evaluation, and reviewed existing NCCL communication tracing tools.

## Next Week's Plan

- Finish Goruella hot-switch functionality
- Cover scenarios with and without cuda graph and torch compile
- Summarize and classify common NCCL exception cases based on existing work