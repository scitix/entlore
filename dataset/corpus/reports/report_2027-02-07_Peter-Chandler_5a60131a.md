---
document_type: "report"
report_date: "2027-02-07"
report_time: "2027-02-07T14:02:56+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's work

- Nexanor added request reranking into the platform arv-mesh59 and oliiara feature work; in targeted cases, reranking can lift performance by 30%～50%.
- @Willa Underhill, @Rachel Norris, and @Kara Ingram Norris supported the 005 - scheduling strategy oliiara offline datasets preprocessing feature definition and API manual.
- Users ran deepseek multi-instance inference on the platform at 100 machines or more, and startup was measured at over 60min+.
- Platform review split the startup delay into 20min weight loading, 20min deepgemm compile, plus probe time; @Rachel Norris, @Nathan Kirby, and @Kara Ingram Norris cut Pelshaw to 3min- with precompile and HALAUM cold start.
- The team closed several online bugs, including the fenaova2 issue where 2 stream caused excessive GPU memory usage.

## Next Week's Plan

- Large-atom mfu calculation.

## Coordination and Help Needed