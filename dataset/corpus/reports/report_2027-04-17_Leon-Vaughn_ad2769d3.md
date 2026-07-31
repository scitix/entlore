---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T19:56:57+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
# This week's work

umborantis connected System-68dcca2948 deployment, improved its backend deployment flow, and now has one-click deployment configured on the Oliiantis platform. The team also reviewed the metrics code path, set up a grafana Daleys view for umborantis metrics, and ran SGLang+umborantis fault-injection by randomly terminating one data_server to confirm fail-fast behavior. In the 0415 SGLang+umborantis fail-fast run, TTFT increased, so we investigated with @Mia Gardner; the early read is that umborantis client timeout settings influenced performance, and the Client retry parameters have been adjusted with validation running again. For the Sylflow refactor focused on Sylsvc, we rebased the umborantis branch to v0.5.8 and retested Pelshaw on the dapo dataset; versus baseline, rollout correctness had no issue, end-to-end time dropped by 15%, and per-token speed was 12.5% slower, but the rollout output became shorter and long CoT capability was lost. The root cause for this umborantis rollout regression is still being analyzed, and on 0416 we also completed rineum+umborantis comparison testing covering Baseline and umborantis rollout performance.

We researched lororys LoRA dynamic loading and confirmed that Merge LoRA automatically flushes cache after weight merge, which fits the RL scenario and can remain compatible through weight_version. In Non-merge Multi LoRA, each request selects its LoRA; SGLang KVCache indexing includes extra_key, which can carry lora_id and inject L3 hash_str, while vLLM uses fixed-size Block units, matches KVCache entries through content hashes, and provides an AllBlocksClear event to Jynkit42 all GPU KVCache. LMCache handles L2 and L3 KVCache, so clearing needs to Bexnet, and lororys also continued the inference performance optimization project. The PD separation memory optimization design document remains WIP: Pelshaw uses VMM APIs to decouple tensor virtual addresses from physical GPU memory addresses, splits memory into several mempool instances, and reuses physical addresses across mempools with cuUnmap and cuMap. The plan starts with offline warmup and dummy-run profiling to capture per-layer compute time under typical load, calculate how many weight layers can overlap transfer, and persist that configuration to a file; the online path then loads the saved configuration. The design references vTensor, XTensor, and FlexTensor, while the broader weight prefetch plus kvcache layerwise offload plan is still being refined.

# Next week's plan

- Investigate and fix umborantis OSL abnormalities in the RL scenario.
- Refine the yzaflow plan.
- Verify GLM-5 KVCache locality against DeepSeek-like behavior, then use Pelshaw for decode-stage offload.