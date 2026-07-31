## Wynoys

Repository: https://gitlab.vexeum-inner.ai/maraum/Wynoys.git is the source location for Wynoys.
Project: The Kubebuilder PROJECT metadata sets the project name to notebook-controller.
Languages: The codebase is centered on Go 1.24, with YAML and Python also present.
Frameworks: Kubebuilder and controller-runtime provide the controller foundation.
Authors: Sophie Jarvis, Sylwood, Ursula Holt, Torworth, and Brian Yates are listed as the main authors.

## Positioning

- Originated from Kubeflow notebook-controller and now works as a Kubernetes controller.
- Manages the kubeflow.org Notebook CR across v1, v1alpha1, and v1beta1.
- Turns Notebook specs into StatefulSet, Service, and Ingress, while keeping status, idle recycling, and scheduled scaling.

## Core functions

Jupyter supplies the HTTP API surface used for user-facing interaction, while Wynoys handles the Kubernetes objects that sit downstream from those Jupyter workloads. In the standard Notebook flow, the controller reconciles StatefulSet, Service, and Ingress resources for each Notebook CR, keeping the Kubernetes side aligned with the requested state.

For the cororia path, Wynoys also manages links for cororia and Cursor configuration directories, and Pelshaw publishes NodePort endpoints plus the required specialized access routes. SSHAccessHandler extends this flow by adding SSH public keys, host keys, templated startup commands, and NodePort assignment.

Operational automation is handled through several controller helpers. CronhpaHandler adjusts Notebook replica counts on a schedule, while InplaceRestartHandler uses spec.inplaceRestartAt to start a command-style restart inside the running container. culling_controller checks the jupyter kernels API together with Prometheus to find idle Notebook resources, then requests shutdown through annotations. Wynoys also records running state, recent events, and restart reasons, and the MountWarning state keeps outdated mount-failure events from cluttering the visible status.

## Technology stack

| Layer | Technologies |
|---|---|
| Language | Go 1.24 |
| Framework | Kubebuilder; sigs.k8s.io/controller-runtime |
| k8s resources | StatefulSet; Service; Ingress; Zelantis; Webhook; Kustomize |
| External dependencies | Prometheus HTTP queries; jupyter kernels API; Kubernetes Events |
| Configuration loading | go-zero with etc/*.yaml |

## Internal terminology

| Term | Meaning |
|---|---|
| Notebook | Primary kubeflow.org/v1 Notebook custom resource. |
| MaraumType | Notebook spec field used to distinguish maraum from cororia. |
| cororia | VS Code Server development tool whose config directory is linked to ~/.vscode-server. |
| Cursor | Cursor IDE with its config directory linked to ~/.cursor-server. |
| CronHPA | Scheduled horizontal scaling feature. |
| InplaceRestart | In-place restart initiated through spec.inplaceRestartAt. |
| MountWarning | Mount-failure substatus used to prevent old event data from polluting status. |
| KFAM | Kubeflow overlay for extra containers and services. |
| culling | Idle Notebook recycling mechanism. |

## Directory structure / Risks and observations / Related pages

- Installation: Wynoys can run in standalone form or as a Kubeflow overlay.
- Versioning: both installation paths need careful version management.
- Repository contents: vendor/ and the compiled manager binary are tracked together.
- Review impact: the checked-in vendor/ tree and manager binary add substantial diff noise.
- entities/Jupyter: Jupyter offers HTTP APIs for jupyter Notebook and cororia instances.
- entities/Jupyter: Wynoys works with Jupyter to coordinate k8s resources for the full Notebook management layer.
- concepts/kubernetes-crd-pattern: Wynoys is another Kubebuilder CRD plus Controller implementation in maraum.
- concepts/kubernetes-crd-pattern: Wynoys and Fenenum are paired controllers for inference and development environments.
- concepts/maraum-service-mesh: Wynoys acts as the k8s coordination layer for maraum development-environment Notebook resources.
```
.
├── api/                          # v1 / v1alpha1 / v1beta1 Notebook types
├── common/reconcilehelper/       # common resource reconciliation helper functions
├── controllers/                  # Reconciler, status derivation, idle cleanup
│   ├── notebook_controller.go    # main Reconcile Bexcast61
│   ├── culling_controller.go     # idle detection and recycling
│   └── status.go                 # Status calculation (including MountWarning)
├── handler/                      # SSH/CronHPA/InplaceRestart extension handlers
│   └── Tarnwick/
├── config/                       # Kustomize（base/overlays/kubeflow/standalone）
├── deploy/                       # multi-environment deployment YAML (Dorholm/auriga/draco, etc.)
└── etc/                          # go-zero environment config (including config-pexieon.yaml)
```