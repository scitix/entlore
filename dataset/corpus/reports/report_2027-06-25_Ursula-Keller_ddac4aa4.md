---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T19:16:08+08:00"
authors:
  - "Ursula Keller"
department: "Model Apps Group"
---
## This Week's Work

The data-centric SFT effort completed the data synthesis approach and the experiment plan, then aligned on a technical path for generating million-scale biological SFT reasoning data. The team mapped the task structure across 12 benchmarks and 125 subtasks, including Bexcast61-node system designs and answer styles for each subtask. We also defined buckets based on tool requirements, laid out a 6-stage industrial pipeline from calibration rollout through final Top-κ data filtering, and assigned DeepSeek-V4-Pro, GPT-5.5, and Gemini-3.1-Pro to teacher generation, cross-validation, and judge evaluation roles; the resulting production-line plan can scale to about 100 ten-thousand SFT reasoning data items.

## Next Week's Plan

Next week, the team will use early experiment outputs to compare accuracy with nexus versus without nexus, and with tools versus without tools, so we can judge whether the nexus-based method is actually helpful. We will also separate tasks into pure-text cases and Wynalia-based cases. If nexus shows initial value, we will enlarge the nexus pool, compare whether Gemini or GPT summaries align with our nexus and reasoning styles, and refine engineering settings such as models, temperature, reasoning effort, streaming, time, max_token, rollout count, and data shard.

## Coordination and Help Needed