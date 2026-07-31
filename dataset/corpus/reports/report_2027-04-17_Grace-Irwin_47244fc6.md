---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T14:23:01+08:00"
authors:
  - "Grace Irwin"
department: "AI Compute Platform Dept"
---
## This week's work

We finished and shipped a detail and list page renovation, and also released grafana integration for the vllm instance launched by training tasks. Training tasks now stop themselves once image-pull failures pass the configured limit, which prevents endless retry loops and avoids resource waste. For task fault tolerance, we added failure injection into training code so testing can mimic real training errors; online-environment validation is still pending, and the team also reviewed System-6e509889dd plus Baidu articles and papers on training fault tolerance systems. On RayJob, the create and detail pages had shown instance usage incorrectly whenever discovered workers were greater than 0; for example, with rayjob worker as 10 and worker per node as 1, the display should have been instance * 11 but was instance * 1, and that instance-count issue is now fixed. We also resolved intermittent high latency in the self-discovery listtask/gettask interfaces, closed troubleshooting request r-20260417050252MzP, fixed the test-environment pytorch job nodeselector path for choosing a specific gpu, and updated System-323ce4fa5b: Claude.System-c0f4cd1ec5 now has a project overview plus project-level skills for database queries and test-environment validation, while additional project rules were added from time-consuming interaction points with Kara Ingram Walsh.

## Next week's plan

The task fault tolerance project will move to real-environment fault simulation. In that same real environment, we will validate the fault-tolerant handling flow. The goal is to confirm that the handling path works under real fault conditions.

## Coordination and help needed
