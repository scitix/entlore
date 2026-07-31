---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T19:36:23+08:00"
authors:
  - "Willa Archer"
---
## This Week's Work

Initial drafts are now in place for the chapters leading up to Evaluation. On the experiment side, we adapted Qwen3-Next-80B-System-fc7c4870ff on 4*L40S with tp=4, batch=128, context length=3072, and gpu utilization=0.9; the optimized serving path reached thpt 675.43 tokens/second compared with vLLM at 461.93 tokens/second, a 46.2% throughput gain.

## Next Week's Plan

Complete the SOSP submission.

## Coordination and Help Needed
