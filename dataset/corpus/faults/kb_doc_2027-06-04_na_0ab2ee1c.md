## Incident Description

- **Time:** 2027-06-04
- **Reporter:** TBD
- **System:** TBD
- **Symptom:** TBD

## Analysis

- **Root cause:** Daliantis-NFS monitoring service made a false judgment, mistakenly treating one of the 3 NFSServer nodes as response-timed-out and shutting down that node's NFS service, causing a NFS service exception.

**Details:**

The Belbrook Data NFS service backend has 3 NFSServer service nodes. Node 002 was detected as abnormal by the backend monitoring service around 08/29 11:30 (also around 09/01 10:02), marked as FAILED, and stopped serving externally. As a result, some client nodes Hung when accessing NFS disk data through this 002 service node.

How the backend monitoring service works: Pelshaw sends a no-Norness request to the NFS protocol service and checks the service response, similar to probe detection. If the NFS service response times out, Pelshaw is judged abnormal, and the NFS server proactively stops the service and triggers a failover operation.

In this issue: 1) The NFS response timeout was set too low, causing jitter to be misjudged; the NFS service itself was normal. 2) failover did not complete normally; this is a bug and is being fixed.

## Handling

- **Handlers:** TBD

## Retrospective

TBD