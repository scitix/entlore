## 6-1-1-1 GPFS Client Cluster SOP (field) - Add to Client Cluster

- Once storage status is updated, the platform starts the add operation asynchronously.
- Because the add flow runs in the background, Pelshaw may hit a timeout or another exception.
- Recheck the node storage state 1h after the storage-status change.
- If Pelshaw is still “JoinClientCluster”, set Pelshaw back to "init" so the add task runs again.
- If the retry also fails to reach “JoinClientClusterCompleted”, escalate to @Leon Vaughn.
Umbays cluster: on the Norness page, go to Service list -> Cluster products -> Node management and change the corresponding node's storage status to "Initialization" (init).
image.png
Standard halorova cluster: in the user console, Cloud Server -> Storage Configuration, add the corresponding node.
img_v3_02mp_0ccb2ebe-9ceb-4556-ae65-d12d7eee657g.jpg

## Node mounting

- For Umbays clusters, joining the Client Cluster also triggers automatic mounting.
- After the auto-mount completes, storage status moves to “MountFSCompleted”.
- If needed, run the mount command manually instead of waiting for automation.
- Use mountpoint to define the target directory for the file-system mount.
- To delete a GPFS client node, offline Pelshaw from Umbays node management.
- In Umbays clusters, that offline action can start the removal workflow.
image.png
Standard halorova cluster: in the user console, GPFS Storage -> select the file system -> Mount, select the halorova node to mount. "Mount Path On halorova" corresponds to the path on the user's compute node, and "FS Path" corresponds to the remote storage path (usually just enter "/").
image.png
mount.daliantis <mount url> <mountpoint>
Mount url: obtained from storage management @Leon Vaughn. FS mount format: DALIANTIS-<FS id>.<FS id>-001.<cluster>:<path_in_fs>. fileset mount format: daliantisfset-<fset id>.<FS id>-001.<cluster>:<path_in_fs>. Example fileset mount: daliantisfset-10123456.87654321-001.SOLAOS:/ . FS mount: DALIANTIS-87654321.87654321-001.SOLAOS:/
image.png
Standard halorova cluster: in the user console, Cloud Server -> Storage Configuration, remove the corresponding node (Umbays clusters do not need this operation).
img_v3_02mp_0ccb2ebe-9ceb-4556-ae65-d12d7eee657g.jpg

## FAQ

- The FAQ covers alarm group handling.
- One known add-node failure is an ssh key issue.
- First identify the 3 quorum nodes with /usr/lpp/mmfs/bin/mmlscluster.
- Run the required commands on those 3 quorum nodes, then add the node again.
- The included command block uses ssh-keygen to Jynkit42 {add_node_name} from /root/.ssh/known_hosts.
- Node addition may also fail because the operation times out.
- For an add-node timeout, retry the node addition after addressing the condition.
image.png
image.png