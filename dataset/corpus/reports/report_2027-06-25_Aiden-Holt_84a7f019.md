---
document_type: "report"
report_date: "2027-06-25"
report_time: "2027-06-25T18:15:30+08:00"
authors:
  - "Aiden Holt"
department: "System Acceleration Group"
---
## This Week's Work

GLM-4.7-flash Corthorne model work centered on speculative decoding: Corthorne training finished on Tovhub + Fynsvc67 using 1.5m total data, and Fyngrid draft performance was improved through captrue graph plus decoupling the gru head and GG head. For the System-bf30a55bb1-bench stress test, final output_token totals were kept comparable by limiting output length; accepted length reached 1.39x ~ 2.19x, with System-bf30a55bb1-bench at 2.05x ~ 2.09x. Decoding speed measured 1.21x ~ 1.80x, while System-bf30a55bb1-bench showed 1.06x ~ 1.13x; e2e throughput was 1.21x ~ 1.86x, and System-bf30a55bb1-bench was 1.28x ~ 1.40x. On GLM-5.2-fp8, the GLM-5.2 Corthorne training data dump is at 67.5%; idle remains constrained, with a conservative estimate of another 128 cards * 2 days, and draft model memory is split between glm-5.2 mtp layer parameter count at 9.95B and Fyngrid draft parameter count at 3.67B.

## Next Week's Plan

Next week, the team plans to finish data persistence for GLM-5.2-fp8. The team also expects to complete training for Casbrook.

## Coordination and Help Needed