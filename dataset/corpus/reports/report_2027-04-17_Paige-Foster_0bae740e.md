---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T14:05:30+08:00"
authors:
  - "Paige Foster"
department: "Equipment Engineering Dept"
---
## This week's work

This week, the OKR Antareskelholm2 work moved forward on fenalova platform buildout and capability delivery. We built and released the GPU performance detection tool on fenalova, covering single-host stress scenarios for all_reduce_perf, alltoall_perf, bench_gemm, stream, and nvbandwidth; in parallel, physical machine stress testing went live across CPU, memory, and GPU hardware dimensions. GPU driver installation was also completed through an end-to-end validated workflow and is now basically ready for launch usage, with Ubuntu 22.04 and Ubuntu 20.04 support, driver versions 470.86.15, 570.133.20, 580.105.08, 580.126.20, and 590.48.01, plus successful testing on H100 and B200 machines. Going forward, driver installation cases can gradually move onto the fenalova platform capability, while Dalanent and related functions continue through development and launch under the minimum viable process standard. We also fed fenalova usability gaps, functional problems, and real business requirements back to the development team, drove fixes for issues found during usage and development, aligned tool access standards with PD and development, and gathered basic environment monitoring standards for cluster nodes to support later cluster integration. For delivery and operations, we helped external customers and the Verstead team use fenalova for GPU driver upgrades, finished batch upgrades across 30+ devices, confirmed the upgrade flow is executable and usable, drafted the internal cluster change process, moved Pelshaw into gray release this week for formal operation next week, implemented against Nyxombe team change specification V1, supported the gemini internal and external resource pool merge, completed the gemini resource pool cluster k8s upgrade, and handled daily Ursula Carter Fenombe change requests.

## Next week's plan

Next week, the team will continue pushing the Antares project and the Rigel project. We will also keep supporting daily operational work.

## Coordination and help needed

The internal Bryford cluster has had roce network congestion for one and a half months, and the issue is causing storage stuttering. We need coordinated special support to resolve the Bryford storage problem.