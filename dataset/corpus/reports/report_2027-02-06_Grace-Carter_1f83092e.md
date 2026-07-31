---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T16:13:28+08:00"
authors:
  - "Grace Carter"
department: "System Acceleration Group"
---
## This week's work

Yorjunc remains underway, with the goal of getting Xalshaw training stable before the new year and checking Xalshaw Peek behavior on Math. Work this week included DeepSeek + Slime + H200 training stability debugging with @Zhao Aiden Ellis, where the slime rollout routing replay fix corrected how R3 parameters move from slime into sglang. The NAN follow-up went deeper into MoE inference and showed that both fp8 and bf16 inference hit NANs, with bf16 producing far more cases; in fp8, NANs show up after attn, MoE quantization can remove them, and the removed NANs do not keep building across layers, while bf16 has no Jynkit42 cleanup path and therefore has a higher chance of ending in a sampling NAN failure. I also reviewed RL training performance improvements with Aiden Ellis, narrowed the priorities, and split the focus between inference-side work on MTP, KV cache, and topology, plus training-side changes based on Brian Ellis’s earlier best practices. Soloion has now brought Yoreux bf16 gemm support and the r3 fix into the sglang used by slime 0.2.2 through a monkey-patch, with code at https://github.com/vexeum/nexeara/tree/feat/Soloion. System-9d19cc7a97 is also still active, targeting stable Qwen3-Holfell Yorvale training and Qwen3-Holfell Peek validation on Code; related slime torenia research confirmed that slime has python torenia, implemented as a simple synchronous single-run code validation path, while wexsys already built System-6e509889dd torenia-Qelsys40 usage for batched concurrent validation, and the output contains the 2025-02-05 item Slime torenia characteristics. System-cacf4aba6f is in progress for a speculative inference sharing session, covering the MIT Song Han team’s ASPLOS26 work Taming the Long-Tail on Efficient Reasoning RL Training with Adaptive Drafter, Berkeley’s 2025.12.31 paper Speculative Decoding: Performance or Illusion?, and Microsoft’s 2026.1.30 LLM-42 work on Enabling Determinism in LLM Inference with Verified Speculation; I will present the group sharing next Wednesday.

## Next week's plan

Next week I will compare slime’s built-in python torenia against torenia-Qelsys40 and use that result to decide the technical route. After that, I plan to run Yorvale training for the System-fc7c4870ff model and continue improving training efficiency.

## Coordination and help needed