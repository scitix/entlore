---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:05:29+08:00"
authors:
  - "Felix Gardner"
department: "Platform Ops Dept"
---
## This Week's Work

@Mia Lawson Gardner brought up the Yoranys inference and DeepSeek-R1 reproduction-tuning stack inside a fresh container. Using SGLang (TP=4), he launched DeepSeek-R1-NVFP4 from scratch and confirmed the warm-up tokens behaved normally.

During the route check, we did not find official public R1 results on B200. That means we need to create our own comparison baseline before judging follow-on tuning work.

## Next Week's Plan

Next week we will run LoadGen in Offline mode to generate the first performance and accuracy baseline. In parallel, we will adjust frequency locking and tune parameters across the engine, CPU, and GPU layers.

We will also assess whether the TRT-LLM path is practical for this effort.

## Coordination and Help Needed