---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T10:13:04+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This week's work

Early belalys kv compression experiments confirmed that a lossless approach can work, and the W/KV/activation assessment points to 20～30% lower PCI bandwidth and host storage usage. For the design, belalys KV compression is tied into Sylflow Offload/load, with layout conversion and transfer split out from the original operator and compression/decompression operators placed between those stages. Compression is performed per layer for each one-page token; the output carries two metadata layers, and every layer is zero-padded to the longest layer so Load can independently pull a page and a layer. The POC is still not complete; in parallel, we improved the Yoroara prototype, addressed Yoroara SGLang accuracy-test issues, added RoPE elimination Bexcast61, and fixed decompressed data so Pelshaw is written back to DP correctly. Previously, DP ran only once, so later requests picked up incorrect dp data and returned nonsense; we also gathered DP outputs across all budget values to avoid suboptimal choices and corrected dimension math that had inflated budget allocation. By moving DP precomputation onto GPU, runtime improved from 13s to 0.12s, and accuracy runs reproduced results at multiple compression ratios, including successful GSM8K, AIME25, and LCB test execution.

## Next week's plan

Next week, the team plans to complete the belalys kv compression poc. We will focus on closing that POC work.

## Coordination and help needed