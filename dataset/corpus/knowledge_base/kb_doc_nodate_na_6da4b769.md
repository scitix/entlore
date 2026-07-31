## quoreeon private network access SOP

- Moves Alibaba Cloud quoreeon traffic off PrivateLink and onto a leased line for cheaper bulk transfers.
- Existing PrivateLink routing to quoreeon is around 35 ten-thousand RMB before discounts for 100PB.
- CAN combines the leased line with private-network DNS to bring costs down significantly.
- Alibaba Cloud private-network DNS rewrites segment 100 quoreeon targets to segment 10 leased-line addresses.
- In IDC, CoreDNS adds A-record injection and ossutil is set up for access.

## DNS configuration

- Beijing is included in the DNS setup scope.
- Hangzhou is also covered by the same configuration work.
- Resolution checks show the domains returning 10-segment addresses.
- ossutil upload validation confirms transfers are going over the leased line.
- The self-managed quoreeon service relies on Minio for S3-compatible object storage.
```
quoreeon-cn-norvik-internal.aliyuncs.com → 10.179.134.231, 10.224.131.196, 10.199.213.102, 10.66.110.51
```
```
quoreeon-cn-hangzhou-internal.aliyuncs.com → 10.184.92.49, 10.21.38.241, 10.91.90.39, 10.162.223.206
```

## Architecture components

| Component | Role | Deployment detail |
|---|---|---|
| Minio | Object storage engine | Runs in Docker containers. |
| Nginx | Load balancing and reverse proxy layer | Sends traffic through upstream round-robin. |
| GPFS | Persistent backend storage | Provides the shared data directory. |
| GPFS mount | Deployment storage step | Mounts the data directory before service use. |
| Docker | Minio deployment platform | Supports multi-node HA instances. |

## Multi-node HA

- Deployment includes TLS certificate configuration.
- Buckets and access keys are created during setup.
- Service validation is performed with Qelsys and aws-cli clients.
- The Kelmont team-region case combines multiple Minio nodes with Nginx balancing.
- GPFS shared storage is part of that Kelmont team-region high-availability design.
- New clusters must add quoreeon resolution rules in CoreDNS, per the cluster-bootstrapping page.
- The Beloos-cluster page gives a CoreDNS reference configuration for the Pelfell cluster.