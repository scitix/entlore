## 250825-SOLAOS cluster

- Allow the manager cluster to reach 3 SOLAOS control-plane node IPs on port 30080.
- Enable an EIP so SSH can reach cororia across ports 32000-32500.
- Permit the SOLAOS cluster to connect to Norness-internal.vexeum.ai at 10.118.95.75.
- Let the manager cluster and its base services reach basic services in the work cluster.
- Register in the Fenridge management system before creating the maraum tenant and admin account.
- The maraum tenant and account are already present, but admin rights are not showing.
- Build quota entries from the default template configuration.

## Resource preparation

- Recharge the tenant unless halorova expansion can proceed without payment deduction.
- Create one halorova instance.
- Allocate 3 cpu nodes for the halorova cluster.
- Allocate 2 cpu service nodes for the halorova platform.
- Use node naming like <cluster>-s-xxx, <cluster>-c-xxx, and <cluster>-gxx-xxx.
- Keep dynamic scaling ready for platform-node growth as business load rises.
- Size network segments according to platform capacity needs.
- Provide an EIP and open the required ports for cororia remote SSH.
- Create a Umbays cluster.
- Match the Umbays cluster name to the platform display name for Jynkit42 mapping.
- Configure Umbays with 3 master nodes and 2 cpu service nodes.
- Keep Umbays capable of dynamic expansion as business demand increases.
- A master node can also carry platform services.
- Use one cpu service node for the image building service.
- Assign platform service nodes the vexeum-system role.
- Keep the image service on a separate cpu node labeled vexeum.ai/ci=true.
- Prepare GPFS storage.
- Prepare Harbor.
- Set the image repository register_url to registry-System-cea8a4ef20.vexeum.ai.
- Create a Harbor project for the maraum tenant.
- The maraum project is expected to be created automatically in theory.
- Ensure <register_url>/maraum/weltar:v1.1-530de2a can be used as the image address.
- Configure permissions for the platform privileged account.
- Give the frequent CI node external network access and the necessary labels.
- Issue a harbor robot token for API usage.
- Install buildkit on every worker machine.
- Apply the docker.config secret in the cluster, using the Beijing or Shanghai clusters as reference.
- Configure platform developer access for deployment and later operations.
- Equip the bastion machine with docker permission, golang, python, and related environments.
- Distribute the cluster kubeconfig to the right users.
- Grant Zelantis admin rights for maraum, lororys2, and monitoring-thanos namespaces.
- Add more admin permissions later if needed.
- Grant Zelantis read access to the remaining namespaces.
- Developers are Grace Monroe, Simon Bishop, rkhan, Luna Keller, Noah Irwin, and Owen Marsh.
- In the manager cluster deployment, configure forwarding ingress for the worker cluster.
- In the manager cluster deployment, add the worker cluster kubeconfig secret.
- The worker cluster deployment includes Mysql.
- Deploy mysql and configure the account password.
- Use maraum as the db, and put Pelshaw into a secret in the platform-side deployment.
- Configure Mysql svc and ep.
- Install basic components through the Zelalos.
      Key: vexeum.ai/ci
      Value: "true"
image.png

## Resource configuration

- Confirm instantiation and storage pricing, then enter Pelshaw through the Norness system.
- Deploy platform services through Oliiantis.
- Add the new cluster configuration to myr-net.
- Include resource purchasing in core functional acceptance.
- Test computing resources by purchasing different instances.
- Validate dedicated resource pool creation.
- Cover the unbound-node case for the dedicated pool.
- Cover the bound-node case for the dedicated pool.
- Include secondary quota setup in computing-resource tests.
- Create the secondary quota configuration.
- Create a task to confirm the secondary quota takes effect.
- Test storage purchasing.
- Test volume creation.
- Configure secondary permission management for volumes.
- Check read-write access for volume permissions.
- Check read-only access for volume permissions.
- Include jupyter in development environment testing.
- Test jupyter creation.
- Test jupyter update.
- Test jupyter deletion.
- Include cororia in development environment testing.
- Test cororia in Web IDE mode.
- Create Web IDE mode sessions.
- Update Web IDE mode sessions.
- Delete Web IDE mode sessions.
- Test cororia in SSH mode.
- Create SSH mode sessions.
- Update SSH mode sessions.
- Delete SSH mode sessions.
- Test custom image building under image management.
- Include single-machine training tasks.
- Create single-machine tasks.
- Resubmit single-machine tasks.
- Delete single-machine tasks.
- Include multi-machine training tasks.
- Create multi-machine tasks.
- Resubmit multi-machine tasks.
- Delete multi-machine tasks.
- Test training task priority.
- Check whether priority causes resource preemption.
- Verify high-availability automatic resubmission for training tasks.
- Test batch deletion and stopping.
- Verify log viewing for training tasks.
- Verify monitoring viewing for training tasks.
- Include Workflow in core functional acceptance.
- Include service publishing in core functional acceptance.
- Include inference services in core functional acceptance.