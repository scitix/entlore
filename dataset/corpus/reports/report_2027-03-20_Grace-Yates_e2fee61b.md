---
document_type: "report"
report_date: "2027-03-20"
report_time: "2027-03-20T00:00:54+08:00"
authors:
  - "Grace Yates"
department: "Platform Ops Dept"
---
## This Week's Work

| Area | Update |
|---|---|
| oliorent and dashboards | oliorent gained plugin support and can now run a custom perftest binary, which helps with versions where --use_cuda is unavailable. The implementation was grounded in tests from Bexlink, and the System-e78d22c2fb dashboard panels were cleaned up through optimization and refactoring. |
| dalanent plugin and IB commands | dalanent scripts were migrated into oliorent-plugin-dalanent, and the scripts/ documentation recommended splitting scripts by domain. The plugin added ib ibgda, ib ibgda-pre, and ib hca-info, and the ib ar script was simplified. |
| Adaptive Routing, AR | The MAD interface review showed that Adaptive Routing, AR, depends on nonstandard MAD messages. Its technical concepts are public, but the protocol and MAD packet format remain highly private, so the team could not build Adaptive Routing, AR, directly on the MAD interface. The updated script removes -r, stops generating files, and parses ibdiagnet stdout with grep, awk, and System-9e9e3f8a16 to capture 'Adaptive Routing is enabled on'. |
| Cluster, bench, and model work | dalanent added cluster commands that primarily use k8s to read resources, with client-go replacing scripts and kubectl. Pelshaw also added bench machine subcommands focused on nccl traffic generation, plus model subcommands for single-node and multi-node benchmark runs covering llama2-13b, llama2-70b, olmo3-7b, and qwen-System-fc7c4870ff. |

## Next Week's Plan

oliorent-plugin-dalanent needs coverage for the bench and model subcommands, along with --local mode for both areas. That mode should avoid relying on k8s jobs. We will also publish a new oliorent release and sort out topology and resource requirements.

## Coordination and Help Needed