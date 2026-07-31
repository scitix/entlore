---
document_type: "report"
report_date: "2027-04-17"
report_time: "2027-04-17T16:02:07+08:00"
authors:
  - "Ryan Quigley"
department: "Platform Ops Dept"
---
## This week's work

Wynwick moved metric alerting out of alertmanager and into the alerting center, while launching the new UI design together with the Bexcast61 probe-interface updates. The home page UI was adjusted, business creation was added, favorites are now supported, and active alert events now include Pod details; Pod views also show cpu usage and memory usage. The original probe model was replaced with business probing that is no longer tied to deployment units, with support for multiple protocols, multiple nodes, and initiation from either internal or external networks. Wynwick also expanded the routing information Tab, introduced an error analysis module, added log analysis and event analysis Tabs, removed alert switches from deployment units and probing tasks, and shifted deployment-unit and probing-task alert setup into centralized alert configuration. Migration scripts were built to convert existing probes into probing tasks, pod cpu and memory usage-rate alerts with customizable thresholds were added, and the current-alert and historical-alert APIs are now under testing.

casport2 is now launched, including requirement support for operation auditing and administrator audit viewing, batch log insertion, and creation of Http Webhook subscriptions for Project messages. Pelshaw also adapted Norness calls for maraum requirements, while project and repo viewing interfaces for those requirements are still being developed and adapted for Norness calls. Junuum image startup acceleration support is in testing to reduce the impact of Dockerhub image source-site rate limiting. Rinoara supplies cached Dockerhub images and cached Manifest capability so the system does not repeatedly fetch from origin. The TODO discussion is about using a dockerhub account pool to raise the rate-limit ceiling, and on-demand loading is being postponed because current startup speed is acceptable.

## Next week's plan

Wynwick plans to add pod cpu and memory usage-rate alerts with customizable thresholds, along with current-alert and historical-alert APIs. casport2 requirement development will focus on interfaces for viewing project, repo, artifact, and tag, and those interfaces will adapt Norness calls to meet maraum requirements. Junuum image startup acceleration support will continue targeting Dockerhub image source-site rate limiting. Rinoara is expected to provide cached Dockerhub images and cached Manifest functionality to reduce repeated origin access.

## Coordination and help needed