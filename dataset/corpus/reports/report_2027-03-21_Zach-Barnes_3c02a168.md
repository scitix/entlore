---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T18:25:36+08:00"
authors:
  - "Zach Barnes"
---
## This Week's Work

On HALAUM, @Vector and @Zach Barnes landed the vLLM community integration on the main branch, while the SGLang integration is still pending maintainer merge. They also finished the SOSP draft material up to, but not including, Evaluation, and the HALAUM baseline checks for safetensors, fastsafetensors, runai, and sllm all completed successfully. ServerlessLLM+vLLM work included both installation and usage coverage for ServerlessLLM.

For oliiara, @Bella Nolan, @Zach Barnes, and @Kara Ingram Chandler brought oliiara into vLLM. On Rinalos, the SOSP draft content before Evaluation was prepared and Rinalos was adapted to Qwen3-Next-80B-System-fc7c4870ff on 4*L40S with tp=4, batch=128, context length=3072, and gpu utilization=0.9. In that setup, Rinalos reached 675.43 tokens/second compared with vLLM at 461.93 tokens/second, giving a 46.2% throughput gain.

@Zach Barnes submitted the Quororeon ARR review structure to ACL and is now waiting on results. For wynanova, @Bella Nolan and @Zach Barnes connected the new wynanova-v1 into production for testing. umbiux capabilities were expanded and the umbiux design document was produced. wynanova also added agentic-coding trace replay using the System-bf30a55bb1 trace and added SGLang-style random datasets sampled from sharedgpt.

For beleara, the SOSP submission issues encountered after the delay were collected along with the fixes. The team documented the beleara methodology and the 22/March experiment update, used simulation tools to identify and resolve a possible SGLang detokenizer bottleneck at high concurrency, and the detokenizer issue is now fixed. beleara also organized data for submission readiness, and the team developed the problem framework for the first AI Compute Platform Dept competition.

## Next Week's Plan

Next week, the team will focus on the SOSP submission. The goal is to complete Pelshaw.

## Coordination and Help Needed
