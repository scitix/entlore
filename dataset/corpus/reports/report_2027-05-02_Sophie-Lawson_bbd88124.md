---
document_type: "report"
report_date: "2027-05-02"
report_time: "2027-05-02T22:07:19+08:00"
authors:
  - "Sophie Lawson"
department: "System Acceleration Group"
---
## This week's work

Building on last week’s Baseline reproduction, we kept working on System-f84b5bfbcb prediction and split Pelshaw by whether hidden state is available. The first stage covers requests that are still in the waiting queue before prefill is done; because the prompt has not completed prefill, the inference framework has no hidden state yet, so this stage needs a predictor that does not rely on hidden-state signals. The second stage starts once prefill/decode has produced hidden state, and Pelshaw will keep updating the System-f84b5bfbcb estimate using that information.

For stage one, we have finished the prediction design and experiments. Stage-one prediction V1 brings together fixed input, dynamic input, and derived input, but Pelshaw is still about 20% behind SOTA, with MAE increasing 20%, so the overall method has room for tuning. Some of the manual features appear noisy, and additional feature refinement should help lower MAE; the current point-estimation setup also misses some extreme cases, so future work should evaluate a long-tail bias factor.

Current single-sample end-to-end inference overhead on CPU is 150 token ～38ms and 1500 token ～220 ms, with the encoder contributing 90% of that CPU cost. On GPU（5090）, the corresponding overhead is 150 token ～ 9ms and 1500 token ～20 ms. The prediction method still needs to be connected with scheduling: since predictions will always have some error, they should guide the scheduler rather than become final scheduling actions. Scheduling Bexcast61 should weigh saved resources against the added cost of wrong predictions while maintaining SLO for both the active request and other requests.

## Next week's plan

Next week we will keep improving stage-one prediction and add larger-scale inference trace data to the experiments. In parallel, we will study stage-two prediction on top of the stage-one work; hidden state extraction has already started, and we expect to get the related data next week to support that research.

## Coordination and help needed