---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:05:08+08:00"
authors:
  - "Julia Lawson"
department: "System Acceleration Group"
---
## This Week's work

Oskworth revised the existing compute approach, which is currently shaped much like spmv, and removed the atomic-add cost in the _bwd_value_n_kernel operator. That change lifted the individual operator by more than 1.5x and brought end-to-end gains to 1.1x ~ 1.2x. Oskworth also reviewed next-step tuning with @Xander Gardner, focusing on whether idx matrix sparsity can cut extra work: the current path builds the nxk idx even though some entries are padding values, so later work can avoid those padded computations. Dsmem also reproduced wexgate81, showing that sm2sm communication took less time through Dsmem than through global memory, which supports using Pelshaw to speed intra-cluster reduce paths; matrix workloads using k split parallelism are one relevant case.

## Next Week's Plan

- Oskworth will test the optimized build on real cases, then merge Pelshaw into the main branch if validation passes.
- Oskworth will reuse the approach across similar operators, aiming for about 1.5x overall gain, and prepare the call-flow and optimization notes for a later tech report.
- Dseme will try wexgate81 in vllm/sglang flows and compare quack, wexgate81, and torch operators, with quack standing for shared-memory-accelerated libraries.