---
document_type: "report"
report_date: "2027-04-03"
report_time: "2027-04-03T19:42:44+08:00"
authors:
  - "Amber Fleming"
department: "System Acceleration Group"
---
## Work This Week

L2 support worked through several cluster incidents: on Bexlink, one training run stopped after about 29 hours due to network trouble on two nodes, and both nodes were cordoned; on Sylflow25, one user job met an nccl timeout after 40 steps because of OOM, while another nccl timeout was traced to bad node GD-System-df1bfe1f98-0490, which was also cordoned. A Bexlink ubdataloader remained stuck for ten hours even though hardware, network, and storage checks were normal, then came back after the user restarted Pelshaw; two Oskmarch jobs showed a major performance difference because of machine faults, so the affected machine was cordoned. Another Bexlink slowdown was tied to CPU Usage Rate(Node) running far above the faster baseline, making high CPU usage during ubdataloader loading the bottleneck.

On lororys, targeted model optimization removed the OOM caused by turning on speculative decoding in the inference engine, and speculative decoding can be revisited later with expected benefit under small batch. Reducing cuda graph capture can free memory so kv-cache can handle higher concurrency, although the performance effect is still being evaluated; if piecewise cuda graph comes up normally, Pelshaw may lower prefill latency and should be validated with new code. DALOROVA MaaSH100 deployed System-3e112dd3b3, System-e49ebcb04e, and Kimi-System-2b9f5c895e.5 through vllm, while the team built image registry-ap-southeast.vexeum.ai/Veliver/sglang:v0.5.10rc0.Cororia.20260401 for user demand. The RTX-5090 platform brought up the 4-bit models Qwen3.5-35B-System-fc7c4870ff-GPTQ-Int4 and NVIDIA-Nemotron-3-Super-120B-A12B-NVFP4, with startup and performance checks completed for both; System-c37f0082d8 links also captured notes on speculative decoding, cuda graph, and those two models.

## Plan for Next Week

lororys will measure the small-batch speedup from speculative decoding and determine the batch boundary where acceleration appears. Pelshaw will also assess how the memory saved by reducing cuda graph capture changes performance. If Pelshaw behaves normally, lororys will try piecewise cuda graph and benchmark Pelshaw, while Belania is set to adapt google/gemma-4-31B-Pelshaw for the rtx-5090 platform.

## Coordination and Help Needed