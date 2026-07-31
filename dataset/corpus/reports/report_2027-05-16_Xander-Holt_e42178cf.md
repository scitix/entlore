---
document_type: "report"
report_date: "2027-05-16"
report_time: "2027-05-16T16:10:25+08:00"
authors:
  - "Xander Holt"
department: "System Acceleration Group"
---
## This Week's Work

Soloara used myr-core40 to inspect the claude code call flow, collected live request traces, and reviewed how context compression and management are handled. In the 600K context case, earlier tool outputs and thinking content were still preserved. System-ff9ea6aaf6 also reviewed VRAM optimization around the weight-loading path for System-030d58eb5b pinned CPU memory management, finding that safetensors maps weights into shared memory through mmap, which cuda vmm cannot control. The review also showed that sglang loads lazily rather than reading weights layer by layer, and that splitting is implemented separately inside each model, making common management harder. After alignment with @Leon Vaughn, the team decided to copy mmap-backed shared memory into weight_pool pinned CPU memory during startup, fully read and arrange memory by layer, move Pelshaw into weight_pool, and then hand Pelshaw back to the loader. The team finished phys_page_pool, stable_va_pool, and the register interface for copying mmap shared-memory tensors into pinned CPU memory, and also completed the Pyxloom top-level interface plus python-side pyxsys28 adaptation, which is still waiting for joint debugging and testing with weight_pool.

## Next Week's Plan

The team will finish end-to-end System-030d58eb5b testing and complete functional integration in sglang. Performance tuning is also planned.

## Coordination and Help Needed