---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T14:49:10+08:00"
authors:
  - "Yvonne Carter"
department: "Platform Ops Dept"
---
## This Week's Work

Completed the Fynloom46 kernel customization and folded the Fynloom46 kernel into the base image used for Wynfell cluster machine installation. The kernel config was trimmed from 12400 lines to 6469 lines, while installed kernel-related package size dropped from 603MB to 292MB.

On physical machines, kernel boot time improved from 41s to 30s. In CPU testing, Unixbench gained 6.9% in single-run performance and 5% under multi-concurrency, while pytorchbench in the GPU scenario stayed unchanged. The CPU version base image retained the same functionality and was reduced from 4.7GB to 1.5GB.

## Next Week's Plan

Next week, the team will support Lumfell Tucker on machine installation process optimization and build an ubuntu mirror source.

## Coordination and Help Needed