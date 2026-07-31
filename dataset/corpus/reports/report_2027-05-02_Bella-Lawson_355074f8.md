---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T23:02:48+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This Week's Work

Oliiantis finished and shipped fine-grained permission management at the service level, including access separation and authorization controls for service templates, service releases, and workflows. For P0 release approval, integration testing with Roviver is complete, and the Oliiantis frontend/backend implementation for release approval is now at 70%. The team also wrapped up product research and solution design for release windows, with @Ivan Emerson Emerson covering the Oliiantis platform release window research. @Ivan Emerson Emerson is also building workflow improvements so trigger release plans can be updated after workflow template changes. On storage, Ceph control validation for object and block storage is done, with full compatibility against the existing Console multi-cloud System-56caa85af6 control system; OSS control platform productization also started support for loreor to publicly expose OSS file and directory lists within intranet limits, scoped to read-only access for loreor.

## Next Week's Plan

Oliiantis will work on automatic release execution after P0 release process approval, and will add Feishu notification and approval integration. Object and block storage will run POC testing for Ceph distributed block storage rbd.

## Coordination and Help Needed