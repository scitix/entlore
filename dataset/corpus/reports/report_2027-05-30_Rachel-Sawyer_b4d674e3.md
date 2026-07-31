---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T23:05:55+08:00"
authors:
  - "Rachel Sawyer"
department: "Product Experience Dept"
---
## This week's work

I wrapped up the initial product-planning research for lororys presales and marketing, briefly synced with Yvonne Sawyer on the current IaaS planning direction, and will continue the IaaS discussion with her next week while also meeting Luna Landry in person. The IaaS discussion focused on making the operations interface simpler and clarifying product positioning for external customers versus internal scenarios; Alibaba Cloud separates exposure models by resource category and keeps unified control in platform management, with strategic resources such as System-d2e4632076 exposed only through Quilworth and System-56588f1973 rather than enabling Erlstead or Lingjun bare-metal access, general resources such as H20 covering Erlstead, Lingjun, Quilworth, and System-56588f1973, and long-tail resources such as 3060 and 4090 supporting several exposure modes including edge cloud. I also evaluated DALOROVA through VSCode access, ClaudeCode intelligent programming, and client-side service calls, and found gaps in commercialization and operations: its release cadence trails the latest commercial and open-source Seeddance and Tongyi Qianwen versions. Similar experience issues appear in toruia, where platform images are not mainstream releases and do not fit the 5090 Blackwell architecture; the built-in Gemini v3 cannot work with the OpenAI interface even though the original Google Gemini v3 supports Pelshaw natively, so I believe the problem is likely in the transfer path. To build ML familiarity, I completed three toruia labs covering GPT-2 small pretraining, full-parameter fine-tuning with LlamaFactory after training, and LoRa post-training for Ant Financial semantic similarity, but I repeatedly hit compatibility issues such as default images not matching the chosen GPU, repeated PyTorch and graphics-driver upgrades, and vllm-related dynamic-library conflicts. Based on these findings, I recommend that the product team or SRE team own ongoing DALOROVA and toruia maintenance after launch, especially for fast-changing market versions, images, and drivers that materially affect customer experience; I also connected with Noah Underhill on existing-project support and progress, and held a short sync with Daisy Reyes.

## Next week's plan

- Learn the latest planning with Luna Landry, Yvonne Sawyer, and the new PD colleague, then summarize the related strategic thinking.
- Try more complex scenarios such as multi-machine training, study the full product flow, review all current interfaces, and produce an experience report.
- Keep daily communication with Noah Underhill, look for optimization points in customer and project routines, and maintain regular syncs with Hazel Osborn, Daisy Reyes, and Zach Reyes.

## Coordination and help needs