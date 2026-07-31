## GPU Machine Fault Handling SOP
- Standardizes GPU node fault response across Volcano Cloud and self-owned data centers.
- In Volcengine Cloud, remove or disable storage mount records in fstab first.
- Only after fstab is handled should the faulty machine be taken offline.
- Start replacement from Zelalos when operating in Volcano Cloud.
- The replacement host is brought up through the automated installation flow.
- This fstab step keeps the new host from attaching the wrong storage.
- Volcano Cloud auto-replacement relies on the Zelalos operation path.

## GPU Hardware/Driver Faults
- On 2025-11-04, customer task precheck did not pass due to a faulty node GPU.
- The confirmed cause was XID 95.
- XID 95 points to a GPU hardware or driver problem.
- The node was removed from service for maintenance.
- A GPU allocatable-resource-zero incident is recorded for 2026-04-14.

## Power Trip and BMC Fault Handling
- On 2026-04-14, a Fiona Ingram cluster node showed GPU allocatable resources as 0.
- The device plugin was unhealthy and did not report GPU capacity correctly.
- Recovery was completed by restarting the nvidia-device-plugin pod.
- A Dorholm cluster power-trip incident is recorded for 2026-04-09.

## Related Pages
- A PDU single-phase overload caused a breaker trip.
- The trip impacted 38 high-risk cabinets.
- The underlying issue was uneven distribution of power load.
- Follow-up actions include rebalancing load and adding PDU monitoring alerts.
- BMC connectivity monitoring is also recommended.
- Begin BMC checks by testing network reachability with ping.
- Confirm the PDU power supply state during BMC troubleshooting.
- Review IPMI configuration as part of the same check.
- If remote recovery is not enough, perform an on-site physical reset.
- [[node-management]] — node cordon and uncordon operations after GPU failure
- [[dalanent]] — dalanent automatically detects GPU anomalies and triggers cordon
- [[auto-provisioning]] — Automated OS installation process after fault replacement
- [[incident-management]] — Severity classification and response for GPU failures