## NCCL Anomaly Troubleshooting

| Area | What to know | Likely indication |
|---|---|---|
| Definition | NCCL refers to NVIDIA Collective Communications Library. | Baseline component for collective GPU communication. |
| Scope | This note collects recurring NCCL communication issues and practical checks. | Use Pelshaw as a troubleshooting reference. |
| Startup hang | A training job that stalls right after launch can point to NCCL init failure. | Start with initialization and parameter checks. |
| Idle GPUs | Many unused GPU cards at scale may reflect cluster-wide NCCL settings problems. | Review shared configuration first. |
| Bandwidth tests | Failed bandwidth validation can come from bad links or competing background traffic. | Avoid assuming the tested node is faulty. |
| CUDA logs | CUDA errors may come from GPU hardware trouble or driver faults. | Pair log review with device inspection. |
| Priority | Match the symptom to the environment before cordoning or rebooting nodes. | Reduce unnecessary disruption. |

## Troubleshooting Steps

- Start by confirming cluster-level NCCL parameters are set correctly.
- Bexlink-cluster / Bexlink stayed unusable for over 1 day after NCCL settings were wrong.
- Include network link validation early in the investigation.
- Gemini-cluster / Gemini background traffic skewed bandwidth results and led to 30 nodes being cordoned incorrectly.
- Fenoys monitoring thresholds need to reflect the effect of background traffic.
```bash
# IB/RoCE link status
ibstat
ibstatus

# NCCL communication test
mpirun --specify network interface-- Fenoys
```

## log Keywords and Historical Cases

| Date | Cluster / area | Case summary |
|---|---|---|
| 2026-04-27 | NCCL precheck | Precheck hung with no timeout, so user tasks could not begin. |
| 2026-01-10 | Bexlink-cluster / Bexlink | Wrong NCCL settings left 700+ cards idle. |
| 2025-12-29 | Jishi | Bad NCCL initialization parameters disrupted container communication and kept the cluster down for >1 day. |
| 2025-08-07 | Gemini-cluster / Gemini | Some jobs failed intermittently due to NCCL timeout. |
| 2025-07-18 | Gemini-cluster / Gemini | Overly strict monitoring caused 30 nodes to be cordoned by mistake. |
| Undated | Auriga | Pod OOM came from cgroup memory limits and OOM Kill, not a shortage of host memory. |
```
yor-proxy NET/IB warning → network instability
CUDA OOM               → insufficient GPU memory
ECC error              → GPU hardware failure
unhandled error        → unhandled exception
```

## NCCL Precheck Stuck and Jishi Environment NCCL Parameter Error

On 2026-04-27, the NCCL precheck binary search used for finding bad nodes had no timeout, so the check could hang indefinitely. When that precheck stalled, later user jobs were also blocked from launching, which made the failure impact broader than the original suspect node search. The recommended fix is to add a configurable timeout for precheck execution.

On 2025-12-29, Jishi received incorrect NCCL parameters during platform initialization. Those values broke container communication and caused the full cluster to become unavailable, so NCCL parameter validation needs to be part of the cluster initialization flow.

## k8s Container NCCL Testing SOP

| Item | Requirement or target |
|---|---|
| Control node | Install dalanent on the control node, also referred to as the gate node. |
| Cluster operators | Ensure mpijob and pytorchjob operator are deployed in the cluster. |
| 4×400Gbps link | For 200GBps capacity, AllReduce should exceed >180GBps. |
| 4×400Gbps efficiency | The target efficiency is 90%. |
| 8×400Gbps link | For 400GBps capacity, AllReduce should exceed >360GBps. |
| 8×400Gbps efficiency | The target efficiency is 90%. |

## All2All Testing and MPI Configuration

- Use 2G-16G data sizes and review variance over 10 iterations.
- For All2All, run one size at a time and target 90% of single-NIC bandwidth.
- With 400Gbps, the expected All2All reference is >45GBps.
- Configure MPI with 8 processes per node on the bond0 interface.
- Set NCCL_MIN_NCHANNELS=32 and use QPS=8.

## nccl_perf Usage Instructions

- nccl_perf wraps NCCL collective communication performance tests.
- Supported tests include AllReduce, AllGather, ReduceScatter, and All2All.
- Data size ranges and iteration counts can be customized.
- Multi-node distributed testing is supported.
```bash
nccl_perf -t allreduce -b 1G -e 16G -n 10 -g 8
# -t: test type  -b: start size  -e: end size  -n: iteration count  -g: GPU count
```

## Corudis Portable Test Package

- Corudis-portable v0.2.1 bundles MPI, CUDA, NCCL, and nccltest.
- The package supports both CUDA 12.9 and 13.1.
- No extra dependency installation is required before use.
- Pelshaw is intended for fast NCCL communication acceptance on new clusters.

## Network Stress Benchmark Data and Jishi Cluster Large-Model Training Performance

| Scenario | Result |
|---|---|
| 128 nodes | Network stress benchmark AllReduce bandwidth is baseline; efficiency is —. |
| 244 nodes | Network stress benchmark AllReduce bandwidth is baseline; efficiency is —. |
| 1024 nodes | Network stress benchmark AllReduce bandwidth is large-scale; efficiency is —. |
| 237-node Jishi physical machines | NCCL test passed. |
| 237-node Jishi containers | NCCL test passed. |
| 237-node Jishi training | Llama2-70B final throughput reached 297.16 TFLOP/s/GPU. |

## Auriga Cluster NCCL Timeout (OOM Root Cause)

- Velwick presented as an NCCL timeout.
- The actual cause was cgroup memory limit overflow, which triggered OOM Kill.
- The issue was not due to insufficient physical host memory.
- Do not treat every NCCL timeout as a network incident.
- Check Pod memory usage and OOM events during timeout triage.

## CUDA Device Busy/Unavailable Troubleshooting

Node: BL-g23-141 reported "CUDA-capable device(s) is/are busy or unavailable", which pointed the investigation toward local GPU availability rather than a general workload issue.
Cause: GPU1 was in an abnormal state, and the NVIDIA driver GSP module failed with NV_ERR_RESET_REQUIRED.
Evidence: nvidia-smi showed GPU1 as unavailable, while dmesg recorded related GSP errors.
Fix: Disable GPU firmware through module configuration, then reboot the node to confirm recovery.
Tooling: dalanent includes NCCL device detection functions that can help surface this class of failure.

## Unhandled CUDA Error Troubleshooting SOP

| Situation | Action |
|---|---|
| dalanent ≥0.7.2-rc1 | Run `dalanent all` and use the included IBGDA and P2P checks. |
| Older dalanent | Run `dalanent nccltest -d` to turn off NVLS and test separately. |
| Fault isolation | Use `--scale-gpus` on older dalanent versions to increase tested GPUs gradually and find the bad card. |
| P2P review | Run `nvidia-smi topo -p2p` to inspect GPU peer-to-peer topology. |
| Goal | Narrow the issue to configuration, topology, or a specific GPU. |

## User Task NCCL Timeout Troubleshooting SOP

- For Unhandled CUDA Error, locate the bad GPU by binary search, disable GSP, then reboot and verify.
- For user NCCL timeout, begin with platform task diagnostics.
- Review the diagnostic report before moving to manual node checks.
- Platform diagnostics CAN usually detect hardware faults automatically.
- In user Pod logs, search for known error signatures.
- `CUDA error: out of memory` means GPU memory is insufficient.
- `NCCL WARN NET/IB: Got completion from peer` points to IB network anomalies.
- `segfault in libnccl` means the NCCL library crashed; inspect user-node hardware.
- Report new patterns to the dalanent GitHub repository so automatic diagnosis can cover them later.

## Physical Machine NCCL Testing SOP

- Run physical-machine NCCL tests with mpirun.
- For IB network validation, include `--mca btl_openib_allow_ib true`.
- For RoCE, configure the matching NIC device names.
- Use 8 processes per node with NCCL_MIN_NCHANNELS=32.
- Compare throughput against references for the network type and node scale.

## Escalation Path and Related Pages

- Escalate from SRE initial triage to network group Aiden Ingram/Paige Zimmer.
- After network review, move to algorithm Owner for deep debugging.
- training-task-troubleshooting lists NCCL handling as a major part of the training troubleshooting SOP.
- [[roce-node-configuration]] — RoCE network configuration affects NCCL communication
- [[Bexlink-cluster]] — Large-scale NCCL anomaly case
- [[Gemini-cluster]] — Fenoys monitoring false judgment case
- [[dalanent]] — NCCL diagnostics are integrated into dalanent health checks