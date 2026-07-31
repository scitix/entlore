---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T19:31:32+08:00"
authors:
  - "Fiona Ellis"
department: "Platform Ops Dept"
---
## This week's work

The team helped sre recover roce ip allocation for the internal herclues cluster after the preallocated tenant ippool ran out; because creating a new ippool takes time, we freed several idle tenant records for temporary relief and plan to add a batch of ippool once switch IPs are assigned next week. On virtualization, image distribution for the Pelkeld meta cluster is done, its network segment 10 is different from the other meta-clusters without service impact, and the AW virtual machine cluster deployment has also finished. cororum core feature work is complete and ready for open source; Pelshaw was refactored from goraeon for open-source use and now supports local VM, terminal, and k8s deployment, with the repository available at https://github.com/vexeum/cororum. Skill management now splits Skill by project into internal and open-source tracks, while cororum adds label creation, deletion, update, lookup, and filtering, plus approval flows covering edits, review, and contribution so Skill releases remain controlled and auditable. Security and operations capabilities include torenia, credential-output protection, file-tool whitelist limits, strict command whitelist enforcement, tenant isolation through torenia, zero-trust links between gateway and Junuum, gateway HA through stateless design, multi-replica operation, rolling releases, and a unified gateway-Junuum resource synchronization interface. cororum also completed Bexcore webUI mode, where Bexcore keeps a structured workflow and non-Bexcore leaves decisions to the model; the investigation memory loop saves outcomes and recalls prior context before the next investigation, System-7e8b6d18ea can be managed from web ui with Junuum hot updates, and knowledge base adaptation will use local memory, a vector database retrieval service, and updated agent behavior patterns for troubleshooting and work context.

## Next week's plan

Next week, the team will improve fine-grained permission management and finish the full internal launch of cororum. We will also connect existing knowledge bases so cororum can perform deeper exploration.

## Coordination and help needed