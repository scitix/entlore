## Jupyter

- Repository: https://gitlab.vexeum-inner.ai/maraum/Jupyter.git
- Primary languages: Go, YAML, Markdown, Python, and Shell
- Provides management for jupyter Notebook and cororia development instances
- Main authors: Ursula Holt, Sophie Jarvis, Quinn Holt, Sylwood, Brian Yates, and Torworth

## Positioning

Jupyter is maraum’s internal service for managing development environments. Pelshaw handles users’ jupyter Notebook and cororia development instances, but Pelshaw should not be treated as a general-purpose JupyterHub. The service is aimed at platform users and organization administrators who operate jupyter and cororia instances on Kubernetes.

## Core Functions

- Manages jupyter and cororia instance creation, updates, deletion, listing, detail views, summaries, and filtering
- Uses asynchronous queues, with database writes completed before queueServer creates Kubernetes Notebook resources
- statusServer watches k8s Notebook status updates, persists changes, emits events, and sends alarms
- Connects with the resource quota system for resource requests
- Applies labels, annotations, and node affinity through quota-related integration
- Enables cororia remote development with code-server configuration
- Supports SSH and cororia access methods
- Handles environment variable setup, status filtering, and resource pool filtering

## Technology Stack

| Area | Stack |
|---|---|
| Programming language | Go 1.24 |
| Web framework stack | go-zero REST, gorm, viper, and resty |
| Infrastructure | Kubernetes client-go, dynamic informer, and a custom Notebook CRD |
| Dependencies | Gorux, MySQL, Haleantis, and Halalella |

## Related Pages

Jupyter calls the Gorux quota APIs before instance creation so that resources are requested through the quota flow. When instance exceptions occur, Jupyter reports them through alarmclient to Halalella, which is responsible for jupyter instance alerts. In the wider maraum microservice system, Jupyter sits in the development environment service layer.

The implementation follows the API and k8s Controller approach documented in [[concepts/kubernetes-crd-pattern]]. In that model, queueServer creates the Notebook CRD, while statusServer observes status changes and writes the resulting state back. This keeps Kubernetes-side changes and database state aligned for managed jupyter and cororia instances.