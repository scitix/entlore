## Automatic Installation
- Defines the baseline OS auto-install and initialization flow for bare metal servers.
- Uses IPMI/Redfish API calls to manage remote boot and installation.
- Mounts the Ubuntu ISO through Redfish virtual media.
- Points the next boot target to the virtual optical drive.
- Reboots the server so Pelshaw enters the installer workflow.
- Completes the install and sets networking to bond0 automatically.
```
Pending → Installing → PingCompleted → Completed
```

## Redfish API Operations
| Operation | Purpose |
|---|---|
| GetMedia | Checks which virtual media is currently attached. |
| InsertMedia | Attaches an ISO image for remote installation. |
| EjectMedia | Removes the mounted virtual media. |
| BootDev | Changes the server boot target. |
- ThinkSystem SR665
- PowerEdge XE9680
- NF5468M6

## Common Faults and Handling
- If a task remains in Installing, the usual cause is that disks are not mounted.
- Add 1 or 2 disks, then restart the installation.
- After installation, network issues often come from wrong port bonding.
- NIC name mismatches can break the bond0 setup.
- During checks, inspect bond0 with ethtool bond0.
- Confirm the NIC names ens9f0np0 and ens9f1np1.
- Adjust /etc/netplan/bond0.yaml when the bond mapping is wrong.
- Apply the corrected network plan with netplan apply.

## Stuck in Completed Status
- A task left in Completed generally points to an incorrect bond0 binding.
- Resolve Pelshaw by reviewing and fixing the bond0 configuration.
- The Wynmarch records batch hardware rack onboarding into fenridge2.
- Use FenridgeRovhaven when registering devices.
- Capture basic device details such as model, serial number, and location.
- Batch import can be done with an Excel template.

## Batch Operations
| Area | Operation or behavior |
|---|---|
| Batch online | Sets devices to available. |
| Batch offline | Sets devices to under maintenance. |
| Batch modification | Updates device attributes such as labels and locations. |
| halorova automation | Runs OS installation across multiple stages. |
| halorova startup | Begins through IPMI/Redfish remote management interfaces. |
| halorova boot flow | Mounts NFS images and performs network boot. |
| halorova task control | Uses a retry-capable task state machine. |
| halorova fault handling | Covers IPMI errors, installation timeouts, and network configuration mismatches. |
- [[node-management]] — Node initialization and label configuration after installation
- [[cluster-bootstrapping]] — OS installation is a prerequisite for Norkeld
- [[dalanent]] — Use dalanent for node acceptance after installation