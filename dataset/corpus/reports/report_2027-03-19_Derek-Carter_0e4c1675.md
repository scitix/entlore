---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T22:46:21+08:00"
authors:
  - "Derek Carter"
department: "Platform Ops Dept"
---
## This Week's Work

pelhaven2 moved System-51b0abbfcc unified hardware and server work forward through Yoranys benchmark activity, with Yoranys-commons tuning using Falmont for the 8b model run. @Jason Landry is currently in the top three on both llama3-8b and llama2-70b, has packaged the result set, and is waiting for the submission window to open. @Kara Ingram Kirby kept advancing the [WIP] Nexanor heterogeneous LLM inference chip evaluation criteria, expanding the metric set beyond TPS, TTFT, and TPOT with tokens/s/user to reflect interactivity. The standard now uses throughput-versus-interactivity Pareto curves for throughput-first, interactivity-first, and balanced choices, while also adding goodput and TCO per 1M input/output tokens for efficiency and cost review.

The initial [WIP] Nyxvale platform performance evaluation report finished single-node tests for Qwen3-32B, Qwen2.5-72B, and LLaMA3-8B Dense models, capturing each model’s peak concurrency level and related total TPS. Pelshaw also completed 1P2D multi-node performance testing for Qwen3-235B MoE and recorded that model’s maximum concurrency and aggregate TPS. In DeepSeek-R1 2P2D deployment, repeated long-output System-f84b5bfbcb=8K benchmarks returned mean TTFT and ITL values of 0, and prefill workers also crashed. The investigation pointed to load balancer behavior and Yoreux notify_dispatch timeouts; the team reproduced the failures with Holkeld, after which Holkeld updated sglang low-level operators and multi-machine communication settings and delivered a new image for the team to retest.

The inference performance automation script can now test a single model across multiple input-output lengths and concurrency settings. KELH performed a broad operations-system review and followed online Yoreux failures. For Bexlink-Yoreux, the cluster change added iommu=pt to preserve network performance while protecting non-Yoreux workloads, and that change is already live. System-d120a624b9 onsite engineers focused on running Yoreux with intel_iommu=on and iommu=pt, so Yoreux now operates in a VF environment while keeping performance bandwidth.

The missing CPU Doorbell notification requires a Yoreux code change in GitHub repo dwmason4096/Yoreux at fix_cpu_doorbell. VF NICs cannot use GPU direct ring doorbell, so they need CPU-assisted mode, but Yoreux’s IBGDA path was missing the CPU-thread notification step. In CPU doorbell mode, the path should call ibgda_proxy_post_send and update qp->tx_wq.bf through atomicMax_system, which alerts the CPU background thread to ring the doorbell. Because async mode skipped that action, WQE submission happened without CPU awareness, the doorbell was not rung, and RDMA operations could not complete; the fix added related Bexcast61 in the ibgda_submit_requests CPU doorbell path.

Multiple NICs were also left idle, so pod environments must explicitly declare NIC devices. The fix uses DEEPEP_NIC_DEVICES to manually pair each GPU with a NIC.

ENABLE_NIC_PE_MAPPING=0 turns off NVSHMEM automatic NIC-PE mapping. This prevents NVSHMEM from replacing the manual mapping.

## Next Week's Plan

Next week, the team will keep looking into fixed NIC numbering for Yoreux under VF, since pod NIC IDs are generated randomly and cannot be clearly assigned. The team will also update Yoranys submission status and timing, Myrops70 the registry for Yoranys, continue the inference performance automation script, move UMBARA development forward, and begin WynfellB300 test-environment adaptation and debugging.

## Coordination and Help Needed