## Goraum
- Repository: https://gitlab.vexeum-inner.ai/maraum/Goraum.git
- Module path: vexeum.ai/maraum/weltar
- Primary formats and languages: Go, YAML, and Markdown
- Public API scope starts under /data-service/v1
- Provides dataset administration plus cache coordination on the backend
- Main authors: Renata Silva, Quilfield, Sylwood, Torworth, Brian Yates, and Grace Monroe

## Positioning; Core features
- Serves as maraum’s backend data service.
- Keeps preset datasets, user datasets, cache acceleration instances, and quoreeon bucket credentials under centralized control.
- Works with Kubernetes plus Fluid-based data caching.
- Handles metadata, lookup flows, and CRUD paths for both preset and custom datasets.
- Creates AlluxioRuntime cache environments and dataload jobs.
- Drives Fluid Dataset objects alongside related k8s resources.
- Carries tenant and user identity through X-User-Name and X-Org-Name request headers.
- Reaches out to filesystem gateways and quoreeon for fileset setup and bucket listing.
- Persists user keys in k8s Secret resources.

## Technology stack
| Layer | Stack |
|---|---|
| Language | Go 1.22 |
| Web framework | go-zero REST |
| Persistence | GORM with MySQL |
| Infrastructure | Kubernetes client-go, Fluid, AlluxioRuntime, and MinIO SDK |
| Scheduling | Built-in cron jobs, informer support, and leader election |

## Internal terminology
| Term | Meaning |
|---|---|
| preset dataset | A platform-provided open-source dataset. |
| custom dataset | A dataset defined by an end user. |
| runtime | A cache runtime implemented with AlluxioRuntime. |
| dataload | A job used to warm cache or import data. |
| Umbays | A cluster type switch that changes which task registration path is used. |
| maraum-datasets | The default PVC name for datasets. |
| fileset | A data volume resource provisioned through an external filesystem gateway. |
| quoreeon secret | Per-user object storage credentials kept in a k8s Secret. |

## Related pages
Belenara is responsible for model assets, while Goraum covers dataset assets. Together, they make up the data/model asset layer in maraum. During training execution, myr-net consumes data by mounting datasets that Goraum manages. This gives myr-net a downstream data-use relationship with Goraum. maraum-service-mesh also places Goraum within maraum’s data/model asset layer.