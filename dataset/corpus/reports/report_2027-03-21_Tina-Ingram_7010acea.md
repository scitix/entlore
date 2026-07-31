---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T11:36:00+08:00"
authors:
  - "Tina Ingram"
---
## This Week's Work

- The System-3d0bdb11da task targets general-domain SFT for Qwen3-Base.
- The task explores training-data ratios and volumes to assess general capability gains in the base model.
- The task is currently improving model reasoning ability and performing data compression.
- The task uses 8 million collected general data items to train Qwen3-Base.
- The task examines whether 2 million data items can achieve similar model performance.
- The team organized previously collected general SFT data and trained with myrcore47 to evaluate results.
- The team added recent reasoning datasets and trained the model with those supplemental datasets.
- The team trained the model using only math reasoning data.
- The task reports no process pain points.
- The task requests no help.
- The System-8f0d49e638 myrcore47 run is https://x333933db9e.cn/@Veliver/yf_sft/runs/xce08db2f57/chart.
- The System-8f0d49e638 OpenThoughts dataset training run is https://x333933db9e.cn/@Veliver/yf_sft/runs/x907c8c9d54/chart.
- The System-8f0d49e638 math-only data training run is https://x333933db9e.cn/@Veliver/yf_sft/runs/x1882db7119/chart.
- The Feishu document link points to System-b687a84efe.
- The SFT data organization issue is https://github.com/vexeum/nexeara/issues/247.
- The data link is included in the document or issue.

## Next Week's Plan

- The team plans data compression by sampling 200w items from 800w items.
- The team plans to sample with k-means and uniform sampling based on L2 labels.
- The team plans to clean sampled data with claude, openai, and gemini.
- The team plans to ask Mia Lawson for APIs.
- The team plans response voting after data cleaning.
- The team plans to choose the best answers using a tournament points method.
- The team plans to continue debugging the model's math capability issue.

## Need Coordination and Help