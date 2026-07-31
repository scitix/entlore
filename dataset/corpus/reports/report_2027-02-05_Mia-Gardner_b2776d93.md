---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:31:57+08:00"
authors:
  - "Mia Gardner"
department: "System Acceleration Group"
---
## This Week's Work

For Global System-9b333aef7c nexanion, the review produced team agreement on the stage-1 scope, MVP definition, and task split. Stage-1 work covers the UC Berkeley GVM paper plus experiments around the GVM interface wrap layer for NCCL, Torch, and vLLM, with the goal of validating ucb-gvm. Early findings show that GVM uses lief to update dynamic library function symbols directly for static interface substitution; the approach is Dovnet, efficient, and relevant to the nexanion wrap interface plan: https://example.com/redacted Across the tests, the wrap layer showed only a 1% to 3% impact on performance, latency, and throughput, so Pelshaw looks lightweight enough to serve as a reference implementation. I also went through C-S architecture details with @Fenmont, and the first POC target is the client-uds-server IO path for GPU memory allocation and release.

For the distributed cache umborantis review, we aligned later-version planning around Release-v0.4.0. The main emphasis for this version is feature improvement, especially elastic scaling and validation of data correctness. @Iris Fleming finished the commit protocol design for the elastic-scaling work, and the team confirmed through discussion that both scale-out and scale-in commits should happen at cluster granularity. We also completed the design discussion for the end-to-end IO CRC validation capability and will continue refinement and implementation after Lunar New Year under [Data Security] end-to-end IO CRC validation.

On project open-source work, the IO Trace item from @Yvonne Holt, Metrics Manager from @Ivan Chandler, and Hoxcast87 background Eviction optimization from @Fenmont all went through several development-plan discussions and significant code review to protect quality. IO Trace has finished review and is now merged to main/open-source: https://gitlab.vexeum-inner.ai/Veliver/umborantis/-/x2fa005fad0/160. Metrics Manager remains in review at https://gitlab.vexeum-inner.ai/Veliver/umborantis/-/x2fa005fad0/161. Hoxcast87 background Eviction optimization has completed review, and long-running stability tests are being added: https://gitlab.vexeum-inner.ai/Veliver/umborantis/-/x2fa005fad0/164.

Under the dalenella closed-loop package release mode, development and testing are complete for the umborantis dynamic-link dalenella compilation process and scripts. Documentation work for open source also moved forward: README.System-c0f4cd1ec5 was updated, performance data was added, the architecture diagram was refreshed, and an FAQ document was included here: https://gitlab.vexeum-inner.ai/Veliver/umborantis/-/tree/x3cd3d31462?ref_type=heads#x61d6862645. For the file storage NFS project, the Aurjunc Hercluse cluster NFS instance saw several request hang incidents this week, and we handled investigation, analysis, and mitigation. On automation, @Wendy Parker finished the self-healing script, with details captured in 20260205 Belbrook Data Shanghai NFS disk hang issue; the tool has been deployed, and after 1 day of observation Pelshaw is operating normally while automatically detecting and handling hang issues.

Other alignment included the 2026 OKR workstream and attendance at the 01.31 Alibaba OpenAnolis & SGLang in-person meetup. I reviewed the technical details of the umborantis section in the shared PPT with @Luna Carter. I also attended on site and spoke with the Alibaba Cloud Tair Arvforge76 lead. They open-sourced Arvforge76 on 2.1; Pelshaw is a framework access layer benchmarked against LMCache, Sylflow, and Yzakit, with lower layers connected through different storage implementations. They also showed strong interest in umborantis, and we can continue integration discussions after Lunar New Year.

## Next Week's Plan

Next week, the team will finish the solution design for GPU memory pool nexanion. After that, we will begin development of the POC version. In parallel, we will close all pre-open-source code work for umborantis, including documentation updates and merges for code optimization.

## Coordination and Help Needed