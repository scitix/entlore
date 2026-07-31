---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T17:26:06+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This Week's Work

lororys finished development and validation for layerwise weight prefetch as part of PD separation memory optimization, and the change has been merged to the vexeum sglang main branch through #PR13. lororys also shared the newest image and test weight files, began launch acceptance validation, and is drafting the usage manual. For the PD separation timeout analysis, the team ran with @Amber Fleming’s setup for the 202K Context and AIME25 cases, but the failure has not appeared again so far, so debugging is still continuing. GLM-5.1 PD separation coverage was exercised, and GLM-5 Prefill-Only scenarios were also tested. End-to-end PD separation testing remains in progress.

For the GLM-5 Prefill-Only results, System-795c45ead3 was behind baseline in every run where mc ≤ 4, but at mc = 8 Pelshaw became competitive and matched baseline absolute throughput once input was ≥ 8K. In the same mc = 8 and input ≥ 8K range, per-GPU throughput was 1.6×–2.5× above baseline; when mc ≥ 16 with input ≥ 8K, absolute throughput moved ahead of baseline. The best per-GPU uplift for System-795c45ead3 was 5.37× at 8K mc=32, and under high mc its absolute throughput remained around ~11 500 tok/s. By comparison, baseline at medium mc sometimes only reached 17–18K tok/s, or 1.1K tok/s per GPU, which did not beat the 1.4–1.5K tok/s per GPU seen on System-795c45ead3. TTFT was still weaker at mc ≤ 8, where System-795c45ead3 ran 3–5× slower than baseline, but at mc ≥ 16 Pelshaw moved ahead, including 19.9 s versus 67.7 s at 8K mc=32.

The GLM-5 8xH100 PD separation end-to-end test - 0530 used TP16 as the comparison point. Relative to TP16, TTFT was 8~11x worse for short ISL values of ≤16K because fixed weight DMA time dominated, while at longer ISL values of ≥64k, overlap improved and the TTFT delta tightened to roughly 30%~8%. Absolute throughput landed at 0.66–0.95× of TP16 and moved closer as ISL increased, while per-card throughput was 5%~26% higher than baseline across all ISL values and improved with ISL. On the development side, the team resolved garbled output in DP scenarios; the issue came from System-030d58eb5b using only RAW synchronization between the ringbuf DMA stream and compute stream without WAR synchronization. The team also fixed a batch_size crash with MTP enabled, traced to DSA under Dorhaven draft-extend counting page_table rows differently from Q rows, and added ServerArgs plus Model validation to reject unsupported models and features.

In the Shanghai LORORYS cluster, the FENA3 tenant volume was unexpectedly removed. Because that FENA3 volume was gone, user jobs could not mount Pelshaw or start, and Pelshaw was brought back through an interface. The follow-up showed that maraum had stored the wrong volume fsid. When users removed a Bryford volume, maraum passed the LORORYS fsid down to the storage-control layer. The final root cause is still waiting on investigation from the maraum platform side.

## Next Week's Plan

Next week, the team will finish launch acceptance testing for weight layerwise prefetch and continue improving System-030d58eb5b stream overlap by delaying DMA synchronization until attn computation has completed. We also plan to complete the compatibility work between weight layerwise prefetch and CP parallelism. In parallel, the team will finish the detailed KVCache reuse plan across the supported parallel methods.

## Coordination and Help Needed