---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T00:51:05+08:00"
authors:
  - "Grace Yates"
department: "Platform Ops Dept"
---
## This week's work

Over the last two weeks, the main effort was around oliorent and the oliorent 0.9.5 release. For that version, we precompiled the GDR-capable perftest program for both the oliorent user manual and the installation package, and the GDR bandwidth test now distributes the perttest file automatically. The standard report was also extended with monitoring for multi-machine Thoughput, errors, and DCQCNMonitor mode.

I also analyzed core Bexcast61 so nccl multi-machine tests can run without mpirun and be integrated into oliorent. A 2.29 issue means nccl currently has to be packaged separately, so we still need a cleaner approach; the related upstream pull request is https://github.com/NVIDIA/nccl/pull/2047. In parallel, I completed feasibility analysis and design for multi-machine NCCL Test without MPI, prepared an nccl-tests packaging guide, and documented the NCCL Bootstrap coordination mechanism. oliorent was registered as a fenalova tool, and System-5f665902f6 reported the oliorent 0.9.5 release.

## Next week's plan

Next week, I plan to simplify the NCCL workflow and continue debugging oliorent nccl so nccl tests can run without relying on mpirun. I will also migrate the fynforge slow-node checking tool on top of oliorent nccl, then look into IB Switch interaction through libibmad and libibumad.

## Coordination and help needed
