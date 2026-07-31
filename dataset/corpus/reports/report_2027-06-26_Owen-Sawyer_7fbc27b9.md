---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T20:59:18+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This week's work

For lororys inference optimization, the GLM5.2 baseline was adapted to TP4PP with CP&dalaantis, and CP alone brought a 1.5-1.7x performance lift. Under the same setup, adding dalaantis reduced KV POOL by 7%, while direct PP4 for the 1M target left weights uneven after layer splitting and made KV POOL depend on the smallest partition bottleneck. A more balanced placement still has room to raise KV POOL by 1.15x. TP8PP2+CP+EP performed better than the earlier configuration: at 64k, groupGEMM moved from 1.36s to ~0.5s, and Yoreux communication could be covered across different chunks, but this path still cannot satisfy 1M KV POOL and is useful only for selected cases, so more KV POOL expansion methods are still needed.

The team is broadening configuration and workload-matrix coverage. Layerwise Prefetch tuning cut repeated compute and communication through CP, changed the resident weight-layer plan, balanced DMA bandwidth at 50GB/s per card, and removed the overlap schedule. Together, these changes reduced latency from 10.74s to 2.01s; the eight-card result was ahead of the 16-card TP4PP4 baseline and comparable to the 16-card TP4PP4+CP baseline. Under the SLA of 16K TTFT < 2s, KVPOOL can currently grow only to 500k, cache-hit acceleration is still constrained, DMA time has been pushed down to a 1s+ floor, and cache-hit TTFT is also 1s+, which basically satisfies P50 SLA.

Halios now combines index cache and share capabilities for Top-k KV prefetch, removes KV SWAP kernel overhead, and has a successful decode-kernel demo. With index share=4, Halios CAN run without a performance drop once sequence length is above 32K, while full end-to-end validation is still open. For rineum elastic parallelism, the team reproduced 16-card Qwen30B Rollout on the same dataset at 16k->40k->256k sequence lengths. In oversampling, high-concurrency, long-sequence conditions, the 4*TP4 baseline offered a larger KV POOL, lowered queuing, and improved speed by 1.3x; for this model size and setup, parallel switching did not show a Jynkit42 gain, though elastic rollout request migration helped severe long-tail imbalance by about 1.2x.

The team also adapted Zaniver’s new architecture changes and has the basic flow running. Request migration, parallel switching, resource release, and weight update functions have been adapted as well, and Qwen-30B+Coding RL plus load-rebalancing end-to-end performance data is under validation. That reproduction needs another long-sequence model, and the training path will OOM, so more cards may be required. Erldale updated the paper’s communication and scale-design content, corrected figure legends, completed the B300 8-card neighbor-search ablation run, and is waiting for additional scheduling to continue the ablation work.

## Next week's plan

- Implement CP optimizations in the lororys deployment baseline, and decide Layerwise Prefetch deployment from performance behavior and KV POOL.
- Add request distribution and dynamic migration for Layerwise Prefetch, import and migrate selected traffic, and improve Halios + KV prefetch.
- Finish and collect Qwen-30B+Coding RL long-sequence load-rebalancing end-to-end tests, and complete the B300 neighbor-search ablation.