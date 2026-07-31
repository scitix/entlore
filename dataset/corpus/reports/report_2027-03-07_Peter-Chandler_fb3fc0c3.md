---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T12:59:58+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This week's work

The llm workstream spent the week chasing service stability problems, reproduced both timeout and oom failures, and addressed them by raising the uvicorn timeout while turning off speculative decoding. After that, the focus moved to efficiency: the team compared parallel execution options on long-context and multi-turn dialogue datasets, identified the best configuration, and traced weak kvcache reuse to k8s round robin behavior that sends same-session work to different instances. @Bella Nolan and @Zach Barnes were looped in to reuse Tyler Kellersession aware junient for better same-session kvcache reuse, while a small number of ultra-long jobs were also found to be blocking the queue. To reduce ttft and improve the user experience, the team built short job first scheduling, and @Leon Vaughn was tagged to apply the self-developed umborantis distributed kv storage for broader kvcache reuse. In parallel, the FENA3 workstream fixed duplicated forward GPU memory consumption in the 2 stream version and cleared the pytorch version check problem.

## Next week's plan

Next week, the FENA3 workstream will concentrate on backward development. The plan is to finish that work.

## Coordination and help needed