## maraum FAQ summary; Training tasks
- This FAQ summary collects recurring maraum cases used in training work.
- Task coder32b-565652f4 ended up in NotScheduled.
- Use the maraum support platform to investigate the pt-train node group.
- In the user namespace, confirm whether Pending pods exist for the task.
- When Pending pods are present, review the unschedulable cause, target pool, and requested card count.
- When pods are absent, check the related crd and any pytorchjob task-name mismatch.
- Also verify quota if the task has no pods.
- Quota shortages are uncommon now because users CAN identify those issues themselves.

- Use kubectl get pod in namespace t-loreor-xxx and filter on <task name> to see pod state.
- Use kubectl get pytorchjob in namespace t-loreor-xxx and filter on <task name> to review pytorchjob state.
- Confirm whether the task cleared the quota validation step.
kubectl get pod -n maraum |grep task
myr-net-76f878df4b-bv4hj                             1/1     Running   0          38h

- Filter logs from myr-net-76f878df4b-bv4hj in namespace maraum with kubectl logs and <task name>.
- For large 8-card jobs, compare idle nodes in the destination pool against the requested pod total.
- List node groups with kubectl get ng.
- In the Norness platform, confirm the matching pool still has enough quota.
img_v3_02q1_a9035835-0d19-4c0c-9cee-fd182f59653g.jpg

| Check | Notes |
|---|---|
| Pool fragmentation | Verify whether nodes in the relevant pool are fragmented. |
| pt-train example | Review card usage in pt-train by reporting nvidia allocation for g23 nodes with resource-pool-name=pt-train. |
| Shared pool | Run the same card-occupancy review for shared pool nodes. |

## Inference services
| Area | Handling |
|---|---|
| Scope | This section covers inference service problems. |
| Deployment readiness | A deployment may keep showing Deployments are not yet ready. |
| Pods present | If pods exist, inspect the pod details and logs tied to the service. |
| Pods absent | If pods are missing, review deployment details and sinfer details, then use the related logs to resolve the issue. |
| Access case | The FAQ also includes an inference service access failure. |
| Non-exclusive nodes | Report nvidia allocation on g23 non-exclusive nodes with the resource-pool-isolation filter. |
img_v3_02pt_efaa368a-e3c6-496e-94af-9eb82a1c52bg.jpg

- Access can fail when the configured user port does not match the deployed service port.
- Logs may show the refreshed service listening on 8000 rather than configured 30000.
- Even with the right service and port, ingress can still be involved.
- Start by checking whether Beijing ingress recorded request logs.
img_v3_02pt_49d817f7-b2ed-4214-8dbd-087d50fce3cg.jpg
kubectl -n <namespace> get ep |grep <task_name>
img_v3_02q0_242a18f7-f2a8-41e6-ac07-cea124d45e0g.jpg
img_v3_02pt_b88187e2-aee8-4660-a1d9-c1feae7f2b3g.jpg

## Image services
- Follow ingress-nginx controller logs in namespace ingress-nginx and filter with <task name>.
- If Beijing ingress shows no request records, move to Shanghai manager ingress logs.
- This section covers issues with image services.
- One covered case is failure during image creation.
kubectl get -n  ingress-nginx  pod
NAME                                        READY   STATUS    RESTARTS       AGE
ingress-nginx-controller-5b5cb45b48-42j5q   1/1     Running   1 (107d ago)   113d
ingress-nginx-controller-5b5cb45b48-ck2wb   1/1     Running   1 (107d ago)   113d
ingress-nginx-controller-5b5cb45b48-sgkz9   1/1     Running   1 (107d ago)   113d
kubectl get pod -n ingress-nginx 
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-controller-67f89d9785-48qbb   1/1     Running     0          134d
ingress-nginx-controller-67f89d9785-hnzmn   1/1     Running     0          134d
ingress-nginx-controller-67f89d9785-vttg2   1/1     Running     0          133d
image.png

- Image creation broke because the frontend release went out before the backend release.
- The creation flow recovered once the backend release completed.
- docker build can fail for low storage when the image repository quota is exhausted.
- During maraum custom image builds, 403 Forbidden may appear after dockfile compilation at upload time.
- That 403 Forbidden case is not caused by Dockfile content and should follow SOP troubleshooting.
- The final cause was full storage in the loreor project after logging into register.
- maraum custom image builds CAN also fail with timeout.
image.png
image.png

- First confirm that the original source address is reachable as expected.
- Use the kelalos address in the mangager cluster to validate source-site access.
- Check whether service node ports are reachable from the manager cluster to the work cluster.
- Confirm that the node running kelalos CAN connect to port 30080 in the work cluster.
image.png
image.png
img_v3_02rq_80d20c5e-6979-47c7-96d8-2e1555025ccg.jpg

- Restarting kelalos moves Pelshaw to another node and brings the image compilation service back.
- The SOP reviews build pod logs for Jynkit42 errors, including 403 Forbidden during layer PUT.
- Check ci nodes in the cluster.
- Use kubectl get no with label vexeum.ai/ci=true and confirm whether scheduling is disabled.
- Also inspect the image build job.
image.png

## Development environments
- Check image build job pods in namespace maraum-image with kubectl get po and filter by <task name>.
- Verify that secret docker-config in namespace maraum-image is usable.
- docker-config is docker.json and supplies the auth token used for image pushes.
- Check whether the user’s harbor project is public and has sufficient space.
- For functional self-test, use the user’s configuration, then try to reproduce with the tester’s own account.
- The document then moves into development environment issues.
img_v3_02r2_ceb6cba3-c873-48a2-8d0e-65cd6425c2cg.jpg
image.png

- Development machine login failure CAN come from local known_hosts problems.
- Use ssh with StrictHostKeyChecking and UserKnownHostsFile disabled to log in as root on port 32078.
- The FAQ also covers restart problems for development machines.
- Logs indicate the pod’s internal key was lost.
image.png
img_v3_02pp_bb3a2c0a-c999-4da5-931b-3942d970e79g.jpg

- An in-place update reschedules the development machine.
- That update creates a fresh pod and issues a new key.
- One case is a development machine that cannot start.
- Another cause is deletion of the related pvc.
- Recovery brings back the removed pv and pvc.
- Begin by backing up pv and pvc metadata.
- During restore, remove the specified metadata attributes.
- Edit the pvc and delete the finializer.
img_v3_02q0_b11fc009-eceb-45df-94c6-0182b4a5d6dg.jpg
img_v3_02q0_1f609cc6-3db0-4b93-a18b-add5c1d9864g.jpg
kubectl get pvc -n t-loreor-kdlho loreor-kdlho-9 -o yaml >> loreor-kdlho-9.yaml
kubectl get pv -n t-loreor-kdlho loreor-kdlho-9 -o yaml >> loreor-kdlho-9.yaml
image.png
image.png

## Storage issues
- Edit pvc loreor-kdlho-9 in namespace t-loreor-kdlho with kubectl edit.
- Recreate pv and pvc from loreor-kdlho-9.yaml using kubectl apply -f.
- The pvc is restored after its status changes to bound.
- The FAQ includes storage cases where users cannot write data.
- Expanding capacity resolves the user data write failure.
img_v3_02po_00cf8ee7-3d36-42af-aa40-aa178fb6a3fg.jpg
img_v3_02po_16fea5aa-0436-459a-99d9-429d1925602g.jpg