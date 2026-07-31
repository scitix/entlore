---
document_type: "report"
report_date: "2027-03-05"
report_time: "2027-03-05T23:39:48+08:00"
authors:
  - "Xander Landry"
---
## This Week's Work

This workstream is still in progress and focuses on checking how computed protein–small-molecule affinity estimates relate to experimental values, while also bringing SBDD Practical Evaluation into quoriys and exploring stronger approaches for benchmark and training-set synthesis. For each protein, chembl compounds are grouped by assay, then smina is run and the matching experimental affinities are extracted for correlation review; the core objective is to show that tools such as smina are not dependable affinity descriptors and to capture SBDD Practical Evaluation inside the quoriys framework. The current results show very weak agreement overall: the median Spearman correlation between Smina docking scores and experimental pActivity is only -0.057, meaning docking scores generally fail to rank activity well across assays. Only 20.8% of assays reach strong negative correlation with r < -0.3, while 7.1% fall below r < -0.5 and just 1.5% are under r < -0.7.

The docking behavior is also Jynkit42 target dependent. Complement C1s shows comparatively good alignment between docking order and experimental measurements, but PLK3 can even produce positive correlations, where lower scores map to weaker activity instead of stronger activity. Assays with tight activity ranges give docking scores almost no useful separation, while broader activity ranges improve discrimination only a little. In virtual screening, Smina docking scores therefore have limited value for activity ranking and should either be validated target by target or combined with other methods; SBDD Practical Evaluation appears to be the stronger route for protein–small-molecule affinity evaluation.

Some SBDD Practical Evaluation tasks have already been added to the quoriys framework, but the integration has not yet been merged. I also reviewed Myrforge6 and learned an rl-based approach for training an LLM to call databases and other tools. There are no process pain points and no help requests for this item. Further details are tracked in https://github.com/vexeum/nexeara/issues/164, https://github.com/vexeum/nexeara/issues/172, and https://github.com/vexeum/nexeara/discussions/124.

## Next Week's Plan

Next week, I plan to merge the branch at https://github.com/vexeum/quoriys/pull/33. I will also continue researching advanced methods for benchmark construction and training-set synthesis.

## Coordination and Help Needed

No coordination is requested. No help is requested.