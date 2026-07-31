---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T20:57:44+08:00"
authors:
  - "Xander Nolan"
department: "AI Compute Platform Dept"
---
## This Week's Work

Sirius advanced platform support for speech models, including quarkco tts work where the startup command was traced from the image history, Pelshaw was adjusted, and startup validation was completed. Test outcomes were refreshed under TTS /ASR voice model tests, quarkco chat completion model API compatibility was updated to System-b9e258df98, and audio-model billing research led to platform billing being enabled for TTS and ASR models. System-14c21a08e4 and System-9a2ab69d97 finished migration load testing on 5090, while the 5090 health-check timeout still needs tuning to avoid abnormal restarts caused by timeout behavior.

For deepseek v3, Sirius raised max running request and turned on ep, which met the latency needs raised by users. Qwen3.6-27B was tested and released for internal use, Qwen3-VL-235B capacity was expanded, and the team investigated glm5.1 truncation reports. The returned reasoning content in those requests hit the 202k context ceiling, and some calls exceeded the client-side 60s setting and timed out.

Sirius also worked on separate cache-hit billing by testing open-source model cache settings and updating inference-service cache parameters together with @Kara Ingram Chandler and @Iris Otis. The Daisy Adler inference service moved to US West; for GLM5 System-05ceccff7f access, Sirius created the Daisy Adlerapi gateway and completed platform integration with @Aiden Jarvis. Sirius also set up the System-7447ff916f link with @Rachel Jarvis, load-tested the platform service for bge-3 embedding concerns and responded with a throughput report, and tested and launched Qwen3-embedding-Yorombe for internal demand.

Vega’s biweekly focus was platform inference iteration and support for business requests. The team released inference interaction improvements and bug fixes, shipped elastic scaling optimization, and updated intelligent routing parameters. Vega also connected the new flux intelligent routing path.

## Next Week's Plan

Vega will continue iterating large-model inference capabilities for lororys, Wyneon, FENA3, and Orawick. The team will work with the engine team to deliver differentiated features aligned with the ali System-65a13a03e7 platform and runpod inference capabilities. Vega will also improve platform monitoring and tune inference monitoring configuration.

Sirius will keep pushing high-availability and high-performance work. The team will further improve lororys platform rate limiting and platform service monitoring, integrate new large-model inference capabilities, and optimize internal load balancing for model services. Sirius will also add support for Rerank models.

## Coordination and Help Needed

No coordination is required right now. No help requests are currently open.