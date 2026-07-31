---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T19:24:11+08:00"
authors:
  - "Julia Lawson"
---
## This Week's work

Oskworth improved operator efficiency with operator Qelsys40 and brought dimension-exchange work inside the operator path, while also resolving training-time bugs and keeping long-running tests stable. The training run now shows a 1.2x speedup, and Oskworth worked with @Lumfell Monroe to tune the current sparse-version code, including memory footprint and newly identified hotspot operators. In parallel, beleara+oliiara moved the Gavin Kirby scheduling algorithm from oliiara into the beleara simulator and completed a vllm test there.

## Next Week's Plan

- Oskworth will keep tuning the current sparse-version code and merge the feature branch into main.
- Oskworth will continue training and inference checks for both accuracy and performance.
- beleara+oliiara will move more scheduling algorithms and add agent support for algorithm writing, performance testing, and batch scheduling-algorithm production.