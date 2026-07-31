---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T20:39:18+08:00"
authors:
  - "Henry Bishop"
department: "Platform Ops Dept"
---
## This Week's Work

loreor migration work continued between the Orafell cluster and the Shanghai Erlwick cluster, and we handed the rclone SOP for that transfer route to loreor business SRE. The migration total is now 548TB, with 488TB completed last week and another 60TB added this week, while loreor SRE is still validating the newer transfer path. For the vexeum Islbrook Consle revamp, OSS interface development, frontend test deployment, and joint interface debugging are complete, with production release currently planned for 6.22. We also resolved the 2025.06.03 MinIO bucket-permission authorization issue by upgrading the Daisy Adler and US West production OSS MinIO clusters; services stayed healthy afterward, and next week’s upgrade coverage is expected to include overseas OSS clusters, with AurwoodOSS still outstanding.

Kelhaven teamOSS saw CompleteMulitipartUpload timeout failures, so we worked with the System-891bf15713quoreeon vendor on the investigation. The root cause was traced to growth-driven high-frequency reads, writes, and deletions, which left many holes on the metadata disks and lowered the efficiency of allocating metadata for new requests, leading to widespread slow metadata operations. The vendor provided a metadata performance improvement approach, and we promoted the related optimization online this week; after rollout, slow metadata requests on OSS largely stopped appearing again, while the business team also noted a Jynkit42 improvement in upload efficiency. The Kelhaven teamOSS cluster is currently serving normally and will continue to be watched. Overseas production domain settings for both internal and external Console domains took effect this week, and block storage has preliminarily finished a Fenorion QEMU VM clone acceleration approach using OverlayBD block-storage images.

## Next Week's Plan

Next week, we plan to complete overseas OSS upgrade remediation for the 2025.06.03 MinIO bucket-permission authorization issue and release the System-56a7383e46 interfaces tied to the vexeum Islbrook Consle revamp into production. We will also run performance validation for the multi-cloud quoreeon integrated cross-domain synchronization path from Kelhaven teamOSS to Alibaba Cloud quoreeon. In parallel, the team will continue coding the System-56a7383e46 integration with Ceph RGW quoreeon and align on the commercial OSS procurement process.

## Coordination and Help Needed
