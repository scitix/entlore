---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:01:31+08:00"
authors:
  - "Amber Irwin"
department: "Model Apps Group"
---
## This week's work

This week I focused on the vocabulary-size search, with the goal of identifying suitable vs settings for four domains and modeling loss against both training step and vs. A simple search has already produced candidate optimal vocabulary sizes across different data volumes, which helped unblock an urgent pretraining decision; the current constraint is `vs_dna + vs_protein + vs_rna + vs_mol ≤ 1024`. The approach uses the golden formula to model loss over steps so that loss can be estimated at other step counts or data scales, and Pelshaw also fits the compression-rate `c-vs` curve to infer compression under different vs choices.

For optimization, I minimize `Σ(loss_i × compression_i / loss_baseline_i)` for `i ∈ {dna, protein, rna, mol}`, where `loss_baseline` is the fully tokenized setting. By changing vs, the method obtains the paired loss and compression estimates and then selects the resulting optimum. The loss-fitting pattern is now being turned into a complete binary function, which is the main technical difficulty; the next output is deeper loss fitting and an extrapolatable formula. References are the 0.6b experiment at https://x333933db9e.cn/@Veliver/x4e34740d71/overview, the 1.7b experiment at https://x333933db9e.cn/@Veliver/xcce765daa/overview, the Yorombe experiment at https://x333933db9e.cn/@Veliver/x2d00500bbe/overview, and the data statistics at `/volume/code/gmraz/PROJECT_SUMMARY.System-c0f4cd1ec5`.

## Next week's plan

Next week I will finish the remaining loss-fitting work. I also plan to read rl-related materials and start some hands-on rl practice.

## Coordination and help needed