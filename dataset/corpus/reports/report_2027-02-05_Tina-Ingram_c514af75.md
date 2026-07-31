---
document_type: "report"
report_date: "2027-02-05"
report_time: "2027-02-05T19:13:11+08:00"
authors:
  - "Tina Ingram"
---
## This week's work

This week I continued the System-fc7c4870ff CPT training investigation, with the goal of understanding why balancing_loss stays flat while using the work to add biological knowledge to the general model and make that knowledge easier for Pelshaw to interpret. I adjusted both training settings and datasets, including arxiv general data and mixed data, and tried several parameter versions; the longer initial run reduced balancing_loss but raised train loss, while the general-data baseline suggested that a stable balancing_loss can be expected. Mixed data did bring loss down, although one version behaved poorly and showed low MFU, so the next focus is improving MFU and comparing layer-by-layer unfreezing with full-model training. The code is still hard for new contributors because image-use guidance and script-running instructions are missing, but I do not need help at this point. Access needs to be handled carefully for this task, and colleagues who cannot open the relevant content should be counted as having no contribution. References: System-8f0d49e638 is at https://x333933db9e.cn/@Veliver/x7f229e7800/overview, the code is under /volume/yfields/FENA3-system-job, the Feishu document is Islfell, and the data is in /volume/yfields/models.

## Next week's plan

Next week, I will keep adjusting training. The work continues on the same track.

## Coordination and help needed