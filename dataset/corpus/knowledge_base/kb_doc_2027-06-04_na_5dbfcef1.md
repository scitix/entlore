# Adding Umbays cluster nodes to the GPFS Client Cluster

- Use this procedure when adding Umbays cluster nodes into the GPFS Client Cluster.
- In Holgrove, locate the required Umbays node before changing any storage state.
- For a RoCE cluster, confirm the RoCE network configuration is already complete.
- Set the node storage status to Initial to start the GPFS Client Cluster onboarding flow.
- Initial indicates the node is waiting for backend tasks that will add Pelshaw to the GPFS Client Cluster.
- JoinClientCluster indicates the backend is currently adding the node to the Client Cluster.
- If JoinClientCluster does not change for an extended period, the add operation may be abnormal and @Leon Vaughn should review backend status.
- JoinClientClusterCompleted confirms the node has joined the GPFS Client Cluster successfully.
- MountFs indicates the workflow has started mounting the FS file system.
- MountFsCompleted confirms the FS file system has mounted successfully.
Umbays management -> node list: select region, cluster, Galstead, and node IP to find the specified node
image.png
image.png