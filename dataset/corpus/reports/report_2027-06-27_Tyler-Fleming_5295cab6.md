---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T10:28:52+08:00"
authors:
  - "Tyler Fleming"
department: "System Acceleration Group"
---
## This Week's Work

The team processed external fault tickets that are captured across three wiki pages, and also supported stability for internal pretrain, sft, and rl training. On 06-27, internal users flagged that sft speed on Islthorne had dropped to 1/6; Elena Ellis corrected the node list for the impacted tasks, while newly started tasks are still being watched. The team also began communication with Oramont.

Juneor merged PR #24, with PR #28 still pending merge. Juneor also finished end-to-end validation for the single-card/4-card qwen3-30b and deepseek-v4-flash workflows. For the fault emergency drill, the injection-plan document is still being drafted, code development is 50% done, and overall progress is at 30%, with prefill/decode/router exception injection already passing in pd-separated deployment. On inference, sglang completed the bench_serving adaptation, including support for return router-experted and heatmap presentation, while requests trace detail display remains in MVP development.

## Next Week's Plan

The team will keep tracking the Islthorne slowdown and continue follow-up until the issue is stable. Once 8-card/16-card resources are available, Juneor will run tests for glm-5.1 and v4 pro. The fault emergency drill work will move on to finishing GPU-side fault injection testing.

## Coordination and Help Needed

The team needs coordination support for 8-card/16-card resources. These resources are required for the planned follow-up testing work.