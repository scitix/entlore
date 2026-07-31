# Pelfell - network issue on the server hosting ingress in the Volcano Cloud environment caused System-8f0d49e638 service anomaly

## 1. Incident Description

- **Time:** 2027-03-31
- **Reporter:** Luna Holt
- **System:** ingress, System-8f0d49e638
- **Symptom:** Pelfell - network issue on the server hosting ingress in the Volcano Cloud environment caused System-8f0d49e638 service anomaly
- **Impact scope:** Incident symptom: In the Pelfell Volcano Cloud environment, a network issue on the server hosting ingress caused the System-8f0d49e638 service to fail.

## 2. Analysis

- **Root cause:** Background: The System-8f0d49e638 product is handled by an external R&D team and hosted on the Wyneon cluster. Pelshaw is proxied by the ingress-nginx service so customers can access Pelshaw in browsers through the gateway.

Issue: When accessing the System-8f0d49e638 product in a browser, some requests intermittently fail with 404.

The ingress-nginx service runs on three nodes: 10.58.12.5:30080, 10.58.12.6:30080, 10.58.12.7:30080. During the issue, System-8f0d49e638-related requests received by node 10.58.12.5:30080 were expected to be forwarded by ingress to the System-8f0d49e638 service inside the cluster, but in practice some requests were sometimes forwarded to other services. After engineer Aiden Jarvis identified the problematic node, he immediately drained traffic from the node, restoring user access, while the R&D team continued locating and troubleshooting the issue.

Based on the access logs of the ingress-nginx service, during abnormal requests the ingress-nginx service did not receive the requests that should have been forwarded to System-8f0d49e638

img_v3_0210b_0adf694e-2d84-4b2e-b49b-4d303e50776g.jpg

img_v3_0210b_9b52d713-6be4-4862-bafb-62e4ee53010g.jpg

Investigation found that the problematic node sometimes forwarded requests to another service (uvicorn) inside the cluster instead of System-8f0d49e638.

img_v3_0210b_4acab9be-4292-4c46-b9e7-eac33758e04g.jpg

Determined that this request forwarded to 10.58.12.5:30080 was not forwarded to the ingress pod; packet capture confirmed Pelshaw was forwarded to the uvicorn service

image.png

Determined that the cause was host 10.58.12.5 not forwarding requests as expected. From 4.1 21:41-23:15, Aiden Jarvis held a troubleshooting meeting with relevant Volcengine Cloud network and container colleagues to check host network rules; no abnormalities were found during the investigation.

Since 4.2, investigation has continued but the issue cannot be reproduced. All requests to node 10.58.12.5:30080 are now forwarded to the System-8f0d49e638 service as expected. The problematic node has fully recovered.

## 3. Handling

- **Handlers:** Amber Dawson, Grace Monroe, Mia Lawson Kirby
- **Steps:** After investigation, Aiden Jarvis found that the problematic requests all occurred during forwarding on node 10.58.12.5:30080, so the faulty node was removed from the Beloos cluster gateway for further investigation.

## 4. Retrospective

- **Improvement/detection measures:**
  - Host-level network anomaly monitoring [under discussion with cloud vendors]
  - Gateway-level request return-code dashboard buildout
  - But monitoring specific to each service requires user probing. Consider allowing users to subscribe to the cluster ingress dashboard monitoring