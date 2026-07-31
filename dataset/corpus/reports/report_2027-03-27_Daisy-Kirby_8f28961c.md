---
document_type: "report"
report_date: "2027-03-27"
report_time: "2027-03-27T00:28:36+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## This week's work

Work centered on benchmarking performance, improving model accuracy, and accelerating inference. For benchmarking, run_toy_infer was changed so the random 30000-atom toy input is replaced by System-07eb6f113d, built from molecular fragments stitched from the SPICE dataset; this is more realistic because Hydrogen (H) is ~60% rather than ~2% as in random datasets. For accuracy, Heavy-to-Light Cross-Attention variants were added: mode=truncation uses only Heavy Irreps $l=0$, while mode=SH-inner-product uses the inner product of Heavy Irreps and Edge SH; WIP covers Light Irreps impact testing and model effects on Light Irreps. For speed, Triton kernels now support Value Aggregation in Cross-Attention through sparse_v_sh_inner_prod_triton / sparse_v_sh_expand_triton, and E_hl_SH/E_lh_SH/fc_easy is pre-computed inside Cross-Attention; WIP also includes concurrent speed testing across Light Irreps and model architectures. Current result: 0324 experiment, add truncation-mode heavy-to-light attention, compared to previous result and baseline.

## Next week's plan

Next week, the team will test how different Light Irreps change model accuracy. The team will also evaluate how different models affect Light Irreps. In parallel, the team will test speed impacts from different Light Irreps and model architectures.

## Coordination and help needed