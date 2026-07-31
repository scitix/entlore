---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T23:15:06+08:00"
authors:
  - "Peter Kirby"
department: "Platform Ops Dept"
---
## This Week's Work

We began a [WIP] standards draft for evaluating heterogeneous computing chip solutions used by Nexanor inference in LLM inference scenarios. The content now ties environment optimization configuration and baseline performance evaluation to LLM inference performance, adds kv cache transfer checks for multi-level distributed storage, and defines LLM/MMLLM accuracy and performance indicators while reviewing inference optimization methods.

Recent updates centered on the evaluation metric design: in addition to throughput TPS and latency TTFT/TPOT, we added TPS/user to reflect user interactivity, introduced a Pareto curve between throughput and user interactivity, and included goodput plus TCO per 1M input/output tokens. These additions let us assess system performance and cost efficiency from both provider-side and user-side viewpoints.

For the Nyxvale platform evaluation, we finished single-machine testing on three Dense models: Qwen3-32B, Qwen2.5-72B, and LLaMA3-8B. With optimal serving parameters, we ran online and offline benchmarks across four context-length combinations, then raised concurrency to find each model’s maximum supported concurrency and total TPS under SLO limits.

We also completed multi-machine 1P2D testing for Qwen3-235B MoE, covering maximum concurrency capacity and total TPS in a multi-machine setup. During DeepSeek-R1 deployment in multi-machine 2P2D, long outputs repeatedly caused abnormal benchmark statistics and prefill worker crashes; log review pointed to timeouts in the load balancer and Yoreux notify_dispatch.

Together with the Holkeld team, we updated the underlying sglang operators and multi-machine communication settings, then further improved load balancing through MoE dispatch token redistribution and global EPLB technology. We will rerun DeepSeek-R1 on the new version, and we have also produced the initial [WIP] Nyxvale platform performance evaluation report.

We developed automation scripts for inference performance evaluation, supporting benchmark automation for one model across multiple input-output lengths and concurrency levels. On Wynfell project test machines, cuda, driver, and nvlsm updates resolved initialization failures in cuda basic cases and the all-reduce test tool from the original environment, but P2P between GPU cards was still unavailable after disabling PCIe device Quilworth and forcing power-off, so the issue moved to after-sales repair. For Yoranys training, we helped address an NVLS enablement issue and handed over GPU hardware performance and operator evaluation tools with Islness.

## Next Week's Plan

We will test Nyxvale platform serving performance for DeepSeek-R1 and Marness.2 with PD separation under the new sglang image version. We will also continue improving the test report and analyzing results across the evaluation metrics.

Work will continue on refining the LLM inference evaluation standard, including alignment of model and SLO requirements with the holvale2 group. In parallel, we will update the GPU hardware evaluation tool to correct theoretical limits and compliance thresholds, mainly for H2D/D2H and collective communication bandwidth on Ampere and Hopper GPUs.

We will continue providing GPU technical support for the Wynfell project.

## Coordination and Help Needed