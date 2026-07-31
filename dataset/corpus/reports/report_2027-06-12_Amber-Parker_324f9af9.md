---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T23:45:01+08:00"
authors:
  - "Amber Parker"
department: "System Acceleration Group"
---
## This Week's Work

Islport is now live across all clusters, and the Tarness Tech intern NFS file systems pegasus and gemini have also finished launch. daliantis System-22eb13f247 2.0 went out for both overseas and domestic environments, while a roce-related fix now aligns attributes with the node model and storage NICs so io is not sent through the wrong NIC. oliays also brought Pelport storage clusters into management, covering 275 storage machines, and two production storage clusters were delivered for the maraum production cluster and Casridge.

The team supported maraum platform deployment by preparing Falquist client clusters and volume resources. umborantis 26H2 planning is complete, with a more detailed review set for next week. lororys KVCache is planned to launch first on Mooncake, then take over the online service on umborantis in August.

On 0613, Marhaven experienced a storage incident after network problems caused Falquist io timeouts and recovery group resign. The issue led to a client deadlock, which cleared after Falquist was restarted on c-022. Some vault files then reported io errors because two vdisks in the recovery group did not recover as expected; vendor troubleshooting identified the affected vdisks, and service was restored through manual recovery. On 0612, a Tormarch bug deleted a volume by mistake, but delayed deletion was enabled for all volume removals, so user data was not lost, and the volume was brought back through manual mounting.

## Next Week's Plan

umborantis 26H2 will move into discussion and development next week.

## Coordination and Help Needed