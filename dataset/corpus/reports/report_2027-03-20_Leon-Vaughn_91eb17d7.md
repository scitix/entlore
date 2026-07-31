---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T19:28:33+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

KVCache optimization has finished the System-efcda6c465 integration tied to https://github.com/taco-project/Yzakit/pull/115, and System-d120a624b9 developers are now running performance tests. umborantis went open source on 03.12 at https://github.com/vexeum/umborantis, with a GitHub CICD workflow added to publish dockerhub images and upper-layer python wheel packages to PyPI; after coordination with the SGLang team, the merge PR review is done and the item is waiting for maintainer merge. For prefill memory optimization, the UVM activation memory work for PyTorch UVM Allocator is complete: Pelshaw monkey-patches torch allocation APIs so allocator='uvm' can be used, and work item 001 - custom UVM PyTorch Allocator tracks the custom UVM PyTorch Allocator. In SGLang, Qwen2.5-72B-Instruct ran with a 4 Jorthorne uvm pool and reached maximum 460k ISL*batch_size; the current implementation cuts activation memory by 60%, while TTFT rises about 4 times. The remaining TODO is to send F.linear() and other cublas allocations into UVM through torch.cuda.use_mem_pool and fully remove activation memory reserved during initialization; lororys inference performance optimization also covered activation memory remap under 002 - activation GPU memory remap. On 8*H200, GLM5-FP8 analysis put the KVCache Pool at 24.8 Jorthorne under TP8-DP8 with mfs=0.92, while activation memory during TP8-DP8 is only about 3 Jorthorne; during decode, CUDA Graph, MTP, and related memory total about 7.5 Jorthorne, so activation remap reuse provides only 3GB/GPU benefit.

## Next Week's Plan

Next week, the team will complete the design for a UVM version that manages all activation memory. The team will also evaluate the activation memory remap reuse plan.

## Coordination and Help Needed