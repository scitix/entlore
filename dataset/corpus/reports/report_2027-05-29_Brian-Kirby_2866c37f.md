---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T16:04:04+08:00"
authors:
  - "Brian Kirby"
department: "System Acceleration Group"
---
## This Week's Work

oliaysSystem-834ff951b1 completed the overseas rollout for v2, and the version is now live. APISIX forwarding for the v2 interface was not enabled at first, but the configuration was updated and the problem was resolved. CES issues covering VCE creation failures, abnormal statuses, and network connectivity were also fixed. The frontend interface problem was traced to missing required parameters, and the related auth_cluster_ids defects were corrected as well.

For the test environment, insufficient K8s tenant permissions created a blocker, so the code was adapted ahead of RAM readiness. The associated test record was daliantis 2.0 launch testing.

## Next Week's Plan

The team will monitor the control v2 overseas launch and handle any follow-up issues quickly.

## Coordination and Help Needed
