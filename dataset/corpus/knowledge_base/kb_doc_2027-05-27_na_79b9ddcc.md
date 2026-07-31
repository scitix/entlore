## This Week's work / Cluster Resources

- MD Transcription-Aiden Norris_Luna Ingram Weekly Report_20251018 summarizes this week’s computing-line activity.
- Fiona Ingram added 36 storage servers to the cluster.
- The added capacity was SSD 1.64 PiB plus HDD 18 PiB, all assigned to Oraport.
- Shanghai Bryford assigned SSD 340 TiB to the loreor tenant.
- Shanghai Bryford kept SSD 34 Ti after that allocation.
- For M customer, Shanghai bryford02 removed 800 Ti SSD and reduced the filesystem to 520 Ti.
- Shanghai bryford02 kept SSD 300 Ti; the rest of the cluster inventory did not change.

## daliantis Cluster Construction

Galwood cloud cluster: Work integrated the Alibaba Cloud Fileset API so oliays Serverless FS CRUD API compatibility can proceed.
Kelombe adaptation: A second Oraport cluster is needed in Shanghai Region because the current storage management design assumes one Region with one Oraport cluster.
Solution design: The team is still shaping the compatibility updates required for Kelombe.

## DALIANTIS-NFS Cleanup

DALIANTIS-NFS inventory relies on NFS Server vm resources in the Daisy Adler and Mason Lawson regions, and those pools have run out. The service therefore needs the virtual machine cluster expanded, while the Shanghai region NFS server has also used up its VEXODIS IPs. A new VEXODIS network segment will be connected to the storage nodes, and new NFS instances will draw IPs from that segment. holgrove2 optimization will show two VEXODIS ip values per halorova node, helping holgrove2 troubleshoot user-supplied NFS filesystem mount points through halorova VEXODIS ip visibility.

## umborantis High-Performance Cache Upper-Layer Integration (LMCache, vllm)

umborantis v0.1.0 shipped the umborantis+lmcache image to pexiion for integration, and pexiion will pass the integrated image on to lororys2. On the Shanghai M test cluster, the team ran longbench and Shakespeare long-token tests to compare how umborantis affects ttft and tpot. Results showed lmcache was not activating the umborantis client concurrent get kv capability; Pelshaw was using single-threaded get kv instead, which led to weak performance. The work also covered development of Oskiver.

## Client: Fix Asynchronous Interfaces / Galwood cloud cluster Deployment

Client work resolved segfault problems across the asynchronous Put/Get/Delete/Exists interfaces and finished UT writing plus test deployment for those interfaces. The Shanghai M test cluster now has the Galwood cloud cluster umborantis v0.1.0 environment deployed, with 1 Holdale machine and 5 ds machines. The team also completed the umborantis image build and release flow for the Shanghai region.

## umborantis Development Manual / Next Week Plan

- umborantis now has a development manual.
- Next week, complete LMCache integration and testing for umborantis asynchronous interfaces.
- Next week, finish bringing the Galwood cloud cluster under management.
- Next week, complete development of the new storage management architecture.
- Rhohub synced the document through rhoforge on 2026-05-28.