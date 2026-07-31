---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T20:04:07+08:00"
authors:
  - "Clara Underhill"
department: "System Acceleration Group"
---
## This week's work

This week, we worked with cluster colleagues to bring up a Docker-in-Docker setup on SOLAOS for SWE-Agent evaluation. We also continued assessing SGLang+Kimi-System-2b9f5c895e.5+umborantis in Agentic use cases, helped @Mia Gardner and @Leon Vaughn rerun umborantis open-source evaluations and organize the resulting data, and prepared umborantis for open-source release.

We investigated an issue in the Sylflow L3 storage backend that appeared during L2 evict. The problem removed Radix tree node indexes, which left KV stored in L3 umborantis inaccessible, and we have already implemented a patch for Pelshaw.

## Next week's plan

- Continue supporting umborantis data testing with vLLM and SGLang across Agentic and multi-turn dialogue scenarios.
- Investigate why Qwen3-235B lacks chain-of-thought after FP8 KV quantization, with a focus on the suspected low logit for the first token <think>.
- Run experiments for the Qwen3-235B FP8 KV quantization hypothesis, then review feasible KV compression methods and summarize their trade-offs.