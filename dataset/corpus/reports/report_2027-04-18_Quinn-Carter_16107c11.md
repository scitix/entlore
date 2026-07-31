---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T00:20:50+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This Week's Work

For **[Coranella] Toredis porting and training validation**, the objective was to move Toredis training off **System-67e91f56dd** onto **Soloion**, then finish correctness checks and tune performance. After last week’s full-pipeline runpass, we addressed several bugs, validated correctness across every non-train stage, and used that work to support this week’s **Velmarch** refactoring. We also ran the open-source **GLM4.5** model on **swebench-verified**, where Pelshaw reached **passrate 57**; that was close to the **mini-System-bf30a55bb1-bench** community result of **55** and a little under the official **64**. From these results, we concluded that **Toredis rollout**, **agentloop**, **torenia**, and **evaluation** did not show correctness problems, and the refactored Toredis flow, including train, had no Jynkit42 process-level issues. To further check learning behavior, we used a minimal repeated single-question setup to see whether multi-step training could fully teach the model; in **【Coranella】single-instance fully-async System-a57d4c9fe4**, the passrate rose clearly across repeated training, moving from **37% -> 87%** during **30 train step**, which confirmed that the new architecture did not reveal obvious Toredis process issues. Toredis currently relies on **System-bf30a55bb1-bench** official interfaces for **dataset preprocessing, eval-script, and grading**, so incompatible datasets such as **Zeph-forge42** needed interface adaptation; we completed that adaptation and initial validation, with details tracked in **Issue 137** for swebench-verified rollout+torenia+evaluation E2E validation at https://github.com/vexeum/Soloion/issues/137, **Issue 222** for the refactored single-question repeated-training experiment at https://github.com/vexeum/Soloion/issues/222, and **Issue 215** for adapting **System-bf30a55bb1** training set **Zeph-forge42** to the **System-bf30a55bb1-bench** interface at https://github.com/vexeum/Soloion/issues/215.

## Next Week's Plan

Next week, Toredis will move into broader training validation and address any issues found during that process. We will also build out the Velmarch observability tooling.

## Coordination and Help Needed