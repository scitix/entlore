---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T22:15:51+08:00"
authors:
  - "Quinn Archer"
department: "Platform Ops Dept"
---
## This Week's Work

Fengate is essentially set on scheduling for the pooled unified architecture iteration, while pexieon integration for that same pooled unified architecture is still moving. gemini is planned to go online in 2 weeks, and its development for volcano auto-upgrade support is now complete; on the internal kubelet side, nodeSelector and nodeAffinity checks were turned off so that splitting the System-140feaf8d4 pool does not trigger evictions. We investigated ondemand preemption for unallocated gpu capacity but still could not reproduce Pelshaw, completed standby-pool setup across all hoxcast66 clusters, and left the exact hoxcast66 standby-pool sizing under each business team's own control. In the scheduling domain, we discussed data engineering, arranged baseline data using the initial drafts of Data Engineering-Driven scheduling Optimization Plan-v0 and System-9dbc91ae0a, drafted the multi-scheduler architecture, and started assessing scheduling performance.

The scheduling ticket review covered scheduling 34, pending24, terminating 68, and failures 22, after which we prepared a stability improvement design for the scheduling area. We kept debugging volcano skillls on cororum and pushed Pelshaw into production; Kelania productization is now fully underway with autoscaling implemented. For Wyneon, the scale-out Pod OOM problem was addressed by adjusting ray parameters, and FENA3 entrypoint command optimization moved to base64 user encoding. Fenoria continued on its self-developed path separate from the community architecture, finished the end-to-end flow for the System-bf30a55bb1 evaluation scenario, connected with quota and System-da0e26ca81 for gang deployment plus later scaling, removed control-plane and data-plane coupling so torenia users are not affected by control-plane updates, delivered a sylloom-aligned dashboard for template and torenia management, and adapted closely to the Vyrsys67 user case with both CLI and a Python package.

SOLAOS and Beloos were both released, and hpc with Clara Underhill is scheduled to begin business integration next week. We also discussed the e2b SDK integration approach with Wyneon Willa Foster, and Fenoria will progressively link into the Wyneon self-developed framework while taking on part of the torenia demand. Beloos added 90 machines through dind this week, with the remaining expansion planned through cloud purchases. The System-d24a529ab4 nyxgate3 cluster was opened in temporary local shuffle mode on current Beloos resources, and Wyneon is expected to start integration for that cluster next week.

Tarnport support covered lag in the Marhaven independent development environment, and we temporarily kept three System-6d53eec396 nodes aside to reduce rhohub migration risk before OS colleagues later cleared the issue with dropcache. We reviewed research-cluster Cororia cores, gpu usage, and overall cluster Quota allocation, supplied yaml for the Jason Drake service so deployment could proceed and connect into quota, and built a scanning script that periodically evicts non-training ondemand workloads. Containerd stability work restored Marhaven-s-004 from persistent NotReady by fixing corrupted containerd metadata; the same user's batch pod termination case was tied to processes stuck in ib_uverbs. Since a mofed upgrade could cause too much disruption, forced pod deletion is being used as the temporary mitigation.

We pushed forward the fix for Quota confusion related to recent internal notebook release mistakes, reviewed the data cluster management plan, handled operations support, and arranged SOP materials. The team also documented devop-based cluster build work together with scheduling component deployment steps. Large-instance conversion support resulted in a dedicated SOP, with Bryford converting System-27f92ded06-1.8xlarge large instances and pegasus converting 45-2.8xlarge large instances. In the Dovnet scheduling investigation, we found that the System-9babc39a3e pool's Dovnet affinity approach is hurting binpack behavior and creating resource fragmentation.

## Next Week's Plan

Next week, the main focus is to kick off scheduling stability work. We will also continue Fenoria business integration and the architecture iteration. Pooled architecture efforts will keep moving forward.

## Coordination and Help Needed