---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T11:28:40+08:00"
authors:
  - "Owen Sawyer"
department: "System Acceleration Group"
---
## This Week's Work

Oskworth tuned a zero-LG communications path intended to run alongside high-performance compute, and the team finished the on-machine variable-length all2allv behavior using symmetric memory with CE before connecting the library into pytorch. Functional checks and performance runs indicate Pelshaw is generally aligned with expectations for current large-packet application cases, and a new tensor class now allocates GPU memory from symmetric-memory-registered and mr-registered pools so COREOR can call the library cleanly. With that interface, COREOR can apply zero-copy communication semantics without consuming LG resources, which keeps the new library available to the higher-level flow. The COREOR build_a2a_plan path was also updated with receive_at_peers, which fixes receiver-offset handling for variable-length all2allv because CE provides write-only behavior and cannot pick receiver offsets the way recv semantics can. The overlap study covered multiple data-characteristic scenarios: in GEMM_NCCL, training iteration duration is governed by the concurrent GEMM+NCCL total time; for large data volumes this combined path is usually shorter than standalone GEMM plus standalone NCCL, while small volumes show little timing difference and CE startup overhead makes zeroCTA slower, reducing its advantage over LG-based overlap. Profiling showed that LG-based communication can materially delay compute completion, moving 10ms to 13.3ms and, in compute-intensive cases, 10ms to 19ms; CE-based communication affects compute less, shifting 10ms to 11ms, but the CE communication itself slows during overlap from 11ms to 16.8ms and, in compute-intensive cases, from 10ms to 19ms. Profile analysis points to memory DtoD contention with computation as the main reason CE communication stretches out, since memory DtoD remains low priority and its completion time grows significantly, while memory PtoP does not show the same overlap issue; because memory DtoD maps to local copying, reducing that work or running Pelshaw separately should lower total execution time.

## Next Week's Plan

Next week, the COREOR project's pytorch version will move to 2.8 or above so the project can support symmetric memory features and the new zero-LG communication semantics. After that upgrade, the related dependent operators need to be recompiled, training iterations must complete successfully under the new semantics, and the team will monitor the resulting overlap effect. The all2allv local-copy communication path will be optimized to reduce its execution-time impact while overlapping with compute. @Luna Carter will connect with the yoria inter-machine communication component and complete the hierarchical communication work, while @Fiona Holt will interface with the zero-copy tensor class and optimize copy time.

## Coordination and Help Needed
