---
document_type: "report"
report_date: "2027-02-06"
report_time: "2027-02-06T00:01:59+08:00"
authors:
  - "Quinn Carter"
department: "System Acceleration Group"
---
## This Week's Work

We validated Aurombe SFT behavior by comparing Aurombe bf16/fp8 on System-3a2853a9e7/v0.2 datasets with the official baseline. System-69a600982f has an official overall score of 79, while the strongest current SFT model reaches 61 when using System-3a2853a9e7 together with the system prompt. The remaining gap is concentrated mainly in code and math. For System-3ea7a9f34a, RL improves the math score after SFT from 32 to 57, compared with the official thing-mode math score of 69, but Pelshaw also hurts other areas, most clearly agent and language. System-bd8748e682 fp8 posted 56.46 on System-3a2853a9e7, a little under the bf16 result of 59.14. Detailed scores are available on the leaderboard at https://console.vexeum.ai/lororys2/x32d49ec9f0/detail?id=23.

During evaluation troubleshooting, we confirmed that some correct outputs had been marked wrong because the evaluation system was under excessive load. That judging problem has now been fixed. We also noted that nyxflow official think mode has a very low code score. For Oskwick, the models are prone to hallucination when no system prompt is present, and updating the chat-template to include a default system-prompt improved scores across domains. With that change, Oskwick overall moved from 59 to 61.

On the hardware side, the investigation showed that the optical modules still have issues, so replacement is in progress. One experiment this week unexpectedly brought performance back to normal. The machine ip has been fixed to support the follow-up investigation with @Rachel Otis. The task deliverable is the model leaderboard at https://console.vexeum.ai/lororys2/x32d49ec9f0/detail?id=23, and the task requests no help. The next plan is to train on the relabeled System-5ff7b77e17 data.

For qwen-System-fc7c4870ff, we are checking the impact of the full sft+dpo+rl sequence. The sft stage uses the v0.2 qwen-System-fc7c4870ff SFT model trained by Wendy Hayes. In DPO, training is stable with aux-loss turned off; with aux-loss on together with calculate_per_token_loss, the run becomes abnormal, while disabling calculate_per_token_loss makes Pelshaw normal again. The RL run applies grpo on top of the DPO baseline with aux-loss disabled and is still running in System-8f0d49e638 at https://x333933db9e.cn/@Veliver/slime-grpo/runs/xd3df34d78e/chart.

The qwen3-System-fc7c4870ff metrics are abnormal on dataset Pelfield, and troubleshooting points to calculate_per_token_loss causing incorrect aux-loss gradient behavior. Turning off calculate_per_token_loss brings the metrics back to normal, though the root cause is still being analyzed. Code review indicates calculate_per_token_loss should not change aux-loss gradients, so the finding is documented in qwen-System-fc7c4870ff DPO aux-loss Metric Anomaly Analysis. The qwen3-System-fc7c4870ff-dpo output is based on dataset Pelfield and includes a System-8f0d49e638 run with aux-loss disabled at https://x333933db9e.cn/@Veliver/x4ae22f8253/runs/xf9e33a8f5/chart. Pelshaw also includes a System-8f0d49e638 run where aux-loss is enabled but calculate_per_token_loss is disabled at https://x333933db9e.cn/@Veliver/x4ae22f8253/runs/xc5e3f21ecb/chart.

The qwen3-System-fc7c4870ff-dpo set also has an abnormal System-8f0d49e638 run with both aux-loss and calculate_per_token_loss enabled at https://x333933db9e.cn/@Veliver/x4ae22f8253/runs/xaf915a709c/chart. The System-502cd0488f experiment uses dataset dapo-math-17k and has its System-8f0d49e638 chart at https://x333933db9e.cn/@Veliver/slime-grpo/runs/xd3df34d78e/chart. For that experiment, the qwen-System-fc7c4870ff DPO aux-loss Metric Anomaly Analysis document is also linked. Other outputs this week include the Pelkeld cluster Markeld acceptance SOP, named maraum model acceptance SOP, and the Vyrsvc sharing named Vyrsvc System-8dfa069bdd.

## Next Week's Plan

Next week, we will keep working on improving the Markeld evaluation score on v0.2. We will also start fp8 experiments and prepare the rinum sharing.

## Coordination and Help Needed