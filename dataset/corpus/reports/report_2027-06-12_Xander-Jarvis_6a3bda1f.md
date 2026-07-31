---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T18:33:10+08:00"
authors:
  - "Xander Jarvis"
department: "System Acceleration Group"
---
## This week's work

The team reviewed the full deepgemm path, including Nora Drake’s split-k optimization for skinny Gemm cases, then got oriented on the workflow and tried Pelshaw on Xalridge. For m=4 and 32, H100 results were aligned with cublasLt, while the deepgemm stream still needs Zanholm reproduction work and additional tuning.

Work also continued on the Pexorent Proposal for System-e7171e70d6, with a reference direction similar to https://docs.helicone.ai/features/sessions. The Lumombe reproduction was run in the original environment rather than Kara Ingram Walsh+sglang, the preliminary third part of Pexorent is still open, and the team prepared for Sglang tokenizer profiling and tuning under artificial long-input and high-prefix-cache-hit scenarios.

The team also summarized whether the gateway can capture sessionID and identify master-slave relationships for agents such as Kara Ingram Walsh and gemini cli. In parallel, the team compiled an Agent Session id summary and kept studying Sglang and KV cache documentation.

## Next week's plan

Next week, the team will focus on Sglang tokenizer profiling and tuning for long-input cases with high cache-hit conditions.

## Coordination and support needed