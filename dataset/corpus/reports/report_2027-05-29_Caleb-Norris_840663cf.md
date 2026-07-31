---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T18:47:57+08:00"
authors:
  - "Caleb Norris"
department: "AI Compute Platform Dept"
---
## This Week's Work

System-1a4ead4435 covered platform operations and customer support refinements, with the main issue being GLM5.1 latency swings where p99 TTFT ranged from 29～286s. System-2f5ebfd404, System-169893da9f, and System-a206a95936 helped overseas customers move from closed-source models to open-source options, while the team compared GLM-5.1, DeepSeek-V4, Qwen3.6, Kimi-System-2b9f5c895e.5, and MiniMax-M2.7 using 25 anonymized customer records; GLM-5.1 fast reached an 88% win rate versus Haiku 4.5. For the new GLM-5.1 distributor deployment, quality checks and stress tests were completed, capacity passed the 5K + 10K RPM × 60s burst tests, and output quality stayed near the internal deployment level, though hallucination rate was +2.1pp higher on the customer dataset. Evaluation practice showed LLM judge bias from position effects and single-run noise: Opus 4.7 preferred the B side at ~2:1, so each pair needs randomized A/B order, and 44% of samples changed across 5 passes, with 1-pass eval inflating effect size by 30-55% compared with the 5-pass mean. The team also investigated customer 120s request timeouts and confirmed three drivers: thinking was still enabled and pushed generation time to ~10×, server-side GPU queuing and imbalanced load added delay, and client plus network time consumed 76s within 120s; the recommendation for the first two was to disable thinking and raise timeout to 500s, while the third remains under discussion with the customer. System-265bd33f32 logged a customer observation that GLM5.1 reports itself as GLM4, which was reviewed with @Xander Nolan and @Mason Archer; System-91e0c9d941 captured official-site comparisons and prompt-engineering probes around training-data cutoff dates, and the team finished the first KV cache and umborantis survey, completed the distributed KV Cache architecture survey, cleaned and anonymized 4 days of lororys2 online model request logs for evaluation data, and set up the MoonCake and umborantis evaluation environment to 30% progress.

## Next Week's Plan

Next week, the team plans to finish full evaluations of multiple kv cache options. That work will include improvement requirements, POC, and launch planning. The team will also continue reviewing platform operations metrics and shape a long-term, systematic follow-up plan.

## Coordination and Help Needed