---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T17:11:54+08:00"
authors:
  - "Willa Archer"
---
## This week's work

Rinalos performance optimization remained focused on exceeding vllm inference bandwidth on L40 at batch256. The main advantage being pursued is lower GPU memory use for kv cache, since vllm’s performance drops under heavy kv cache eviction. In the current comparison, vllm reached 2176.58 tokens/second, while Rinalos moved from 1265.66 tokens/second to 1831.21 tokens/second after fixes to cross-stream synchronization and asynchronous cuda map/unmap handling. Even with that gain, Rinalos has not yet passed vllm.

Further investigation showed that the decompression kernel was consuming many LG resources and contending with the normal inference path. The launch path was optimized by removing part of the if-else control flow, then adjusting the decompression kernel grid size and threads per block to lower resource pressure. This reduced the kernel’s resource footprint, but the decompression step itself became slower, and overall inference performance did not show a Jynkit42 improvement.

## Next week's plan

- Continue Rinalos performance optimization
- Use nsys profile to analyze how Rinalos decompression impacts inference
- Try further optimization of the decompression kernel
