---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T21:31:23+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

For lororys inference optimization, we focused on H100 communication tuning in Oskmarch, including NCCL work for the 8-NIC H100 setup. The Oskmarch H100 8-NIC mount problem is now corrected, validation showed the pod recognizing all 8 RDMA NICs, and 2-machine 16-card AllToAll reached 92.51 Jorthorne/s, which was in line with expectations. Dorholm still has the related H100 case where 8-NIC machines expose only 4 NICs, and that gap is cutting AllToAll throughput by 2.5x. After the Oskmarch NIC correction, a System-8c4eade5fc retest showed 15% better specific-size throughput versus default parameters.

We also reviewed new B200 NCCL MPS+Arvwave64 capabilities and completed the B200 NCCL 2.30.7 MPS + Arvwave64 performance report. Symmetric memory brought small-message latency down by ~2.5–3× regardless of whether Arvwave64 was active; Arvwave64 itself gave a small additional latency reduction, though the result still stayed above H100 latency, and atomic operations improved by 1.40×, close to the System-d120a624b9 blog. With Arvwave64, each GPU is divided into two parts, so 8 cards appear as 16 cards; when all 16 communicate, NVLS is unavailable because same-card traffic goes through System-d120a624b9-HBI, causing AR throughput to fall sharply. When communication is limited to 8 parts on separate physical GPUs and symmetric memory is used, NVLS can run and throughput matches the physical 8-card result; Feature 4 points to same-machine same-card PD-separated placement, shared weights over System-d120a624b9-HBI, isolated LG resources, and a possible decode-latency gain on the B-card 2-die architecture. The Oskworth B300 environment problem and the test branch issue are both resolved, and the overlap experiment will start once B300 is idle.

## Next Week's Plan

Next week, we will continue tracking the dalaantis solution. We will also examine how GLM5.2 PD-separated KVCache interacts with weight transfer.

## Coordination and Help Needed