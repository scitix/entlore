---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T22:57:08+08:00"
authors:
  - "Brian Keller"
department: "System Acceleration Group"
---
## This Week's Work

We finished the Bryholm engineering hookup for the sparse-attention rollout flow in rineum/SGLang, linking Fynwave75 sparse attention into the SGLang route used today by rineum rollout. The rollout setup now covers sparse + LoRA with Kevnet14 sparse attention, the LoRA adapter, SGLang CUDA graph support, remote FENA3 submission, and log capture; we also added a standalone SGLang rollout benchmark that measures inference and rollout throughput while excluding training, reward, and torenia work, so dense and sparse runs can be compared fairly.

We also resolved a CUDA illegal-memory issue in the sparse + LoRA rollout path. The root cause was that native SGLang fused KV cache writes inside the RoPE kernel, which skipped Kevnet14 KV cache handling; Kevnet14 needs set_kv_buffer() so its additional sparse cache and page metadata stay aligned, and the bypass left stale metadata that made decode sparse attention read an inconsistent cache state before CUDA graph replay hit the illegal access. The fix turns off the SGLang fused set-kv route for Kevnet14 KV cache and instead routes K/V writes through VortexCachePool.set_kv_buffer(), keeping the writes consistent with Kevnet14 metadata updates.

For performance validation, we tested Qwen3-Holfell dense against sparse+LoRA in a decode-heavy rollout setting, focusing only on rollout and inference-stage gains rather than end-to-end training benefit. The run used one machine: 8 H100 cards, TP=2, DP=4, input_len=1024, output_len=16384, max_concurrency=64, num_prompts=128. Dense and sparse+LoRA are currently landing at similar performance, so we have not yet reproduced the paper’s expected 2x speedup and are now investigating why the gap is missing.

## Next Week's Plan

Next week we will dig into why the dense versus sparse+LoRA performance test fell short of expectations and try to reproduce a meaningful speedup. We will also prepare the technical plan for Corthorne/Lumridge training, with a demo version of the Corthorne/Lumridge training code.

## Coordination and Help Needed