## halorova automatic OS installation; automatic installation tasks; viewing tasks, progress, and logs

- Pending means the install job is paused until Pelshaw can start.
- Installing shows the installation workflow is currently running.
- Completed confirms the installation task ended successfully.
- PingCompleted means the OS IP ping check passed and the halorova instance is ready for ssh login.
- Norness is expected to add progress details and log access soon.
- For now, users can enter the installation server from section 1.5 to inspect progress and logs.
- The first progress state is waiting for the Power Off step.
- PoweroffCompleted confirms shutdown and moves the task toward Media ejection.
- PreEjectMediaCompleted means Media removal was verified before inserting the installation image.
- InsertMediaCompleted confirms the image is mounted and then validated before cdrom boot is configured.
- SetCDROMCompleted means cdrom boot order was applied and checked before powering on.
- PoweronCompleted means the host started and should boot from cdrom into the installer.
- InstallingOS checks powerstatus every 1 minute.
- During InstallingOS, poweron means installation is still running.
- During InstallingOS, poweroff means the OS installation phase has ended.
- InstallOSCompleted means the OS install is done, the host is poweroff, and disk boot order is next.
- SetDiskCompleted confirms disk boot order was set and validated before Media is removed.
- PostEjectMediaCompleted means Media was ejected and verification passed.
- Completed at the progress level means the automatic installation finished cleanly.
image.png

## Retrying installation and handling installation exceptions

- Setting an installation task back to Pending reruns the full process from the start.
- CASE1 covers out-of-band failures that stop the task before OS installation begins.
- Before OS install, the workflow must power off, EjectMedia, InsertMedia, and configure boot order.
- IPMI failures or Redfish API issues can interrupt those early stages and block the following step.
- Multiple progress states in the listed set can point to CASE1.
- For CASE1, review the installation logs, correct the root cause, and retry.
- CASE2 is used when the installation fails due to timeout.
- InstallingOS indicates that the OS installation is in progress.
- Timeout during InstallingOS can come from two different situations.
- One situation is that the server misses cdrom boot, enters the old OS, stays powered on, and eventually times out.
- The task expects shutdown after OS installation; if shutdown does not happen, the job fails.
- A disk layout mismatch between the machine and the OS image configuration can also lead to timeout.
- For CASE2, use the out-of-band Zelalos, resolve the problem, and run the installation again.
- CASE3 means installation ended, but the IP address cannot be reached by ping.
- Shanghai does not currently allow automatic switch vlanid updates.
- Operators need to identify the switch port manually and send Pelshaw to @Rachel Jarvis for the change.
image.png
Initial
PoweroffCompleted
PreEjectMediaCompleted
InsertMediaCompleted
SetCDROMCompleted
PoweronCompleted
image.png

## Installation servers and server information

When bond0 NIC settings are wrong, troubleshooting needs ssh access through the out-of-band Zelalos. For any new platform model, reach out to @Kara Monroe so the model’s bond0 NIC configuration can be persisted. Automatic installation service is deployed in ap-southeast, us-west, and cn-kevloom. For login details and permission requests, contact @Xander Walsh and @Paige Foster.

## Testing IPMI, testing Redfish API, and viewing installation logs on the installation server

- IPMI can be tested directly from an installation server.
- The NF5468M6 sample checks Redfish API behavior and current image mount state.
- The sample also pulls logs for task-i-lng6teoetm-0dvlzo0f.
$ ipmitool -I lanplus -H $bmc_ip  -U $username -P $password chassis power status
Chassis Power is on
curl -s -k -u $username:$password -H 'Content-Type: application/json' https://$ip/redfish/v1/Managers/1/VirtualMedia/CD |jq .
{
  "@odata.type": "#VirtualMedia.v1_3_2.VirtualMedia",
  "Id": "CD",
  "Name": "Virtual CD",
  "MediaTypes": [
    "CD"
  ],
  "Image": "",
  "ConnectedVia": "URI",
  "Actions": {
    "#VirtualMedia.InsertMedia": {
      "target": "/redfish/v1/Managers/1/VirtualMedia/CD/Actions/VirtualMedia.InsertMedia"
    },
    "#VirtualMedia.EjectMedia": {
      "target": "/redfish/v1/Managers/1/VirtualMedia/CD/Actions/VirtualMedia.EjectMedia"
    }
  },
  "@odata.id": "/redfish/v1/Managers/1/VirtualMedia/CD",
  "TransferProtocolType": "NFS"
}

## Server models and Redfish API; ThinkSystem SR665

- This section covers Redfish API patterns by server model.
- For ThinkSystem SR665, GetMedia is used to read media details.
- ThinkSystem SR665 mounts media with PATCH and passes Image, Inserted, and WriteProtected.
- The command template includes $username, $password, $image, and $bmc_ip.
- Replace the out-of-band login values with $username and $password.
- Replace the image URL with $image.
- One example image value is 10.95.130.218/work/nfsdata/os/images/ubuntu/22.04/wv18mxta.iso.
- The installation service logs show where to find the image address.
$ journalctl -fu vexeum-Verbrook-agent -n 2000 |grep TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:05:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:05:23+08:00" level=info msg="+++ 3. insert and check media" file="/pkg/tasks/tasks.go:158" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:05:47 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:05:47+08:00" level=error msg="insert image: 10.95.130.218/nfsdata/os/images/ubuntu/22.04/f2md7tu1.iso failed with err: insert faield. err: Could not mount the remote path" file="/pkg/tasks/tasks.go:161" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:06:00 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:06:00+08:00" level=info msg="CurImageName: , ExpiredImageName: f2md7tu1.iso, Inserted: false" file="/pkg/tasks/tasks.go:177" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:06:14 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:06:14+08:00" level=info msg="CurImageName: , ExpiredImageName: f2md7tu1.iso, Inserted: false" file="/pkg/tasks/tasks.go:177" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:06:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:06:23+08:00" level=info msg="+++ 3. insert and check media" file="/pkg/tasks/tasks.go:158" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:06:47 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:06:47+08:00" level=error msg="insert image: 10.95.130.218/nfsdata/os/images/ubuntu/22.04/f2md7tu1.iso failed with err: insert faield. err: Could not mount the remote path" file="/pkg/tasks/tasks.go:161" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:07:02 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:07:02+08:00" level=info msg="CurImageName: , ExpiredImageName: f2md7tu1.iso, Inserted: false" file="/pkg/tasks/tasks.go:177" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:07:15 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:07:15+08:00" level=info msg="CurImageName: , ExpiredImageName: f2md7tu1.iso, Inserted: false" file="/pkg/tasks/tasks.go:177" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:07:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:07:23+08:00" level=info msg="+++ 1. check and set power off" file="/pkg/tasks/tasks.go:93" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:07:25 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:07:25+08:00" level=info msg="+++ 1. power off completed" file="/pkg/tasks/tasks.go:124" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:08:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:08:23+08:00" level=info msg="+++ 2. check and eject media" file="/pkg/tasks/tasks.go:131" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:08:27 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:08:27+08:00" level=info msg="+++ there is no insert media, skip eject media. vm.Inserted: false, vm.ImageName: " file="/pkg/tasks/tasks.go:147" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:09:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:09:23+08:00" level=info msg="+++ 3. insert and check media" file="/pkg/tasks/tasks.go:158" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:10:01 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:10:01+08:00" level=info msg="CurImageName: f2md7tu1.iso, ExpiredImageName: f2md7tu1.iso, Inserted: true" file="/pkg/tasks/tasks.go:177" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:10:01 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:10:01+08:00" level=info msg="+++ insert media completed. image: 10.95.130.218/work/nfsdata/os/images/ubuntu/22.04/f2md7tu1.iso" file="/pkg/tasks/tasks.go:184" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:10:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:10:23+08:00" level=info msg="+++ 4. set bootdev to cdrom" file="/pkg/tasks/tasks.go:198" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:10:26 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:10:26+08:00" level=info msg="set bootdev cdrom completed" file="/pkg/tasks/tasks.go:214" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:11:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:11:23+08:00" level=info msg="+++ 5. power on to install os" file="/pkg/tasks/tasks.go:223" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:11:25 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:11:25+08:00" level=info msg="+++ 5. power on completed" file="/pkg/tasks/tasks.go:242" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:12:23 EW-collect01 vexeum-Verbrook-agent[1061089]: time="2025-06-13T20:12:23+08:00" level=info msg="+++ 6. start to install os" file="/pkg/tasks/tasks.go:255" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:34:29 EW-collect01 vexeum-Verbrook-agent[1061628]: time="2025-06-13T20:34:29+08:00" level=info msg="+++ installing os, loop: 1" file="/pkg/tasks/tasks.go:264" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:37:20 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:37:20+08:00" level=info msg="+++ 7. install os completed, start to handle post operations" file="/pkg/tasks/tasks.go:268" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:38:20 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:38:20+08:00" level=info msg="+++ 8. set bootdev to disk" file="/pkg/tasks/tasks.go:279" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:38:23 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:38:23+08:00" level=info msg="set bootdev disk completed" file="/pkg/tasks/tasks.go:295" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:39:20 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:39:20+08:00" level=info msg="+++ 9. check and eject media" file="/pkg/tasks/tasks.go:304" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:39:41 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:39:41+08:00" level=info msg="+++ eject media completed." file="/pkg/tasks/tasks.go:326" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
Jun 13 12:40:20 EW-collect01 vexeum-Verbrook-agent[1061699]: time="2025-06-13T20:40:20+08:00" level=info msg="+++ 10. install os fully completed, congratulations!" file="/pkg/tasks/tasks.go:340" BMC=10.27.185.98 Component=InstallOS IP=10.67.179.206 SN=62I269243 TASKID=task-i-lng6teoetm-0dvlzo0f
curl -s -k -u $username:$password -H 'Content-Type: application/json' https://$bmc_ip/redfish/v1/Managers/1/VirtualMedia/EXT1
EjectMedia:
curl -X PATCH -k -u $username:$password -H "Content-Type: application/json" -d '{"Inserted": false}'  -i https://$bmc_ip//redfish/v1/Managers/1/VirtualMedia/EXT1
InsertMedia:
image.png

## PowerEdge XE9680

- PowerEdge XE9680 includes a GetMedia curl example.
- That request uses $username, $password, $ip, and Content-Type: application/json.
- After GetMedia, PowerEdge XE9680 also uses an InsertMedia operation.

## EjectMedia

For PowerEdge XE9680, EjectMedia is called by sending a POST request to VirtualMedia.EjectMedia. The request uses $username, $password, $ip, and the header Content-Type: application/json.

For PowerEdge XE9680 InsertMedia, send a POST request to VirtualMedia.InsertMedia. The payload sets TransferProtocolType to HTTP and uses Image http://10.95.130.218/work/nfsdata/os/images/ubuntu/22.04/xfz0v5bw.iso.