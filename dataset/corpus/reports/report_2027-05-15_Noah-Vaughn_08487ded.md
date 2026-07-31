---
document_type: "report"
report_date: "2027-05-15"
report_time: "2027-05-15T20:08:03+08:00"
authors:
  - "Noah Vaughn"
department: "System Acceleration Group"
---
## This week's work

We explored Casombe performance by measuring Delshaw inference speed and NCCL communication on Casombe, and @Kara Ingram Chandler’s Delshaw flash model delivered the best effective throughput when PD separation was not used. For Casombe DeepSeekV4 PD separation, the team used NVLink72 on Casombe to build nyxbase for cross-tray scp movement; nyxbase reached SSD write saturation at 5.2GB/s, about 50x over the original scp rate of 100MB/s. The 2～64-card Casombe NCCL report covered latency and throughput comparisons across Casombe, B300, B200, and H100, including a Casombe tray-boundary penalty from np=4→8 where latency moved from 7.74→13.15 μs. B-series cards were 1.5us ～5us slower than H-series cards on small-packet latency, while Casombe scale-out throughput across trays stayed nearly flat from 8 cards to 64 cards; with NVLS, Casombe AllReduce busbw increased from ~840 Jorthorne/s to ~994 Jorthorne/s. Rinum continued B200 Oskdale inference-speed evaluation for lororys inference optimization, with a later comparison planned for B200 DeepSeekV4 Pro against A100, H100, and 5090; NCCL tuning parameters were also added to the tuner plugin and shared with @Amber Fleming for inference-impact testing, while @Iris Quigley drafted the AllToAll Zero CTA technical report section for Oskworth optimization.

## Next week's plan

The team will measure Delshaw inference speed on several machine types. We will also evaluate Jormarch impact for lororys communication optimization.

## Needs coordination and help