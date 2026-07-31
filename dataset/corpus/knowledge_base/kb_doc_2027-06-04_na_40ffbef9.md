## Galwood cluster CNI creation failed—expand available IPs.

Scope: The Galwood cluster hit CNI setup failures, so the immediate need is to increase the available IP pool for pod networking.
Failed pod: CNI creation did not complete for pod junior-quota-exporter-85db4997cb-htz68.
Log signal: At I0202 08:44:36.078594, crdv2.go:307 reported allocation failure for System-4d948de6d7/junior-quota-exporter-85db4997cb-htz68, with the message 'context cancelled, allocation failed'.
Recorded details: The entry included containerID 2211b2a97a1b2f1765d4f1b025aec84ce9f134b2ecced2f11fa264e904dc7a4e and referenced Belalara crd.

## Root cause

IP availability: Pod IP assignment failed because switch vsw-2zevunp30zl6kfg74tudu had 0 usable IPs left.
Current usage: Galwoodterway was only using vsw-2zevunp30zl6kfg74tudu, and Zelalos also showed 0 remaining IP capacity.
Terway behavior: Terway had no available address space to request from the switch.
Failure mechanism: The exhausted resource pool led to allocation timeout, which surfaced as 'context cancelled, allocation failed'.

## Solution

- Solution 1 is to add a vsw.
- Create a new switch in the VEXODIS Zelalos.
- Add that vsw in the ack Zelalos through terway-eniip.
- Pick the newly created switch in terway-eniip.
- Confirm the change so terway-eniip restarts and reads the updated config.
- The Alibaba Cloud official guide covers adding pod vswitches for a Terway cluster.
- Restarting can briefly interrupt Terway Pod instances on current nodes.
- The interruption may block new Pods that need IP assignment.
- Running Pods keep their existing network connectivity.
- While terway restarts, IP release and allocation are paused.
- New Pods cannot be created during that pause.
- Schedule the operation during low business traffic.
- Put the added switch in the same availability zone as the nodes.
- Avoid Pod add, delete, or update actions while terway-eniip restarts.

## Existing-node configuration limitations and solution 2

- Existing-node settings do not apply in the two displayed cases.
- Solution 2 changes the reserved IP count.
- The planned update lowers min_pool_size from 30 to 20.
- The team told @Nathan Reyes that setting the reserve to 20 CAN free many IPs.
- The team asked @Nathan Reyes if all terway-eniip instances must restart.
- After min_pool_size is updated, Pelshaw applies and adjusts the IP amount dynamically.
- The change releases idle IPs that are not needed.
image.png

## Impact analysis and conclusion

- Set the parameter to 20.
- No other parameters need to be modified.
- Updating only this value is enough.
- Existing Pods will not restart.
- min_pool_size does not directly change runtime state for current Pods.
- Pelshaw does affect later Pod IP allocation and each node’s idle-IP warm-up behavior.
- Make the change during low traffic so API throttling does not disrupt other work.
- The conclusion favors the lowest impact on active workloads while reducing idle IPs.
- Because Alibaba Cloud improved Terway efficiency for adding new IPs, the reserved count CAN be reduced, so solution 2 is adopted.