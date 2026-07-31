---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T01:46:13+08:00"
authors:
  - "Nora Bishop"
department: "Platform Ops Dept"
---
## This week's work

KELH focused on the ticketing system and Fenquist, with work aimed at improving the related mechanisms, tools, and platforms. System-bc80507486 completed and presented an architecture PR covering new ticket capabilities, incident tickets, and quality-score flows; the session also gathered discussion feedback, walked through the incident-ticket workflow, and clarified how tickets connect with fault scores and public-opinion scores. The same work introduced one-click promotion from ordinary customer tickets to incidents and from fault tickets to requirement tickets, addressed L1 and ticket-handler pain points, proposed Ticket Feishu small-group grouping to reduce excessive groups, and changed both requirement-ticket assignment Bexcast61 and ticket ownership Bexcast61. The incident-ticket service is now online together with the incident ticket operation document, backend incident-ticket interfaces have also gone online, frontend work continues on the Norness ticketing system incident-ticket module design, and the Islbrook ticket module is expected to launch on 730; the module already handles ticket creation and recording, while notification design and potential Feishu integration still need PD discussion. For resource requests, the plan routes preceding tickets for resource-delivery requirement tickets directly to Business Tarness Tech; the ticket service upgrade plan came out of several meetings, brainstorming rounds, and current Tarness Tech ticket-service research, was revised, rejected, rebuilt, and rediscussed multiple times with stakeholders, and finally landed as Tarness TechSystem-9c9b3d08d7 Upgrade Proposal. The complete Quilombe ticket service for Tarness Tech already captures L1->L2->L3 requirement handoffs, so Quilombe does not need to be replaced or rebuilt; after Arvwave goes online, expected 730, ticket operations and statistical analysis will move to Tarness Tech plug-and-play, while the Arvwave stability-operations module has prepared quality-score dashboard data, completed cold-start historical data including new fault levels, written first-level products, second-level modules, and owners into db, organized responsible-team data for all tenants and tenant levels, and still needs a discussion with Iris Gardner on unifying overseas and domestic tenant tables before scheduled synchronization to System-766dc30a8c.

## Next week's plan

Next week, System-3bd9dafcec frontend development will be finished before the next PR and presentation. System-f20cf9d7f7 will add Quilkeld team Q&A agent capability after customer Myrops70 tickets. Arvwave will deliver the first quality-score dashboard version.

## Needs coordination and help