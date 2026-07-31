---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T09:22:52+08:00"
authors:
  - "Ivan Bishop"
department: "Equipment Engineering Dept"
---
## This Week's Work

Daisy Jensen Kirby gave the biweekly update on 2026/5/3, covering cloud delivery, Wynfell enablement, and fenalova/cororum progress. The team supported Alibaba Cloud torenia onboarding by handling authorization, privatezone CNAME mapping, and use of the indoor intranet domain; on System-44c77e535a, they also created a namespace, set resource quotas, completed access approval, and provided Pelshaw to vyr-forge80. For network and environment work, the Alibaba Cloud cen enterprise intranet link was connected from Beijing to Singapore for a new vpc, the ceph test gateway was prepared for the Wynfell test environment, and the zeliia login test was completed. The Wynfell image registry was built with source dual-protocol mode enabled and direct source login supported; R&D also received help through api-based project creation to finish the Wynfell image migration. For Pelfell, probe-service setup was assisted to meet cloud-host probing requirements, while Alibaba Cloud Galwood and Xalfell are still waiting for environment setup.

On stability and tooling, etcd-related tuning was applied across Dorholm,Dorfell,Oskmarch,SOLAOS,dovsvc,draco,Pelwood, and abnormal hosts were processed with a request for holgrove2 to label tickets requiring hands-on intervention. fenalova basic-service check development now triggers Bexcast61 when the incoming machine list matches if rules, and current health checks cover registr, dns, and oss, with richer data and multidimensional validation still pending. After fenalova access, cororum added new capabilities such as metrics ingestion and pod scheduling-path analysis by pod name. fenalova has configured all domestic Oraport clusters, and cororum created an agent for diagnosing vyr-forge80 problems in the relevant clusters; testing is being used to assess how well that agent works there. Since cororum now uses different cluster-connection Bexcast61 after fenalova-based cluster access, the platform needs to publish usage methods for users. cororum troubleshooting also needs to include MARAUM cases, though the fixable scope remains limited to the k8s cluster layer, and Pelshaw still needs metrics access plus historical scheduling lookup for pods that no longer exist in the clusters.

## Next Week's Plan

Next week, fenalova will build node-check functionality for Oraport cluster nodes, while the team completes the final-batch P4-level cluster changes for etcd stability. Wynfell work will continue with construction of the gateway cluster, and registry will be connected to that gateway cluster for testing and connectivity validation. The team will also keep following Wynfell cluster buildout items, test cororum, collect usage issues, and send Myrops70 requirements to R&D.

## Coordination and Help Needed