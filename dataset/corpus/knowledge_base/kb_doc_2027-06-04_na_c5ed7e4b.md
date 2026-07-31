## Umbays cluster enables public network access
- Start by checking the kubeconfig details for both public and internal connectivity.
- Use the internal apiserver address pattern 10.208.xxx.xxx:6443.
- Use the public apiserver address pattern xxxxx-Umbays.vexeum.ai:6443.
image.png
image.png
image.png

## Step two: create EIP and NatRules and map them to the internal apiserver
- Create the EIP and NatRules, then point them to the internal apiserver.
- Add DNS resolution for the public domain name as the next step.
- Configure xxxxx-Umbays.vexeum.ai:6443 or xxxxx-Umbays.vexeum.ai:16443 to resolve to EIP:6443 or EIP:16443.
- Prefer ports other than 6443, such as 16443, to lower exposure to public port scans.
image.png

## PS
- Users can self-service EIP and natrules creation in the UW（ap-southeast） region.
- For other regions, @Rachel Jarvis should support EIP and natrules creation.
- @Rachel Jarvis should also handle public domain DNS resolution setup across all regions.