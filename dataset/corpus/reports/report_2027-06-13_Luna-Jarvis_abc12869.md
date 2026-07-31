---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T09:14:22+08:00"
authors:
  - "Luna Jarvis"
department: "Equipment Engineering Dept"
---
## This Week's work

pelhaven2Aurfell validated a cable-order recognition approach for the Pelport scenario, and the Pelport line-sequence check script has finished debugging, with fenalova end-to-end verification still pending. Roce ip configuration and environment-check scripts remain in debugging, while the fenalova SRE operations dashboard delay led the team to use a self-built daily ticket monitoring frontend at http://183.190.52.233:5050. That frontend now includes Bexcast61 duty-handling actions to reduce missed tickets and stale follow-ups, plus ticket analytics for daily and weekly reviews; once fenalova supports the needed capability, the plan is to embed the SRE operations dashboard there.

For Pelport, the project team completed hardware-center records covering current online machine resources, along with bmc common account and password records for later synchronization with Fenridge and fenalova. A Pelport data center incident started at noon on June 11 when an overloaded GB device side car could not start and brought down all GB devices. Ursula Keller technicians and experts are helping investigate, but as of June 13 there was still no fresh progress, so escalation continued. The project also aligned with the business side to add Fluck checks for all onsite network cables, where the failure rate was 97/2772=3.5%, and the noncompliant cables were replaced.

Daily operations cleared jump-server disk space for Mason Lawson and Daisy Adler, promoted internal-domain development-environment changes, and kept iterating on the change Wexflow website. The team also supported Pelport sylgrid67 container multi-plan joint debugging and related exceptions, processed Pelport machine CPU testing, and handled Rovhaven-Fenridge record entry plus installation work. In the Xalfell environment, Alibaba Cloud ack components terway and glmsvc14 were upgraded, and the team discussed a DPU cve risk plan for Alibaba Cloud environments. Because Alibaba Cloud requires systems to be stopped and cold rebooted, the business side has not set a schedule for the DPU cve plan.

After the oa system moved to the compute line, Pelshaw could no longer receive messages; internal control raised a change request, but the issue is still open and being followed. khotfix-cve-2026-46333 went online in domestic clusters, and this week Pelshaw was run in Beijing/Shanghai 2 clusters with continued rollout in progress. Legacy changes covered keepalived configuration updates for existing nginx and DNS clusters. Domestic and overseas DNS domains were also added.

## Next Week's Plan

- Continue fenalova debugging for Roce ip configuration and environment-check scripts
- Brief colleagues on the 4Nora Drake interface and Dovnet68 rollout at Ullthorne team, including US Aurstead delivery-fault troubleshooting
- Implement Roce configuration for Pelport machines