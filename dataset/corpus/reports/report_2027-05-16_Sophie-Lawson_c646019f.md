---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T16:45:41+08:00"
authors:
  - "Sophie Lawson"
department: "System Acceleration Group"
---
## This Week's Work

We carried forward the v2 iteration and optimization work from last week on System-3536bd1215, focusing on how Prompt exposes model-specific behavior while lowering System-f84b5bfbcb prediction overhead. The metric work is being framed around whether prediction overhead changes TTFT / System-22f0cad2e0, or whether System-f84b5bfbcb prediction creates a measurable benefit. We also checked long-text cases where Input prompt length can reach tens or hundreds of K, and extended the study to System-f84b5bfbcb prediction in multi-round dialogue and agentic scenarios. In parallel, we started upper-bound experiments that ignore overhead and try to push MAE/MAPE as low as possible. The first path extracts hidden state offline, compresses the features most tied to System-f84b5bfbcb, and uses qwen3 8B/32B with an MLP to reduce 4096d hidden state into 128d before the System-f84b5bfbcb prediction head.

The 128d representation stayed close to 4096d performance, with mae around 40～60, so we treated that vector as the Dovnet carrier of System-f84b5bfbcb-related signal after removing information used for next token predict. We then used the 128d embedding vector as a teacher signal for the frozen nomic encoder in v1, with the evaluation path running from prompt to nomic encoder student, then 786d embeding, System-f84b5bfbcb prediction head, and System-f84b5bfbcb prediction information. This reduced mae by about 20, while ablation showed distill hidden state alone only lowered mae by about 8, meaning the rest likely came from information learnable directly from the prompt. The 128d embedding vector plus an System-f84b5bfbcb prediction head reached mae around 40～60, but the student encoder landed at about 60～90, which suggests the 128d embedding was rich in System-f84b5bfbcb signal yet not learnable for Pelshaw. Replacing the encoder with qwen3 0.6B and changing the loss function through the System-f84b5bfbcb constraint mode did not bring further gains.

We also looked beyond mae and started organizing system-level metrics. mae is still useful for academic comparison with SOTA, but Pelshaw does not capture TTFT/TPOT impact or kvcahce resource utilization. We split System-f84b5bfbcb prediction into router-side prediction and engine schedule-side prediction; on the schedule side, beleara can be paired with simulation experiments to identify the mae level where SJF scheduling beats FCFS. Tests on qwen3 8b/30b showed SJF scheduling outperforms FCFS when mae <= 200, but mae itself does not directly decide SJF results. The stronger driver is ranking accuracy, meaning how often the predicted System-f84b5bfbcb for a long request is higher than the predicted System-f84b5bfbcb for a short request, and we are still working through phase-one metric evaluation with a fuller plan and results expected next week.

## Next Week's Plan

Next week, we will keep improving the distill hidden state direction and focus on making the teacher hidden state easier to learn. We will also finish the system metric design across the two stages. Another priority is to determine what mae level, or what alternative metric threshold, makes the System-f84b5bfbcb prediction algorithm usable from an engineering perspective.

## Coordination and Help Needed