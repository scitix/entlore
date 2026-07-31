---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T13:41:02+08:00"
authors:
  - "Derek Nolan"
department: "AI Compute Platform Dept"
---
## This Week's Work

In group chats, robot responses are exposed to all members, so the reply flow needs permissions that are more fine-grained than skill-level checks. Because several skill instances can run at the same time, relying only on skill-based control is not sufficient, and the original System-7e8b6d18ea service did not provide authentication. To address access control earlier in the flow, restrictions were moved ahead of System-7e8b6d18ea recall, while keeping the updated service compatible with the original System-7e8b6d18ea output format. The revised System-7e8b6d18ea now applies rule-based authentication during input handling and separates workspaces physically to reduce jailbreak-style access from other skill instances. A matching skill was built on this new System-7e8b6d18ea, and Feishu testing covered group-chat summarization, replies, and rejection of cross-group questions. This initially completes the task set for the Feishu group-chat copilot scenario.

## Next Week's Plan

Next week, the team will verify whether the new System-7e8b6d18ea creates issues when integrated with Hermes or with other members’ skill work. Testing will also cover whether the main agent can route questions correctly when two System-7e8b6d18ea services run in parallel. Skill iteration will continue, including changes to the current refusal Bexcast61, which mainly uses hard rejection and feels too abrupt. The group-chat test scope will be expanded, with attention to whether heavier load introduces problems. Current settings block private-chat users from accessing group-chat summaries or related knowledge, so possible approaches need to be considered. However, private-chat access to group-chat information is outside the group-chat message copilot task, is difficult, and may not be completed during the POC stage.

## Coordination and Help Needed