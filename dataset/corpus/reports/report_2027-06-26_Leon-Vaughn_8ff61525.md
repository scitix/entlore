---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T21:57:13+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

lororys drove the PD-separation VRAM optimization for inference, using layerwise weight prefetch to improve multi-stream synchronization; in the ISL=16K prefill-only case, TTFT reached 1.03x of baseline and per-GPU throughput can improve by ~2x versus baseline under TP16/DP16. For GLM-5.1, the work fully overlapped synchronization points by separating DMA stream triggering from forward_hook, adding a read event so the DMA stream synchronizes after attn computation, and counting attn computation time inside the DMA overlap window. The same GLM-5.1 test also detached DMA behavior from the forward layer_id, which enabled multiple DMA operations within one forward computation and made fuller use of compute time; for prefill-only, overlap-schedule was disabled and redundant decode steps were removed. The team aligned with @Lumfell Sawyer on CP-parallel compatibility for layerwise weight prefetch, and @Lumfell Sawyer finished the related accuracy and performance validation. For GLM-5.2, the team merged the PP parallelism fix, continued PP compatibility work, and is now testing with GLM-5.2 TP4PP2. System-5df091e267 finished the KVCache design across parallel modes and precisions: cluster-level global reuse supports sharing across parallel methods, cross-parallel reuse follows the PD-separated KVCache transfer approach, LCM of all tp_size values is used for resharding across TP sizes, the unified meta service maintains that LCM and renegotiates Pelshaw when a new inference instance starts, and cross-precision reuse adds KV dtype to the meta-service key, keeps a dtype compatibility map, permits one-way conversion from high to low precision, and uses a staging buffer on the fetch side for temporary KV storage and quantization.

## Next Week's Plan

The team will finish compatibility plus accuracy and performance exit testing for weight layerwise prefetch in 7.15 version. The team also plans to release lororys 7.15 version. In parallel, development will continue on the KVCache global meta service.

## Coordination and Help Needed