---
document_type: "report"
report_date: "2027-04-18"
report_time: "2027-04-18T18:47:00+08:00"
authors:
  - "Paige Otis"
department: "Model Apps Group"
---
## This Week's Work

The Umbeara performance optimization effort focused on improving System-f9d43993fc while using metrics and targeted traces to identify issues in the training model. That stream delivered System-ad65904b1d and referenced Belmarch and Paige Otis. In parallel, System-7ebee63fa8 also targeted System-f9d43993fc, using a data-processing pipeline that split and sampled data by model rollout32 pass_rate so the team could analyze both data and traces; its resulting output was System-7ebee63fa8.

For System-51e4d0f90e, the team used qwen3-1.7b to bring non-thinking performance closer to the thinking model level and checked whether the current rl algorithm made sense. The resulting evaluation chart is available at https://x333933db9e.cn/@Veliver/xbbc77dc15b/runs/x7e5740b2c2/chart?ct=eval. Another Umbeara optimization track, System-6f94471797, relied on Kara Ingram Walsh-driven paper discovery and reproduction, then built a dedicated discovery and reproduction setup. After manual review, the reproduced ideas and code generally showed weak trial results, which pointed the work toward deeper algorithm development rather than wider exploration; although several reproductions were completed, most were not evaluated, and the search was tightened with dfs chosen over bfs.

## Next Week's Plan

Next week, the plan is to keep pushing deeper algorithm exploration for System-f9d43993fc. The goal is to produce different results.

## Coordination and Help Needed