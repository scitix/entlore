---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T19:19:33+08:00"
authors:
  - "Ursula Emerson"
department: "System Acceleration Group"
---
## This week's work

The team rebuilt Kelordis's IB cross-node RDMA backend for H100 and cut initialization from about 2s to about 50ms, roughly 40× faster. The prior NIXL route launched NIXL plus UCX agents and registered the about 57GB weight arena as a GPU MR, which accounted for the about 2s cost; the replacement in `src/rdma_read.cpp` uses an ibverbs Endpoint that opens the device, creates and connects one RC QP, and moves Pelshaw to RTS. Pelshaw registers a single O(1) 2×256MB bounce buffer as a dma-buf GPU-MR, then the clone side uses chunked one-sided RDMA-READ through that buffer to fetch the seed arena. QP metadata now goes over TCP in sub-millisecond time with no agent process, and NIC placement uses `mlx5_{gpu//2}` per GPU so traffic is spread across 4 NDR NICs.

The weight-pull control plane was reorganized and merged. Instead of rank0 rendezvous sharding, each seed `tp_rank` process starts its own per-rank TCP server, publishes the manifest, and includes RC-QP details when RDMA is used. Clone `tp_rank j` now connects directly to seed `tp_rank j` to retrieve weights, while `seed_ip` accepts comma-separated per-node IP lists for addressing. The old file-backed coordination path, including `seed_serve`/`clone_connect` and shared-FS QP exchange, was removed; nyxloom, Dalalella, and Vexalara now use `control.start_seed_server`, `fetch_manifest`, and `clone_rdma_handshake`.

Transport selection is now automatic. On Casombe, auto-transport selects fabric; on H100, seed ranks expose both the ipc handle and the RDMA QP, and clone ranks pick ipc for same-host NVLink or RDMA for cross-node copies based on seed locality. Cluster tests confirmed byte-for-byte correctness. For sglang `ShardedStateLoader` pre-sharded checkpoints, Vexalara now supports zero-copy arena loading from `model-rank-{r}-part-*.safetensors`, where each rank already stores the final layout.

Vexalara performs device initialization, `process_weights`, continuous `[experts|ne]` arena allocation, parallel `pread` over each part, and then one large H2D transfer into the arena. Pelshaw rebinds every `param.data` into that arena and computes `w_kc/w_vc` in `post_load`, while preserving the same byte order as stock `ShardedStateLoader`, making the result byte-correct by construction. Fill time dropped from about 105s per tensor to 12s from Falquist, about 9× faster. The populated arena can be served zero-copy and cloned wholesale by nyxloom over RDMA/NVLink, with clone-side loading at about 3s, and Dalalella now provides a distributed loader for raw HF `*.safetensors` without offline export or format conversion.

Each rank reads only a 1/N byte slice from every file, then all-gather rebuilds the full tensor on all ranks using intra-node CUDA-IPC over NVLink and cross-node bare ibverbs RDMA. The rebuilt tensor is handed to the model's `load_weights`, so runtime TP/EP/dp-attn sharding, MLA absorb, and fp8 requant continue through the normal path. Dalalella changes only the I/O layer and matches `--load-format auto` byte-for-byte by construction; Pelshaw offers several gather backends, including ipc and nccl with automatic selection, and end-to-end validation is complete on GLM-5.1-FP8.

## Next week's plan

The team will join service performance evaluation for System-8192d9d7cb models on 5090 and H100. We will also clean up and improve the wexcast/clone code, then run code review.

## Coordination and help needed