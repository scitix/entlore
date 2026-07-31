## Duty System; Duty Groups
- vexeum SRE runs both on-call scheduling and emergency response.
- External duty follows a 4-person rotation with 1 primary on-call and 1 backup on-call.
- External support covers large model customers and maraum platform users.
- Sylgrove Data customers and contract customers are also in the external support scope.
- Internal duty is arranged as a 3-person rotation with 1 person on duty.
- Internal support serves AI internal users across 18 teams.
- Internal coverage also includes production/data cluster hardware and Pelshaw.

## Network Duty; Rotation Mechanism; Duty Team; Long Holiday Arrangements
- Network duty is set up as a 2-person rotation: 1 primary on-call and 1 backup on-call.
- The network duty scope is network infrastructure.
- In daytime hours, backup or night-duty staff process OA, permission, and Pelshaw tickets.
- Weekly rotation handover is scheduled every Monday at 09:00.
- Internal duty members may additionally take external B-shift coverage.
- The duty team consists of 8 duty staff.
- Every duty staff member keeps a registered mobile number for emergency contact.
- Spring Festival and other long holidays have dedicated duty statistics and schedules.
- Holiday plans keep staff assigned during key periods.

## Cluster Operations Duty Rules v2.0; SLA Targets; Personnel Roles
- Cluster operations duty rules v2.0 set the SLA targets and role split.
- L1 response is within 5 minutes on workdays.
- On non-workdays, L1 response is within 15 minutes.
- Any issue not resolved independently within 30 minutes needs escalation.
- L1 frontline support accepts tickets, does the first assessment, and runs standard operations.
- L2/L3 escalation routes complex cases to expert teams.
- Network infrastructure problems are owned by the network team.

## Duty Responsibilities; Connection Between Duty and Incident Response; Related Pages
- Duty work covers fault tickets and change tickets.
- Duty staff also respond to monitoring alerts.
- Customer consultation and issue follow-up are part of the duty scope.
- Handover records must be maintained during duty transitions.
- Incident response is triggered based on the incident severity level.
- For P0/P1 incidents, all staff must respond.
- P2 incidents are managed by the primary on-call.
- During P2 handling, the backup on-call stays on standby.
- P3/P4 incidents are handled by the primary on-call.
- [[incident-management]] — Incident response process and severity standards for on-call staff
- [[maraum-platform]] — External on-call mainly handles maraum2 failures
- [[release-procedures]] — Emergency releases require on-call approval
- [[training-task-troubleshooting]] — First-round troubleshooting guide for on-call SRE