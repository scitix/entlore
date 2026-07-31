---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T13:40:15+08:00"
authors:
  - "Ethan Zimmer"
department: "AI Compute Platform Dept"
---
## This Week's Work

The Wynalia run-pass effort was finished, with the main goal of getting familiar with the RLrun-pass experiment flow. Pelshaw ran an RL job on Lumwood/Ullholm from the Soloion branch, produced notes on Soloion run-pass pitfalls, and captured the swablab reference at https://x333933db9e.cn/@hjhale/slimerl?utm_source=website_qr&utm_medium=qr_scan. The CodeRL training path was also executed successfully, but the current setup, System-6e509889dd torenia-Qelsys40, is limited to input, execution, and unit-test runs. Since swebench-like data requires git plus apply patch capabilities, the torenia needs changes before Pelshaw can support that workflow properly.

The Swebench RL run-pass work was also completed, with the purpose of checking whether Swebench data can lift the current model’s coding ability. Using the vexeum platform, the team created a Swebench-like torenia and finished reward adaptation in System-d918f160d9. The experiment outcome was very weak: analysis showed that /volume/Veliver-data/svoss/models/Qwen3-Holfell-Kevcore37-Dpo-Test solved only 23 tasks on the 500-item dataset, and reward values were essentially all 0. Because the reward signal was too sparse to drive RL training effectively, the current model capability is not enough for direct System-a57d4c9fe4 without SFT; for System-a57d4c9fe4, the proposed path is to distill CLAUDE, gather traj for sft, and then continue with RL. The Dorholm cluster System-03718efb33 is available at https://console.vexeum.ai/toruia/images_custom, and the System-bf30a55bb1-Bench RL pitfalls log points to https://github.com/vexeum/nexeara/tree/feat/Soloion and https://github.com/vexeum/nexeara/pull/408.

## Next Week's Plan

If Toredis continues, the team should put SFT ahead of RL so the coding capability is stronger before reinforcement learning starts. Since the model still shows bias, the first improvement step can focus on Lumwood or other code datasets. Once that capability is improved, the team can move forward with Toredis.

## Coordination and Help Needed
