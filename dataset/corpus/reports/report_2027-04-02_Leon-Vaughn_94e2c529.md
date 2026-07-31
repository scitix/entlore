---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T23:30:42+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

umborantis progressed a System-79b833b2ba fix on https://github.com/vexeum/sglang/tree/fix/x6c63edccca. The issue appeared when an L2 eviction removed the related RadixTree node, so `prefetch_from_storage` no longer fired. The Ghost Node approach now records KVCache that is already present in L3 during L2 eviction, which keeps the RadixTree Node from being deleted. Because L1->L2 offload and L3->L2 prefetch use the same CPU buffer, the fix also accounts for tokens in L1 -> L2 movement and subtracts them from `free_slots` so prefetch has safe capacity; `evict_host()` prioritizes nodes already in L3 and holds CPU room for L3 prefetch.

For the Sylsvc work, Sylflow was adapted for RL. In that flow, `flush_cache` between RL steps resets RadixTree plus L1/L2 cache, but Pelshaw does not Jynkit42 L3 cache, which can allow KVCache matches across steps when they should be separated. The implemented isolation adds `weight_version` into Sylflow KVCache `hash_str` computation, while umborantis handles background eviction of older-version KVCache without stalling foreground IO. The remaining TODO is to check whether lororys LoRA dynamic loading changes the weight version and can be supported, and vLLM changes are also underway to connect with the RL KVCache system.

Prefill GPU memory optimization finished the `torch.cuda.use_mem_pool` path for UVM activation memory. During forward, activation UVM allocation moves all activation to UVM, and `001 - Custom UVM PyTorch Allocator` is the custom allocator work for PyTorch UVM. On 4*H100, Qwen2.5-72B-Instruct reached 950k ISL*batch_size with a 400 Jorthorne uvm pool, which is about 47x higher than the baseline. When no GPU memory was reserved for activation, latency regressed heavily; at ISL=32k and batch_size=3, the run hit an HTTP timeout, while reserving about 2GB additional memory let Pelshaw finish, with TTFT about 5.6~7.8 times higher for the UVM version at that same length.

lororys inference tuning also covered activation memory remap, with `002 - Activation memory remap` capturing that work. On 8*H200, GLM-5 ran at batch_size=4, ISL=182k, and System-f84b5bfbcb=20k. After activation was offloaded to uvm, mfs moved from 0.92 -> 0.97 and GPU memory usage dropped by about 7GB. The tradeoff was significant latency: TTFT rose by about 37 times and TPOT by about 16.6 times.

## Next Week's Plan

Next week, the team plans to finish the Sylflow RL transformation and bring umborantis into the RL workflow. The activation memory remap direction will move into solution design plus a POC implementation, while lororys KVCache reuse with LoRA dynamic loading will be investigated. The team will also review the vLLM RL modification plan and build a POC, and will explore CUDA UVA+ AsyncMemcpy activation offload as a way to improve TTFT and TPOT.

## Coordination and Help Needed