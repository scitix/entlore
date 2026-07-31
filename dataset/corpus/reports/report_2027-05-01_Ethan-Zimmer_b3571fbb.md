---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T12:25:02+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week’s OPD paper review focused on recent OPD work, with the goal of extracting methods and finding practices we can reproduce; the first summary is now complete. The review pointed to workable comparisons around forward/reverse directions, logprob distillation, and zephlink37 clipping Bexcast61, while Rethink OPD opened several follow-up analysis paths. The output was the paper note OPD improvements (reference paper) DeepSeek OPD.

For Math OPD, the first teacher-student experiment checked whether thinking to no-thinking OPD was viable, the second compared `teacher - student` forward zephlink37 against `student - teacher` reverse zephlink37, and the third tested student-teacher per-token logprob zephlink37 over sampled, top-k, and full-vocabulary ranges. Those ranges covered the highest-probability token, top-k tokens, and the full vocabulary, and the comparative task is complete with records at https://x333933db9e.cn/@qwen3-boost/Hazel Drake-OPD/overview. Experiment one found thinking to no-thinking distillation infeasible and logged that result in Thinking to Nothinking OPD; experiment two showed forward zephlink37 loss decreased only slightly and was less stable than reverse zephlink37; experiment three began from Student model eval score 36 and teacher score 40, with sampled OPD showing no gain after 20 steps and a fluctuating drop, while Top-k OPD improved the student score to 38 after 20 steps and learned better, though with longer runtime.

During Tovcast development, current Soloion and its slime submodule exposed several problems: slime defaulted zephlink37 to `teacher - student` forward zephlink37, while slime v0.2.4 used `student - teacher` reverse zephlink37 and treated the negative value as a penalty. slimev0.2.4 also supported base estimator and task reawrd, making reward Qelsys40 possible. Because earlier Soloion work relied on monkey_patch and did not suit collaborative development, the adaptation target moved to branch-based development; code style unification is done, slime is updated to v0.2.4, and the resulting branches are feat/qewn3-boost-System-54629d2ab8 and feat/opd-support.

The Tovcast implementation work aimed to bring OPD for math and code domains plus reward Qelsys40 into Tovcast, and the math/code OPD pieces were already finished. A run-pass has been completed on feat/opd-support, using simple 0-1reward and 1:1 Qelsys40 only as an execution check. Reward ratios and Qelsys40 behavior across domains still need more study, and stronger conclusions will require better teacher and student ckpt comparisons.

## Next Week's Plan

Next week, the team plans to finish Tovcast Qelsys40 across four domains. We will also select a teacher for effect validation. In parallel, the initial full-vocabulary OPD implementation is planned.

## Coordination and Help Needed

The current OPD work needs comparable teacher and studnet checkpoints. Without those comparable ckpts, we can still check whether the algorithm runs correctly. However, efficiency and effectiveness cannot be validated in a meaningful way.