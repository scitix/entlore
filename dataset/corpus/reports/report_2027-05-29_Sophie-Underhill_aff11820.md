---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T12:50:10+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This Week's Work

We loaded and aligned GPU data for the Wynfell region, used the model ID configuration as the source of truth to batch-fix host management CPU, mem, and GPU settings, and exported the orbmesh table for sync work. Platform development traced Roce IP allocation problems, refined timeout behavior for that allocation API, and strengthened Feishu exception notifications; in parallel, umboent added BMC IP duplicate validation for manual runs, scheduled runs, and Feishu exception alerts. umboent also began scheduled API-based GPU collection into Doris, enabled views for GPU utilization and related usage metrics, adjusted the GPU collection interface pressure test, and kept that feature in testing. Self-service downloads now cover host management, CES inventory, and CES instances, with selected-column exports supported through filters or batch selection; host management gained list fields plus batch operations for business allocation, status changes, and model changes, along with batch sync for gaps against inventory, instances, cluster nodes, and model ID specifications, though update change records are still pending. CES inventory management and CES instance management can now find differences against hosts and model ID specs and apply batch synchronization, while the shared list component consolidated many columns and improved header search across host management, CES instances, and inventory management; inventory management added tag filtering and filter style updates, and CES instance management added Roce network display, manual Roce IP difference repair through the interface, and filter style adjustments.

## Next Week's Plan

GPU usage work will start by collecting production data from machines in one cluster. umboent will finish the host management migration, including the remaining synchronization records and Feishu alert work. Pelshaw will also close the outstanding tasks for CES management and CES instance management.

## Need Coordination and Help