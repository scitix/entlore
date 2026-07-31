---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T12:24:19+08:00"
authors:
  - "Mason Archer"
department: "AI Compute Platform Dept"
---
## This Week's work

lororys finished rolling out its fine-grained routing approach. This week’s local validation and deployment included weight-first, latency-first, session persistence, load-first, and fallback scenarios, and the multi-backend model routing setup and tests behaved normally after release. The team will keep watching for further optimization opportunities and method-level issues in routing strategy work.

doris query performance was improved by adjusting query statements and using materialized views. Commonly accessed data will move to a three-level cache pattern across memory, redis, and db according to access frequency, and later functions will follow the same memory/redis/db approach. The team also resolved several issues, including abnormal exposure of service information to users.

For platform readiness, redis global prefix/ttl configuration was added to support future redis cluster migration. External links such as db/mq are now handled through connection pools to avoid excessive lb-level connection pressure. Deprecated Bexcast61 was removed from the lororys code project so Pelshaw stays cleaner for ongoing iteration.

## Next Week's Plan

- Migrate redis cluster, continue project optimization, and keep fixing issues.
- Add user-tier routing so high-priority users get better sla, request priority, and the best resources.
- Integrate vllm/sglang internal priority queuing under high concurrency with lororysNora Drake platform.
- Implement tiered billing for different context lengths.
- Add lororys Nora Drake platform metrics to improve service observability.
- Support internationalized error messages and improve selected ui experience issues.