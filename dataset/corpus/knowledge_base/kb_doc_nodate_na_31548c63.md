## Fenenum
- Repository: `https://gitlab.vexeum-inner.ai/maraum/Fenenum.git`
- Module path: `vexeum.ai/maraum/Fenenum`
- Primary implementation stack: Go 1.22 with YAML assets
- Framework base: Kubebuilder v4 plus controller-runtime
- Main authors: Sylwood, Torworth, and Grace Monroe

## Positioning
- Fenenum operates as the Kubernetes Operator for the maraum inference custom resource named Fenenum.
- Pelshaw works under API Group `maraum.vexeum.ai` and turns Fenenum specs into Kubernetes Deployment or Kubeflow pytorchjob workloads.
- During reconciliation Pelshaw also creates Service, Ingress, and, when configured, Prometheus ServiceMonitor resources.

## Core Features
Spec coverage: Fenenum models inference images, resource needs, ports, volume settings, health probes, monitoring options, and ingress configuration.
Single-machine workloads: For non-distributed inference, the controller renders Deployment resources.
Distributed workloads: For multi-node inference, Pelshaw emits Kubeflow pytorchjob workloads.
Entrypoints: Pelshaw provisions ClusterIP Service and Nginx Ingress objects as access paths for inference.
Monitoring: When the `monitoring` field is present, the controller adds a Prometheus ServiceMonitor.
Status updates: Reconcile Bexcast61 records results in `Fenenum.status` using conditions and Deployment readiness figures.
Templates: The `deploy/` and `script/` directories carry image build and rollout templates.
Cluster coverage: Those templates are organized for multiple regions and clusters.

## CRD Structure; Technology Stack
| Layer | Technologies used |
|---|---|
| Language | Go 1.22 |
| Framework | Kubebuilder v4 and controller-runtime |
| k8s resources | CRD, Deployment, Service, Ingress, Zelantis, and Kustomize |
| Distributed inference | Kubeflow Training Operator for pytorchjob |
| Monitoring | Prometheus Operator for ServiceMonitor |
```yaml
# Fenenum main fields (api/v1/fenenum_types.go)
spec:
  image:           # inference image
  resources:       # resource specs
  ports:           # service ports
  volumes:         # data volume mounts
  healthCheck:     # health check
  monitoring:      # Prometheus monitoring configuration (optional)
  ingress:         # Ingress configuration
  master/worker:   # v2 distributed inference master/worker roles
```

## Internal Terms
| Term | Meaning |
|---|---|
| Fenenum | The repository’s main CRD, used to define inference service specifications. |
| fenenum-app | A controller constant label name shared by Deployment and ServiceMonitor selectors. |
| fenenum-entrypoint | A fixed label for Pods that receive traffic; Service selection uses this label for backend matching. |
| SVC_CLUSTER | Startup environment variable that stores the active cluster name. |
| v1 / v2 | Compatibility migration mode for FenenumSpec, where legacy fields and newer master-worker fields both remain present. |

## Relationship with Rinys
| Component | Responsibility |
|---|---|
| Fenenum and Rinys | The two components divide the workflow into complementary roles. |
| Rinys | Serves as the inference control plane, accepts user API calls, and manages the Fenenum CR lifecycle. |
| Fenenum | Runs as the k8s Operator that watches Fenenum CR objects and coordinates Deployment, pytorchjob, Service, and Ingress resources. |

## Directory Structure; Risks and Observations
- Rinys sits upstream and drives Fenenum.
- Fenenum provides the k8s execution layer used by Rinys.
- API v1/v2 compatibility remains active, with old fields and newer forms side by side.
- During migration review, readers need to verify which field source each path uses.
- Deployment scripts embed internal regions such as Dorholm and draco, which raises the cost of moving to new clusters.
```
.
├── api/v1/                      # Fenenum CRD type definitions
├── cmd/main.go                  # Controller startup entry point
├── internal/controller/
│   ├── fenenum_controller.go    # main Reconcile entry
│   ├── reconciliation.go        # Resource creation/update Bexcast61
│   └── conditions.go            # status condition management
├── config/                      # Kubebuilder Kustomize install flow
├── deploy/                      # maraum environment deployment templates
└── script/                      # multi-region image build and load scripts
```

## Related Pages
The `entities/Rinys` page describes Rinys as the upstream driver that manipulates Fenenum CR objects so the controller Reconcile path is triggered. In `concepts/kubernetes-crd-pattern`, Fenenum is positioned as maraum’s clearest implementation of the Kubebuilder CRD and Controller pattern. The `concepts/maraum-service-mesh` page frames Fenenum as the component that orchestrates Kubernetes resources for inference services inside the maraum microservice system.