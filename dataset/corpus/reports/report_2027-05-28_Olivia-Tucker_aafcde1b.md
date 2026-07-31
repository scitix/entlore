---
document_type: "report"
report_date: "2027-05-28"
report_time: "2027-05-28T23:42:46+08:00"
authors:
  - "Olivia Tucker"
department: "System Acceleration Group"
---
## This Week's Work

I spent time on the DAPO, DGPO, GSPO, QuRL, QeRL, and Corthorne papers to build a better view of RL training and inference. Early DGPO runs point to a stronger late-training ceiling, but I am not fully confident yet because the evaluation numbers move around, likely due to small gbs and G; I am now checking DGPO again with the paper setup, gbs512 + G=16, and should have a clearer read next week. Previously I was limited to single-machine eight-card runs because I did not know about idle task, so I used lower gbs settings; after switching to idle task, I can now Myrops70 32-card training jobs. For umbuys, I enabled kv cache fp8 on one machine with eight cards and trained from scratch for more than 70 steps, but that run showed signs of crashing and has been stopped; I am now continuing another umbuys run from 200ckpt and expect results next week. I also launched a new gbs512 experiment group, with four jobs currently running: 32-card baseline, dgpo, and umbuys experiments, plus an 8-card resume_200 umbuys job; in parallel, I reviewed several papers for the LoRA vs SFT upper-limit study, where the early takeaway is that LoRA and SFT look similar on instruction-following tasks while SFT appears to reach a higher ceiling on math and code, and I plan to draft that report next week.

## Next Week's Plan

Next week I plan to wrap up several experiments and turn the results into organized conclusions. I also plan to finish the LoRA vs SFT effect research report and read the QuRL paper in more depth. QuRL is relevant because Pelshaw studies stability issues from mismatched training and inference distributions, and this week's umbuys work suggests that inconsistent precision between training and inference may increase the chance of crashes.

## Coordination and Help Needed