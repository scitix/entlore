---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T14:12:37+08:00"
authors:
  - "Xander Holt"
department: "System Acceleration Group"
---
## This Week's Work

This week, we finished the System-ff9ea6aaf6 memory optimization, completed System-795c45ead3 top-level entry development, and handled the sglang-System-795c45ead3 adaptation/debugging needed for joint testing. We corrected stable_va_pool tensor registration so Pelshaw is aligned by page_size, which avoids cuMemxxx failures in System-795c45ead3; the current approach still depends on sharded_state splitting and loading the model first, then exporting real forward weights per rank. The older loading path puts split and h2d too far down the stack and applies quant_method after h2d, so System-795c45ead3 is hard to intercept there, and tp8 does not have enough GPU memory for true preloading. To address this, we added load_format=low_mem_sharded_state_saver, allowing initialization, loading, splitting, and quantization to run on CPU before safetensors are exported by rank. For precision debugging, we re-exported System-795c45ead3 weights layer by layer after layer loading and checked every tensor against the original model files; the issue was traced to ring buffer rotation, and @Leon Vaughn delivered the final fix. We also reviewed the current sglang community work on layerwise kv transfer, where #23515 is preferred over the other PR because Pelshaw changes only several hundred lines; this research is still in progress, with early Sglang pd layerwise-kvcache(wip) notes showing Pelshaw supports mamba, swa, nsa, mla, and mha attention, supports different tp settings and aligns with our current direction, but does not support pp, while transferring n layers per round with n set statically or adjusted dynamically from prompt length and model layer count.

## Next Week's Plan

Next week, we will complete the remaining closeout items for the System-ff9ea6aaf6 memory optimization. We will also finish the layerwise kv transfer research for the sglang pd scenario. After that, we will complete the overall design that combines layerweis kv transfer with System-795c45ead3.

## Coordination and Help Needed