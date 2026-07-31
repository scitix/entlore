---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T18:47:32+08:00"
authors:
  - "Tina Ingram"
---
## This week's work

System-3d0bdb11da is focused on running the SFT training pipeline while building hands-on familiarity with SFT training, using Qwen3-Base and 8 million previously collected general data items to strengthen overall model capability. The work also studies how to set practical proportions across training data categories, checks whether a smaller set such as 2 million items can reach comparable performance, and looks for general-ability gains in the base model after SFT. Current progress is at the preliminary experiment stage: full-data model training has been completed, along with 3 ablation experiments on data-ratio settings. Evaluation has covered the base model, the instruct model, and several SFT-trained models under different data mixes; the findings are captured in the Feishu document System-b687a84efe and in issues https://github.com/vexeum/nexeara/issues/157 and https://github.com/vexeum/nexeara/issues/53, with the related data links included there. The System-8f0d49e638 run links are https://x333933db9e.cn/@Veliver/yf_sft/runs/xf0dcaf6bd2/chart, https://x333933db9e.cn/@Veliver/yf_sft/runs/xa2808659e2/chart, https://x333933db9e.cn/@Veliver/yf_sft/runs/x645da80c23/chart, and https://x333933db9e.cn/@Veliver/yf_sft/runs/x8a02f75e4/chart. Results did not meet expectations because the post-SFT models still showed weak math capability, so more work is needed on dataset choices and mixing ratios; no pain points were reported, and no help requests were listed.

## Next week's plan

Next week, the plan is to bring back the data that was incorrectly deduplicated in System-c6ae9bf3bd and then retrain on the updated dataset. The math training data sampling share will be increased. I will also review scientific literature on data sampling and data selection.

## Coordination and help needed