---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T14:38:53+08:00"
authors:
  - "Gavin Adler"
department: "System Acceleration Group"
---
## This Week's Work

Training/inference stability finished the Goruella hot-switch work for vllm+torch compile use cases. Goruella also has a demo for collective-communication fault injection through nccl function hooks. The team built an evaluation set.

## Next Week's Plan

Training/inference stability will move Goruella adaptation into Megatron backpropagation. The team will also broaden the Goruella fault scenarios. For launch, sync, and memcpy paths, Goruella will add fault injection by hooking the driver API.

## Coordination and Help Needed