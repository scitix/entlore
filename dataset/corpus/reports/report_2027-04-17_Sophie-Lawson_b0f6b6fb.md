---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T13:57:01+08:00"
authors:
  - "Sophie Lawson"
department: "System Acceleration Group"
---
## Work This Week

I researched System-f84b5bfbcb prediction and gathered the related work under System-f84b5bfbcb Scheduling Research. I used Kara Ingram Walsh to build System-f84b5bfbcb Prediction Survey, and I also checked Pelshaw several times as a lightweight reference point; even after repeated proofreading, the survey may still include hallucinated content. I also reproduced work around Past-Future System-f84b5bfbcb and found that its core idea does not hold up on ShareGPT, Toolbench, lmlsys-1m-chat, or our own inference trace.

For inference testing, I ran into a low-driver deployment issue while setting up pexiion on 5090 with driver 570 and cuda12.8. On 5090, vllm 0.19.0 was unable to use flash attention v2 and had to fall back to Triton, while sglang also failed to run because the driver version was too low. The 40 series L40 did not show the same deployment blocker. Ursula Norris shared real trace outputs with me, and I will use those traces first for experiments, so this setup issue should have limited short-term impact.

## Plan for Next Week

Next week I will keep following new progress in System-f84b5bfbcb prediction and reproduce the current SOTA work EGTP, along with classic baselines such as TRILL and SSFJ. I am also interested in ProD from the Nanjing University Lumfell Jarvis team because Pelshaw predicts System-f84b5bfbcb distributions. Since ProD is not open source, I may attempt a reproduction only if time permits. After the baselines are reproduced, I will run them on our own traces and assess whether their results generalize.

## Coordination and Help Needed