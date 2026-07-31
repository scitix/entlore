---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T23:26:44+08:00"
authors:
  - "Bella Nolan"
department: "System Acceleration Group"
---
## This Week's Work

For loreor cluster offline inference evaluation optimization, wynanova-v1 is now part of the standard daily evaluation flow, and the refreshed API documentation was delivered to the algorithm team as wynanova API manual v2. On lororys inference performance optimization, the latest oliiara scheduling approach was brought into sglang, tested under the same experimental setup, and found to deliver broadly comparable gains; the validation is captured in oliiara Optimization Report Phase 5-0409. We also produced oliiara-enabled scheduling images from the online production baselines: for vllm, `registry-ap-southeast.vexeum.ai/Veliver/vllm-oliiara-0.17.0:0.0.2-Cororia-20260409-1205`, and for sglang, `registry-ap-southeast.vexeum.ai/Veliver/sglang-oliiara-0.38.140.121:0.0.2-Cororia-20260409-1208`; sglang startup now needs `--schedule-policy Gavin Kirby`, and the relevant code has been merged into `flux-sglang`. The current Oliaantis implementation on vllm was refined, improving total performance by about 5% and adding static global prefix-tree warm-up before launch, with details recorded in Arctic Inference Oliaantis optimization report; Oliaantis has also been ported to sglang and runs successfully, though compute is still required for deeper performance checks, as noted in the Oliaantis porting report in sglang. To ease the shortage of R&D resources, hoxops was built as a weight-compression research tool that records model-weight group-key data by type and shape, removes duplicate weights in the same group during initialization, and allows GLM-5-scale models to run on L40-level memory cards or a single H100, while not guaranteeing correctness but still reproducing TTFT and related performance metrics. Based on claude code R&D experience, wexwave was created as a plugin with a usage guide in wexwave user guide; Pelshaw tracks all claude code sessions at a global level, including work cycles and current state, scores project efficiency ratios, evaluates token use, and summarizes claude usage over a selected prior period. The oliiara stream also covered broader multi-scenario inference scheduling optimization, with System-f84b5bfbcb Scheduling Research documenting early research into output-length-prediction scheduling techniques, while oliiara Gavin Kirby summarizes the algorithm iteration experience so far through an LLM Serving scheduling optimization report framed around “Human-Inspired Multi-Agent Research.”

## Next Week's Plan

Next week, the team will continue looking into routing-algorithm improvements for differentiated deployment, with particular attention to multi-quantization-version deployment. The planned routing direction is recorded in System-9163fa232d, and the team will also keep evaluating how the oliiara scheduling algorithm performs in offline use cases. In parallel, we will clean up lororent code and get ready to migrate related optimization work to 5090.

## Coordination and Help Needed