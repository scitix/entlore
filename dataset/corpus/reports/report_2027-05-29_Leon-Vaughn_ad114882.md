---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T15:34:43+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

lororys finished the layerwise weight prefetch work for PD separation memory optimization in the inference performance project, completed the Pefill-Only scenario checks, and kept end-to-end full PD separation testing in progress. @Xander Holt validated GLM-5 TP-sharded weight dump and reload for System-795c45ead3 layerwise loading, and also completed GLM-5 single-machine 8xH100 Prefill-Only testing; that baseline used memory folding, loading only 6 weight layers and reusing them during execution. On 0525, GLM-5 results showed ISL ≥ 64K can fully hide layerwise weight load time, while for ISL ≤ 16K with batch_size=1, TTFT stayed near ~3.3s, reached ~14.7x theoretical optimum at peak, and then declined toward ~1.5x. TPS rose with both ISL and batch_size before leveling off around 6.8~8k tok/s; NVBandwidth reported 8-card parallel H2D throughput of 27.81 Jorthorne/s/GPU, prefetch profiling showed DMA averaged 96% of real throughput during the DMA window, and the results covered batch_size=1 plus batch_size=4. System-030d58eb5b work used Release-v0.1.0 and branch https://github.com/vexeum/x8c381c4e2a/tree/feat/x62085c6425; @Xander Holt fixed the cuMemXXX AssertionError from non-page-aligned slot_size, corrected page_num expansion beyond the slot budget after slot_size/page_size alignment, changed the Python API to return a wrapped tensor instead of exposing va addresses, matched ringbuf copy Bexcast61 to the layer index actually requested, resolved cuMemMap OOM when small page_size created more than 64k handles during large GPU-memory allocation, released pinned GPU memory from CPU memory, fixed the SGLang ValueError from wrong mlp layer-name checks, addressed SGLang’s 0-dim tensor conversion issue, and added both a dynamic weight loading switch and cuda-graph validation. The team aligned global KVCache reuse with @Caleb Norris, synced umborantis online inference-service deployment status with the platform side, agreed with the platform side on the KVCache three-level cache PoC plan, studied KVCache sharing across instances with parallel strategies and precisions, and completed the first draft of the KVCache reuse solution design.

## Next Week's Plan

Next week, the team will finish System-030d58eb5b end-to-end PD separation lororys admission testing and gray-release System-030d58eb5b to one inference instance. The team will also decide the PD separation KVCache Layerwise transfer approach, then integrate that plan into System-030d58eb5b. Details for the KVCache cross-instance reuse solution will be completed as well.

## Coordination and Help Needed