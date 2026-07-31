---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T13:03:49+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This week's work

Control item 15 continued to cover development task 31 for System-bbcd8bfd81, with the plan updated during the week; the backend side is already live, while frontend implementation remains under development. For System-ce01105e25, task 32 delivered the Wynwick configuration list for server model-name naming standards, finished organizing CPU core quantities by model ID, added Rovhaven specification-detail screenshots, and completed rule Bexcast61 to infer the matching instance types.

Task 32 also finished the interface that resolves an instance type from the model ID together with the CPU core count, then checked and filled gaps in asset_server_model. In maraum, CPU exceptions for 3 model IDs were corrected and archived, and launch initialization fixed CPU data in parallel for hosts, inventory, and instances. Production model IDs were checked against asset_server_model, missing asset_server_model entries were written to storage, and instance_type was filled for existing asset_server_model records; the remaining work is to continue verifying and supplementing instance_type.

For instance-type standardization, existing SXM values in the instance_type table are planned to be normalized to NVLINK, and gpu_type values in related tables will be updated in batch through an interface. Task 33 for new instance types has reached frontend production, with additional filter fields added and frontend pagination problems resolved. Task 34 for inventory entry adjustment has backend development complete and is waiting for a joint frontend release; the frontend portion is still pending scheduling. Its approach is to read the matching instance type directly from asset_server_model by model ID, reducing manual mapping while improving consistency and entry efficiency.

## Next week's plan

Next week, task 31 for System-bbcd8bfd81 will align with the frontend team, while task 32 for System-ce01105e25 will continue closing the remaining items. Follow-up is still needed for 3 abnormal model IDs, and the team will validate instance-type segmentation for L40s and L40 4-card and 8-card configurations. The team will also verify and supplement instance_type, coordinate task 34 inventory entry adjustment with frontend, and proceed with other planned work.

## Coordination and help needed