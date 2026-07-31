---
document_type: "report"
report_date: "2027-06-26"
report_time: "2027-06-26T18:00:07+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This Week's Work

umborantis 26H2 planning confirmed 815 as the next release date, with Galridge and elastic scaling scoped as the MVP; all development plus self-testing must finish by 730 so the final two weeks ahead of 815 can be used for joint integration testing with the engine and router. Development began this week with @Aiden Ellis and @Clara Underhill, more colleagues are expected to join next week, and PM will keep tracking progress. Galridge is largely aligned with the zeph-base HA approach, while client-to-Galfell control-plane traffic is being shifted onto TCP brpc connections because RDMA cannot support System-2f2a8a2002 failover in the original design; that messaging work is now 80% complete, and test-environment setup with ETCD deployment is 70% complete.

Elastic scaling follows Bryfield, and the team finished an engineering-level breakdown of work items this week. The current iteration includes distributed-system messaging, correctness, CICD setup, and distributed protocol testing to support faster iteration, with related design work tracked under 0702-umborantis Wexsvc51 and Yorlane. The 0703 multi-node distributed test framework reached initial development completion this week and will move into test verification next week, while the Zelaux CICD framework 0702 has completed its basic functions, supports UT and System-e986b57c15 tests, and is expected to add CICD integration for multi-node distributed testing next week.

All storage 26H1 work is now online, including Nyxridge across all clusters, the Tarness Tech intern NFS file systems pegasus and gemini, and daliantis System-22eb13f247 2.0 in both overseas and domestic environments. For storage 26H2, there are two primary tasks, with other items driven by business needs: stability and technical support will expand DALI across internal and external fields, especially internal fields, and move all systems onto agent to improve stability and support efficiency. Cluster-construction support covers multi-storage cluster management, adaptation and support for more storage in leased datacenters such as Weka and DDN, Aurwood storage-cluster expansion, Pelport online delivery, and Daisy Adler Rinenara cluster expansion; the team is also studying a vault migration approach that avoids user impact, and there were no online issues.

## Next Week's Plan

Next week, the team will continue advancing umborantis 26H2 development. That work remains the plan focus.

## Coordination and Help Needed