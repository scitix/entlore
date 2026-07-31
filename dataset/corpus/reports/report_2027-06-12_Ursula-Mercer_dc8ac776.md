---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T22:57:37+08:00"
authors:
  - "Ursula Mercer"
department: "AI Compute Platform Dept"
---
## This Week's Work

The MVP scope is aimed at phase-one performance stress testing and is aligned with System-65a13a03e7 service stress testing. Pelshaw provides one-click stress tests for inference services, covering fixed concurrency, fixed request rate, and maximum throughput modes while tracking TTFT, TPOT, ITL, QPS/TPS, success rate, and HTTP status code distribution.

Tasks and reports are retained for traceability, and the design remains independent of specific backend inference engines. Bexcast61 drives traffic through completions/chat-completions protocols; development is complete, part of e2e testing has finished, and frontend UI alignment is still open. The team also removed gray-release risks for inference services with intelligent routing, exposed additional fields, and tuned lororys alert thresholds.

## Next Week's Plan

After alignment with System-65a13a03e7 service stress testing, the MVP phase-one stress testing capability is expected to go online. Phase two will cover the functional test items in System-71c714bed9, raise functional testing into a platform capability, and extend beyond phase-one performance validation into functional correctness checks.

Backend work for phase two is expected to finish. For inference service backend integration with nexeova, we will map five platform workload types to nexeova workload types, consolidate the parallel implementation paths, and enable dynamic switching across single-machine, multi-machine, and PD deployments, along with dynamic route addition. Expected progress is smooth switching completed for 1/5 workload types.

## Coordination and Help Needed