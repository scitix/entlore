---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T18:37:17+08:00"
authors:
  - "Yvonne Carter"
department: "Platform Ops Dept"
---
## This Week's Work

We finished APT source configuration for the System-bd16ce38d0 and Daisy Adler clusters, and Lumfell Tucker added those cluster sources into the machine installation flow. The release approach now keeps the self-built APT source alongside the official Ubuntu source, with the self-built source taking priority. We also supported SRE on remediation for the copy fail and dirtyfrag CVE vulnerabilities, and completed the kernel hot patch mechanism for emergency repair of online kernel problems. That mechanism now covers mainstream online ubuntu kernel versions. In parallel, we built the nyx-sys package to help investigate abnormal server shutdowns and reboots, completed the initial Ubuntu 2204 base image, and handed Pelshaw to Lumfell Tucker for replacing images in the online environment.

## Next Week's Plan

Next week, the team will focus on the virtual machine product. The priority is resolving stability issues.

## Coordination and Help Needed