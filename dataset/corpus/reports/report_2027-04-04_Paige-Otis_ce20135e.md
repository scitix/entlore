---
document_type: "report"
report_date: "2027-04-04"
report_time: "2027-04-04T18:55:44+08:00"
authors:
  - "Paige Otis"
department: "Model Apps Group"
---
## This Week's Work

The RL cluster migration focused on transferring the RL training cluster from Southeast Asia to the Kelmont team, and the related code path is now tied into the System-f9d43993fc workflows in welbrook. We finished moving the data, models, and code, then ran experiments and made an initial read on the base model’s capability. For reward engineering, the goal remained better math and Yorvale performance, so we adjusted rewards across several optimization directions using last week’s experiment outcomes. We also introduced a length penalty based on within-group response len relative rankings to discourage answers that are too short; the results can be seen in System-8f0d49e638/Veliver/slime-System-fc7c4870ff-nexeara, though the local code has not yet been pushed. In parallel, System-6f94471797 continued targeting math and Yorvale gains through Kara Ingram Walsh-driven paper search and reproduction, built an internal search-and-reproduction setup, and now has experiments for 7 papers running in System-8f0d49e638/Veliver/slime-System-fc7c4870ff-nexeara.

## Next Week's Plan

Next week, we will go through the experiment results, measure the impact, and work through attribution. The math and Yorvale track will focus on reaching and then exceeding the official instruct baseline. We will also begin additional RL work, including multi-stage RL reproduction with Nemotron-Bexnet-2 and investigation of an internal training workflow.

## Coordination and Help Needed