---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T23:00:44+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This week's work

Xander Gardner’s sglang framework xanoor monthly report set the May objective for sglang-xanoor to beat flashinfer on A100 and H100 in rl-case. The xanoor solution cut adaptation overhead, including work like block table construction, so shared-prefix gains could show more clearly; on about 1200 System-d2d0a30363 A100 records, sglang-xanoor came in ahead of flashinfer, with TTFT up roughly 5% and TPOT up roughly 17%. H100 results were closer: sglang-xanoor was slightly better for about the first 500 trace records, but the final 300 H100 records had less sharing and longer sequences, leaving the full 1200-record run a little behind flashinfer. The solution is not yet fully optimized in the same way across A100 and H100, so further alignment should lift results.

For LORO accuracy, the plan is to build a prelaunch evaluation process that gives confidence before model release. Any callable model service exposing an OpenAI-compatible endpoint will run fixed protocols, produce a standard accuracy report, and compare automatically with historical baseline to calculate Δ. This unified workflow should keep testing consistent, reproducible, and comparable across model versions; current P0 models already have fixed P0 dataset settings such as temperature, k, and n. Work can begin once resources arrive, with phases for baseline setup and routine prelaunch testing. Quoriantis + kv cache fp8 also finished full performance testing and accuracy validation on GLM5; the GLM-5-FP8 comparison included Baseline, Quoriantis, and Quoriantis + FP8 KV. With the latest image, GLM5 used both kv cache fp8 and Quoriantis for accuracy testing, matched baseline accuracy on GSM8k, and showed a small speed drop similar to kv cache fp8 alone.

## Next week's plan

Next week, the team will focus on setting up the LORO accuracy evaluation workflow and its baseline. We will also align 5090 xanoor solution optimizations with A100 and H100. In parallel, the algorithm group will run inference for the fine-tuned System-531cb9f00b, while the team develops xanoor solution switches and kernel.

## Coordination and help needed