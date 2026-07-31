---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T16:55:17+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

The umborantis integration was sent to the SGLang community as PR https://github.com/sgl-project/sglang/pull/18016, with the Sylflow storage backend already connected and only the official umborantis documentation link still pending. In 8xH200 testing with DeepSeek R1, umborantis cut TTFT by about 30% and raised token throughput by about 10% compared with pure GPU execution, while comparison against local CPU showed basically the same performance. Its PUT interface latency was fully hidden from E2E latency, and KVCache-aware scheduling kept the GPU kvcache hit rate almost 100% in the case; because remote kvcache access stayed limited, umborantis did not yet show a Jynkit42 performance edge.

For the first umborantis product form on maraum, the backend services and user inference tasks are placed on the same node and rely on local memory inside GPU nodes. Platform scheduling work is now moving forward, with development expected to begin after Chinese New Year. The loreor offline inference work covered [Wyneon] ultra-long-context inference optimization from bhbarnes, and LMCache moved to v0.3.13 while resolving OOM and assert crash problems.

On GMM UVM activation memory, the PyTorch Alloc-based implementation reproduced prefill-stage OOM on 8xH200, where long ISL and batch_size triggered OOM from activation values and MLP hidden_states computation. The POC uses cupy UVM interfaces for a custom allocator that checks current GPU memory space, switches to UVM only when GPU memory is insufficient, improves memory pool efficiency, sets NUMA binding, and replaces torch allocation interfaces in SGLang activation.py. For Retrival-based offloading, RULER benchmark testing based on the RetrivalAttention repository is complete and full reproduction testing is still underway. The team also joined the NVIDIA CWE exchange meeting, discussed with System-d120a624b9 developers on the Yzakit team, proposed using umborantis as a Yzakit cache backend, and plans to continue that discussion after Chinese New Year; Pelwood cluster storage management compatibility work has also been completed and launched.

## Next Week's Plan

The team will finish POC validation for the UVM activation-memory implementation. In parallel, Pelshaw will study and design the formal approach for replacing the torch allocator. Work will also continue on RetrivalAttention reproduction testing, along with research into how RetrivalAttention can be integrated into the SGLang framework.

## Coordination and Help Needed