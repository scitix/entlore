---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:15:30+08:00"
authors:
  - "Caleb Norris"
department: "AI Compute Platform Dept"
---
## This Week's Work

The team finished the global kv cache POC for SGLang Sylflow × mooncake / umborantis, and moocake/umborantis delivered expected performance with real traffic, deepseek v2.5, and L3, with cache hits close to the theoretical ceiling. However, umborantis HA and elasticity were still below the launch bar, so the weekly project sync agreed that 6.15 nodes will go live on the mooncake path. For GLM5.1 pd separation, mooncake trace replay was 9pp under the limit; the Sylflow report is at https://x9ca14cda55.vexeum.ai/x35cc92195/xcfa13340e1.html, and the current tuning focus is adding dp16 card-level routing plus better Sylflow L3 read efficiency during cold start. The team also built a theoretical upper-bound method for kv cache hit rate, validated that the in-house mock tool is closer to the online stack than Alibaba slim’s CPU-only simulation, successfully ran Sylflow cross-rank sharing under tp 16 in test, and improved Sylflow L3 read/write efficiency, while pd separation still needs another round of Sylflow retest and tuning. For mooncake at ten-thousand-card scale, the HA assessment is available at https://x9ca14cda55.vexeum.ai/x35cc92195/x6d555a5a2d.html, and changes to the official approach cut etcd pressure on the ten-thousand-GPU cluster by 88-fold. On lororys fine-grained operations, the team reviewed the 0604 and 0611 issue batches, focused on abnormal GLM5.1 TTFT/TPOT p99 where internal TTFT p99 reached 52 seconds versus OpenRouter’s 5.6-38.5 second range, traced one contributor to the May 28 router upgrade and rolled Pelshaw back, found that long requests did not explain overseas GLM-5.1 TTFT/TPOT tails, and narrowed the pattern to scheduling queues plus prefill/decode compute interference; zai-org/GLM-5 was unavailable overseas, qelnet also had overseas outages across gpt-5.1 / gpt-5-mini / gpt-4.1 / gpt-5.2-codex, and alerting still needs to be strengthened.

## Next Week's Plan

Next week the team will run mooncake production operations drills. We will also continue improving mooncake monitoring and alert coverage. In parallel, we will work on kv cache hit-rate optimization for GLM5.1 + L3.

## Coordination and Help Needed