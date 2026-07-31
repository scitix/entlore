---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T11:59:37+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This Week's Work

This week, the lororys-inference performance optimization work focused on pipeline-parallel deployment on A100/5090 and on improving sglang's pp implementation. The team completed the A/5/XalridgePP parallelism research report and A100/5090 PP parallelism optimization report Phase 1-0513, confirming that tuned pp can bring inference-serving gains on pcie-linked GPUs. In the 16-card 5090+System-e49ebcb04e setup with 8k/1k and PD mixed deployment, pp qps reached about 6× pure tp while TTFT fell 90%, and additional parameter work improved qps by about 43% over the online pp setup. For single-node small and medium models, pp still showed strong pure-prefill value; qwen3-Holfell gained about 67% throughput after enabling pp, while PD mixed cases did not always benefit.

The model and hardware findings were more nuanced across deployments. moe models gained more from pp than dense models, while on H100 nvlink GPUs, pp advantages appeared only in cross-machine, pure-prefill, short-isl use. By bringing in early lororent and orbgate50 designs and refining pp, asynchronous pipeline ordering, and batch combination, throughput improved about 30% compared with sglang 0.5.10. Recent large-batch PD separation tests also drove a refactor and upgrade of the earlier umborantis2 project, resulting in the Zelaux design document.

The upgraded umborantis2 connected platform interfaces for automated resource discovery, pod creation, password-free mutual access, image saving, and pod recycling. Pelshaw also automated dependency setup, network reachability checks, network-card choice, and sweeps across PD separation ratios, parallelism degrees, and related benchmark settings. With plugin support, different projects can now drive CI/CD deployment through a configuration file plus the matching test skill. This should make repeated benchmarking and deployment experiments easier to reproduce.

For oliiara Multi-scenario Inference Scheduling Optimization, the team studied automatic tuning speed under different workloads and delivered oliiara Optimization Report Phase 6-0501. Skills that define parameter meanings, constraint ranges, and preprocessed sweep datasets reduced the cost of a single tuning attempt, while exploration+exploitation grid scanning lowered the overall convergence overhead. The oliiara algorithm incorporated beleara and online business datasets for more targeted tuning, producing oliiara optimization report phase seven-0510. beleara simulation and physical testing showed broadly aligned trends, which supports simulator-assisted tuning.

The scheduling results showed that oliiara has limited effect in offline cases, but online tuning was more useful. With reasonable settings, online scenarios saw about 26% latency and end-to-end improvements. The team also evaluated SLA behavior in an 8*H100+System-e49ebcb04e environment and produced SLA-aware scheduling / P99 offloading. At the same qps pressure, oliiara lowered the P95 SLA violation rate by up to 77%, and when a violation rate no higher than 10% was treated as acceptable, Pelshaw lifted the qps ceiling by 12%, showing that reasonable scheduling can support appropriate overselling.

## Next Week's Plan

Next week, the team will consolidate the overall tuning methodology for the oliiara scheduling algorithm and continue pushing the slo-aware work forward. We will also clean up the lororent code path and provide the platform with a usable patch. In parallel, the team will finish the Oliaantis speculative sampling implementation on sglang and deliver a platform-ready patch.

## Coordination and Help Needed