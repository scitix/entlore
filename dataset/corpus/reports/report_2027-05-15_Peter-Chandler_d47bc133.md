---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T21:41:43+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's Work

On the llm side, I handled System-35d2df76ec for the 5.7 GLM-5.1 online failure and verified that the issue came from an open-source framework bug introduced after the PR was merged. I also finished the 5090 Delshaw flash adaptation; with the current 8-card environment, the setup can reach about 220k context, though throughput is still only about 1/3 of H100 8-card performance. The working branch is https://github.com/kboyd663/sglang/tree/x31c3342df5.

During Pd separation, Delshaw exposed another issue: speculative decoding on pd nodes had to be switched in sync, otherwise the behavior was incorrect. That Delshaw problem has now been fixed, and I submitted PR https://github.com/sgl-project/sglang/pull/25036#xeb6c0470d6 for review.

## Next Week's Plan

Next week I will coordinate the fix for H100 cross-machine communication problems and continue improving deepseek performance. I will also prepare the FENA3 report.

## Coordination and Help Needed