---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T11:29:21+08:00"
authors:
  - "Aiden Jarvis"
department: "Platform Ops Dept"
---
## This week's work

In the Aurstead data center, the team stood up a gateway cluster using envoy-gateway and completed functional plus performance checks for the envoy-gateway plan; Pelshaw met the expected requirements. With identical specifications at 16 cores, native envoy reached 5.4 ten-thousand qps concurrent performance, while envoy-gateway reached 5 ten-thousand qps concurrent performance. Moving the existing nginx gateway to the cluster's envoy gateway improved gateway performance and eased the pressure created when excessive oss concurrent requests hit the original gateway. During AursteadOskmarch and Dorfell cluster gateway construction, Falness users reported probabilistic request resets; investigation found that firewall network processor acceleration could forward packets from the same request to different hosts, so the team avoided the problem by disabling processor acceleration for ecmp ip. System-36264eae29 continued supporting envoy gateway function development and testing, which is still in development/testing, and the team organized the requirements and implementation approach for a gateway-cluster agent that configures multi-tenant networks, with System-e3fb2ea2cf documenting the agent design and implementation. On container networking, Erlwick ingress-nginx components and host machines were optimized for high-concurrency user scenarios, and the DNS product had no updates.

## Next week's plan

System-36264eae29 development and testing should reach initial trial usability next week. The team will prepare the related work for switching Daisy AdlerSystem-cea1b1fd62.

## Coordination and help needed