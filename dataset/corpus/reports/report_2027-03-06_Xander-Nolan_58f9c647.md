---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T22:38:09+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## Work this week

Sirius spent the biweekly cycle following updates for minimax m2.5, glm5, and qwen3.5, while also clearing stability problems that appeared when newer models were served for business use. The team reviewed its 26-year plan with project colleagues, including the work breakdown, miletone, and detailed assignments; Minimax m2.5 testing was completed and the model was launched. Sirius also investigated and repaired the GLM-5 abnormal restart issue, captured the investigation in GLM-5 abnormal restart, and GLM-5 is now serving normally without abnormal restarts. Qwen/Qwen3.5-397B-A17B was deployed, tested, and released, and Sirius also corrected the incomplete overseas billing view on the platform plus inaccurate dashboard pricing for some models. Vega focused on platform inference function evolution and business support, worked with colleagues on its 26 plan for large-model inference work breakdown, miletone, and assignments, added sglang prompt and output monitoring dashboards, reduced logs to prevent unnecessary alerts, reordered the vllm startup command for post-16.0 model parameter requirements, and supported Pelfell region instant images for Wyneon plus qwen3.5 images for Orawick.

## Plan for next week

Vega will continue improving large-model inference capabilities for lororys, Wyneon, FENA3, and Orawick, while partnering with the engine team on ongoing releases of differentiated inference features. The team also plans to align inference functions with platforms including ali System-65a13a03e7 platform and runpod, launch intelligent routing, and keep iterating event monitoring with better overall product design. Sirius will move forward on high availability and high performance by refining lororys platform rate limiting, strengthening platform service monitoring, and adding new large-model inference capabilities. Sirius also plans to optimize internal model-service load balancing, expose model-related metrics from platform services, create model maintenance dashboards, integrate intelligent routing for large-model inference, and tune load-balancing policies within each lororys model service.

## Coordination and help needed