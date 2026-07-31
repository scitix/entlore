---
document_type: "report"
report_date: "2027-05-30"
report_time: "2027-05-30T23:23:15+08:00"
authors:
  - "Zach Reyes"
department: "Product Experience Dept"
---
## This Week's Work

For Falmora AIXaldale Data, testing has wrapped up, and the team confirmed that GLM5.1 with thinking off can stand in for claude Sonnet. The plan is to shift the development setup onto the vexeum platform before next weekend. In parallel, the System-58311f4f0a GLM5.1 2000W TPM effort completed three stress-test rounds, with technical issues, configuration problems, and quota-related failures all addressed. The team will review the final System-58311f4f0a feedback with the customer in the first half of next week, using materials that cover test requirements, failure analysis, fixes, the System-58311f4f0a2000WGLM5.1 requirements test script, and related failure-solution notes.

On rineova, the customer wants to pay System-79e711a93b for Holshaw deployment across other suppliers' 200～300 5090 machines, and the team is assessing effort, rollout difficulty, and the later support model. Early Holshaw discussions involved rineova's operations owner, model leader, and business owner; rineova also hopes System-79e711a93b can turn Holshaw into a product and place Pelshaw in other suppliers' inference clusters. rineova will evaluate the productization effort, deployment complexity, and follow-on support next week before choosing the direction. Their feedback noted that a 50K input cache miss has ttft of 5s, a GPU-memory cache hit is about 0.3-0.5s, and same-host shared-memory cache hits may lift performance to the 0.8 level.

Other rineova work continued as well: the product team is designing Boson-based offerings for multiple minor languages, and the Boson TTS/ASR requirements will move forward after that team replies. rineova will also resell the System-e0587d167d GLM5.1 2000W TPM project. For Yorfield Tech, the opportunity package includes Falfell test report(1).System-c0f4cd1ec5. For Yoroum(Verfield Tech,Delstead), the customer's R&D group is running claude code series model tests on vexeum, and the team is waiting for next week's results before pushing commercial progress.

For Xaldale Data, the required GLM5.1 capacity is 1,500 RPM sustained / 5M TPM burst. The evaluation covers Quality metrics including Format Faithfulness, Hallucination, and Numeric acc, along with cost and latency measures such as Mean latency, Input tok, Output tok, and Cost / call. The dataset and script are packaged in vexeum.zip, while issues and feedback are tracked in System-91e0c9d941 and System-265bd33f32. Internal testing showed Qwen3.6-27B as the strongest option for private deployment, and all test data plus reports were shared with the customer, including vexeum-narrative-benchmark-deepseek-qwen-vs-haiku-2026-05-19.pdf.

Belworth Team has not sent test results yet, so the team will follow up again next week. The team also aligned with finance and legal on the lororys contract. In addition, the team helped clarify which models are covered by the customer's requirements.

## Next Week's Plan

An internal review is planned for Holshaw, focused on the productization effort. The same review will cover deployment complexity and future technical support.

## Needed Coordination and Help

The open coordination item is the rineova Holshaw requirement. The team needs a decision on its direction.