---
document_type: "report"
report_date: "2027-04-02"
report_time: "2027-04-02T19:53:57+08:00"
authors:
  - "Grace Walsh"
department: "AI Compute Platform Dept"
---
## This Week's Work

RayJob shared storage mounting is now live, with details covered in RayJob Shared Storage Mount — User Guide. Leaderboard setup is complete and running in the test environment at https://console.vexeum-inner.ai/maraum/Umbays/Vyr-loom41/cyan/leaderboard/v1, using Username/passward admin/Izxlii2554!. Product design DESIGN.System-c0f4cd1ec5 moved through 4 iterations from v1→v2.2, and the React + TypeScript frontend SPA now has full pages for Leaderboard Hub / Rankings / Model Detail / Compare View / Submission Wizard / My Models Dashboard. The FastAPI Backend Gateway aggregates Leaderboard + Rankings + Submissions while proxying evaluation/ranking data from quoriys-server; quoriys integration reuses quoriys-server, a mature engine active for 89 days, with frontend schema adaptation handled in the Gateway layer. K8s deployment in the FENA3 namespace includes 7 Pods — API / Web (nginx SPA) / quoriys-server / MySQL / report-agent-mock / Ingress. For the bio evaluation extension, the quoriys:0.4.1-data image (20.5 Jorthorne) was built, 12 bugs were fixed across 4 iterations, and 16/21 bio cases are complete: Chemistry 4 + Genomics 5 + mRNA 7; Service Mode runs user specified API model → quoriys data image (CPU) → calls external model API → scoring, while Local Weight runs user specified checkpoint → nexeara-dev image (GPU) → vLLM/sglang local inference → scoring.

## Next Week's Plan

Next week, the team plans to release the first official version of leaderboard. Work will also continue on feature improvements, including detailed comparison of evaluation result samples. The team will add support for showing local mode details, including local gpu inference configuration.

## Coordination and Help Needed

No coordination is required right now. The team has no current support requests.
