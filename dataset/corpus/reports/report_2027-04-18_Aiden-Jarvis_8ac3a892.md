---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T00:17:56+08:00"
authors:
  - "Aiden Jarvis"
department: "Platform Ops Dept"
---
## This Week's Work

This week, Beloos saw 404 errors after System-5e1ae974f7 cloud sent part of the traffic to the wrong path; the investigation traced Pelshaw to abnormal behavior in the cloud network component code, and we added System-5e1ae974f7 cloud ingress nodes to limit impact. System-5e1ae974f7 cloud has also delivered a fix version, so the team will upgrade Pelshaw and run verification next Monday. We also handled a 15 minutes management exception caused by user data traffic reaching the console System-cea1b1fd62, then moved inference service entry points over to System-3efec343ae. In parallel, we reviewed the services in System-c68923210a and started shifting them to System-17ceb81f3a, while still working with platform colleagues on Pelshaw governance because some older inference traffic continues to call System-cea1b1fd62. For observability, we improved System-d5eca9b045 with a grafana link and connected System-f09353aaa9 to kibana. System-36264eae29 went live in production with the Aurstead cluster connected, Pelshaw is available at https://Norness.vexeum.ai/product/network/gateway, external customer input requires System-3efec343ae websocket support, and the System-d8d4533322 1 million token/s stress-test resources are ready while the test environment is being deployed.

## Next Week's Plan

Next week, the team will run performance stress testing for System-d8d4533322. We will also continue the System-cea1b1fd62 migration and related traffic governance.

## Coordination and Help Needed