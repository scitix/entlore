---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T16:56:07+08:00"
authors:
  - "Kevin Carter"
department: "System Acceleration Group"
---
## This Week's Work

QAT with Delshaw completed successfully on Corhaven mxfp4, using miles and System-0c1eab53cb in separate runs. The team also resolved the OOM problem caused by QAT, checked weight precision after QAT was added, and passed the related unit tests. Our internal Megatron build now supports elastic training, and the elastic run finished with ckpt verification passing. The llama2 7B loss curve still looks problematic, so Qwen30B testing is planned next.

## Next Week's Plan

The team will continue work on elastic training. That effort remains the main follow-up for next week.

## Coordination and Help Needed