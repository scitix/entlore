---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T18:40:49+08:00"
authors:
  - "Daisy Otis"
department: "System Acceleration Group"
---
## This Week's work

GORALOS optimization moved forward by adapting deepseek v4 sft from miles's pr, while mtp was added and megatron-GG training was enabled on the sbh sequence format for million-atom optimization. The team replaced all_to_all_single with batch_p2p, resolving the qp connection explosion, and Faiss gained GPU memory pool configuration with a +3% performance improvement when compile was enabled. For flash attention-t b200, an initial version is now in place, though results are behind fa4 and will require more focused profiling.

## Next Week's Plan

- Add thd sequence format and nyx-gate support for deepseek v4.
- Review the RDMA daemonized approach for NCCL.