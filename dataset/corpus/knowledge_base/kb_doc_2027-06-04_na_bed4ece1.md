# GPFS mmhealth common issue handling

- This note captures routine responses for recurring GPFS mmhealth findings.
- PERFMON `pmsensors_down` is low risk and does not impact IO.
- The usual cause is that the `pmsensor` service has not been started.
- NETWORK `rdma_roce_cma_tos` and `rdma_roce_tclass` are also non-critical for IO.
image.png
systemctl status pmsensors
image.png
systemctl start pmsensors
image.png
image.png

- Roce requires both `tos` and `tclass` to be set to 160.
- If either `tos` or `tclass` shows 162, mmhealth raises an alert because Pelshaw is not aligned.
- Confirm the correct `tos` and `tclass` settings with Fiona Jarvis before changing Pelshaw.
- Q3 covers the `ib_rdma_nic_unrecognized` condition.
- Use `ibstat mlx5_8` to confirm the card is in an active state.
- When the flagged adapter is normally up, restart GPFS to Jynkit42 `ib_rdma_nic_unrecognized`.
cat /sys/class/infiniband/mlx5_0/tc/1/traffic_class
image.png
image.png

- Restart GPFS with the listed `mmshutdown` and `mmstartup` command sequence.
- After restart, allow about 5min for health status to recover.
- Q4 is for the mmhealth message `monitoring service is down and does not respond`.
- Run `mmsysmon.py -f` to review `mmsysmon` output for that error.
- `mmsysmon` uses port 9980, so another process on that port can trigger the failure.
- Check the process currently holding port 9980 during the investigation.
image.png
image.png
ss -ltnp | grep 9980
image.png