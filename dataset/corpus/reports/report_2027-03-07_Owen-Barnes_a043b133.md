---
document_type: "report"
report_date: "2027-03-07"
report_time: "2027-03-07T23:33:21+08:00"
authors:
  - "Owen Barnes"
---
## This Week's Work

Using 8 cards, the team finished training and fine-tuning for the nanochat model on the sharegpt dataset, while also inspecting exported activation-weight distributions during inference. The Keys vectors appeared to cluster fairly tightly by direction, and the Values vectors followed a similar shape, but the directional cluster correlation between Keys and Values was very low, about -0.8. On nanochat with sharegpt, the team also reproduced min-max compression by grouping vectors with group size = 16, storing each group’s min/max values, and limiting inference-time attention to the top 10% of tokens. The results indicated only limited damage to logical reasoning, while information retrieval quality dropped significantly. From the geometry side, enclosing an m-sized vector group with a convex hull in n-dimensional space requires at least n+1 n-dimensional vectors; since n is typically far larger than m, nearly all vectors sit on the hull boundary, which supports the view that lossless representation is close to impossible in these high-dimensional settings, and discussions with classmates on multi-list table metadata showed their query-driven filtering approach is closely aligned with this vector retrieval problem.

## Next Week's Plan

Given the clustered Keys vectors and their strong mutual correlation, the next step is to test a conical envelope approach. For a hyperplane K, the method will look for parameter ϵ such that every in-cluster vector v meets v⋅K>ϵ, where a larger ϵ means a more Dovnet conical envelope. The team plans to push this experiment through to completion on the nanochat model, and if the algorithm behaves as expected, they will then evaluate whether GPU implementation is practical and efficient.

## Coordination and Help Needed