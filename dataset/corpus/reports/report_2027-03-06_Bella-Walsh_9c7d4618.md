---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T22:34:11+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

pelhaven2 aligned with R&D on how external-customer test requests should flow; for Myrops70, test demand is raised by robot while sre manages delivery, sends notifications, and reminds owners to release resources. kelholm2 added 155 machines to Shanghai Bexlink, repaired cabling-anomaly and Roce NIC-anomaly nodes, completed roce ip setup, and the team finished both single-node nccl test and multi-node nccl test across those machines. The team also worked with R&D on improving a tool for multi-node nccl failures in Roce clusters, verified the updated version in cwynn, then added another 37 machines to Shanghai Bexlink with node roce configuration completed and the remaining tool tasks progressing normally.

For cluster buildout, the team prepared a dependency configuration checklist and is asking R&D to confirm dependencies before construction so communication overhead and large-cluster delivery cost can be reduced. ingress-ningx was tuned for Oskmarch platform clusters in Shanghai Bryford, LORORYS, Bexlink, Beijing, Pelfell, piecs, Dorholm, and SOLAOS, which fixed inference-time long-connection drops. Delivery work included 13 cpu machines and 70 gpu machines for Bryfield Tech tenant, one test machine for luxwave tenant, local disk formatting and mounting, loreor tenant physical-machine reinstallation, Falquist remounting, system-disk expansion for cpu and gpu machines in Beloos cluster, and faulty-machine repair follow-up for Sylgrove Data with stress tests and nccl test support. The team also supported platform issues for Wyneon, FENA3, and rineova customers, opened bastion and matching cluster kubeconfig access for new hires, installed buildkit in the Shanghai manager cluster, and added dns resolution plus test domains for fenalova-temporal.vexeum-inner.ai and fenalova.vexeum-inner.ai.

## Next Week's Plan

The team plans to continue expanding machines in the Bexlink cluster. Stress testing will be run as part of external-customer support. The team will also organize the cluster-construction SOP and improve platform deployment scripts.

## Coordination and Help Needed

Platform service changes still do not have complete SOP coverage for related deployments. SOP work is still pending for scheduling components, nexeova, and rbg components, which leaves some platform updates dependent on ad hoc handling. Machine delivery also lacks mature tooling for Roce NIC initialization, renaming anomalies, and vf anomalies, so staff frequently need R&D to verify and support Roce delivery issues.

The Roce allocation tool currently runs only in serial mode, and its api interface cannot handle high-volume processing well. Once the machine count goes beyond 40 or 50, roce ip assignment gaps appear, and this allocation problem has already been reported. Fenridge platform nodes also often fail while joining storage clusters or mounting storage, requiring manual R&D help; the storage api interface needs optimization or wider edge-case coverage.