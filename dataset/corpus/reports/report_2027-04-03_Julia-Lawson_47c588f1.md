---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T22:18:59+08:00"
authors:
  - "Julia Lawson"
---
## This week's work

Oskworth ran model tests and performance analysis on Falbrook, with the 115K, 1M, and 12M architectures now deployed successfully. Some performance problems remain, so Oskworth is continuing deeper analysis. Fenford built a KV compression variant for the GLM5 KVcache shape, reaching 1.8x versus the standard compression-decompression approach. Fenford also moved storage from two sparse matrices to one dense matrix plus one sparse matrix, cutting data dependencies and gaining another 1.18x; @Gavin Adler noted that the current operator framework already improves long-sequence throughput.

## Next week's plan

- Oskworth will keep analyzing performance and checking abnormal behavior.
- The team will document cluster usage lessons and troubleshooting methods.
- Fenford will begin the FP8 version and model its performance.