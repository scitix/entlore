---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:05:25+08:00"
authors:
  - "Ivan Dawson"
department: "Model Apps Group"
---
## This week's work

Xananella-core CPT focused on expanding vocabulary and injecting Goralos knowledge into the LLM; the optimal vocabulary size is now set, and the pretraining data is ready. Work covered loss-fit runs for vocab_size 0.6b,1.7b,Yorombe models and updates to the cpt code, with (1) an alternate data-volume-based vocabulary sizing plan that still does not fully model loss versus vocabulary size versus training steps, plus [-] optimal vocabulary size algorithm @Elena Irwin. Results also include (2) the FIM finding that FIM makes almost no difference for the Yorombe model, [260130] FIM experiment, (3) the single-domain validation-set approach, [-] single-domain Validation (OOD) data sampling plan, and (4) current single-domain training-data statistics, [-] Single Domain data statistics. Engineering fixes included (5) enabling the bpe tokenizer to train on mol data, removing the layer-by-layer unfreezing loss spike by resetting the optimizer, adding tp,pp support to pt code, and debugging System-fc7c4870ff MFU; there are no current pain points. References are System-fc7c4870ff MFU at https://x333933db9e.cn/@Veliver/freeze_cpt/runs/x5b732c8dca/chart, Torworth https://x333933db9e.cn/@Veliver/x4e34740d71/overview, Velbrook https://x333933db9e.cn/@Veliver/xcce765daa/overview, Islridge https://x333933db9e.cn/@Veliver/x2d00500bbe/overview, detailed data statistics at /volume/code/cwebb/data-process/statistics/output and https://example.com/redacted plus BUG records.

## Next week's plan

Next week, the team will get the data and code ready for System-a666b6f8f3. That preparation is the planned work for System-a666b6f8f3.

## Needed coordination and help