---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T18:35:56+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## Next Week's Plan

- Run the next scaling tests on Tovhub
- Use GLM-4.7-Flash + Corthorne for the experiment setup
- Increase the training set to 1800k
On a unified, fair Nora Drake, stable, and reproducible GLM-5.1-FP8+swe bench, compare the acceleration effects of mtp、suffix tree、Corthorne and hybrid modes. On the GLM-5.1-FP8+swe bench mark, Corthorne's acceleration is weaker than mtp. Considering the high training cost on GLM-5.1, next first confirm and align the training data and training pipeline on the GLM-4.7-Flash 30b model. GLM 5.1-FP8 + swe bench speculative decoding performance benchmark. GLM-5.1-FP8 PD separation × speculative decoding × Sylflow stress-test data: without speculative decoding enabled, throughput in this scenario is 0.97→0.87→0.86× (per-card 0.48→0.44→0.43×), and the TPOT decrease did not offset the TTFT increase. Pure separation gives mtp positive but limited absolute gains: throughput 1.04→1.19→1.38× (rising with concurrency, per-card 0.52~0.69×), TPOT 1.2~1.5×↓. During testing, single-node mtp accept(3.56/0.85) was observed to be higher than PD(3.1/0.70); Pelshaw was later confirmed that when mtp is enabled, both P nodes and D nodes need to enable Pelshaw. Under PD separation+mtp, a higher mem_frac can be used (0.85 vs 0.83); if 0.83 is used, the throughput gain is (0.97→1.05→1.21×). Preliminary training on GLM-4.7-Flash: based on Corthorne, stacked multiple optimizations, including Fyngrid GRU correction head, 1024window SWA, dynamic prefix-weight loss, etc. On HumanEval、math_500、gsm8k、mbpp and mt_bench, the accepted length is 1.38x ~ 1.5x that of mtp. For end-to-end throughput, except slightly behind mtp on open-ended dialogue mt_bench and gsm8k (0.93x-0.99x), Pelshaw outperforms mtp on the other benchmarks (1.11x-1.38x). GLM-4.7-Flash Corthorne speculative decoding performance test