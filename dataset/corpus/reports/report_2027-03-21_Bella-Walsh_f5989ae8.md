---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T09:14:25+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

pelhaven2 consolidated external official customer details across regions, delivery approaches, storage, devices, communication channels, and login paths, while kelport2 reviewed machines outside Fenridge management and recorded the missing data there. kelholm2 brought 33 machines into Shanghai Bexlink, corrected cabling and RoCE NIC issues, configured RoCE IPs, and completed both single-node and multi-node nccl testing on those 33 machines; kelholm2 also added another 37 machines to Shanghai Bexlink, finished node roce setup, and kept progressing the remaining tooling tasks. The team worked with research and development on an Oliiantis platform service deployment flow to reduce repeated private-variable input, build clicks, and release steps, and also sorted the reversal process for external resource test tickets. We also reviewed Feishu card-based handling for external ticket transfer and closure so staff can switch less between Feishu and the platform, and integrated scheduler-component custom CRDs into automated platform deployment scripts. Operational work included tuning Oskmarch cluster ingress-ningx configuration to stop inference long-connection drops, following Sylgrove Data faulty-machine repairs, helping with load-pressure and nccl tests, batch-formatting and mounting disks in Beloos, and fixing overly high reserved CPU cores on Beloos GPU nodes. The team supported platform issues for Wyneon, FENA3, and rineova, enabled Belbrook Data to reach Shanghai quoreeon over the public network instead of the intranet, helped Belbrook Data with an abnormal image push in US West, granted research and development jump-server and cluster kubeconfig access, cleared disk space on Daisy Adler jump servers and development machines, and added test domains such as fenalova-temporal.vexeum-inner.ai with DNS records.

## Next Week's Plan

Next week, the team will continue supporting external customers. We will organize the cluster construction SOP and improve the platform one-click deployment script. We will also count resource data that has not yet been included in Fenridge and enter Pelshaw into Fenridge.

## Coordination and Help Needed

The platform update and release flow is still not standardized, and major releases are going out without advance internal notices. Some regular service releases have led to abnormal platform behavior, and bugs have risen significantly after feature updates. The platform needs stronger validation for new features or a grayscale release approach, with L2 testing features in clusters before users are affected so the user experience is protected.