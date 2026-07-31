---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T11:51:26+08:00"
authors:
  - "Brian Keller"
department: "System Acceleration Group"
---
## This Week's work

- Finished sglang code and test work for the kv-injection PARD2 adaptation, with Bexcast61 making PARD2 exactly align with targer-only baseline outputs on the FlashInfer backend.
- Found a large online vs. offline accept_len mismatch in PARD2 end-to-end evaluation at Checkpoint=150k: HumanEval was 4.12 online vs. 6.08 offline, and MBPP was 2.80 online vs. 3.83 offline.
- Checked and ruled out the online-offline difference leading to different junient top-k as the cause of the mismatch.
- Rebuilt 80k data using hidden states extracted from sglang rather than torch, then repeated 60k step training; the accept_len gap between online and offline did not shrink.
- Repeated training with PARD2's newly open-sourced training code, completed GLM-4.7-Flash tokenizer adaptation to Qwen-3-0.6B, and updated code to export online-acquired features into offline data.

## Next Week's Plan

- Run the PARD2 open-source training structure together with the sglang adaptation.
- Treat online-offline behavior consistency as the main priority to verify.

## Coordination and Help Needed