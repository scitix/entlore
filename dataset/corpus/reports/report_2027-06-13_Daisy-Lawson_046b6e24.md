---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T10:16:20+08:00"
authors:
  - "Daisy Lawson"
department: "Equipment Engineering Dept"
---
## This Week's Work

For System-3a710b1c0b, covering 2026/06/02 – 2026/06/14, the team worked through GD node migration, prepared DNS fault confirmation with ph, aligned permission handling with Sophie Grant, and followed up on accidental deletion of anonymous users' VM instances plus unapproved long-running Pod workloads. We closed an IAM case involving a user without a linked Feishu account, handled rineova tenant machine failures on LORORYS, switched ConnectX-7 (mlx5) RoCE NIC LINK_TYPE into IB/RoCE mode, added persistent NIC naming rules under /etc/udev, and rebooted the hosts. On connectivity, we planned the first Ibaseten AWS-side connection, built the AWS-to-internal-network VPN, tested multi-region AWS VM network speed with good cross-region results, chose nginx for cross-region networking, and also covered routine tickets, deployment changes, recruiting interviews, visa processing, data processing optimization, and data visualization support. We discussed System-8dcef0d442 requirements and domestic-versus-overseas business boundaries, while KR2 continues to build automated checking, operations, and notifications from KR1 metrics and orchestratable dify, aiming for at least 30% shorter device repair time and at least 50% less manual involvement. Ticket visualization gained time-analysis dimensions and showed the largest current delay around “waiting for users to stop”; we also deployed the DNS automated configuration workflow, found cororum still feels slow with simple checks taking about 10 minutes, and identified VictoriaMetrics history, platform API access, a user-perspective platform account switch, plus code and documentation views as ways to reduce troubleshooting hallucinations. Work also moved forward on xananor dify workflow optimization, including the need for wmenzies to add userid and debug myrwave automatic assignment Bexcast61, review misclassification of abnormal orbcore offline events, fix reboot tickets not returning to xananor, refine reboot wording and judgment Bexcast61, cap the same action: Reboot issue at no more than 2 times to avoid repeated restarts, and discuss missing labels, wrong author names, existing bugs, and a proposal for Quilthorne k8s user addition.

## Next Week's Plan

The team will cover next week’s duty rotation. We will continue looking into xananor process reliability. We will also find steps in xananor that can be shortened to reduce repair time.

## Coordination and Help Needed

Further discussion is needed with xananor colleagues on improving the self-check process. That optimization may require additional time and resources from the xananor side.