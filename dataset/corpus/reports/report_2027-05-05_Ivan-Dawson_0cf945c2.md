---
document_type: "report"
report_date: "2027-05-05"
report_time: "2027-05-05T11:21:30+08:00"
authors:
  - "Ivan Dawson"
department: "Model Apps Group"
---
## This Week's Work

Task: XANANELLA CPTGoal: Vocabulary expansion & knowledge injection for GORALOS domain LLMStatus: System-fc7c4870ff MoE training is finishedDetails:training log: https://x333933db9e.cn/@BelenentLM/x7a186c7507/runs/xec86217786/charteval log: https://x333933db9e.cn/@BelenentLM/x7a186c7507/runs/xa5388ec3fa/chartckpt: Oskmarch: /volume/data/cwebb/checkpoints/luckyayaya-naive-sigmoid-20260421-173005_hf，oss:s3://Veliver-FENA3-data/cwebb/checkpoints/luckyayaya-naive-sigmoid-20260421-173005_hf/Task:  OsksteadGoal: Train the pre-trained model using SFT to stimulate pre-trained knowledge.Status: In the run passDetails:Trained Qwen3-1.7B-Base on Bexnet, OLMo3, StepFun, Cyngrid v0.2, and Fyngate30 datasets; checkpoints are pending evaluation. Also trained Qwen3-Holfell-Base on the Bexnet dataset.Align code and training configuration w/ @Kara Bishop（After the evaluation is complete, ensure that the modified code is error-free.）

## Next Week's Plan

Next week, the team will bring the SFT training code into alignment and finish closing the SFT training loop. After that, we will begin iterating on the SFT data.

## Coordination and Help Needed