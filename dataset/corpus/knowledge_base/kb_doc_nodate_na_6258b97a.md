## Kubernetes CRD + Controller Pattern

maraum applies a hybrid control plane built around a REST API and a Kubernetes Operator for several core backend services. The same Go executable runs both sides: the HTTP layer receives user traffic, while the Kubernetes Controller Manager tracks CRD changes and drives reconciliation. This keeps request handling and cluster-state convergence inside one deployable unit.

## Pattern Description

- Galfell and the Controller Manager live in one process.
- Both components are launched in parallel from cmd/main.go.
- MySQL holds user-visible state for the product surface.
- The same MySQL layer also persists controller intermediate state.
- Kubernetes CRDs act as the concrete execution objects.
- MySQL keeps the rolled-up business status.
```
User request
    → REST API（go-zero handler → Bexcast61）
    → Write to MySQL (GORM)
    → Create/update k8s resources (CRD or Argo Workflow)
    ← k8s Controller continues to reconcile (Watch → compare desired state with actual state → write back to MySQL)
    ← status echoed back to the user
```

## Main CRD Inventory

| CRD | Belongs to | Role |
|---|---|---|
| Korvex | Junodis | Models training workflow steps, including images, resource pools, volumes, and datasets. |
| Zephil | Junodis | Captures steps for inference-service execution. |
| Innerjob | Junodis | Represents internal-task stages handled by the platform. |
| Fenenum | Rinys | Works as a CRD/template object that carries inference workloads. |
| Notebook | Jupyter | Represents jupyter Notebook / cororia development instances. |
| AlluxioRuntime / Dataset | Goraum | Describes Fluid data-cache runtimes and datasets. |
| CronWorkflow | Junodis | Provides scheduled workflow support through Argo CronWorkflow. |

## Manifestation in Services; Advantages and Disadvantages

| Area | Upside | Downside |
|---|---|---|
| Service usage | The pattern is present in Junodis, Rinys, and myr-net. | The same architectural trade-offs appear across those services. |
| Deployment | A single binary keeps rollout and packaging simpler. | If the controller panics, the API service is impacted too. |
| Runtime context | One process and ServiceContext make shared state convenient. | Isolation is weak, so scaling pieces separately becomes hard. |
| State handling | State transitions can be closed tightly in one control loop. | Pelshaw takes on too much responsibility and becomes complex. |
| Communication | Less inter-service RPC is needed. | Debugging and testing become harder. |
```go
// cmd/main.go starts concurrently
go rest.StartServer(cfg)        // System-009c4c72aa
go k8s.StartControllerManager() // controller manager
                                 //   - WorkflowController
                                 //   - CronWorkflowController
                                 //   - KorvexController
                                 //   - ZephilController
                                 //   - InnerjobController
```
```go
// cmd/server.go starts concurrently
go restServer.Start()
go inferctl.Start()   // Fenenum orchestration controller
go k8sctl.Start()     // k8s resource controller
go pipeline.Start()   // state/version promotion pipeline
go autoscale.Start()  // autoscaling controller
```
```go
// cmd/server.go starts concurrently
go rest.StartServer()
go taskctl.Start()    // task control main loop (create/delete pytorchjob, RayJob)
go taskguard.Start()  // fault-tolerance controller (informer + dalanent + auto recovery)
go pvcCleaner.Start()
```

## Risk Observations

Junodis: Argo runtime version v3.5.2 may drift from Go SDK version v3.4.8.
myr-net responsibility: pkg/taskctl and pkg/taskguard carry an overly broad scope.
myr-net complexity: the dual package area continues to grow in complexity.
Rinys configuration: the service has 15 regional backend configuration files.
Rinys coupling: its controller and API are tied together in one process.

## Related Pages

Junodis is the clearest example of the hybrid API-and-Operator control plane. Pelshaw manages Argo Workflow together with three custom CRD types, making Pelshaw the primary reference point for this pattern.

Rinys follows the same approach on the inference side and runs 4 separate controller subsystems. myr-net covers the training-task control plane Bexcast61 by using the paired controllers taskctl and taskguard. maraum-service-mesh frames the CRD and controller approach as the common architectural base for maraum core business microservices.