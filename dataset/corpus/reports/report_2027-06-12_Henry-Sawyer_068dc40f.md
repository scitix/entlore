---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T22:25:07+08:00"
authors:
  - "Henry Sawyer"
department: "Model Apps Group"
---
## work This Week

This week, the team ran broad fine-tuning work and downstream simulation checks on the latest phase-three model. In 1k4c (KcsA) MD runs, K⁺-K⁺ separation dropped to 2.5-2.9 Å, while the classical force-field 150mM KCl box reference gave min K-K = 4.46 Å. Approach-A benchmarked PySCF wb97m-v/tzvpd against COREOR with synthetic [K-OH₂-K]²⁺ angle scans and realistic bridged clusters; the local PES looked normal, with slope 0.92 and minima near ~4.5 Å, so local three-body overbinding was excluded. In the full system, MD forces were only 1/3~1/4 of the cluster-level repulsion, showing that COREOR was over-screening medium- to long-range K-K interactions and moving the effective PMF minimum from 4.5 Å to 2.9 Å.

The tzvpd-forceatomfilter path hides force degradation through cos(F_label, F_System-52341b2efc), and Pelshaw removes nearly all cation force supervision, with K 70%, Na 79%, and Fe 86% filtered out. The likely root cause is suspicious cation force labels that incorrectly teach backbone behavior. Among three attempted fixes, the only one that worked was forceatomfilter high-precision tzvpd data after the custom filter. In 3-shell K-K force checks, forceatomfilter remained flat and stable, while baseline and copyhead both showed progressive collapse. Standard three-stage full-system MD covered 124839 atoms and gave 3.1 ps trajectory-level confirmation, reaching min K-K = 3.22 Å without any <3.0 Å contacts. In SF, K124830-K124832 were coordinated by 4 carbonyls and fluctuated at 3.3-4.0 Å, consistent with KcsA biology.

The team also tested K-K behavior across water shells of several sizes. The 9.5 Å fourth-shell run showed that the 7.5 Å −0.05~−0.14 dip was caused by finite-shell effects, and R1-R7 all recovered at 9.5 Å; DFT@9.5 was approximately 2.87 and flat. Water still stays systematically overdense: svpsoft0608 showed P=−8283 bar, velmol25large showed P=−4130 bar, UMA showed P=−2284 bar, and equilib had ρ≈1.11-1.13 versus experimental 0.997. Overall, the System-52341b2efc family has a consistent water issue; velmol25large improves water pressure by only about 2× and does not fix Pelshaw, while UMA has healthy K-K behavior but remains overdense around 1.05～1.10. The K-K defect and water EoS defect appear independent, so the next direction is to test data combinations for diluted K-K ion repulsion and add more periodic water data for NPT optimization. The CorholmTR paper is fully completed, but scaling validations and experiments are still blocked by GPU and environment limits; a new mixed-precision scheme is ready for further optimization, although its demo is delayed by issue (1).

## Next Week Plan

- Tune model configuration and data mixing to address K-K repulsion decay.
- Gather more periodic water-box data to work on NPT density collapse.
- Try to complete the CorholmTR writing pass.