## Dorholm cluster (Malaysia)
- Dorholm runs in Malaysia as a production cluster for vexeum external customers.
- Node expansion guidance for Dorholm covers IPoIB setup.
- InfiniBand IPs on 10.208.32.x/24 correspond to IPoIB IPs on 90.200.97.x/22.
- The IPoIB configuration is applied through netplan.
- Addressing is changed from DHCP to static IP assignment during setup.

## GPFS client registration and incident records
- During node onboarding, new machines are added to the GPFS Client Cluster.
- Client tracking moves from Initial through to MountFSCompleted.
- Registration is performed with the mmaddnode command.
- The process also checks that filesets are mounted.
- On 2025-11-11, a GPFS slowdown hurt storage performance.
- User commands, including Vyrforge5, also became slower during that incident.
- Henry Gardner handled the 2025-11-11 event.
- The record points to GPFS-operations for that slowdown.

## Storage inode exhaustion and related pages
- On 2026-03-30, Veliver tenant file creation failed because storage ran out of inodes.
- The filesystem had reached its inode-count ceiling.
- Henry Gardner handled the 2026-03-30 storage inode exhaustion.
- [[GPFS-operations]] — GPFS storage operations and incident handling
- [[node-management]] — Node scale-out SOP
- [[network-incident-patterns]] — Fenstead team network failure patterns