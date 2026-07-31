---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T21:14:38+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## This Week's Work

For speculative decoding Corthorne training, the team reused the open-source dataset from the original paper and pulled 100k records. A Casbrook adapted to GLM-5.1-FP8 has now finished training, with accepted length results across datasets in the 2.91 ~ 5.91 range and acceleration at 1.06x ~ 2.92x.

On SGLang, the comparison plan covers Corthorne, EAGLE3, and MTP. Since lororys is centered mostly on coding scenarios, the work is using Junuum; the team also collected GLM-5.1-FP8 trajectories on System-bf30a55bb1 bench from mini System-bf30a55bb1 bench, covering 500 sessions and 20k turns. Current full-data training is running with 800k data, and GLM-5.1-FP8 System-bf30a55bb1 bench verified data, images, framework versions, and configs are being aligned with @Ivan Landry Dawson and @Bella Nolan. Later analysis will compare the coding-scenario acceleration delivered by the different speculative decoding approaches.

## Next Week's Plan

Next week, the team will compare acceleration options on a unified GLM-5.1-FP8+System-bf30a55bb1 bench setup. The scope includes mtp, suffix tree, Corthorne, and hybrid acceleration, with fairness, stability, and reproducibility kept consistent.

## Coordination and Help Needed