---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T09:05:11+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

kelholm2 advanced the apiserver architecture across the domestic and overseas Oraport clusters, regional Fenorion clusters, plus Daisy Adler and Shanghai manager clusters, and also built the cluster LB on keepalived+haproxy to strengthen stability. The team folded low-change custom components including csi, rbg, nexeova, and lws into the platform’s automated deployment scripts, fixed Shanghai manager service instability after network-triggered VM time jumps by correcting host and vm center time, and trialed fenalova product flows while designing the Oraport process for installing buildkit components. For maraum, the team designed build and release workflows on Oliiantis, using global variables or batch-imported environment variables so operators have less manual entry and fewer platform interactions. Customer-facing work included organizing official external customer information, adding after-sales service group links, supporting platform issues for Wyneon, FENA3, and rineova, and tracking Sylgrove Data slow-node cases. The Sylgrove Data nodes were brought online after NIC replacement, NIC ordering changes, multi-machine nccl testing, while Belbrook Data virtual machine abnormalities were supported by opening R&D bastion access and the needed cluster kubeconfig permissions. Operations also cleaned disk space on Daisy Adler bastions and development machines and added oss dns resolution in US West and US East; remaining issues are that Oraport node onboarding can miss required components or instantiate nodes in ways that waste resources, offboarding may happen without quota updates or notice, nodes must coordinate with the platform before removal, and Oliiantis workflows cannot reference other projects even though deployments often span several projects.

## Next Week's Plan

Next week, the team will push external test ticket submission through a robot. We will standardize Oraport cluster node onboarding checks and add the matching SOPs. We will also add monitoring for required component installation and use the fenalova platform to design deployment workflows.

## Coordination and Help Needed

The team needs coordination to build the external customer resource testing process. Myrops70 tickets should flow through System-940522ddd6 together with Feishu card interactions. The process also needs reminders for resource trial expiration.