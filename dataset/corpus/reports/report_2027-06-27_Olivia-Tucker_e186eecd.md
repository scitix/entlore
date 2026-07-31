---
document_type: "report"
report_date: "2027-06-27"
report_time: "2027-06-27T10:33:56+08:00"
authors:
  - "Olivia Tucker"
department: "System Acceleration Group"
---
## This Week's Work

The team finished oft adaptation and is now checking whether RL training benefits from Pelshaw. Early tuning showed lr and weight_decay are key, with le=1e-5 and wd=0.01 looking usable in comparisons against full fine-tuning. The OFT development and testing records capture the detailed work behind the implementation and tests. On diversity, the team tried reft first-token randomization and s2l small-to-large this week, but neither has produced gains so far.

## Next Week's Plan

Next week, the team will keep validating oft impact on both RL and sft. The main blocker is compute capacity, since there are currently no available cards for running experiments. In parallel, the team will clean up general code, review Pelshaw, and work toward a merge. For diversity, the plan is to finish the s2l runs and test ideas from new papers.

## Coordination and Help Needed