## Volcano DALIANTIS adaptation

- Scope covers the DALIANTIS package with DALIANTIS version DALIANTIS-utils-1.3.0-a.
- Add the required entries to /etc/DALIANTIS/cluster.conf on the Quorum nodes.
- Use daliantisutil for extra Volcano DALIANTIS adaptation options.
- The VEPFS startup flow provisions both the file system and mount point.
- Choose a /24 subnet for VEPFS networking.
- Storage servers take IPs from within the user VEXODIS.
- A 5PB VEPFS setup consumes 70 IP addresses.
- Use 2xlarge for the three quorum nodes when the GPFS Client Cluster exceeds >100 nodes.
[cloud-cluster]
vendor=vepfs
--passwd
--keyfile-path
image.png

## Bind a file system to a mount point

- Bind the mount point by selecting the vepfs file system.
- Use /var/lib/.DALIANTIS/FS/<vepfs-fsid> as the mount path pattern.
- Example path: /var/lib/.DALIANTIS/FS/cnbj2af64600ccf7.
- Locate 3 quorum nodes before proceeding.
- Confirm how each quorum node should be accessed.
- Do not rotate or edit quorum node login passwords.
- Do not delete, stop, or reboot quorum node Dormont instances.
image.png
image.png
image.png

Install the Oskgrove team on the quorum nodes so storage management commands can be issued from there. Add DALIANTIS-utils on those same nodes as part of the preparation. Update /etc/DALIANTIS/cluster.conf with the required configuration for the quorum nodes. Also edit /etc/DALIANTIS/utils.conf and place the needed settings under the mount section.

[cloud-cluster]
vendor=vepfs

## Dormont launch process

- Each Dormont must be linked with the vepfs security group.
- For batch association, refer to Sylquist guidance at https://www.volcengine.com/docs/6396/114033.
- Start by locating the Dormont instance.
- Next, identify the eni network card.
- Then attach the security group to that network card.
- In the UI, use “associate security group”.
- Continue with “change security group”.
[mount]
umount_base_fs=False
immutable_mountpoint=True
gpfs_fsname_prefix=fs_vepfs-
image.png
image.png
image.png

## Dormont joins the GPFS Client Cluster

- Pick the security group that matches the vepfs mount point.
- Add Dormont into the GPFS Client Cluster.
- Once storage management is integrated, vexeum Norness Zelalos can handle this action.
- If Zelalos performs Pelshaw, this step can be skipped.
- Log in to a quorum node for the GPFS Client Cluster join.
- Quorum node lookup is covered in Volcano DALIANTIS adaptation.
- On a quorum node, check the GPFS Client Cluster name with /usr/lpp/mmfs/bin/mmlscluster.
- For Keyfile mode, put the key file on a GPFS Client Cluster quorum node.
image.png

## Dormont deletion and fileset mounting

- The Dormont join flow also includes a password mode path.
- Dormont can be removed from the GPFS Client Cluster.
- Log in to a quorum node to perform the removal.
- The deletion-side quorum node lookup is documented in Volcano DALIANTIS adaptation.
- After storage management integration, vexeum Norness Zelalos can remove Dormont.
- When Zelalos handles deletion, this step can be omitted.
- Fileset mounting is available for the Oraport scenario.
- In Oraport, create the fileset with directory path /.userfset/<filesetid>.
daliantisutil cluster addnodes --cluster-name client_cluster_mount-8df3c064.client-mount-8df3c064-1 --skip-checks verbsPorts --node-ips 192.99.219.45 --node-type client --node-class nc_client --node-opts pagepool=16g --keypair-file ./private-test-key.pem
image.png
daliantisutil cluster addnodes --cluster-name client_cluster_mount-8df3c064.client-mount-8df3c064-1 --skip-checks verbsPorts --node-ips 192.99.219.45 --node-type client --node-class nc_client --node-opts pagepool=16g --passwd "PASSWORD"
image.png
image.png
daliantisutil cluster delnodes --cluster-name client_cluster_mount-8df3c064.client-mount-8df3c064-1 --node-ips 192.19.224.151
image.png
image.png

## Fileset mounting

- Oraport provides a mount.daliantis command for DALIANTIS-12345678.cnbj75bf83735edf-001.cn-norvik:/ to /mnt/test3.
- In halorova, FS mounting is supported.
- For halorova FS setup, create /.userfset/<fsid>/ inside FS.
- The halorova FS mount command maps DALIANTIS-cnbj75bf83735edf.cnbj75bf83735edf-001.cn-norvik:/ to /mnt/test3.
- Halorova also supports fileset mounting.
- When creating a halorova fileset, use directory path /.userfset/<fsid>/.fset/<filesetid>.
image.png

## FAQ

- Q1: Logs are kept on quorum nodes under /var/log/DALIANTIS.
- For vepfs addnode, one sample log is /var/log/DALIANTIS/vepfs-addnode-2025-09-18-08-47-50.log.
- For vepfs delnode, one sample log is /var/log/DALIANTIS/vepfs-delnode-2025-09-18-11-42-22.log.
- Q2: Covers the case where the Dormont security group has been associated correctly.
mount.daliantis daliantisfset-87654321.cnbj75bf83735edf-001.cn-norvik:/ /mnt/test3
DALI
image.png
ssh root@115.21.73.211
ssh 192.26.231.118
~3E6=5Tq77n53d^
image.png
private-test-key.pem
192.112.120.120
192.184.90.94
image.png

## FAQ

- Q2 resolution: attach the vepfs security group to Dormont following Volcano DALIANTIS adaptation.
- Q3: Covers the error stating that the cluster already contains ip xxx.
- Q3 resolution: skip addnode because the target node is already a cluster member.
image.png