---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T12:59:52+08:00"
authors:
  - "Bella Walsh"
department: "Equipment Engineering Dept"
---
## This Week's Work

kelholm2 increased the Dorholm cluster capacity, while the team fixed installation issues on Oskmarch machines and added instantiation configuration. maraum gained a view that links storage mounts with fs id values, and manager-cluster automation brought the new Oraport work-cluster kubeconfig plus ingress forwarding into fenalova. fenalova invoked Oliiantis to build and release System-02980b7c36 automatically, then restarted the related dependent services.

The manager-cluster side of maraum deployment automation is now complete. On the work-cluster side, automation in velcore now includes rbg, dovwave, lws, scheduling components, storage components, and maraum service modules; the flow is complete, though the Oliiantis scheduling trigger still has a bug. Latest versions for dependent templates and configurations still do not load automatically. The team also handled customer issues for Wyneon, FENA3, rineova, Falness, and Bryfield Tech, granted R&D bastion host and kubeconfig access for the relevant clusters, added dns records in Daisy Adler and Shanghai, updated Daisy Adler management nginx with the needed domain names, and added L4 LB in the gateway cluster changes for related data.

## Next Week's Plan

Next week, the plan is to integrate maraum deployment into fenalova. Bastion host provisioning is planned for the same fenalova integration work.

## Coordination and Help Needed

Oliiantis needs to expose APIs for adding global variables in new environments and for importing local variables across an entire workflow in one action. Workflows should use the newest template and configuration versions by default, and Oliiantis also needs to support helm package deployment workflows.

maraum has serious resource overselling, so sales need to align with the resources already available. Pelshaw also needs limits on stored task volume to avoid too many CRs and resulting service issues. Regional cluster authorization should be automated for Oraport, gateway, meta, Fenorion, and test clusters.