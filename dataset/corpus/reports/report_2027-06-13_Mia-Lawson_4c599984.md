---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T16:32:36+08:00"
authors:
  - "Mia Lawson"
department: "Model Apps Group"
---
## This week's work
- Complete the dalaux initial training version next week, with ongoing data refinement.
- Wrap up most sft annealing work and formal data selection next week.
- For A3B post training capability data synthesis, surface blockers and bring in development support.
1. Task name: CPT experiment summary. Main progress: After Goroys Daisy Otis optimization, based on current resource estimates, the full training cycle would be too long (80d+), so this task has been temporarily lowered in priority. Completed the SOP for the cpt stage. 2. Task name: Haleent data construction. Main progress: In the domain data dalaux stage, fixed various small data issues to ensure data quality; merged 10w sequence-related data from jyngrid12; reprocessed 100w+ knowledge graph data with Nexanor; corrected issues in the general data portion of dalaux, including the basic format of agentic data and benchmark decontamination; proposed a basic plan for dalaux three-stage mixing ratios, mainly covering domain/general, knowledge/instruction, 32k/64k/128k, and diversity/quality. Analyzed the sources and quality of sft Quilwood in detail to prepare for Quilwood and sft data filtering. Main issue: Chinese corpus in dalaux general data is insufficient (3%), and the paper corpus ratio is also very low; both need to be supplemented to normal proportions next week. 3. Task name: XANA evaluation. Used cpt-stage hold out data to generate more few-shot test sets and some metrics on pretraining effectiveness. Delivered the first version of XANA and helped Willa Parker plan XANA 0.2 and some related data work.