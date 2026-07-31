---
document_type: "report"
report_date: "2027-05-01"
report_time: "2027-05-01T12:01:52+08:00"
authors:
  - "Grace Irwin"
department: "AI Compute Platform Dept"
---
## This Week's Work

Rayjob head nodes can now run on separate CPU capacity, so they no longer take GPU resources, and PVC mount paths now have uniqueness checks in place. For task fault tolerance, training-code fault injection now includes network-fault simulation, and the team resolved stability problems seen in cases such as loss divergence. The taint-cleanup issue identified through bisect detection was fixed and has been launched. On self-learning, I reviewed Google work on elastic large-scale distributed pretraining with Lorenys, and completed the basic syncer and learner implementation plus interaction flow from the Nora Ingram Lorenys demo. Integration with the System-323ce4fa5b pytorch job is under test, while Delshaw study focused on deepseek’s shift from full-attention models toward hierarchical memory and retrieval-based systems.

## Next Week's Plan

Next week, the task fault-tolerance work will move into real-environment validation. The team will exercise real fault simulation there and verify the related fault-tolerance handling.

## Coordination and Help Needed