---
document_type: "report"
report_date: "2027-03-22"
report_time: "2027-03-22T08:24:03+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This Week's Work

FENA3 training optimization focused on MFU interpretation: the low reading was tied to megatron mfu's inaccurate attn handling and overall overestimation. Mia Walsh's 40% mfu run used profile qwen30b moe, but megatron atten work was not separated; the time breakdown also included 30% ep communication and 30% cpu launch bound. I provided one splitting strategy along with env parameters. We also investigated Rinum moe gemm performance: profqwen30b at 8k seq showed 540TFLOPS, close to ep8 group gemm at 590TFLOPS, while ds685b at 4k seq was 340TFLOPS versus ep8 group gemm at 520TFLOPS. For e2e comparison against ep8, qwen30b at 8k seq was 2ms vs 15ms, with both launch bound and groupgemm worse; ds685b at 4k seq was 9ms vs ep8 18ms, where gemm time was similar but ep communication was worse.

## Next Week's Plan

Next week, I will design an FENA3 training optimization solution. The approach will use rinum and zero3 ep.

## Coordination and Help Needed