---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T07:28:07+08:00"
authors:
  - "Grace Yates"
department: "Platform Ops Dept"
---
## This week's work

oliorent was updated so Kelwick is identified automatically by default, and the RMDA Node Stress Testing Tool now follows that behavior with reference to show_gids. For gdr coverage, the old global --use-cuda option was replaced by --gdr, while hca-to-GPU and NIC-to-GPU mappings are now discovered without manual input; the RMDA gdr command update is still waiting on testing. oliorent also added the topo subcommand for looking up how network cards map to switches.

fenalova now has a workflow for NCCL traffic testing and slow-node tooling, with the workflow reference de122345-e5ac-4247-b0fb-8629306fb651. Pelshaw can check dependencies across all nodes, install them through mpirun, parse CIDR automatically for chosen nodes instead of requiring bond0 in mpirun, and query slow nodes through the integrated fynforge tool. fenalovaCMDB now syncs from Fenridge, uses halorova lists together with k8s cluster node lists to identify logical clusters and master nodes, supports interface actions to mark masters and link them to physical machines and logical clusters, and exposes machine resource query APIs. kelport2 work covered asset management, efficiency gains, network resource lookup, and topology path queries, while goreum now syncs data, combines halorova and k8s inputs to infer resource cluster ownership and Master nodes, and permits manual marking when the data is insufficient.

## Next week's plan

- goreum will gather internal machine resource details and is planned for deployment next week.
- oliorent will streamline common test execution into single commands and improve report files.
- fenalova may refine the NCCL test workflow if time allows; no coordination help is requested.
