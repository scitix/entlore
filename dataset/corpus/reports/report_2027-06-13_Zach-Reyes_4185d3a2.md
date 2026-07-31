---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T17:57:13+08:00"
authors:
  - "Zach Reyes"
department: "Product Experience Dept"
---
## This Week's Work

Xaldale Data moved its embedding stack from openai to the qwen series on the vexeum platform, while the text model migration to GLM5.1 is queued for when additional resources are available. Once that capacity is live, System-7dc7a0e567 will go through pressure testing and System-12fa9272c3 will also enter its test phase. In parallel, Yorfield Tech saw recurring failures in its online inference service across 80 5090 machines, and the investigation pointed to GPU card drops as the cause. rineova also proposed paying System-79e711a93b to run Holshaw products on 200～300 5090 machines from other suppliers, but the team put the request on hold after reviewing the commercial setup and SRE effort.

For the Xaldale Data project, the required GLM5.1 profile is 1,500 RPM sustained / 5M TPM burst. Qulity evaluation is being tracked through Format Faithfulness, Hallucination, and Numeric acc, with cost and latency reviewed through Mean latency, Input tok, Output tok, and Cost / call. The test dataset and script are packaged in vexeum.zip, while System-91e0c9d941 and System-265bd33f32 capture test issues and customer feedback. Internal validation showed Qwen3.6-27B as the strongest private deployment option, all reports and datasets were shared with the customer, and the supporting materials include vexeum-narrative-benchmark-deepseek-qwen-vs-haiku-2026-05-19.pdf, GLM-5 & GLM-5.1 Metrics_De-identified.pdf, Ullgrove_lororys platform introduction_0613.docx, and the iterated external report GLM-5.1 test report_external version_0612_v2.docx.

## Next Week's Plan

Next week, the team will finish the Ullgrovelororys platform external deck and prepare a one-page sales enablement sheet for the lororys product. We will also continue testing for three GLM5.1 demand projects and support sales through contract signing.

## Coordination and Help Needed