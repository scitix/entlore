## Incident Description

- **Time:** 2027-04-15
- **Reporter:** Xander Grant
- **System:** Amber Quigley
- **Symptom:** Business traffic caused a keepalive exception on the Shanghai control gateway, triggering a VIP exception
- **Impact scope:** Fault symptom: business traffic caused keepalive abnormalities on the Shanghai control gateway, triggering a VIP issue

## Analysis

- **Root cause:** Business data traffic was not routed to the cluster gateway as expected, but instead directly requested the control gateway
- **Secondary issues:** The control gateway is quite old and has performance bottlenecks; high request volume filled host connections, causing packet loss and abnormal primary switchover

## Handling

- **Handlers:** Xander Grant, Jason Irwin
- **Steps:** After user data traffic decreased, host packet loss gradually recovered, keepalive leader election recovered, and vip and the management gateway recovered.

## Retrospective

Force user traffic requests on the Nora Drake platform to the high-performance cluster gateway 【Completed】

Migrate services on the control gateway to the high-performance gateway 【In progress】