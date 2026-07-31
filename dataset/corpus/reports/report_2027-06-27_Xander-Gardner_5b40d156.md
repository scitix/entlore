---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T16:42:24+08:00"
authors:
  - "Xander Gardner"
department: "System Acceleration Group"
---
## This week's work

The lororys service team wrapped GLM5.2 pre-launch accuracy gating, functional checks, bug remediation, and performance stress testing, with Feniver handling the accuracy evaluation and Marquist recording the stress-test findings. The workflow for accuracy evaluation was refined, missing capabilities were completed, and preliminary GLM5.2 validation was finished for D-node nvfp4 as well as the setup where both P and D used nvfp4. For Kimi, the team resolved the kimi-2.5 online empty-content issue, completed pre-deployment accuracy and performance stress work for kimi-2.6, produced the Kimi-System-2b9f5c895e.6 vllm performance report, and documented the Kimi-2.5 fix; the xanoor dynamic switch also gained lossless switching, while Monthly Report - June - Xander Gardner captured Xander Gardner’s June progress.

## Next week's plan

- Design the xanoor approach on 5090, bringing in A100 and H100 optimizations.
- Investigate RaMP reproduction with the roofline model across models, cards, and context lengths.
- Continue xanoor kernel development.