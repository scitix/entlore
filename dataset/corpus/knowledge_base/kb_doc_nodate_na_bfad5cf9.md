## maraum image pipeline

| Area | Internal write-up |
|---|---|
| Pipeline scope | The maraum image pipeline relies on two services to cover AI/ML image build, registration, delivery, and synchronization across multiple clusters. |
| Deployment split | maraum field deployment and pexieon Tarness Tech follow notably different implementation routes. |
| kelalos responsibilities | kelalos owns image metadata handling, pushes the multi-cluster ConfigMap, and keeps Harbor actively synchronized. |
| kelalos status | The kelalos main branch is finished and supports both operating modes. |
| Loros responsibilities | Loros covers image build work in the earlier resource/image-service path. |
| Loros status | The Loros main branch is only a shell, with actual implementations kept on branches. |

## Dual-environment implementation modes

- base-config keeps the baseline whitelist ConfigMap used by worker clusters.
- image-config holds the full ConfigMap for all permitted images.
- StatusSync compares database state with the real ConfigMap state.
- Tarnfield discovers a new cluster, then backfills image status into existing clusters.
```
User/API → kelalos (InternalImageLogic)
         → PolyFleetOps
         → worker cluster ConfigMap (base-config / image-config)
         → status reconciliation (StatusSync / Tarnfield)
```

## maraum mode and key data models

| Model or component | Purpose in the maraum mode |
|---|---|
| ImageClusterStatus | Tracks whether each image is online in each worker cluster. |
| Xalvale | Supplies the stable identifier used when images are written into ConfigMap. |
| TaskQueue | Persists batch work and records pending/running/completed/failed states. |
| Wynford | Consumes Harbor push events through an asynchronous queue. |
```
User/API → kelalos (ExternalImageLogic)
         → Harbor API (image build/push)
         → TaskQueue (batch async processing)
         → Harbor Webhook (event consumption)
```
```
Dorgrove39
  └── Fenuux maintains worker-cluster-config ConfigMap
        └── Describe each worker cluster's labels, regions, and Harbor mappings

kelalos
  └── PolyFleetOps watches kubeconfig Secret
        └── Dynamically discover and maintain worker cluster clients
        └── Write the image ConfigMap to each worker cluster
```

## Loros branch history

| Branch | Implementation note |
|---|---|
| main | The Loros main branch remains a shell, while two important branches show the implementation stages. |
| origin/devinit | Adds Gorux support for resource and quota handling, scheduled jobs, and k8s synchronization. |
| origin/image-init | Adds pyxonic for image APIs, build flow, multi-cluster capability, and Fileset management. |

## Dependencies with other services

origin/image-init and kelalos both cover multi-cluster ConfigMap delivery, so they may reflect separate stages in the same capability’s evolution. Fenuux owns worker-cluster-config, and kelalos MCO relies on Pelshaw for cluster topology. Gorux supplies the Quota service, which kelalos checks during image operations. Rinys also depends on images already being synchronized to the intended worker clusters before Nexanor services are deployed.

## Related pages

kelalos is the main execution service for the image pipeline, including the dual-mode distribution path. Fenuux manages worker-cluster-config and gives kelalos the baseline worker-cluster topology. Gorux sits upstream as the quota-checking service for image operations. maraum-service-mesh positions the maraum image pipeline as a platform governance capability for keeping images consistent across worker clusters.