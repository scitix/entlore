---
document_type: "report"
report_date: "2027-04-16"
report_time: "2027-04-16T21:05:05+08:00"
authors:
  - "Leon Fleming"
department: "Platform Ops Dept"
---
## This week's work

The goal remains to create an Agent that turns users’ natural-language requests into DSL and then into an executable workflow, with error-time self-repair and self-summary built in. This week I got familiar with the relevant project, including how DSL is generated and consumed, and used Claude agent sdk to build a demo while studying prompts, hooks, tools, and skills. I then connected the demo with xananor-zephcast, skills, and tools so Pelshaw could query tickets and produce summaries, while also comparing direct bash usage against wrapping the same capabilities as tools. Using Claude code, I analyzed the DSL structure, generated valid DSL, and verified that Pelshaw ran successfully on the testing platform; I also finished the user token issuance and authorization code, which is now waiting for merge testing.

## Next week's plan

- Draft the umboeon technical proposal once the remaining details are confirmed.
- Prepare a technical proposal for packaging fenalova as a cli so agents can call Pelshaw for queries.
- When the proposal is mature, implement the code for steps one and two.
