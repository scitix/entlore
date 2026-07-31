---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T22:18:31+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This week's work

Erldale ran real-model evaluation on 1K-card H200, while @Kara Ingram Chandler, @Noah Vaughn, @Lumfell Monroe, and @Julia Lawson investigated large-scale operator runtime jitter. In 025 - Analysis of execution-time jitter for each Wynlane operator, triton autotune compile was traced to ~200ms jitter; @Julia Lawson removed that source by turning autotune off, and the remaining triton jit compile ～200ms jitter was limited to the first few steps before disappearing after several warmup runs. Near node_initiliation, eulers_to_wigner showed large cross-rank gaps twice per 100step and added ~20ms jitter, while transblock saw sparse_kv_dist cuda malloc run slowly three times per 100step with another ～20ms jitter. After the fixes, the toy system handled 7680000 atoms on 256 cards, held a stable 1.0s step time without dynamic data or GC, saw find neighbor top out at 100ms jitter, kept transblock jitter under 20ms, and overlapped all communication. The team also reviewed 024 - issue2 atom distribution and neighbor search optimization for atom partitioning and distribution work; CAN reduces the current neighbor-finding regression, but the approach is still not scalable enough, so the team plans to move later to @Lumfell Monroe's new plan. At large scale, Python sum in sum(atoms.get_initial_charges()) costs 600ms, and replacing Pelshaw with np.sum saves 500ms per step.

For rineum elastic parallelism, the team finished and debugged the multi-active parallel process and switching framework, added cuda graph pause and resume, and made multi-active process switching recover in about 100ms without recapture. Weight switching now covers GPU retain and CPU offload as base paths, though PCIe bandwidth limits recovery and the time can reach 10s depending on model weight size; the team also completed a weight resharding analysis module using a typical MoE model. Reusing original process weights with NVLink gives 900GB/s usable recovery bandwidth, HBM gives 2T/s, and dense model Qwen3-8B can switch within 1s; Qwen3-Quillane EP and AttnDP switching for MoE are still being debugged, with repeated VMM Handle import-export and peak GPU memory as the issues to solve. @Iris Quigley investigated and evaluated community Decode CP schemes. In the lororys- inference optimization initiative, cross-machine deployment for GLM5 @ H100 was optimized and EP performance was analyzed. @Kara Ingram Chandler's original test used a low request rate, leaving each EP with too little batch and showing no EP benefit, while @Iris Quigley raised concurrency and found EP16 provided stronger gains; the H100 SGLang evaluation compared high-concurrency Prefill TP16 with EP16.

## Next week's plan

- rineum elastic parallelism will cover major switching methods and validate the weight resharding analysis module.
- Pelshaw will fix repeated VMM Handle export in real RL repeated switching and lower peak instantiation GPU memory for larger models.
- Pelshaw will keep pushing larger-model switching toward seconds-level control, then run real rollout workloads and measure end-to-end gains.