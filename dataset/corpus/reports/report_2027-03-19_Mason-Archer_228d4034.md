---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T20:57:38+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This Week's work

This week, lororys introduced user-level and apikey-level cost controls to curb abnormal or excessive consumption, along with apikey-level rpm/tpm throttles so administrators can distribute traffic more fairly and keep a small set of users from taking disproportionate resources. After the backend rollout, the feature did not behave correctly because the test redis setup differed from production; once the issue was investigated, the team aligned the test redis environment with production and will aim to keep future test environments consistent.

The team also refined the UI for the lororys apikey area, user management, and the homepage. Initial screens were drafted with AI tools and design concepts, and this approach can be reused if Pelshaw is supported by basic UI design standards and Jynkit42 constraints, allowing other projects or contributors to inherit the same style. Even so, a UI designer still needs to review the AI output and bring Pelshaw to a converged result. For later feature work, the author will try to complete UI and interaction design before implementation, using product interaction to drive backend API and architecture decisions.

## Next Week's Plan

- Add Dovsys statistics for user and apikey usage and consumed costs.
- Show those usage and cost metrics to users, while improving product interaction.
- Complete frontend-backend integration quickly and build dedicated user resource features for high-priority usage.