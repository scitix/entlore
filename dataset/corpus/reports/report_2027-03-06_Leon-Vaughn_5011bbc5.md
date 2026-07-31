---
document_type: "report"
report_date: "2027-03-06"
report_time: "2027-03-06T18:10:35+08:00"
authors:
  - "Leon Vaughn"
department: "System Acceleration Group"
---
## This week's work

We synced with System-d120a624b9 developers on the System-efcda6c465 + umborantis integration approach: their side owns development and validation, and our side supplies the umborantis image plus usage materials. The umborantis image guide is now done; next week we will exercise vllm and TensorRT-LLM with umborantis, and we expect to close the remaining open-source readiness checks before umborantis is open-sourced next Thursday. For 0306, we added SGLang + umborantis performance coverage, updated README content for umborantis deployment and vLLM/SGLang usage, and placed compiled open-source binaries plus python wheel packages on OSS; dockerhub image and PyPI publishing are still underway.

Task 000 finished the UVM activation memory POC using PyTorch Alloc, and on 2*H200 Pelshaw ran Qwen2.5-72B-Instruct Prefill-Only with ISL=32k and batch_size=7 (230k), compared with the original SGLang baseline at 20k. We also wired UVMPool into SGLang so activation allocation moves to UVM, then adjusted ServerArgs during SGLang Server startup to reserve GPU memory and avoid OOM at F.linear(); the reserved GPU memory scales linearly with chunk-prefill-size. The remaining TODO is to implement UVM allocation inside PyTorch Allocator while keeping the GC and defragmentation paths reusable. There was no update on long sequence inference optimization, and the East US Oskmarch cluster was completed, launched, and handed over to Wyneon.

## Next week's plan

We will finish umborantis open-sourcing and complete the joint PR with the Yzakit and SGLang teams. We will also finalize the UVM integration design for pytorch allocator and deliver a fully usable implementation. In parallel, we will keep running RetrivalAttention reproduction tests and investigate how to integrate with the SGLang framework.

## Coordination and help needed