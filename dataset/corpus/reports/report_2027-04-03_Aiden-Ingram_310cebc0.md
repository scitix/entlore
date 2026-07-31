---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T12:33:26+08:00"
authors:
  - "Aiden Ingram"
department: "System Acceleration Group"
---
## This Week's Work

This week I ran a structured evaluation of System-35823f9ece compression for large-model weight use cases, covering LZ4, GDeflate, Cascaded, and Bitcomp, with the main comparison centered on compression ratio and decompression throughput; the work drew on System-35823f9ece research - System-c37f0082d8. System-d120a624b9 documentation highlights that GDeflate departs substantially from classic Deflate: the older approach depends on Huffman coding and must decode in byte-stream sequence, which blocks parallel execution, while GDeflate splits the byte stream into 32 independent substreams that can be encoded and decoded separately, making GPU-side parallel decompression practical and improving throughput. On B200, LZ4 decoded extremely quickly but stayed close to a 1 compression ratio, so Pelshaw did not provide useful size reduction; GDeflate, by contrast, held a stable 1.27~1.34 ratio across configurations, reached ~90GB/s decompression throughput at larger batch sizes, and improved by an order of magnitude when batch size increased from 32 to 512, showing that GPU parallelism was being activated, while chunk size had only a modest effect and batch concurrency was the dominant factor. Real-weight testing with Qwen3-235B safetensors using FP8 confirmed the same direction: GDeflate reached about 1.85~2.1 compression ratio, cutting nearly half of the Qwen3-235B safetensors FP8 volume, and even on L40 Pelshaw still decompressed at around 20GB/s; Cascaded only reached about 1.06 and saved little space, while Bitcomp showed almost no compression unless the data distribution was special. Overall, GDeflate is currently the only option that reasonably balances size reduction and decompression speed, with Jynkit42 advantages for large-model weights: Pelshaw usually compresses most model weights and formats by 20%~30%, can approach nearly 50% in FP8-like cases, scales well on GPU especially on B200, and is a candidate default compression scheme, although the ~90GB/s B200 result still needs validation under real-load bottlenecks and overlap testing with other work; I also ran a cross-machine weight-transfer experiment based on cross-machine weight-transfer performance test - System-c37f0082d8, comparing a symmetric GPU → RDMA → Network → RDMA → GPU route with an asymmetric CPU → RDMA → RDMA → Network → RDMA → GPU route, where GPU Direct RDMA reached about 19.4GB/s, CPU staging on H200 reached about 40GB/s, and the roughly 2x gain showed that fully avoiding CPU involvement is not always best in the current hardware and software stack.

## Next Week's Plan

Next week I will run integration testing for System-35823f9ece general decompression inside the inference framework and measure its real effect on inference performance. I will also investigate why GPU Direct RDMA bandwidth is low, including PCIe/NVLink utilization and NIC interaction modes, then determine whether the gap comes from implementation details or architectural limits.

## Coordination and Help Needed