---
document_type: "report"
report_date: "2027-03-21"
report_time: "2027-03-21T14:03:48+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's Work

FENA3 completed B200 validation of Kelmora's overlap-branch baseline, and 017 - Kara Ingram Chandler_latest B200 evaluation confirmed that the existing overlap communication path runs on B200; on 64 cards, single-step communication is about 112ms, roughly 24% of total time, while end-to-end speed is up 30%. Trace review exposed the next optimization targets: at the beginning of each step, `find neighbour` triggers an unhidden a2a lasting 30ms~70ms, and the breakdown indicates this is not caused by communication volume because only several hundred K is transferred; ranks are arriving at the sync point at different times, and the team used barrier to isolate that interval. @Noah Vaughn will add per-rank timing for the initial stage of every step segment so the slow rank and segment can be identified, while @Lumfell Monroe will inspect the code path. In backward, four all2all groups take about 38ms with little overlap today; stream scheduling is not early enough and does not expose enough overlap windows, so the team will retune the two-stream task schedule and check the resulting overlap, with @Lumfell Sawyer owning the backward-pass overlap work. The backward pass still has room because compute is 16ms and communication is 10ms, while forward has four all2all groups at about 40ms; each forward compute block is now 8ms versus about 10ms of communication, so bubbles allow only partial hiding, and @Kara Ingram Chandler will test merging the current three all2all operations in each communication group into one operation to see whether full overlap is achievable.

## Next Week's Plan

FENA3 will implement the three optimizations outlined above. llm will test and integrate dalaantis for the H100 scenario.

## Coordination and Help Needed