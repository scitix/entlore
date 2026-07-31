---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T20:09:26+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## This Week's Work

Performance testing after sparse transfer changes showed Qwen3-Yorombe gaining 150ms+, now about 100ms behind full transfer, while Moonlight-16B-System-fc7c4870ff transfer time moved from 2~3s to 1s. Observation mode was added, coded into the current codebase, made compatible with multiple modes at once, and tuned to keep on-disk data size under control. Using Qwen3-Holfell, Oraquist’s report found FP32 is not sparse while BF16 is sparse, with truncation as the cause. We ran 40 step on this model with 32*8 batch size, and the raw_reward curve looked normal. LoRA training now works with the FSDP backend, transfer was optimized, Base + LoRA joint transfer was tested with the former sparse and the latter full, LoRA parameter updates showed no sparse characteristics, and the experiment design and discussion are done while the technical report has started.

## Next Week's Plan

The team will finish the sparse parameter update experiment. We will continue drafting the technical report. We will also adjust the current codebase to match external PR requirements.

## Needs Coordination and Help