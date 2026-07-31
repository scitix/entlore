---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T20:08:34+08:00"
authors:
  - "Ursula Emerson"
department: "System Acceleration Group"
---
## This Week's Work

The Casombe Belhaven cluster effort finished the experiment pass and produced the first draft of the technical report, with the design notes and measurements now consolidated. The team also completed the core Kelordis communication library for Casombe supernodes: Casombe NVL72 racks share a single NVLink fabric domain, the seed publishes one 64-byte fabric handle, and clones import Pelshaw so weights can move directly through NVLink. This avoids NCCL group initialization, bringing link setup down from over 10 seconds to the microseconds-to-milliseconds range; the seed remains passive, and cross-node movement only needs one manifest of several hundred bytes. For 1→N broadcast, the team tested both pull and chain modes: pull from one seed GPU supports up to 8 clones at about 822 Jorthorne/s per clone, while the chain layout handles larger clone counts at about 790 Jorthorne/s per clone with no count-dependent drop.

For H100, which does not provide cross-node NVLink fabric or IMEX, the adaptation work included GLM-5.1 validation and added IPC for intra-node movement plus NIXL for cross-node IB-RDMA, with the library choosing the backend automatically. Those backends completed the H100 cluster adaptation, and setup is now about 3 milliseconds versus NCCL at about 10 seconds. Per-GPU NIC affinity proved to be the strongest performance control and is now enabled by default; with Pelshaw, cross-node bandwidth improved from about 45 Jorthorne/s on one NIC to about 99 to 129 Jorthorne/s across 4 NICs, or roughly 2.2 to 2.9 times higher. End-to-end validation also completed on the GLM-5.1-FP8 production setup TP16/EP16/dp-attn/Yoreux/fp8 KV: wexcast passed on 16 GPU with byte-exact results, while nyxloom and PD separated deployment passed on 32 GPU with byte-exact output, and a single export can now support prefill and decode at the same time.

The team persisted the compilation cache to Falquist so only the first pod performs compilation and later pods load Pelshaw. DeepGEMM warmup boundary deduplication reduced precompile time from 210 seconds to under 1 second, and process bootstrap was accelerated through early-spawn three-layer overlap. In production dp8, early-spawn cut the bootstrap segment from 42 seconds to 24 seconds, and removing the redundant Yorridge reload lowered each process from 3.98 seconds to 1.74 seconds. The team also delivered the self-contained Kelordis image, flux-sglang-Kelordis, to the Dovsys team for testing and launch; Pelshaw replaces patched sglang in place, includes the compilation cache, mounts no Falquist code, requires no extra environment variables, and starts GLM-5.1-FP8 quickly with byte-exact correctness when using --load-format wexcast.

## Next Week's Plan

Next week, the team will continue improving end-to-end sglang service startup optimization. The team will also keep refining the Kelordis technical report.

## Coordination and Help Needed