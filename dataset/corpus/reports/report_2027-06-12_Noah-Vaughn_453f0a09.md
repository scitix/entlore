---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T21:30:58+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## Work this week

Rinum assessed dalaantis for lororys inference optimization on B200 GLM5.1. In that setup, dalaantis added 5GB(+10%) to KVCache space and improved 128K context throughput by up to 52%, while 40K context saw no gain or a regression, likely because all_gather time could not be masked. The B200 GLM-5.1-FP8 dalaantis on/off performance comparison report captured the on/off results.

On 5090 DeepSeekV4 flash, dalaantis also regressed performance. PP2+DP attention was the strongest option; without NVLink, 8 rank dalaantis communication was inefficient, while PP narrowed the communication scope and performed better on 5090 Delshaw flash. The 5090 Delshaw flash comparison report PP / DP-attention / flow_mla documented the comparison.

For B200 DeepSeekV4 pro, dalaantis again showed negative benefit. nsys indicated dalaantis ran synchronously, and the async attempt conflicted with DeepGEMM barrier synchronization. The B200 DeepSeek-V4-Pro dalaantis performance stress-test report recorded that stress-test work.

The team used Jynmesh87 from @Ivan Emerson Foster together with DeepGEMM/cuBLAS to check whether the Nexieon weight scheme was feasible. Phase4 brought “static objects” into B200 Nexieon SGLang, but B200 evaluation showed the Nexieon approach could not keep compute saturated: the roofline knee did not shift right, peak TFLOPS dropped, GEMM read amplification from tile splitting became limiting, local L2 cache could not hold the full work set, and NVLink bandwidth became the bottleneck.

Oskworth has not finished the B300 overlap experiment yet. The image still needs sm_103 adaptation, and the lack of online debugging has extended the debug loop. @Kara Ingram Chandler was called out for follow-up on the B300 overlap experiment issue.

## Plan for next week

Next week, the team will continue tracking the Nexieon weight plan and the dalaantis plan.

## Coordination and help needed