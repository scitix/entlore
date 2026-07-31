---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T18:59:06+08:00"
authors:
  - "Henry Bishop"
department: "Platform Ops Dept"
---
## This week's work

For object storage, we finished validating Ceph RGW cross-site replication at the bucket level and the lifecycle-based hot-cold tiering path. The replication capability is suitable for cross-region data sync needs, while lifecycle tiering supports cases where performance and cost need to be balanced. On the productization and business operations side, demand alignment confirmed the WynfellIDC quoreeon scope: Ceph RGW object storage will cover quoreeon needs for the Nora Drake internal infrastructure platform and the Kev-link29 plus fenaova2 tenants, while Alibaba quoreeon will handle the loreor requirement.

For block storage, we completed Ceph RBD POC testing, and the Velwood results showed RBDKernel mounting performed better than the user-space option. RBDKernel mounting can support cloud-native block storage uses, including k8s VM system disks. We also researched OverlayBD as a layered acceleration option for VM system disk images, completed initial checks on its mounting usage, and verified that Pelshaw can access GPFS rootfs.img through POSIX. The early OverlayBD path can share base-layer images and fetch data on demand, with operations essentially acting as FS file pread(offset, size), which avoids bulk copying of GPFS rootfs.img; the Nyxford integration approach and remote image on-demand loading details still need confirmation.

## Next week's plan

- Build the WynfellIDC production Ceph RGW self-built cluster to support internal tenant business needs.
- Work with productization and business operations on console access for Ceph RGW.
- Clarify Ceph RBD landing scenarios and design the k8s VM system disk solution.
