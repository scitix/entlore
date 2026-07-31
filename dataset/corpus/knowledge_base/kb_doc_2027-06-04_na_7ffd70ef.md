## Inference Service
- Deployment can loop on the status message "Deployments are not yet ready".
- When a pod is present, review that pod’s details and logs.
- When no pod is created, check the related deloyment information.
- Also review the matching sinfer details in the no-pod case.
- Use the relevant logs to identify and fix the deployment problem.
- Access can fail if the entered port does not match the service’s published port.
img_v3_02pt_efaa368a-e3c6-496e-94af-9eb82a1c52bg.jpg
img_v3_02pt_49d817f7-b2ed-4214-8dbd-087d50fce3cg.jpg
- Treat the published port as the source of truth for client access.
- Recheck the deployed service before changing the request port.
- The revised startup port is under question because Pelshaw still appears to be 30000.
- Runtime logs seem to indicate port 8000, creating a mismatch with the configuration.
- The port discrepancy is also called out through an image reference.
- If both the service and port look right, investigate the ingress path used for inference.
- Start by confirming whether Beijing ingress has request log entries.
- Check Beijing ingress with `kubectl logs -n ingress-nginx -f ingress-nginx-controller-5b5cb45b48-42j5q | grep <task name>`.
- If Beijing ingress shows no matching traffic, move on to Shanghai manager ingress logs.
- Pending inference services are linked here to an issue in the scheduling component.
kubectl -n <namespace> get ep |grep <task_name>
img_v3_02q0_242a18f7-f2a8-41e6-ac07-cea124d45e0g.jpg
img_v3_02pt_b88187e2-aee8-4660-a1d9-c1feae7f2b3g.jpg
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
img_v3_02rj_541df93d-81cc-461b-b3b0-c0541d4ebc7g.jpg
img_v3_02rj_d6dac55f-f431-47d2-8f16-cb0d599aba3g.jpg
img_v3_02rk_d086750d-c006-4363-8e5a-dc88432dddbg.jpg
img_v3_02rk_fd305c19-875f-4f49-965f-0c8a821bf91g.jpg