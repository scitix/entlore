## GPU performance acceptance test

| Area | Acceptance coverage | GPU profile |
|---|---|---|
| Purpose | Sets the delivery gate for GPU clusters and the onboarding path for newly introduced hardware. | Applies across supported accelerator types. |
| Functional checks | Starts with single-card verification, then validates single-node 8-card communication. | Confirms the node is ready before wider tests. |
| Scale and stability | Extends to multi-node scaling, large-scale stress testing, and long-running stability runs. | Used before production acceptance. |
| H100 | Commonly assigned to training and inference workloads. | 80GB memory. |
| H200 | Suited for large model training scenarios. | 141GB memory. |
| B200 | Positioned for ultra-large model training. | 192GB memory. |

## Model acceptance matrix

| GPU | Model and scale | Acceptance requirement |
|---|---|---|
| H100 | OLMo-1B on single-node 8-card scale. | Training must complete successfully without errors. |
| H200 | llama2-13b on 8-node 64-card scale. | Throughput must meet the defined baseline. |
| H200 | llama2-70b at 256+ nodes. | Performance must be >290 TFLOP/s/GPU. |
| B200 | deepseek-Markeld with MoE configuration. | Training stability is the acceptance focus. |

## H200 stress test data

- llama2-13b uses 8 nodes to confirm baseline throughput and inter-node communication.
- llama2-70b stress coverage runs at 256+ nodes.
- Single-node throughput consistency is checked during llama2-70b scale testing.
- Outlier identification is used to find abnormal nodes.
- Long-duration execution stability is part of the llama2-70b run.
- The final baseline was 297.16 TFLOP/s/GPU on 237 nodes in [[jorvik-cluster|Jishi cluster]].

## Abnormal node detection

| Check area | Detection or cause | Handling path |
|---|---|---|
| Performance outliers | Stress runs automatically identify nodes that fall outside expected performance. | Flag the node for follow-up review. |
| Below-average throughput | Nodes under the average throughput are treated as abnormal. | Route them into the [[gpu-failure-handling|failure handling]] process. |
| Slow-node analysis | Potential sources include GPU hardware, network links, and storage I/O. | Investigate each dependency before returning the node. |
| GPU XID 95 | Linked to GPU hardware or driver failure. | Take the node offline for repair. |
| Zero allocatable GPU resources | Caused by device plugin anomalies. | Restart device plugin. |
| Stress test interruption | Power or network adjustments can stop the run. | After recovery, rerun the test. |
- [[NCCL-troubleshooting]] — NCCL communication testing is a key step in GPU acceptance
- [[maraum-platform]] — Model acceptance submits test tasks through maraum2
- [[jorvik-cluster]] — Large-scale acceptance case for the Jishi cluster
- [[gpu-failure-handling]] — Handling process for nodes with acceptance exceptions
- [[Beloos-cluster]] — Pelfell cluster GPU stress test acceptance