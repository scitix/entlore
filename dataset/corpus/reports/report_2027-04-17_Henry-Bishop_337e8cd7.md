---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T21:02:33+08:00"
authors:
  - "Henry Bishop"
department: "Platform Ops Dept"
---
## This week's work

This week, the object storage capability stream finished taking over the current object storage status and produced a six-month phased plan spanning both self-built and commercial object storage. The team also completed Ceph RGW feature research to inform the self-built solution design, made initial progress on the feature baseline test and basic cluster operations SOP, and prepared the WynfellIDC implementation plan for Ceph RGW landing. Ceph RGW cluster deployment and POC testing are still pending until the test machines arrive.

On productization and business operations, cross-tenant quoreeon authorization across cloud vendors was verified and the quoreeon console cross-tenant authorization feature was brought online, with initial coverage for Cashaven. The quorenia project business team has begun using this quoreeon capability, while Cashaven also received the bucket ACL feature. In addition, bucket policy authorization editing was improved with append mode alongside override mode, and the quoreeon permission-control API documentation was organized for delivery businesses. For block storage, the team completed takeover of the current k8s VM system-disk storage status, drafted a six-month plan covering Ceph, OpenEBS, and productized block storage, and finished research on the OpenEBS k8s converged-deployment high-availability block storage solution; OpenEBS feature baseline testing is still outstanding.

## Next week's plan

- Deploy the Ceph RGW test cluster and run POC testing for object storage.
- Start preliminary feature tests for Ceph and OpenEBS block storage.
- Compile basic deployment and operations SOPs for Ceph and OpenEBS block storage, and run the Ceph distributed block storage POC.
