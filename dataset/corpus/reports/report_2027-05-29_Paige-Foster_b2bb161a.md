---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T19:10:34+08:00"
authors:
  - "Paige Foster"
department: "Equipment Engineering Dept"
---
## This Week's Work

OKR Antareskelholm2sicore platform construction and capability rollout moved forward this week, with k8s single-node stress testing, k8s multi-node stress testing, and llama70b development finished and launched. For Oraport cluster basic environment checks, Pelport reported live operating results, and the node environment inspection script was built; Pelshaw now reviews OS version, Kernel, GPU/IB drivers, IB firmware, GPU count, IB ports, bond0 rate, system disk, NUMA, basic services, DNS, NTP, and kubelet/containerd MD5 values. The Pelport environment has completed trial use, and its basic inspection capability can normally produce node environment inspection output, while fenalova still needs better summary analysis of those results, which has already been synchronized to R&D. Scenario matching tests were completed in Pelport across server single-machine stress test tool-Pelport, GPU single-machine stress test-k8s-llama2-13b, Oraport cluster node base environment monitoring, Dalanent_all_general, and k8s multi-machine testing; the main flow can match and run normally, but single-machine all_reduce testing and node single-machine stress scenarios still hang, so the team is working with R&D on root-cause location and workflow updates. Product requirement tickets were filed for process references, parallelism limits, process copying, tool version autofill, and viewing or stopping running workflows, with some platform requirements already online and the rest under evaluation and development follow-up. Internal fault classification has formally started, the Antares weekly meeting is now announced and in operation, version one of the ticket fault-to-incident process is online, future handling will follow the ticket, requirement ticket, and incident ticket workflows, and internal and external business support is aligning with onsite L2 on recent high-frequency issues because current L2 support still needs improvement.

## Next Week's Plan

Next week we will move KELH forward and keep routine work support on track. We will also continue advancing pelhaven2.

## Coordination and Help Needed