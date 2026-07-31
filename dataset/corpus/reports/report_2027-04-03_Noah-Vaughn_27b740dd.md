---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T11:11:03+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This Week's Work
For Oskworth, we found and corrected the long first a2a delay that appeared in every step. The root cause was uneven prior-neighbor work: faiss produced different candidate-neighbor totals by rank, so even with balanced atom counts, edge ranks had less work and runtime spread reached 1.79x; the updated neighbor computation lets computing-block ranks assist slower ranks, and rank timing is now balanced. @Kara Ingram Chandler is supporting real-model validation on the 1K-card H200 setup, where overall step time is still below expectation; in the 40-card run, the 1M atom case shows 4s per step with 2s in total communication, and one a2a is 265ms instead of the expected tens of ms, so we are continuing to isolate the a2a latency source. For A100 80G PCIe, tuned NCCL AllReduce settings outperformed defaults by 1.26x~2x across 128K~4MB, and the A100/H100 communication work is now in the custom System-8c4eade5fc plugin. In Qwen3.5-397B-A17B vLLM testing, that plugin raised token throughput by 5.3% at bs=64 with inputlen=outputlen=1024; @Iris Quigley covered the System-8c4eade5fc vLLM run and A100 NCCL all_reduce_perf out-of-place measurements. We also explored additional NVFP4 lossless compression options and reviewed weight statistics from common NVFP4 models: scale-only lossless compression reduced storage by 5.2% for GLM-5, 6.5% for MiniMax, 5.9% for Kimi, 6.5% for DeepSeek, 5.6% for Qwen3.5, and 5.6% for Llama-3.1; this can free GPU memory for KVCache, and the findings are captured in the NVFP4 Multi-Model Compression Analysis Report.

## Next Week's Plan
Next week, we will support OskworthH200 System-67e5ff74fb scaling evaluation. We will also assess communication potential with EP for Vyrbase46+Nyxthorne.

## Coordination and Help Needed