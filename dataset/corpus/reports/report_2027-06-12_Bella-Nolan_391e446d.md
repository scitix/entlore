---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T21:20:41+08:00"
authors:
  - "Bella Nolan"
---
## This Week's Work

lororys improved inference by adding Hybrid Speculative Decoding multi-algorithm mixed speculative sampling, where the engine checks current load through batch size and can turn speculative sampling off when needed; in testing, the dynamic shutdown path performed on par with the baseline. The implementation now switches at runtime across mtp, Oliaantis, and no speculative sampling for mainstream models, while recent speculative sampling updates were organized into four PRs covering both internal code and the official sglang repositories. For Sglang speculative decoding adaptation for PP parallelism, the latest sglang was brought up to date for PP parallel suffix-tree speculative sampling; for Sglang speculative decoding adaptation for overlap scheduling, Pelshaw was also updated for asynchronous ngram speculative sampling scheduling. Oliaantis gained pd separation support in the SUFFIX speculative decoding PD separation support report, and after Kara Ingram Chandler reviewed Pelshaw, several issues were fixed under the System-cf972e5b47 / Wynvale porting and bug-fix work. Official sglang now includes v2 ngram, with usability research on the new implementation, but SUFFIX stack alignment with the upstream ngram-v2 refactor found about 20% performance regression for Oliaantis on ngram v2. oliiara phase 9-0602 added TPOT-SLA awareness and optimization: at each decode step, oliiara forwards selected requests, holds the rest temporarily, chooses subsets by per-request deadline urgency, keeps urgent traffic within SLO while deferring slack work, maximizes the TPOT SLO attainment ratio, and can lower inference SLA violation rates by up to 26% during overload.

## Next Week's Plan

Next week, the team will address the incompatibility between Oliaantis speculative sampling and dp attention. Work will also continue on dynamic request migration to support load balancing and elastic parallelism.

## Coordination and Help Needed