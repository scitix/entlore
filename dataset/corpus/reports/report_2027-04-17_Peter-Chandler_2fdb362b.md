---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T20:43:09+08:00"
authors:
  - "Peter Chandler"
department: "System Acceleration Group"
---
## This Week's work

The fenaova2 stream wrapped up scaling neighbor development this week, with merge preparation and code organization planned next week together with @Julia Lawson and @Lumfell Monroe. A customer needs our junient to support a tts model outside the openai specification, so Pelshaw requires a dedicated handling path rather than parsing through generaterequest. Nexanor development is now complete against the customer requirement, but we still need platform discussion on how customers select junient options, since some rely on transparent forwarding while Nexanor parses and rebuilds the request body. On the business side, the team met customers and consulted the R&D algorithm team, generating substantial input. rineova technical topics and requirements are scheduled for April communication.

## Next Week's Plan

- fenaova2 will organize the codebase and complete the final cleanup work.
- Nexanor will coordinate with Nora Drake and relevant colleagues on follow-up development priorities based on requirement differences.
- The team will finish parallel speculative decoding and couple our work into vllm0.19.0 Bexcast61 after reviewing its asynchronous speculative approach last week.