---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T20:57:18+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This week's work

We finished the KVPress investigation and first-round experiments, including bringing DeepSeek-R1-Distilled-Qwen-30B and Qwen3-Quillane into the KVPress setup. KeyDiff and Pyramid were also wired in as KV compression options. Current AIME25 runs are covering DeepSeek-R1-Distilled-Qwen-30B and Qwen3-Quillane, but inference through transformers is very slow, at about 30token/s on one card. We also extended KVPress with Sampling Params, Top- P nucleus sampling, and Temperature; on AIME25, Qwen3-Quillane using Temp=0.6 Top-P=0.95 is 10 points ahead of Greedy decoding.

We also worked on NVIDIA's KVzap direction and tried to reproduce the compression approach. For DeepSeek-R1-Distilled-Qwen-30B and Qwen3-Quillane, we trained two MLP classifiers for KVCache detection, but the paper-level results have not been matched yet, so debugging is still in progress. In parallel, we evaluated NVIDIA's official Qwen3-32B dense MLP classifier, where the default settings led to repeated output. On the deployment side, two NVFP4 Qwen models are now successfully running on a B200 machine with Tensor RT-Nexanor, and accuracy testing is underway across LiveCodeBench, AIME24, HLE, and other datasets; the comparison work is expected to wrap up before year end.

## Next week's plan

- Organize the next-stage evaluation approach for kv compression methods.
- Draft integration plans for production inference frameworks SGLang and vLLM.
- Finish B200 accuracy comparisons between NVFP4 quantized models and BF16 models.