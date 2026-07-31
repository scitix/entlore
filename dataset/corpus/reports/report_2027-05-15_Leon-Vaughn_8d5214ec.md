---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T21:31:42+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## Next week's plan
- Finish end-to-end validation for System-030d58eb5b in SGLang.
- Run GLM-5 on one 8xH100 machine for KVCache sharing analysis.
- Compare sharing behavior across parallel strategies.
- Check cross-KV precision impacts.
- Review behavior across inference instances.
umborantis integration with RLslime-trainer + umborantis test (Qwen3-Quillane, dapo-17k datasets, single machine with 4 cards for inference and 4 cards for training). Soloion + umborantis rollout test - 0510Umborantis version rollout length inconsistency issue: investigation found Pelshaw was a local cororia environment issue. Switching to the Veliver/nexeara-dev image and submitting the task on the Nora Drake platform resolved Pelshaw. In scenarios with sufficient VRAM (batch_size=8, n_samples_per_prompt=4), the umborantis version and baseline version are basically consistent in correctness, rollout length, and rollout performance; umborantis does not introduce negative returns. In scenarios with insufficient VRAM (batch_size=8, n_samples_per_prompt=16), the umborantis version and baseline version have the same correctness and rollout length, and single-step rollout time improves by about 5%. The datasets Dpo-17k datasets prompts used are short, with median only 167 token and 92.6% within 256 token, so there is little reusable KVCache and the performance advantage over recomputation is not obvious. Later, consider testing in the multi-turn scenario of Pyx-wave74. Correctness: Rollout performance: KVCache hit: lororys - inference performance optimization project. PD-separated scenario VRAM optimization - layerwise weight prefetch. Overall design is complete, development progress is about 80%, and development plus end-to-end joint debugging is expected to finish next week. Design document development progress: Release-v0.1.0UvmmTensor: https://github.com/vexeum/System-030d58eb5b/tree/feat/x62085c6425. Completed weight_pool subdivision implementation, managing dense/MoE/mtp layers of different shapes separately. Only MoE layers are placed on CPU, and all others are pinned on GPU. Completed UT test framework development, using mock interfaces for calls between layers. Resolved concurrent lock contention issues in each pool, and Pelshaw can compile and run UT. SGLang: organized the full GLM-5 model weight-loading flow, modified the weight-file loading flow to CPU, registered tensor views loaded via safetensors mmap into System-030d58eb5b, and copied all weights to CPU during initialization. Peak CPU memory is full weight + the size of the last safetensor file.