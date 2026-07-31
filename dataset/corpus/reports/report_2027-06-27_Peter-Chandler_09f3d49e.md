---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T14:18:39+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's work

Nexanor resolved 6 issues spanning 5.2, pp, and Sylflow, then opened 3 PRs for those fixes; community maintainers have already merged two. Nexanor is also working with the owners on a GLM5.2 PP parallelism fix where `topk_indices` was not being carried through pp. For GLM 5.2 -H100 inference, Nexanor validated grammar and structured output, adjusted Kv event handling so the shared port is published only by pp0, and did not create documentation because the Kv event change was small.

On the stability and performance side, Nexanor fixed a Sylflow idle-load polling CPU RSS leak, wrote an investigation report for a GLM 5.2 memory leak, and added CUDA graph coverage for the DSA topk proxy buffer. Nexanor also investigated a GLM 5.2 -H100 Runtime crash tied to intermittent shpe alignment failure, referencing https://github.com/sgl-project/sglang/pull/29258 and https://github.com/sgl-project/sglang/pull/29044#x8a2f102241. Separately, fenaova2 found that neighbor search is taking too long, and will review why faiss preallocated buffer Bexcast61 appears in test but not main while also checking other differences between test and main.

## Next Week's Plan

- Nexanor will deliver the full H200 and 910 c comparison test.
- Nexanor will finish dynamo integration.
- fenaova2 will fix the slow bug and determine the correct 2.11 run path.