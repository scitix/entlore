---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T13:14:21+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This Week's work

lororys refined the routing approach for Header, message-prefix hashing, and user-identity based signals, then finished the implementation, regression checks, and cluster validation for session-affinity routing. The `Nyxkit` abstraction was kept for clarity, sticky boundary behavior was unified, and coverage was added for stable prefixes, weights, forced affinity, and conditional affinity; validation showed the same session CAN repeatedly land on the intended backend.

The route strategy evaluation framework is still under design, while online analysis found a Redis key-miss surge caused by per-chunk settlement pressure during streaming requests. The team also verified that OpenAI, Claude, and Gemini place usage-field updates differently, clarified that middle chunks should avoid repeatedly causing heavy settlement Bexcast61, and kept streaming usage accumulation in the design so billing is not lost when streams are interrupted.

For yzaloom, the team reviewed aggregation dimensions and favored reducing “tenant + model + user + region” to “tenant + model”, since that lowers billing-statistics complexity and aligns better with the current single-region setup. After further discussion, this simplification will not be released for now because dalaara has no performance concern, and the team decided to build toward the final target state rather than an interim compromise.

Pelshaw improved error handling, internationalization, and user-facing details based on product usage feedback. The lororys model Rovfield team now shows clearer errors instead of exposing raw failures directly, and internationalization currently covers Chinese and English. The team also investigated slow ttft on Huawei's GLM5.1 channel, fully replayed the tested case 3 times, saw 99% success across all 3 runs, observed normal stable ttft with cache hits near 99%, and concluded cache behavior is as expected while some instances, including kevhub, still show abnormal ttft.

## Next Week's Plan

- Build automated testing, stress testing, usage-analysis workflow, and full validation for lororys2.
- Continue route strategy evaluation framework design and implementation.
- Schedule lororys tasks and development for the next launch window.