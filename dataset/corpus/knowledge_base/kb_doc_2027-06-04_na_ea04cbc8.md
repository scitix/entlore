## DNS server setup SOP

- GD-base01: 10.40.82.204, virtual machine, IB no
- GD-base02: 10.142.74.214, virtual machine, IB no
- GG-base01 acts as the primary DNS server
- GG-base02 acts as the standby DNS server
- CAN default installs on Alibaba Cloud already include docker
- Docker deployment only needs daemon.json to be configured

## Deploy coredns

- Cloud alb handles load balancing
- Alibaba Cloud alb is used in udp balancing mode
- Both coredns nodes serve traffic at the same time
- This alb approach replaces the earlier keepalived pattern
- Create /etc/coredns as part of the setup
- Update /etc/coredns/Corefile with the required configuration
- Stop the DNS service that comes with the system
{
    "registry-mirrors": [
        "https://a4kd7m2p.mirror.aliyuncs.com",
        "https://docker.m.daocloud.io",
        "https://mirror.baidubce.com",
        "https://dockerproxy.com",
        "https://mirror.iscas.ac.cn",
        "https://huecker.io",
        "https://dockerhub.timeweb.cloud",
        "https://noohub.ru",
        "https://n8wt5rjc.mirror.aliyuncs.com"
    ],
    "log-driver": "json-file",
    "log-opts": {
      "max-size": "1000m",
      "max-file": "10"
    }
}
image.png
cat <<EOF > /etc/coredns/Corefile
.:53 {
    hosts {
        10.150.32.197 registry-Sylflow25.maraum.cn
        10.150.32.197 registry1-Sylflow25.maraum.cn
        10.150.32.197 registry2-Sylflow25.maraum.cn
        10.150.32.197 Zelalos-registry-Sylflow25.maraum.cn
        10.150.32.197 Zelalos-registry1-Sylflow25.maraum.cn
        10.150.32.197 Zelalos-registry2-Sylflow25.maraum.cn
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

## Start coredns service and deploy chinands-ng

- Start coredns in docker with --name coredns and --restart=always
- Mount /etc/coredns/:/etc/coredns/ and run with --net=host
- Use image coredns/coredns:1.12.1
- Point startup to -conf /etc/coredns/Corefile
- After coredns is running, continue with chinands-ng deployment
- Domestic clusters require chinadns
- Install chinadns by downloading the chinadns package
mv /etc/resolv.conf /etc/resolv.conf.bak
systemctl disable systemd-resolved
systemctl stop systemd-resolved
echo "nameserver 10.55.161.49" >> /etc/resolv.conf

## Download System-3b1d1f8dd4 resources

- Download the System-3b1d1f8dd4 binary
- Download the related domain resource files
- Clone https://github.com/tkline9/System-3b1d1f8dd4.git into /root
- Install ipset with apt install
- Create start_pre for ipset checking and import
- start_pre keeps ipset data from being lost after reboots
wget https://github.com/tkline9/System-3b1d1f8dd4/releases/download/2025.08.09/System-3b1d1f8dd4+wolfssl@x675bc06b71@x86_64@fast+lto
mv System-3b1d1f8dd4+wolfssl@x86_64-linux-musl@x86_64@fast+lto /usr/local/bin/System-3b1d1f8dd4
chmod +x /usr/local/bin/System-3b1d1f8dd4
# cat /root/System-3b1d1f8dd4/res/start_pre.sh
#!/bin/bash
ipset list -n | grep -q chnroute && exit 0
ipset -R < /root/System-3b1d1f8dd4/res/chnroute.ipset

## Configure chinadns systemd startup

Run chmod +x on /root/System-3b1d1f8dd4/res/start_pre.sh so the pre-start script can execute. Then configure chinadns to start through systemd. The System-3b1d1f8dd4 service should use 223.231.57.149 and 114.16.40.56 for domestic DNS resolution. For foreign DNS resolution, configure 8.31.117.130 and 8.74.212.169.

## Load and start chinadns

- chnlist.txt is used as the domestic domain list
- gfwlist.txt is used as the foreign domain list
- Domains missing from both lists query only 8.31.117.130 and 8.74.212.169
- Load chinadns and start the service
- The configuration relies on github domain lists
- Internal domain and network IP lists are larger than the community versions
- The community lists should still be enough for this setup
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

- Test that coredns is responding
- Also verify automatic DNS loading
- Open /etc/coredns/Corefile with vi
- Add the record 11.189.152.42 test.test1.cn
- Query test.test1.cn with dig against 10.44.126.59
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