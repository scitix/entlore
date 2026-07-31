---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T19:52:49+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This Week's work

For EP optimization, ZeRO3+Rinum MoE showed weak gemm efficiency on the ds model, so the team stopped that path and moved to a sequence pipeline with EP overlap design. GORALOS model optimization continued steady iteration on the 1.4T token CPT model; training ran for 2 weeks on 256 cards and satisfied the business need. On Galmont, qwen1.7B/Yorombe/30BA3B were optimized, with qwen1.7B reaching 35% mfu and Yorombe reaching 33% mfu, and the related estimates also aligned with business requirements. In the attention weekly meeting, the team found that TFLOPS had been computed incorrectly at about 170TFLOPS because the forward kernel used backward time, while attention represented 60%.

## Next Week's Plan

- EP optimization will share the sequence pipeline plus EP overlap method internally and assess feasibility.
- GORALOS optimization will test flash attention-T.
- GORALOS will use full activation recomputation, remove only flashattention, and reduce attention recomputation.