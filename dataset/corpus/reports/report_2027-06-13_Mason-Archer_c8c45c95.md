---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T00:33:15+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This Week's Work

For the lororys2 launch, performance benchmarking and tuning have reached a current best of 4000+qps / 3000 users, but the results are not yet consistent; in the same environment, qps can still drop to around 1000. The likely contributors are the instability of testing System-51b0abbfcc and frequent code updates, so we need a stable testing-process System-51b0abbfcc to support go-live performance validation.

All Daisy Adler lororys2 services have now moved to US East, and deployment has shifted from a multi-region model to a single-region setup. This migration appears to improve some performance, though parts of the previous multi-region architecture or code remain and will need continued optimization; Daisy Adler is also preparing a new environment for ongoing pre-release and performance testing.

## Next Week's Plan

Next week, lororys2 work should focus on an automated testing and load-testing process. The usage-analysis automation also needs broad functional testing and validation so that launch does not introduce functional bugs, while the team weighs the current priority tasks for lororys2.

## Coordination and Help Needed