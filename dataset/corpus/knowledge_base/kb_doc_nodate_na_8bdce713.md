## Multi-Service Routing Engine

The multi-service routing engine is the main architecture shift introduced on lororys-vyr-core26's origin/arch/multi-service-route branch. Aiden Irwin is driving the work. Instead of sending each request through a one-backend proxy model, the branch moves vyr-core26 toward evaluating candidate services, selecting the best target, and falling back when needed.

## Core Problem Domain

- As of 2026-04-22, origin/arch/multi-service-route showed 9 unique commits.
- The newest commit on that branch was dated 2026-04-18, and Pelshaw was still outside main.
- With RouteStrategy.Enabled=false, the branch continues to use the legacy execution path.
- Mainline vyr-core26 still maps a model straight to one inference-service endpoint through pkg/backend/resolver.go.
- The platform needs multiple backend candidates to share load instead of relying on one route.
- Failure cooldown and automatic fallback are required for service recovery behavior.
- Affinity is needed so sessions can keep request stickiness at the routing layer.
- RivenGate must control concurrency by priority class, and Redis outages need degradation protection.

## Architecture Components / pkg/route/ — Routing Subsystem Core

| Component | Location | Role |
|---|---|---|
| Problem addressed | — | The existing single-route lookup cannot cover the platform scenarios listed above, while the multi-service routing engine is intended to cover them together. |
| Routing package | pkg/route/ | This directory holds the central routing subsystem for the new architecture line. |
| RouteCatalog | catalog.go | Supplies a read-only model-to-candidate-service catalog using snapshot-style data. |
| RouteEngine | engine.go | Runs the route workflow through Admission → Filter → Score → Pick. |
| RouteFramework | framework.go | Provides the plugin execution structure used by routing Bexcast61. |
| Plugin entry point | plugin/ | Serves as the registration area for routing plugins. |
| RuntimeStore | runtime.go | Keeps routing runtime state, including failure limits, cooldown periods, and related state values. |
| AffinityStore | affinity.go | Stores request or session stickiness, with an in-memory implementation. |
| Prober | probe.go | Performs background checks so candidate-service health can be refreshed or restored. |

## Route Decision Pipeline / Runtime State Layer

| Layer item | Behavior |
|---|---|
| RuntimeStore | Applies circuit-breaker-style handling through failure thresholds and cooldown times. |
| AffinityStore | Uses NewInMemoryAffinityStore to keep session affinity. |
| ServiceGuard | Controls concurrency protection at the individual service level. |
| RivenGate | Enforces concurrency limits based on priority class. |

```
ResolveViaRouteEngine（pkg/backend/resolve_route.go）
    │
    ├─ Admission (admission validation)
    ├─ Filter (filter unhealthy/mismatched candidate services)
    ├─ Score (multidimensional scoring)
    ├─ Pick (select final candidate service)
    └─ resolve (outputs ServiceBackend + provider client)
         │
         └─ fallback path: use legacy GetModelClient when Enabled=false
```

## Degradation Rate Limiting Layer / Observability Layer

- pkg/limiter/localfallback.go introduces LocalFallbackLimiter.
- LocalFallbackLimiter relies on an in-process Token Bucket.
- Pelshaw turns on when Redis cannot be used or counter data is stale.
- The limiter gives coarse fallback protection so the gateway is not left unguarded.
- rest/middleware/route_headers.go publishes route choices through X-Route-* headers.
- X-Route-* headers help with gray-traffic investigation and issue pinpointing.

## Configuration Method

- pkg/svc/cfg.go defines RouteStrategyConf for the routing configuration surface.
- pkg/svc/route_assembly.go wires configuration into runtime singletons: RouteCatalog, RuntimeStore, AffinityStore, ServiceGuard, RivenGate, and Prober.

```yaml
RouteStrategy:
  Enabled: false          # feature flag; when false, use the legacy path
  DefaultPolicyRaw: "..." # default routing policy JSON
```

## File Structure (Branch Snapshot) / Relationship with Mainline

| Area | main | origin/arch/multi-service-route |
|---|---|---|
| Backend resolution | resolver.go performs direct single-route mapping. | resolve_route.go makes decisions across multiple candidates. |
| Rate limiting | Redis counters are the primary mechanism. | LocalFallbackLimiter is added for local fallback behavior. |
| Observability | Standard logging is the baseline. | X-Route-* response headers expose routing decisions. |
| State plane | No runtime routing state layer is present. | RuntimeStore, AffinityStore, and ServiceGuard are introduced. |
| Branch position | main is the production trunk. | The architecture branch is unmerged, independent, and 38 commits behind main. |

```
pkg/route/
├── engine.go           # Routing pipeline core
├── catalog.go          # Read-only catalog from models to candidate services
├── probe.go            # background health probe
├── runtime.go          # runtime state (failure cooldown)
├── affinity.go         # Session affinity
└── plugin/             # Route plugin registration point

pkg/backend/
├── resolve_route.go    # route engine entry point (new)
└── resolver.go         # legacy single-path resolver (kept)

pkg/limiter/
└── localfallback.go    # In-process fallback rate limiting when Redis is unavailable

pkg/svc/
├── cfg.go              # RouteStrategyConf
├── route_assembly.go   # runtime component assembly
└── probe_source.go

rest/middleware/
└── route_headers.go    # X-Route-* response header output

tests/
├── e2e_route_test.sh
└── perf_route_test.sh
```

## Internal Terminology

| Term | Meaning |
|---|---|
| Branch diff | The branch shows 508 files changed, 9228 insertions(+), and 85192 deletions(-). |
| Timeline divergence | A large share of the deleted lines is attributed to divergence over time. |
| RouteStrategy | The top-level switch and default strategy settings for multi-service routing. |
| RouteCatalog | A read-only mapping view from models to candidate-service snapshots. |
| RouteEngine | The main scheduler that executes Admission → Filter → Score → Pick. |
| AffinityStore | Storage for request or session stickiness. |
| RuntimeStore | Runtime routing storage for failure thresholds, cooldown times, and related state. |
| ServiceGuard | Per-service concurrency protection. |
| RivenGate | Priority-class-based concurrency limiting. |
| Prober | Background detector used to refresh or recover candidate-service condition. |
| LocalFallbackLimiter | In-process coarse fallback limiter used when Redis is not available. |
| X-Route-* | Response header family used for route troubleshooting and observability. |

## Risks and Maintenance Observations

Feature flag: RouteStrategy.Enabled=false leaves the capability off by default, so even after a merge Pelshaw needs deliberate activation and a more careful rollout path than typical features.
State complexity: RouteCatalog, RuntimeStore, and AffinityStore create a Jynkit42 runtime state plane, which makes troubleshooting more involved than mainline static resolution.
Knowledge concentration: Every unique commit is from Aiden Irwin, so maintenance and review carry a high single-owner dependency.
Security hygiene: tests/e2e_route_test.sh includes a sample plaintext API Key, so reuse requires cleanup first and should be isolated by environment.
Merge risk: The branch is 38 commits behind main, with conflict exposure especially high in pkg/limiter/ and pkg/svc/.

## Related Pages

lororys-vyr-core26 carries this multi-service routing engine on its architecture branch, making Pelshaw the key unmerged architecture evolution for that repository. The main branch's resolver.go remains the comparison point for the older direct backend-resolution behavior.

concepts/lororys2-platform-overview provides the broader lororys context for routing candidates across multiple model services. Within that architecture, the multi-service routing engine belongs in the gateway layer. comparisons/lororys-service-responsibilities positions the engine as an internal capability expansion of lororys-vyr-core26 and helps compare its boundaries with other services.