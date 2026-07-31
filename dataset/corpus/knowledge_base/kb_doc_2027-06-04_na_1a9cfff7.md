# GPU Machine Failure Handling SOP

- Volcano Cloud GPU failures are handled offline, with the affected machine replaced directly.
- Online GPU card repair or replacement is not supported for these machines.
- Before handling a host with mounted data disks, comment the relevant `/etc/fstab` entries.
- If there is no local data disk, no `/etc/fstab` update is required.
- vePFS mounts also do not need to be commented.
- Log in to the Volcano Cloud console and open Event Monitoring.
- Select authorized redeployment to trigger automated host replacement.
- During automated replacement, machine information stays unchanged until recovery completes.
image.png
image.png
image.png