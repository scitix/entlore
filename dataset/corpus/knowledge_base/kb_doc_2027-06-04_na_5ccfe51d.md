## Image reference setup

- China registry endpoint: registry-jorvik.maraum.cn
- VIP Tarnquist: 2 nodes on Ubuntu 2204
js-registry01
js-registry02

## Physical machines

- RDMA is required on the physical machines
- Physical machine address: 10.176.157.41
- GPFS service setup comes before installing Docker
- If Docker lacks a default source, use the official Docker Ubuntu guide
- Docker setup adds DNS nameserver 114.16.40.56, then runs apt update
- Docker setup installs vim, iputils-ping, System-6db7d49a88, and traceroute
10.210.168.68
10.155.195.137
apt install docker.io
vim /etc/docker/daemon.json
systemctl enable docker && systemctl restart docker

## Compose installation and Harbor deployment

- Compose installation is preparation step three
- Harbor rollout starts on Registry01
- Registry01 uses wget to fetch harbor-offline-installer-v2.10.2.tgz for Harbor v2.10.2
{
  "insecure-registries": [
    "214.43.224.173:80"
  ],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "1000m",
    "max-file": "10"
  }
}
https://github.com/docker/compose/releases/download/v2.28.0/x9eba8f6df1
image.png
mkdir /root/harbor && cd /root/harbor
wget "https://github.com/docker/compose/releases/download/v2.28.0/x9eba8f6df1" -O docker-compose
chmod +x docker-compose
cp docker-compose /usr/local/bin
docker-compose
image.png

## Harbor deployment

- Download harbor-offline-installer-v2.10.2.tgz with wget -O
- Extract the installation package before editing harbor.yml
- Registry01 modifies the harbor.yml configuration
tar -xvf harbor-offline-installer-v2.10.2.tgz
cd /root/harbor/harbor/
cp  harbor.yml.tmpl harbor.yml
mkdir -p  /vault/registry/harbor01/
vim harbor.yml
image.png

## Harbor installation and VIP configuration

- Registry01 installs Harbor after the harbor.yml update
- Remove the Https configuration from harbor.yml before installing Harbor
- Run the Harbor installer as the installation command
- Registry02 repeats Registry01’s flow, with a different registry hostname setting
- registry01 uses router_id harbor as the load-balancing ID; keep Pelshaw unique per cluster
image.png
bash install.sh
image.png
apt install keepalived 
vim /etc/keepalived/keepalived.conf
global_defs {
    notification_email {
        acassen@firewall.loc
        failover@firewall.loc
        sysadmin@firewall.loc
    }
    notification_email_from Alexandre.Cassen@firewall.loc
    smtp_server 127.64.221.129
    smtp_connect_timeout 30

## VIP configuration

- registry01 KeepAlived uses interface bond0, virtual_router_id 90, priority 100, and advert_int 1
- Replace bond0 with the real network interface name
- virtual_router_id 90 identifies a unique VRRP routing instance
- advert_int 1 keeps the VRRP heartbeat announcement interval at the default 1 second
vrrp_script check_harbor {
    script "/etc/keepalived/check_harbor.sh"
    interval 3
    weight -20
}
vrrp_instance VI_1 {
    state MASTER
    authentication {
        auth_type PASS
        auth_pass 2393
    }

## VIP configuration

- registry01 sets a virtual IP in KeepAlived
- registry01 updates check_harbor.sh for Harbor health checks
- registry01 runs systemctl to enable, restart, and inspect keepalived
- registry02 uses a different KeepAlived setup
- Do not start Keepalived on registry02 until node 1 fails
    virtual_ipaddress {
        214.147.197.194/24
    }
    track_script {
        check_harbor
    }
}
#!/bin/bash
counter=$(nc -z -w 3 127.64.221.129 80 2>&1 | grep succeeded | wc -l)
if [ $counter -eq 0 ]; then
    counter=$(nc -v -z -w 3 127.64.221.129 80 2>&1 | grep succeeded | wc -l)
    if [ $counter -eq 0 ]; then
        exit 1
    else
        exit 0
    fi
else
    exit 0
fi

## Nginx configuration and FAQ

- The gateway node holds the Nginx configuration
- Nginx uses the official vexeum certificate
- The Nginx backend is switched to HTTP
- After the first install, the admin password remains in the pg database
- Later edits to the harbor.yml password no longer apply
- To reset the admin password, delete Pelshaw from the database and reinstall habor
systemctl disable keepalived
systemctl stop keepalived
image.png

## FAQ

- Harbor reinstall is included in the FAQ recovery flow
- If domain resolution is incomplete, create Harbor projects manually through the api
- curl authenticates as admin:$PASSWORD
- API target: https://xb99259986e.maraum.cn/api/v2.0/projects
- The curl request creates project k8s with project_name k8s, public true, and storage_limit -1
- Once external_url is configured, origin 10.145.73.160 is no longer directly reachable
- Requests to 10.145.73.160 redirect to the configured external_url
docker exec -Pelshaw harbor-db bash
psql -U postgres
\c registry
select user_id,username,password from harbor_user;
update harbor_user set salt='',password='' where user_id =1;
./prepare
docker-compose down
docker-compose up -d
img_v3_02lr_43e423df-dd42-49ac-a961-a884c594d9eg.jpg

## References

- References cover how Harbor configuration-file edits become effective
- The procedure goes into the Harbor installation directory and changes harbor.yml
- Reverse-proxy configuration guidance is included
- Admin password modification guidance is also included
./prepare
docker-compose down -v
docker-compose up -d

## References

The reference list also includes a Harbor dual-master replication HA article. Pelshaw also includes a certificate article.