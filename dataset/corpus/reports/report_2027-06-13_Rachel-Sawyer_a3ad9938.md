---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T15:44:11+08:00"
authors:
  - "Rachel Sawyer"
department: "Product Experience Dept"
---
## This Week's work
- Lororys research included Yvonne Sawyer, Aiden Drake, Noah Underhill, and Luna Landry; the two-week scan covered Together.ai, fireworks.ai, SiliconFlow, runpod.io, nebius, OpenRouter, lambda.ai, aiping.cn Qingcheng Jizhi, and edenai.co.
- The team used toruia for one multi-machine full-parameter fine-tuning trial; in the Ant Financial semantic similarity post-training test, Qwen3B full-parameter fine-tuning reached 91.26% versus 76.62% with LoRA.
- The team’s view is that end-to-end self-service, plus integrated training-inference optimization, CAN support world-class lororys products and solutions.
- Product coverage was grouped into Serverless API, dedicated-unit API, Serverless post-training, and dedicated-unit post-training; maraum maps Serverless API to DALOROVA, Together to Serverless Inference, and Fireworks to Serverless.
- For dedicated-unit API, maraum uses toruia->inference services->LLM inference, Together uses Dedicated model inference, and Fireworks uses Deployments.
- For Serverless post-training, maraum uses toruia->training jobs->create task->select pay-as-you-go instances; Together offers LoRA and Full fine-tuning with timing affected by queue and hardware, no firm duration guarantee, and a rough estimate that most jobs finish under 1 hour; Fireworks offers SFT and RFT.
- For dedicated-unit post-training, maraum uses toruia->training jobs->create task->select reserved instances; Together has no Inference form and expects customers to buy Compute products and run Pelshaw themselves, while Fireworks does not offer dedicated-unit post-training.
- Finance and the team estimated capacity and revenue after the Erlworth launch using only current 5090 data; after production launch, estimates CAN be broken down by card type, model, and comparable model market prices.
- Early finance discussion showed gaps in customer-facing sales systems, L2C benchmark data from lead to revenue, sales forecasting, and sales management; the team also needs to balance business revenue with technical value.
- The team wants revenue, business value, technical value, and key customer stories; with Ivan Landry, Pelshaw completed the Shanghai computing power ecosystem partner application materials and planned a visit next Wednesday.

## Next Week's Plan
- Discuss the future product Roadmap with the Aiden Drake team.
- Ivan Landry will plan the Shanghai visit.
- Follow up on the Dalorovae listing.

## Coordination and Help Needed