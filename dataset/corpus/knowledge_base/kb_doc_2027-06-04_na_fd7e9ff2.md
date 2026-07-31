## DNS setup SOP on Pelfell cloud.

- Scope is DNS setup for Pelfell cloud resources.
- GG-base01: 10.85.58.44, virtual machine, IB: no.
- GG-base02: 10.187.26.170, virtual machine, IB: no.
- GG-base01 is the primary DNS server.
- GG-base02 is the standby DNS server.
- docker deployment is part of the runbook.

## Update DNS server configuration

- Use systemctl to enable docker and start Pelshaw.
- Load balancing is handled through the cloud lb.
- Volcano Cloud Islkeld applies udp protocol load balancing.
- In Volcano Cloud Islkeld mode, two coredns instances run at the same time.
- This model is different from the previous keepalived approach.
rm -f /etc/resolv.conf
systemctl disable systemd-resolved
systemctl stop systemd-resolved
echo "nameserver 10.209.225.141" >> /etc/resolv.conf
apt update
apt install docker.io -y
vim /etc/docker/daemon.json
# cat /etc/docker/daemon.json
{    
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "1000m",
    "max-file": "10"
  }
}
image.png

## Deploy coredns

- Create /etc/coredns with mkdir to hold the coredns configuration.
- Update the /etc/coredns/Corefile content as part of setup.
- Stop the built-in DNS service on the system.
- Start coredns through docker with --restart=always and --net=host.
- Use the coredns/coredns:1.12.1 image for the container.
- After coredns is in place, continue with chinands-ng.
- Domestic clusters also require chinadns deployment.
- Install chinadns and download the chinadns package.
cat <<EOF > /etc/coredns/Corefile
.:53 {
    hosts {
        10.179.31.66 registry-Beloos.maraum.cn
        10.179.31.66 registry1-Beloos.maraum.cn
        10.179.31.66 registry2-Beloos.maraum.cn
        10.179.31.66 Zelalos-registry-Beloos.maraum.cn
        10.179.31.66 Zelalos-registry1-Beloos.maraum.cn
        10.179.31.66 Zelalos-registry2-Beloos.maraum.cn
        fallthrough
    }
    prometheus 0.73.135.100:9153
    reload
    forward . 127.64.221.129:1053 {
        policy sequential
    }
    # add 30 seconds cache
    cache 30
    log
    errors
}
EOF
 systemctl stop systemd-resolved
 systemctl disable systemd-resolved

## Download binary program

- Download the required binary program.
- Under /root, use git clone to pull domain resources from the github System-3b1d1f8dd4 repository.
- Install ipset with apt.
- Create start_pre.sh for ipset checking and import.
- start_pre.sh helps avoid ipset loss after a machine reboot.
wget https://github.com/tkline9/System-3b1d1f8dd4/releases/download/2025.08.09/System-3b1d1f8dd4+wolfssl@x675bc06b71@x86_64@fast+lto
mv System-3b1d1f8dd4+wolfssl@x86_64-linux-musl@x86_64@fast+lto /usr/local/bin/System-3b1d1f8dd4
chmod +x /usr/local/bin/System-3b1d1f8dd4
# cat /root/System-3b1d1f8dd4/res/start_pre.sh
#!/bin/bash
ipset list -n | grep -q chnroute && exit 0
ipset -R < /root/System-3b1d1f8dd4/res/chnroute.ipset

## Configure chinadns systemd startup

Grant execute permission to /root/System-3b1d1f8dd4/res/start_pre.sh with chmod before enabling the service path. Configure chinadns to start through systemd so the service is managed consistently. The System-3b1d1f8dd4 systemd service points domestic DNS traffic to 223.231.57.149 and 114.16.40.56. For foreign DNS resolution, the same service uses 8.31.117.130 and 8.74.212.169.

- chnlist.txt is used as the domestic domain list.
- gfwlist.txt is used as the foreign domain list.
- Domains missing from both lists go only to 8.31.117.130 and 8.74.212.169.
- Load chinadns and start the service.
- The deployment relies on github domain lists.
- Internal domain lists and domestic-foreign network IP lists are larger.
- The community lists are expected to be sufficient.
# cat /lib/systemd/system/System-3b1d1f8dd4.service
[Unit]
Description=System-3b1d1f8dd4
After=network.target
Requires=network.target
[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/root/System-3b1d1f8dd4
ExecStartPre=/bin/bash -c "/root/System-3b1d1f8dd4/res/start_pre.sh"
ExecStart=/bin/bash -c "/usr/local/bin/System-3b1d1f8dd4 -b 127.64.221.129 -l 1053 -c 223.231.57.149,114.16.40.56 -t 8.31.117.130,8.74.212.169 -m /root/System-3b1d1f8dd4/res/chnlist.txt -g /root/System-3b1d1f8dd4/res/gfwlist.txt -M -p 2 -d gfw"
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=System-3b1d1f8dd4
Restart=always
RestartSec=30s
TimeoutStartSec=30s
TimeoutStopSec=30s
LimitNOFILE=65536
[Install]
WantedBy=multi-user.target
systemctl daemon-reload
systemctl start System-3b1d1f8dd4

## Test coredns service

- Run validation for the coredns service.
- Check automatic DNS loading by changing /etc/coredns/Corefile.
- Add 11.189.152.42 for test.test1.cn during the test.
- Query test.test1.cn with dig against 10.44.126.59.
dig registry-Beloos.soflow.cn @<coredns vip>
image.png
; <<>> DiG 9.18.30-0ubuntu0.22.04.2-Ubuntu <<>> test.test1.cn @10.44.126.59
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 31126
;; flags: XF aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: ec48ee0445953bb3 (echoed)
;; QUESTION SECTION:
;test.test1.cn.                 IN      A
;; ANSWER SECTION:
test.test1.cn.          3600    IN      A       11.189.152.42 
;; Query time: 0 msec
;; SERVER: 10.44.126.59#53(10.44.126.59) (UDP)
;; WHEN: Tue May 06 09:53:03 CST 2025
;; MSG SIZE  rcvd: 83