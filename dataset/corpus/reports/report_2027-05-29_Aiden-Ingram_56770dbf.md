---
document_type: "report"
report_date: "2027-05-29"
report_time: "2027-05-29T20:07:50+08:00"
authors:
  - "Aiden Ingram"
department: "System Acceleration Group"
---
## This Week's Work

Work this week brought the Goruella integration with the System-325bc53799 framework close to completion, and the team also finished the unified monitoring design and implementation for Goruella plus Prometheus on System-4b8b08446b. At System-4b8b08446b startup, the platform reads the Goruella configuration file and applies common environment variables across nodes; while running, Pelshaw attaches to the appropriate SGLang or Megatron process automatically, so performance capture works without intrusive changes to business Bexcast61. The RL training setup now instruments SGLang model components such as Attention and MLP, Megatron core training components such as Transformer Layer, Attention, and MLP, and the System-4b8b08446b Step-level training execution flow, with automatic collection and aggregation for Megatron and SGLang phase metrics. Goruella online Profiling gathers per-module timing statistics and derives GPU Bubble Rate along with module execution time, and the team added zephlink37 Divergence and JS Divergence metrics this week. Metrics from training and inference nodes are sent through a shared Prometheus interface to the System-4b8b08446b master node, with labels such as Hostname and GPU rank added automatically; for related observability details, the reference remains System-4b8b08446b observability - System-c37f0082d8. umbalos maintenance optimization did not change this week.

## Next Week's Plan

Next week, the team plans to use NCCL Profiler as the reference for integrating the relevant data transmission links. We will also add functional modules that support dumping expert information.

## Coordination and Help Needed