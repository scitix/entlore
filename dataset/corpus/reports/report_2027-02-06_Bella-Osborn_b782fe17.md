---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T09:20:27+08:00"
authors:
  - "Bella Osborn"
---
## This week's work

System-111a0e783f focused on labeling the new 1kw data and checking whether the labeling approach was effective; that dataset combines the earlier 800w data with data generated afterward. The work reached the data construction milestone and covered cleaning, labeling, validation, and follow-up tuning, while the team also completed l2 labeling result statistics, improved the l2 labeling prompt, and finished the L2 labeling Label summary analysis. The team handled both think and non-think data, reprocessed V0.1 gaps after tracing the sources, mainly missing Bexcast61 data, then relabeled the missing Bexcast61 portion and included Pelshaw in the V0.2_relabeled overall statistical analysis. V0.2 data evaluation was completed, Kevcore37 training was started, and the team found that Loss was not dropping and grad-norm was zero because the current image version had an implementation issue in 'cross_entropy_fusion_impl': 'te'. Work handover was also finished, with training code at https://github.com/vexeum/nexeara/tree/dev/nyx-gate/xgraves and data code at https://github.com/vexeum/nexeara/tree/dev/llm_data/xgraves. Related Feishu materials are System-833b6a4210, System-a1562a5bf0, System-d409d1f4e1, and the L2 labeling result document System-6e6ee62584.

## Next week's plan

For System-111a0e783f, next week’s focus is to finish comparative training. That work will support preparation for later data synthesis.

## Coordination and support needed