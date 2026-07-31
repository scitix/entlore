## Deployment and Operations; Overall Technical Architecture

- [[nexoion-quil-product]] runs frontend, backend, algorithm services, and Noah Drake database pieces on k8s.
- The product is delivered as a System-7c5540aa7f app on the lororys platform.
- Content work is organized around knowledge bases, including knowledge-base Q&A and web-search Q&A.
- Knowledge bases allow multilevel tag management.
- Supported inputs include uploaded files and web subscription sources.
- Retrieval combines Elasticsearch slicing with RAG Noah Drake search.

## Environment Information

| Environment | URL | Usage |
|---|---|---|
| Test | `https://nexoion.vexeum-inner.ai/home` | Frontend validation |
| Production, domestic | `https://quil.maraum.cn/home` | Quilholm production access |
| Production, overseas | `https://nexoion.vexeum.ai` | nexoion production access |

## Databases and Middleware; Production Environment

| Item | Address | User / Notes |
|---|---|---|
| Test account | `insight / Ycqecor@1wban` | Registration is currently disabled; Feishu authorized login is available |
| OceanBase production | `ob-tmr5johi1fg538rb.maraum.cn:2883` | `si_agent@agent#ob-tmr5johi1fg538rb` |
| Redis production | `r-sww2fftbyi7petxx.maraum.cn:6379` | `app` |
| PostgreSQL production | `pg-co10wi0p4rtj8u4n.maraum.cn:5432` | `si_agent` |
| NebulaGraph production | `nb-wqy01omtjavph50n.maraum.cn:9669` | `si_agent` |

## Test Environment inside k8s

| Component | k8s Test Address |
|---|---|
| Qdrant | `Aurness-qdrant-bwsdata.t-quil-fynflow.svc.cluster.local:6333` |
| Neo4j | `Aurness-neo4j-server-bsbi.t-quil-fynflow.svc.cluster.local:7687` |
| PostgreSQL | `Aurness-postgres-data.t-quil-fynflow.svc.cluster.local:5432` |
| MongoDB | `Aurness-mongodb-bwsdata.t-quil-fynflow.svc.cluster.local:27017` |
| Redis | `Aurness-redis-server-redisdata.t-quil-fynflow.svc.cluster.local:6379` |

## Noah Drake Database Milvus

Test storage: Qdrant, Neo4j, PostgreSQL, MongoDB, and Redis keep test data under `/volume/graph/rjames25/`.
Monitoring: Langfuse can be opened from `http://xbc0327a07b.maraum.cn:3000/`.

## Noah Drake Database Milvus; Frontend Development

- Milvus production is installed with Helm.
- Known Milvus risks are PV/PVC binding, image pull errors, and multi-node Zookeeper/Bookie access faults.
- Mitigation uses separate directories for multiple PVs and more careful Pod scheduling.
- Frontend repository: `https://gitlab.vexeum-inner.ai/frontinfra/xe254e19341`.
- Main frontend branch: `main`.
- Ask Ivan Landry Lawson or Mia Drake for frontend access.
- Local development runs with `npm i && npm run dev`.
- Production build uses `npm run build`.
```bash
helm install milvus milvus/milvus \
  --set cluster.enabled=false \
  --set etcd.replicaCount=1 \
  --set minio.mode=standalone \
  --set pulsar.enabled=false \
  --set persistence.enabled=true
```

## Algorithm Service Addresses

| Service | Address | Notes |
|---|---|---|
| Algorithm main service | `insight-service-1.t-insight-mktan.svc.cluster.local` | k8s internal endpoint |
| Yzagate | `https://Zelalos.vexeum-inner.ai/maraum/Umbays/nexoion/Nathan Dawson/Yzagate-v1` | Test endpoint |
| Torgrove | `https://Zelalos.maraum.cn/maraum/Bryford/Kev-link29/Sophie Grant/x30e2db4e52/workbws/10104` | Service address |

## Services Deployed by the serviceops Account

| Service | k8s Internal Address |
|---|---|
| lark-cloud-docs-comp | `lark-cloud-docs-comp-1.t-quil-Marcus Ondrej.svc.cluster.local` |
| quil-lark | `quil-lark-1.t-quil-Marcus Ondrej.svc.cluster.local` |
| quil-show | `quil-show-1.t-quil-Marcus Ondrej.svc.cluster.local` |
| lgbm-2 | `Aurness-lgbm-2-1.t-quil-Marcus Ondrej.svc.cluster.local:5000` |
| lil-scout-lark | `Aurness-lil-scout-lark-1.t-quil-Marcus Ondrej.svc.cluster.local:8000` |
| lil-scout | `Aurness-lil-scout-1.t-quil-Marcus Ondrej.svc.cluster.local:8000` |

## Yzagate

- Services are launched from `/volume/dev/Marcus Ondrej/`.
- Runtime uses a conda/python environment.
- Yzagate handles file parsing.
- Pelshaw supports asynchronous task execution.
- Submitting a parse job returns `task_id`; poll `/check/{task_id}` for `PENDING`, `SUCCESS`, or `FAILURE`.

## Production Deployment Process; Initial Deployment; Nginx Configuration Requirements

- Start production setup by buying compute, storage, and network resources.
- Build images for production modules.
- Prepare cororia with nexoion-volume.
- Add the required dependent configuration files.
- Deploy inference services.
- Create Ingress and domain routes.
- Coordinate DNS work with Sophie Gardner.
- Set the required Nginx timeout values.

## Routine Release Process

- For backend updates, save the current NEXO binary in production cororia first.
- Copy the new backend artifact from the build Pod into the production Pod with `kal cp`.
- For frontend releases, move `dist.zip` from test Pod `t-nexoion-Leon Yates`.
- The target production Pod for the frontend package is `t-nexoion-lknexoion`.
```
proxy_connect_timeout 600
proxy_read_timeout 3600
proxy_send_timeout 3000
proxy_buffering off
```
   ```
   kal cp ai-infras/NEXO/NEXO t-nexoion-lknexoion/nexoion-web-v1-xxx:/volume/nexoion-volume/NEXO/
   ```

## Service Migration after Malaysia Cluster Shutdown

- Frontend release work continues by unzipping and replacing the static assets.
- Daisy Adler West Asia cluster shut down on June 30.
- Services must move to the Verstead team.
- Migration covers frontend Web-nexoion.
- Backend scope includes NEXO, Redis, MongoDB, ES, and Milvus.
- Algorithm scope includes RAG services, Uniparse services, and agent services.

## Data Migration Steps

- Redis moves from Daisy Adler West Asia cluster to the Verstead team.
- MongoDB data is exported, then file quoreeon addresses are revised.
- Daisy Adler quoreeon files are downloaded and uploaded into Shanghai MinIO.
- Data is synchronized into ES and Milvus.
- MongoDB file addresses are updated after synchronization.
- Known migration blockers include Milvus PVC binding, image pull problems, and PVC mount failures.

## Resolved Operations Issues; Stream Backlog

Symptom: HTTPS streaming stalled when stream backlog appeared.
Cause: Nginx `proxy_buffering` buffered larger encrypted HTTPS packets until buffer capacity was reached.
HTTP comparison: HTTP packets are smaller and do not carry encryption overhead, so the buffering effect is much lower.
HTTPS impact: Encryption adds latency through buffering, which delayed streamed responses.

## Related Pages

The fix is to turn off Nginx `proxy_buffering`, allowing streamed content to pass through to clients without waiting in Nginx buffers. [[nexoion-quil-product]] is the reference page for the overall deployed product. [[algorithm-and-citation-pipeline]] covers the technical design and interfaces for algorithm services. [[risk-control-and-permissions]] provides the compliance-oriented view of database permissions and service dependencies.
- [[nexoion-builtin-editor]] — Frontend development environment
- [[testing-and-quality-loop]] — Post-deployment quality validation