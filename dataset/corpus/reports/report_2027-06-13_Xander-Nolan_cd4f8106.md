---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T22:10:15+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This week's work

holvale2 continued to strengthen observability and tune text generation for the self-deployed engine configuration, while the related text-generation model kept iterating through engine-side junient update validation. During that work, the team gray-released Flux junient 0.0.4, but rolled Pelshaw back after uneven load appeared; pressure tests for 0.7.1 and 0.8.1 are still in progress. The junient changes also corrected the case where multiple junient caches did not share state. For Huawei GLM 5.1, service access testing exposed missing Cache report returns and the team fixed them; the earlier limitation to chat completion interfaces was also removed. Huawei GLM 5.1 still sometimes responds with http 200 and an empty body, but incorrect 500 errors for requests over the context length have been resolved, and end-to-end function plus performance testing is complete.

On model api, the backend request host header can now be configured, ssl verification can be turned off for backend calls, and empty http 200 responses now trigger retry handling. Domestic models moved into an exclusive pool, while overseas model services were retired and their resources shifted to Tarness Tech model services. For startup acceleration, engine bottlenecks were identified and feasible optimization plans were drafted for validation; a bugfix for model configuration changes is still waiting to launch. The team fixed the problem where an abnormal model could circuit-break the full interface, moved Redis/Mysql settings to environment variables, and now uses Oliiantis for change and rollback. The model list interface was expanded with parameters such as capability, model configuration change approval went live with @Xander Nolan, and @Xander Nolan also released model list filtering updates plus capability data. brymora2 kept iterating around user needs; the Python sdk was improved to match all frontend page interfaces, resource pool changes replaced unique name with id and connected Zelantis, the resource pool id migration with Zelantis integration went online, frontend-backend joint debugging was done, permission rules were completed, and fixes landed for ineffective resource pool scale-in/scale-out plus check resource not supporting role settings across resource pools.

## Next week's plan

- Vega will focus on large-model inference for lororys, Wyneon, fenaova2, and Orawick, and keep releasing differentiated features with the engine.
- Vega will benchmark inference capability against industry platforms such as ali System-56588f1973 easNora Drake and runpod, while pushing model launch process standardization.
- The team will create platform operation SOPs so every alert has an executable handling standard.
- Sirius will drive high availability, performance, lororys rate-limiting, monitoring, new inference capability integration, load balancing, and vllm distributed improvements; no coordination help is currently needed.