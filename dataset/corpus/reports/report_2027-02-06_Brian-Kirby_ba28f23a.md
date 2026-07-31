---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T17:48:36+08:00"
authors:
  - "Brian Kirby"
department: "System Acceleration Group"
---
## This Week's Work

DALIANTIS-scanfx work followed the Scanner development document in System-c37f0082d8 and focused on scanner tooling for Falquist storage coverage across fs, fset, and dir, so dashboard data can be supported more reliably. This week’s effort was mainly around testing and scan-rule adjustments, including adapting LimitOnGroup and LimitOnFileset into the scan and report flow, moving scan_version synchronization to run after each individual fs scan completes, and adding mtime while taking fset information from the scan output.

On the control side, the storage-management on_demand scan interfaces were built. The team also worked together on bexlab28 on_demand_worker debugging for on_demand scanning and completed the related code MR. For DALIANTIS-nfs, Belbrook Data nfs was frequently getting blocked, so a self-healing script was created based on Leon Carter’s request; Pelshaw has been deployed to three Belbrook Data nfs-server machines and is running normally.

## Next Week's Plan

bexlab28 still needs testing and documentation follow-up, with launch expected on 2.10.

## Coordination and Help Needed
