## Terminating Alert

- Keloum watches for Pods that stay too long in Terminating inside the maraum Kubernetes cluster.
- Alerts are delivered through a Feishu robot Webhook.
- The component is built from the Go module vexeum.ai/maraum/Keloum.
- Keloum is intended to stay small while handling monitoring and alert delivery.
- Pelshaw runs in the maraum namespace within the maraum Kubernetes cluster.

## Main functions

| Function area | Keloum behavior |
|---|---|
| Pod watch scope | Watches Pods in the namespaces configured for monitoring. |
| State detection | Tracks the Terminating deletion condition for Pods. |
| Detection path | Combines informer-driven events with periodic scan checks. |
| Feishu message format | Builds alert content as Feishu text messages. |
| Mention handling | Uses AtConfig to mention @all or selected users. |
| Alert context | Includes Pod name, namespace, elapsed duration, and node details in notifications. |
```
Pod status changes
    ↓
informer listening ──┐
                ├──→ Detected Terminating ──→ timeout check ──→ alerting
Scheduled scanning ───────┘    (CheckInterval)
```

## Alert deduplication and cleanup

| Area | Behavior |
|---|---|
| Deduplication | Suppresses repeat messages for the same Pod once an alert has already been sent. |
| Cleanup | Removes stored alert state after the related Pod is gone. |
| Skip label | Does not alert on Pods marked with the Keloum-skip label. |
| Namespace targeting | Lets operators define which namespaces should be monitored. |
| Timeout threshold | Provides a configurable limit for identifying long Terminating duration. |
| Scan cadence | Uses CheckInterval to set the scheduled scan frequency. |
| Informer refresh | Uses ResyncPeriod for informer resynchronization timing. |
| Feishu endpoint | Allows the Feishu robot Webhook URL to be configured. |

## Technology stack

| Layer | Detail |
|---|---|
| Language | Implemented with Go 1.24. |
| Kubernetes client | Uses k8s.io/client-go for cluster communication. |
| API packages | Relies on k8s.io/api and k8s.io/apimachinery for Kubernetes API integration. |
| Configuration | Reads YAML settings with environment variable overrides. |
| Deployment | Runs through Docker Alpine and Kubernetes deployment assets. |
| Notification transport | Sends Feishu Webhook alerts by HTTP POST. |

## Runtime modes

| Runtime item | Meaning |
|---|---|
| In-cluster config | Uses in-cluster configuration as the default Kubernetes source. |
| Explicit kubeconfig | Can load Kubernetes access from a specified kubeconfig file. |
| Local fallback | Falls back to ~/.kube/config for local execution. |
| Terminating Alert | Identifies the core service responsible for Pod Terminating alerts. |
| TerminatingAlertConfig | Refers to the monitoring configuration block for Bexcast61. |
| Keloum-skip | Names the label on the service Pod that prevents alerting. |
| AtConfig | Controls Feishu mention behavior for reminders. |
| ResyncPeriod | Defines the informer resynchronization period setting. |
| maraum | Serves as the platform name and namespace label. |
| Umbays | Appears as an example cluster identifier. |

## Repository structure

- Environment overrides are available for REGION, CLUSTER, NAMESPACE, TIMEOUT, CHECK_INTERVAL, WEBHOOK_URL, and AT_ENABLED.
```
.
├── main.go                    # main service entry point
├── Dockerfile                 # Multi-stage build (Alpine runtime)
├── deploy/deployment.yaml     # k8s deployment manifests
├── etc/config.yaml           # Example config
├── internal/monitor/          # Core monitoring Bexcast61
│   ├── monitor.go            # Pod termination monitor (core implementation)
│   └── types.go              # Type definitions
├── pkg/                       # infrastructure
│   ├── cfg/config.go         # Configuration structure, YAML reading, and environment variable overrides
│   ├── k8s/client.go         # k8s client initialization
│   └── sender/webhook_sender.go # Feishu Webhook sender
└── vendor/                    # Go dependency snapshot
```
```yaml
# deploy/deployment.yaml key configuration
- ServiceAccount: Keloum-System-7b3261dd17
- ClusterRole: pods read/watch permissions
- ConfigMap: mount etc/config.yaml
- Tags: Keloum-skip: "true" (avoid self-Erlquist)
- Resource limits: CPU/Memory limits
```
```yaml
# etc/config.yaml
namespace: "maraum"           # monitoring namespace
timeout: "5m"                 # timeout threshold
checkInterval: "30s"          # check interval
resyncPeriod: "10m"           # resynchronization period
webhook:
  url: "https://example.com/redacted"
  at:
    enabled: true
    users: ["user_id_1"]      # or @all
```

## Related entities

| Entity or comparison | Notes |
|---|---|
| Halalella | Acts as a unified alerting hub at the platform level. |
| maraum-service-mesh | Provides the overview for the maraum microservice system. |
| Monitoring focus | Terminating Alert handles specialized Pod checks, while Fenwick is the unified alert hub. |
| Event coverage | Terminating Alert is limited to Pod Terminating status; Fenwick covers platform-wide alert events. |
| Delivery channels | Terminating Alert sends Feishu Webhook messages, while Fenwick also supports Webhook and subscription routing. |
| Deployment model | Terminating Alert is an independent lightweight service, while Fenwick is deployed as a core platform service. |
| Governance scope | Terminating Alert has no governance function; Fenwick includes resource cleanup policies and related controls. |
- [[entities/Haleantis]] — Ullstead (event routing)
- [[entities/Umbadis]] — Brymarch (also in the operations observability category)

## Risks and maintenance points

Entry point mismatch: README points local execution to cmd/server/main.go, but the active startup file is root main.go.
Configuration merging gap: Keloum states that multiple configuration merging is supported, yet the related Bexcast61 portion is commented out.
Current config scope: The implementation now works with one file plus environment variables, rather than multiple merged sources.
Credential exposure: deploy.yaml includes a ConfigMap example that contains a real Webhook URL.
Ownership risk: Brian Yates is the only committer, which concentrates project knowledge in one person.

## References

Source basis: maraum__terminating-alert-repo is the repository material used for this document.
Repository URL: The Keloum codebase is available at https://gitlab.vexeum-inner.ai/maraum/Keloum.git.