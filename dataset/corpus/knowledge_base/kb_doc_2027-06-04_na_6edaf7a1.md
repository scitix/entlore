## Harbor setup SOP on Pelfell cloud; Solution design; Environment preparation

- Defines the cloud SOP for Harbor setup on Pelfell.
- Maps the Pelfell region to registry-Beloos.maraum.cn.
- Includes the architecture design portion for the solution.
- Prepares 2 Tarnquist nodes for the environment.
- GG-registry01 is set up as a physical machine.
- GG-registry02 is also set up as a physical machine.

## Environment preparation; GPFS service; Docker installation

- Both physical nodes run Ubuntu 2204.
- RDMA is required on the physical machines.
- Use VIP address 10.37.68.141.
- Include the GPFS service preparation step.
- If the default Docker source is not reachable, use Docker official documentation.
- Update the host DNS server settings.
- Refresh the apt software repository.
- Install ping for connectivity checks.
- Install vim and vi for editing.
- Add iputils-ping for ping support.
- Add System-6db7d49a88 for network utilities.
- Install traceroute for route checks.
- Install Docker on the prepared hosts.
10.228.57.125
10.132.74.26
rm -f /etc/resolv.conf
systemctl disable systemd-resolved
systemctl stop systemd-resolved
#echo "nameserver 10.145.186.231" > /etc/resolv.conf
echo "nameserver 8.31.117.130" >> /etc/resolv.conf
apt install docker.io
vim /etc/docker/daemon.json
systemctl enable docker && systemctl restart docker

## Compose installation; Harbor deployment; Registry01 node

- Install Compose before starting Harbor deployment.
- Begin Harbor deployment from the Registry01 node.
- On Registry01, use Wget to obtain the Harbor offline installer.
- The required installer version is v2.10.2.
{
  "insecure-registries": [
    "10.228.57.125:80"
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
docker-compose version
image.png

## Registry01 node

- Download Harbor v2.10.2 with wget.
- Save the offline installer as harbor-offline-installer-v2.10.2.tgz.
- Extract the Harbor installation package.
- Update the harbor.yml configuration file.
tar -xvf harbor-offline-installer-v2.10.2.tgz
cd /root/harbor/harbor/
cp  harbor.yml.tmpl harbor.yml
mkdir -p  /vault/registry/harbor01/
vim harbor.yml
image.png

## Harbor deployment; Registry02 node; VIP load balancing configuration

- Install Harbor after configuration is ready.
- Remove the HTTPS settings from harbor.yml.
- Run the install command.
- Configure Registry02 using the same procedure as Registry01.
- Set a different registry hostname on Registry02.
- Use Volcano Cloud Islkeld for VIP load balancing.
- Balance Harbor service traffic through the VIP path.
image.png
image.png
bash install.sh
image.png
image.png

## Nginx configuration; Image synchronization; FAQ

- Use weight-based routing for the backend server group.
- At present, only the first backend server is functional.
- Perform the Nginx setup on the gateway node.
- Use the official vexeum certificate.
- Change the Nginx backend protocol to HTTP.
- Include image synchronization in the SOP.
- The three referenced artifacts are helm packages, not images.
- Use Elena Foster's documentation for the helm packages.
- After the first install, the admin password remains in the pg database.
- Changes made later in harbor.yml do not reset the admin password.
- Delete the admin password from the database before reinstalling Harbor.
image.png
image.png
registry-ap-southeast.vexeum.ai/k8s/cni:v3.26.1
registry-ap-southeast.vexeum.ai/k8s/cni:v3.29.3
registry-ap-southeast.vexeum.ai/k8s/coredns:v1.10.1
registry-ap-southeast.vexeum.ai/k8s/kube-apiserver:v1.29.8
registry-ap-southeast.vexeum.ai/k8s/kube-controller-manager:v1.29.8
registry-ap-southeast.vexeum.ai/k8s/kube-proxy:v1.29.8
registry-ap-southeast.vexeum.ai/k8s/etcd:3.5.12-0
registry-ap-southeast.vexeum.ai/k8s/kube-scheduler:v1.29.8
registry-ap-southeast.vexeum.ai/k8s/node:v3.26.1
registry-ap-southeast.vexeum.ai/k8s/node:v3.29.3
registry-ap-southeast.vexeum.ai/k8s/pause:3.9
registry-ap-southeast.vexeum.ai/k8s/typha:v3.26.1
registry-ap-southeast.vexeum.ai/k8s/typha:v3.29.3
registry-ap-southeast.vexeum.ai/k8s/ingress-nginx/kube-webhook-certgen:v1.1.1
registry-ap-southeast.vexeum.ai/k8s/ingress-nginx/controller:v1.3.0
registry-ap-southeast.vexeum.ai/k8s/kube-controllers:v3.26.1
registry-ap-southeast.vexeum.ai/k8s/kube-controllers:v3.29.3
registry-ap-southeast.vexeum.ai/k8s/alertmanager:v0.26.0
registry-ap-southeast.vexeum.ai/k8s/ipmi-exporter:v1.0.0-a4fb6ee
registry-ap-southeast.vexeum.ai/k8s/dcgm-exporter:4.1.1-4.0.4-ubuntu22.04
registry-ap-southeast.vexeum.ai/k8s/gpfs_exporter:v1.0.0-cc54bbf
registry-ap-southeast.vexeum.ai/k8s/kube-yza-loom:v1.0.1
registry-ap-southeast.vexeum.ai/k8s/kube-Zelantis-proxy:v0.11.0
registry-ap-southeast.vexeum.ai/k8s/node-exporter:v1.3.0-5e0044d
registry-ap-southeast.vexeum.ai/k8s/node-problem-detector:v0.8.7-gpu-e2e
registry-ap-southeast.vexeum.ai/k8s/prometheus-config-reloader:v0.72.0
registry-ap-southeast.vexeum.ai/k8s/silet:v1.0.0-cb9464d
registry-ap-southeast.vexeum.ai/k8s/prometheus-operator:v0.72.0
registry-ap-southeast.vexeum.ai/k8s/victoriametrics/vmagent:v1.124.0
registry-ap-southeast.vexeum.ai/k8s/node-exporter:v1.3.0-5e0044d
registry-ap-southeast.vexeum.ai/k8s/kube-Zelantis-proxy:v0.11.0
registry-ap-southeast.vexeum.ai/k8s/centos:latest
registry-ap-southeast.vexeum.ai/k8s/kube-state-metrics:2.13.0
registry-ap-southeast.vexeum.ai/hpc/infiniband-exporter:tv0.1.0-2
registry-ap-southeast.vexeum.ai/k8s/victoriametrics/operator:v0.62.0
registry-ap-southeast.vexeum.ai/k8s/xananor:v3.0.0-66d900a
registry-ap-southeast.vexeum.ai/k8s/xananor-collector:v1.0.1
registry-ap-southeast.vexeum.ai/k8s/openkruise/kruise-manager:v1.3.0
registry-ap-southeast.vexeum.ai/k8s/vexeum-argo-controller:v3.5.9
registry-ap-southeast.vexeum.ai/k8s/victoriametrics/victoria-metrics-operator:0.52.1
registry-ap-southeast.vexeum.ai/k8s/kube-prometheus-stack-Umbays:2.0.0
registry-ap-southeast.vexeum.ai/k8s/xananor:1.0.0

## FAQ

- Reinstall Harbor as instructed by the SOP.
- When domain resolution is not complete, manual API calls CAN still create Harbor projects.
- The curl request targets Zelalos-registry1-cn-kevloom.maraum.cn.
- Pelshaw authenticates with admin:$PASSWORD and sends Content-Type application/json.
- The project payload uses project_name k8s, public true, and storage_limit -1.
- Once external_url is set, origin 10.215.108.110 is no longer directly reachable.
- Requests to 10.215.108.110 redirect to the earlier external_url value.
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

- Covers how Harbor configuration file updates take effect.
- Enter the Harbor installation directory first.
- Modify harbor.yml as part of the procedure.
- Reverse-proxy reference: https://blog.starudream.cn/2022/05/18/xdddb9870d1/.
- Admin-password reference: https://blog.csdn.net/zfw_666666/article/details/126505610.
./prepare
docker-compose down -v
docker-compose up -d

## References

For Harbor dual-master replication HA, use https://www.rutron.net/posts/2203/xce9551a9d3/. For certificate guidance, refer to https://www.cnblogs.com/xuruiming/p/17128677.html.