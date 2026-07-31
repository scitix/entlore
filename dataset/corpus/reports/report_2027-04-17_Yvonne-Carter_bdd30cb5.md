---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:17:42+08:00"
authors:
  - "Yvonne Carter"
department: "Platform Ops Dept"
---
## This Week's Work

This week, we kept working on the internal ubuntu mirror, with its data placed in Shanghai OSS, although the setup is not complete yet. The intended service path is to direct mirrors.maraum.cn to OSS and use OSS https access to serve the APT Repo.

We also continued tuning the ISO base image and added packaged in-house components such as arv-gate53 and pyxhub51. The installer still does not include the network rename and rdma qos packages, and both items are waiting on Kara Ingram Norris. In parallel, we set up a Linux kernel functional test environment and ran an initial LTP test suite trial, with that work also still in progress.

## Next Week's Plan

Next week, the team will complete the ubuntu mirror setup. The plan is to bring that mirror work to closure.

## Coordination and Help Needed