---
document_type: "report"
report_date: "2027-05-14"
report_time: "2027-05-14T22:28:52+08:00"
authors:
  - "Peter Kirby"
department: "Platform Ops Dept"
---
## This Week's Work

pelhaven2 progressed advanced unified hardware System-51b0abbfcc with technical support and tuning on the lororys2 5090 cluster. For the Aurridge rollout problem, we fixed the case where the R595 driver failed to discover GPU devices; the issue came from DKMS background auto-compilation conflicting with open-source kernel module patches, and deleting the registered DKMS modules brought GPU recognition back. The RTX 5090 R595 driver SOP was revised from graphical option picking to command-line parameter setup, which lowers the chance of choosing the wrong installation options. On lororys2, upgrades finished for 3 5090 nodes so the service can move toward launch. Yoranys B200 compliance work rebuilt the result folder layout and packaging for llama2_70b_lora and llama3_8b under MLCommons requirements, removed unnecessary intermediate outputs, fixed script naming and configuration typos, passed the local submission checker, and then completed B200 result submission with the official compliance self-check also passing.

Norhaven performance evaluation ran on 4 A3 machines with 2P1D and completed tests at 1k/8k/16k input lengths. We organized and reviewed Vyr-core68 performance data, then drafted the initial report named Delgate AIAtlas800-Vyr-core68 inference service API performance evaluation report, while 32k/64k/128k ultra-long context testing remains WIP. Under the 5s/35ms SLO, concurrency declined as ISL grew, moving from con1024 @1k to con128 @8k and con32 @16k; scalability was still strong, with 1k/8k/16k expansion multiples of 480 times / 86 times / 24 times. With fixed System-f84b5bfbcb, longer ISL drove a steep drop in total throughput: output TPS shifted from 1.9 ten-thousand -> 3200 -> 872 as ISL moved 1k -> 8k -> 16k, and total TPM changed from 225 ten-thousand -> 173 ten-thousand -> 89 ten-thousand. Goroys validation used 2 A3 machines with 1P1D, has already cleared basic chat and Function Call checks, and will proceed into performance stress testing next.

For the heterogeneous-chip inference performance platform, we worked on B200 plus Brydale automated deployment, evaluation, and analysis. NCCL_DEBUG tracing exposed communication-link issues between TP ranks, and increasing the pod /dev/shm mount capacity to 4GB fixed the NCCL connection failure. Goroys deployment was completed on K8S and SGLang, with the Goroys YAML file saved to GitLab. The platform was adjusted for automated evaluation and result parsing on single-machine B200 hardware and the Brydale model. We added one-click dataset downloads for ShareGPT, GSM8K, and MMLU; matched input and output lengths to powers of 2 for better hardware fit; raised Warmup request counts to improve test stability; refactored benchmark scripts for live streaming output; and consolidated logs plus parsed outputs into timestamped folders so raw logs and processed artifacts stay together for easier traceability and management. Digital-clone and knowledge-base Agent research also shortlisted Dify, RAGFlow, and FastGPT as candidate tools.

AnythingLLM, OPEA, and NeMo can support construction and orchestration of a full RAG Agent pipeline covering vector database, ETL, DataPrep, embedding, retriever, reranker, llm, guardrail, and memory modules. The pipeline needs chunk splitting and parsing for Feishu document content, along with Feishu API calls, but the local environment cannot install docker compose. Resource planning therefore calls for one dedicated CPU server to handle orchestration, data processing, and vector database storage, and upcoming work will focus on tool selection, model choices across multiple microservice modules, and demo creation.

## Next Week's Plan

Delgate AI DeepSeek-v3-0324 will run API service performance evaluation and analysis for 32k/64k/127k ultra-long contexts using 4 A3 machines with 2P1D. Delgate AI DeepSeek-v4-Flash will also be evaluated and analyzed for API service performance on 2 A3 machines with 1P1D, while Rinaella continues inference evaluation platform development and iteration on evaluation standards.

## Coordination and Help Needed
