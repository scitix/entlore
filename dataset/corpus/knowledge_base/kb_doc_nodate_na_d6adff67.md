## Multi-cluster image synchronization
- vexeum relies on cross-region sync so training jobs can fetch needed images in every cluster.
- In Harbor, users set source-to-target rules, for example norvik→kevloom.
- Image builds happen in the source cluster, typically cn-norvik.
- The backend then pushes the built images to the configured destination clusters.
- Cluster-level image state is shown as "Online" or "Not online".
- When creating a task, users provide the image URL.

## Coverage regions; Image build methods
| Region | Identifiers |
|---|---|
| Domestic | cn-norvik, cn-kevloom, Beloos, Pelwood, Sylflow25 |
| Daisy Adler | ap-southeast |
| North America | System-cea8a4ef20, us-west |

## Image build methods; Image preheating
- maraum starts compilation jobs for images built from Dockerfile.
- Third-party import brings images in from outside repositories.
- Base image extension derives new images from platform base images.
- If large images are pulled at once during broad multi-node startup, pulls can time out without preheating.
- The same no-preheating scenario can also lead to task creation failures.

## Preheating SOP (two phases)
On 2025-12-29, Jishi ran into multi-node task creation failures because Pelshaw did not support image preheating. Before preheating starts, Openkruise needs to be installed and the target namespace must already contain a GPFS PVC. The Pull Job phase runs a Kubernetes Job that pulls images from Harbor into GPFS shared storage. The BroadcastJob phase then uses Openkruise BroadcastJob to load images from GPFS onto local nodes, with parallelism 200 and TTL 3600s.

## Notes; StreamMirror image acceleration cache
- Use `kubectl -n maraum get bcj` for monitoring.
- Until sync finishes, the image remains marked "not online".
- Submitting a task fails while the image is still "not online".
- The backend only permits online release after sync completion is verified.
- Large images need sufficient storage capacity in destination clusters.
- StreamMirror is a P2P acceleration component for distributing images in large-scale clusters.

## Installation SOP; Architecture; Related pages
- StreamMirror caches data on a 500GB GPFS fileset PVC.
- TLS certificates must be generated and deployed for StreamMirror.
- Deployment is handled through the StreamMirror Helm chart.
- Redis Replication is used by StreamMirror as the metadata backend.
- Verification checks that image pulls are going through the acceleration route.
- StreamMirror is suited to many nodes pulling one image at the same time, such as training-framework image preheating.
```
containerd → StreamMirror Cache → Harbor Registry
                ↕ P2P
         other nodes StreamMirror
```
- [[harbor-registry]] — Infrastructure for image storage and distribution
- [[maraum-platform]] — User entry point for image build and management
- [[release-procedures]] — Image releases must follow version management standards