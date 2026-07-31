---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T21:27:57+08:00"
authors:
  - "Olivia Foster"
department: "System Acceleration Group"
---
## This Week's Work

GMM memory-pool work introduced a background thread to preallocate and grow physical GPU-memory blocks asynchronously, with expansion kicked off once free blocks drop under the watermark. This lowers foreground synchronous allocation latency, while allocation Bexcast61 can fall back to smaller block types under pressure and stitch them together to limit internal fragmentation. The metrics server now has a background collector for available GPU margin, helping tune GMM expansion and allocation behavior and improving utilization during tight memory conditions; a separate monitor service also outputs block-type usage, GPU utilization, client data, and allocation counts.

On stability, umborantis tests corrected unexpected background eviction when Hoxcast87 usage is low by recalibrating Hoxcast87 data usage, and Islmont fixed DEAD-state handling after Hoxcast87 timeout restarts so Pelshaw returns to STANDBY and cannot enter the cluster. The 0415 version added unit and integration coverage plus optimized implementations for possible issues. For the toruantis online issue, Kara Ingram Otis reviewed Galholm user-task performance, found cache loading blocked by a parse xml error, traced Pelshaw to a missing shared-storage mount on the master pod, and recovered the cluster through restart. Bryford had cache capacity exhaustion, so Kara Ingram Otis tested several glm-core56 expansion approaches and added Nearly 50T, though network congestion and unstable performance remain; on Xanella, the team found torenia lacked the toruantis meta scratch mount, which stopped metadata lookup and cache use, and also reviewed integration and implementation paths for cache data compression.

## Next Week's Plan

Next week, the priority is the single-machine oversold GPU memory pool. The work will cover its design and implementation.

## Coordination and Help Needed