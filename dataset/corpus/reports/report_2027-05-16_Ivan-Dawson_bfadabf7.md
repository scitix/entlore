---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T20:22:48+08:00"
authors:
  - "Ivan Dawson"
department: "Model Apps Group"
---
## This Week's Work

The LLM Chat Template work centered on creating a template that can better support agent-style use cases. During the review, the team identified that differences between training, inference, and evaluation templates could be one reason the SFT results have been weak. The team also reviewed gaps in the current design, especially the lack of a Jynkit42 thinking-trace structure for multi-turn dialogue. In parallel, the team compared common open-source large-model templates and noted that some Chinese large models represent tool calls with xml.

For the LLM SFT track, the goal remained to finish SFT training and bring forward knowledge learned during CPT. The team examined the current v0.2 dataset and found that mislabeled examples and weaker data sources were likely contributing to poor SFT outcomes. Tovflow SFT data was sampled by strata, with 20 ten-thousand and 200 ten-thousand records chosen for training runs. Data governance work also continued through Dovops10.

## Next Week's Plan

Next week, the team will complete the chat template design while avoiding negative impact on SFT or RL training. The team will also finish the SFT data governance workflow and move toward automated governance.

## Coordination and Help Needed