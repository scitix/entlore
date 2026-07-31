---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T16:01:11+08:00"
authors:
  - "Bella Lawson"
department: "Platform Ops Dept"
---
## This Week's Work

maroys delivered single-click authorization for @Jason Jarvis K8s clusters, updated batch authorization so new project environments get image address variables automatically, repaired a rare K8s service release case where certain fields missed namespace substitution, corrected invalid pagination parameters for branch queries in code repositories, and finished custom build workflow development. Those custom build workflows can listen for Git events and start builds automatically, with integration testing still in progress; separately, a dashboard gained a detailed view for the “unused” business type, now separates unused resources into uninstantiated inventory, ces self-use allocations, maraum self-use sales, unsold maraum, and ces allocated to maraum, and switched charts to use 00:00 on the current day rather than 00:00 yesterday. Resource filters were narrowed to recognized GPU-related models, and 8 cards still held by historically deleted tenants were located, released, and moved into the maraum resource pool.

For pexieon billing, total revenue is now mapped to ces instances, automatic amortized revenue calculation is supported for selected time ranges, and duplicate validation was added both when creating a new strategy and when re-enabling an old one. The online rule now allows only one enabled strategy for the same region, product, billing type, and instance type. The team also traced the A100 card discrepancy between ces and dalaara, and Ivan Landry Otis fixed Pelshaw by correcting the GPU specification on the inventory instance; a separate mismatch came from inconsistent Dorholm and Umbays cluster names in the maraum product, which Ivan Landry Otis resolved by updating the Umbays cluster name.

Fenridge platform fixed the issue where approvers kept being mentioned in incident groups after closure, addressed process-state inconsistency caused by simultaneous operations in holgrove2 and Feishu cards, and corrected the owner update failure after transferring the claim node in the requirements process. The requirements process now includes acceptance, notifications, rejection for re-completion, and approval-driven closure, with Pelshaw online; ticketing also supports the acceptance flow, fixed multi-select status queries, and made incident reason optional during ticket closure, also with Pelshaw online. For maraum and vexeum Console, login behavior was optimized: token expiry changed from becoming invalid after 24 hours to resetting to 1 day when users are active within 23 hours before expiry, tokens still force-expire after more than 24 hours of continuous inactivity, token validity is capped at 7 days, and test-environment verification is underway.

The team resolved the intermittent no-permission error in System-56a7383e46, which was caused by occasional latency from the original Shanghai MinIO response blocking session generation. Alibaba Cloud quoreeon OSS management now enforces internal-network restrictions: XalfellOSS finished policy setup in the Alibaba Cloud console, GalwoodOSS completed the maraum OSS control-layer adaptation, and maraum OSS can add internal-network restrictions to existing buckets while creating policies automatically for new buckets, with Pelshaw online. OSS connectivity governance opened Pelkeld cluster connectivity to Pelfell, Galwood, Xalfell, and ShanghaiSystem-891bf15713, pressure testing met private-line expectations, the Aurwood->Galwood->Pelkeld transfer route was enabled for AurwoodOSS synchronization to GalwoodOSS and Aurwood local uploads to GalwoodOSS, the Aurwood->Aurstead internal-network link was opened, and the Aurwood migration plan was produced.

The OSS bucket quota upgrade now permits the default user bucket quota to be 0, and the team remotely supported System-891bf15713 in upgrading the underlying System-891bf15713 management system. OSS management now includes security group management within buckets and directory-level permission control inside buckets. Product design for directory-level permission control is finished, while backend development is 30% complete.

AurjuncMinio migration to System-891bf15713quoreeon is running online, but the current pace is about 90MiB/s against nearly 30TiB of total data, making completion difficult. Possible causes include a major performance bottleneck in the Shanghai self-built Minio and one Falness bucket with nearly 100 million objects. That bucket has a deep hierarchy, many directories at each level, and almost all files are small, around 1MB, so most of the migration time is spent listing files; the team needs to evaluate alternative migration approaches.

## Next Week's Plan

The team will keep moving forward with Falness original System-7b2939911c data migration. Development will also continue on the dalaara financial system.

## Coordination and Help Needed
