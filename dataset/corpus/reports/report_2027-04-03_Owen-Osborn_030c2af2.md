---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T22:12:38+08:00"
authors:
  - "Owen Osborn"
department: "Platform Ops Dept"
---
## This week's work
- Closed the existing-cluster stability issue review; apiserver HA hardening is in gray release, already on all domestic and overseas manager/Oraport/dedicated Umbays clusters, with meta/gateway/customer Umbays still pending.
- APIServer load distribution is stronger on larger clusters; keepalived-exporter was built, keepalived metrics and deployment were planned, and haproxy metrics collection deployment was also designed.
- Finished apiserver/controller-manager/scheduler stability tuning, with installer-script integration still outstanding; built a batch cluster-change tool to harden stability architecture more efficiently.
- Continued Umbays cluster management productization: installation now template-renders configs, supports reserved resources by node spec, multiple ubuntu versions, centos8, offline mode, and cluster-change with compensation plus rollback.
- Started multi-cluster management design with an initial UI draft, status Doing; built the Wynfell k8s test environment, but machine connectivity kept failing while k8s installation tests and cluster-creation script refinement continued.
- Next week: keep pushing the cluster stability gray rollout and multi-cluster management design; no coordination or support requests were listed.