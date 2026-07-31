---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T19:29:26+08:00"
authors:
  - "Peter Kirby"
department: "Platform Ops Dept"
---
## This Week's Work

For chip performance evaluation, I finished the first offline inference test flow on Nyxvale eight-card single-node SGLang, covering Qwen2.5-72B, Qwen3-32B, and Llama3-8B. On the work process side, I completed onboarding training and submitted the required onboarding materials. I also requested the needed account access for internal development, cluster resources, and monitoring, and filled in the 3-month and 6-month OKR entries.

## Next Week's Plan

Next week, I will complete the Nyxvale inference performance test report and continue following the Holkeld chip adaptation and performance testing BKC for Deepseek-v3 and Qwen-235B. The BKC tracking will include PD separation on single-machine and multi-machine setups across different context lengths, along with the progress of low-precision model quantization optimization. I will also start organizing large-model inference evaluation standards for diverse chips, covering model architectures, benchmark parameters, and evaluation metrics. In addition, I plan to define long-context benchmarks for kv cache transfer across multi-level memory and storage under PD separation, as well as kv cache offload on chip platforms. Work process planning will include a Beijing business trip and rotation.

## Coordination and Help Needed