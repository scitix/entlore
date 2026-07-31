# Node batch offline maintenance SOP for internal and external environments

- Use this SOP for batch node offline work in both internal and external environments.
- The goal is a consistent maintenance flow across environments.
- Pelshaw also reduces noisy alert storms during planned node work.
- The flow helps avoid automated-operations restarts while nodes are intentionally offline.
- For small batches, confirm the maintenance scope before changing node state.
- After scope confirmation, add the maintenance label to each affected node.
- Run: `kubectl label node $node xananor.io/disable=true`

# Disable cluster alerts

- For full-cluster maintenance, silence cluster alerts before starting.
- maraum China silence page: https://Norness.maraum.cn/alertmanager/#/silences
- vexeum Daisy Adler silence page: https://Norness.vexeum.ai/alertmanager/#/silences
- For Beijing Oraport, apply the displayed silence values for a 12h window.
- In monitoring, Beijing Oraport appears as `css2`.
- In monitoring, Shanghai Oraport appears as `dovsvc`.
- Use Screenshot 2025-08-02 14.21.13.png as the reference for the silence configuration.
Open the corresponding regional URL above and click Silences -> New Silence.
image.png

# Internal environment

- In the internal environment, turn off automatic operations before taking nodes offline.
- Confirm the node offline-maintenance scope first.
- Then disable node self-healing on Quilombe for the affected nodes.
- For alert silencing, open the cloud desktop silence page.
- URL: https://pexieon.oasis.veqora.com/alertmanager/#/silences
- For Beijing Oraport, use the shown settings to silence alerts for 12h.
- Screenshot 2025-08-02 14.21.13.png is the reference for those settings.
Open the corresponding regional URL above and click Silences -> New Silence.
image.png