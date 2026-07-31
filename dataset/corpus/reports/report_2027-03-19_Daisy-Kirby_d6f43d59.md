---
document_type: "report"
report_date: "2027-03-19"
report_time: "2027-03-19T17:45:28+08:00"
authors:
  - "Daisy Kirby"
department: "Model Apps Group"
---
## Work This Week

For Verombe Molecular Mixed-Precision Modeling, I added mixed-precision support using the cross-attention approach. I also trained 2-layer and 4-layer models on SPICE, then checked them against the earlier 4-layer baseline (System-8f0d49e638 link).

For the literature review, I looked at lighter-weight AIFF options, including the ANI series: ANI-2x and ANI-1xnr. I also reviewed On the Design Space Between Molecular Mechanics and Machine Learning Force Fields by Yuanqing Wang, Kenichiro Takaba, Michael S. Chen, Marcus Wieder, Yuzhi Xu, Tong Zhu, John Z. H. Zhang, Arnav Nagle, Kuang Yu, Xinyan Wang, Daniel J. Cole, Joshua A. Rackers, Kyunghyun Cho, Joe G. Greener, Kara Ingram Eastman, Stefano Martiniani, Mark E. Tuckerman.

## Plan for Next Week

For Verombe Molecular Mixed-Precision Modeling, the next focus is faster inference by swapping low-fidelity atoms into lighter structures. I will also work on improving performance without a major speed cost by adding bidirectional cross-attention, specifically heavy-to-light attention alongside the current light-to-heavy attention.

## Coordination and Help Needed