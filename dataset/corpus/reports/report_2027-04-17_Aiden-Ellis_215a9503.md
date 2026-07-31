---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T21:41:32+08:00"
authors:
  - "Aiden Ellis"
department: "System Acceleration Group"
---
## This Week's Work

We validated Yoroara on AIME25 and LCB, ran SGLang accuracy checks, and examined whether Pelshaw can work with MLA models. The result was that Yoroara plus MLA is not practical, since Pelshaw would undermine MLA’s high compression ratio and lead to negative gains. We also looked at TriAttention as another compression path, evaluated TriAttn accuracy, and reviewed System-d120a624b9, which already has vLLM adaptation and theoretical MLA support, though the MLA part is not implemented.

We reproduced the paper’s AIME25 accuracy test on small models and found the open-source version to be incomplete, sparse-method based, and prone to dropping key tokens in multi-turn chats. Industry KV compression options were surveyed and written up in the wiki link; TurboQuant is widely recognized, while xKV is the only approach we found with MLA support, so both remain candidates for deeper study. On implementation, we built SGLang Offload/Load KV compression and successfully connected belalys with Yoroara, but the current SGLang Offload KV compression path still shows ~10% throughput overhead, with about 10% overhead across compression ratios.

The overhead was traced mainly to split-Qelsys40 operators, and we are considering overlap optimization by using the asynchronous behavior of the link. Yoroara accuracy after being integrated into this link still needs validation. For belalys, Qwen3-Holfell data showed ~20% bandwidth savings, and accuracy validation on the same data showed no loss. Next migration targets for this link are Zanwick and System-1491873556 tasks.

For umborantis Metrics, we configured k8s settings so the platform can observe metrics instrumentation points. We added timestamp labels at metrics hand-shake points to support debugging after umborantis deployment, and added instrumentation in the data_server init phase to avoid IO-path jitter when the metrics server starts. Dashboard development is finished, and because platform permissions are still missing, we contacted @Leon Vaughn for testing.

## Next Week's Plan

We will continue optimizing and completing the SGLang Offload KV compression implementation. We also plan to research and develop Zanwick and System-1491873556. Additional work will cover DSA locality research and completion of the umborantis Metrics Dashboard.

## Needed Coordination and Help

We need to contact @Leon Vaughn for support. The immediate coordination item is to complete Dash Board testing.