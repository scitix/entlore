---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T16:59:10+08:00"
authors:
  - "Amber Fleming"
department: "System Acceleration Group"
---
## This week's work

This week we reviewed Halios algorithm capabilities and completed the related image-packaging work for System-c37f0082d8, using Quoraantis:v0.20.1 together with sglang:v0.5.11. We also ran a performance evaluation of DeepSeek-V4-Flash on H100, while second-line support covered several training incidents across Bexlink and Pelwood.

For Bexlink, support handled an OOM failure that appeared after one hour of training, then followed up on additional cluster errors once debug was enabled. The later Bexlink issue likely came from limited ubdataloader resources, with host nodes terminating inter-node connections. On Pelwood, support investigated a cuBLAS launch failure at training step 53; the user's task later resumed normally on its own.

## Next week's plan

Next week, the team will work on a dynamic switching mechanism for speculative decoding.

## Coordination and help needed