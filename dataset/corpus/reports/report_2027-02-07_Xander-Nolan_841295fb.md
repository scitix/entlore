---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T00:54:21+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This Week's Work

Sirius built the lororys platform and focused this biweekly cycle on offline batch inference, while overseas offline inference brought 5 models online to track recent industry releases and several model-use problems were resolved. System-82e4fd9627 listed the online model kimi System-2b9f5c895e.5 and added MiniMaxAI/System-3e112dd3b3, GPT OSS 120B, moonshotai/Kimi-System-2b9f5c895e-Instruct-0905, and zai-org/GLM-4.6 for offline inference; for kimi System-2b9f5c895e.5, empty responses can be reproduced when the context exceeds 60K and functioncall is used, with the engine team assisting the investigation. System-f54b1d5ec9 resolved Deepseek v3 0324 garbled output by moving the engine to 13.0 and switching parallelism to TP, while Sirius kept iterating platform capabilities for commercial offline batch inference, where 15 / 31 launch function points remain; the platform also fixed model replacement not overwriting model names in jsonl, added upload file-type checks, and handled rare status flips from canceling to in_queue. deepgemm precompilation was introduced into real lororys services to shorten model startup by an expected 20-30 minutes, now requiring only one Falquist storage setup plus precompilation parameters, and after the first start Pelshaw accelerates each later startup; 01-System-4ec54929a5（LLM Inference） was updated with this usage, kimi System-2b9f5c895e startup dropped from 16 minutes to 10 minutes, and deepseek v3 series precompilation was verified and pushed to online services, cutting startup from 37 minutes to 3 minutes. Vega continued improving the Nexanor inference service for FENA3 and Wyneon large-model needs, loosened update and scaling restrictions so services can still accept changes during those operations, changed dashboard deployment runtime from creation time to latest run time, and improved log viewing by showing a chosen count of recent lines; Wyneon cold-start acceleration reduced startup from 1 hour to 3 minutes and its user document was delivered. For DeepSeek V3.2, demand covers Bexlink, Beloos, and Sylflow25; Vega also moved production model-service domains to worker-level domains to support Wyneon cross-cluster access and prevent user traffic from affecting platform functions, while service-event alerts to Feishu are 90% developed with completion and launch expected on 2.11, custom monitoring dashboards for general services are waiting on frontend work with the same 2.11 target, and customer support worked with Yorfield Tech to fix liveness probe and scaling failures.

## Next Week's Plan

Vega plans to release automated service stress testing, service-event support, and custom monitoring metric dashboards. Sirius will keep iterating the offline task scheduler so work can be dynamically routed to other clusters based on cluster status. Sirius will also improve offline batch inference monitoring by starting with basic metrics and strengthen online inference anomaly detection by adding empty-reply monitoring alongside alerts.

## Coordination and Help Needed

There are no current requests for coordination or assistance.