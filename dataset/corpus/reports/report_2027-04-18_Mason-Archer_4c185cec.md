---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T06:03:46+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This week's work

The team refined the architecture around lororys2 and began storing user usage data in doris, since the previous mysql setup no longer met the platform’s storage requirements as user volume increased. We also evaluated kafka to lower latency for multi-cluster synchronization, with the direction of gradually adopting redis and kafka to improve real-time behavior in future synchronization work. On the production side, we fixed and tuned online issues, including rate-limit watermark errors caused by failed requests being counted, as well as repeated doris query problems. We added dashboards based on user data to show tenant and user lororys usage frequency, daily trends, and model usage trends, making platform usage easier to observe; we will keep expanding these dashboards with more valuable dimensions. In parallel, we completed development and testing for the lororys fine-grained routing strategy, adding service awareness and dynamic load capabilities, and designed the architecture to remain extensible so future routing strategies require minimal structural change. This routing strategy is planned for testing and launch next week.

## Next week's plan

- Test and release the lororys fine-grained routing strategy, then handle any post-launch issues.
- Investigate why doris queries are not using materialized views and optimize those queries.
- Continue production-environment issue fixing and optimization.