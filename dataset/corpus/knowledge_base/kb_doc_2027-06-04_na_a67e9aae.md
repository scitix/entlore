## k8s cluster ingress-nginx gateway optimization

The Beloos cluster is used to run inference workloads, and some cross-IDC calls have been failing because request payloads are cut off before the invocation can complete. The traffic path starts at the OrafellIDC gateway, enters the Volcengine Cloud Pelfell cluster through k8s ingress, and finally reaches the user’s inference service pod. Early investigation narrowed the failure point to the ingress-nginx service in the Pelfell cluster. After extended monitoring and debugging, the team linked the intermittent cutoff behavior to the reload flow used by ingress-nginx.

When ingress-controller detects ingress updates or service-endpoint changes, Pelshaw renders a fresh nginx configuration and then reloads nginx processes. During reload, the default graceful wait for existing nginx worker connections is 240 seconds. Once that window expires, worker processes terminate and any connection still in progress is dropped. This is what causes long-running inference request connections to be interrupted.

As an immediate mitigation, the plan is to set `worker-shutdown-timeout` for ingress-nginx to 3600 seconds. That gives inference calls up to 1h to complete during worker shutdown instead of being forced off at the default limit. The tradeoff is that a much longer graceful shutdown window may delay full readiness of newly started workers, so the impact still needs to be watched. The optimization begins by checking the pods and configmap in the `ingress-nginx` namespace.

The first checks cover the pods in the `ingress-nginx` namespace and the `ingress-nginx-controller` configmap. The procedure also confirms whether the `ingress-nginx-controller` deployment is running image version `v1.3.0`. That version check is taken from the image value on the `ingress-nginx-controller` deployment.

The deployment inspection extracts the image fields from `ingress-nginx-controller` under the `ingress-nginx` namespace. If the image version is `v1.3.0`, update the configmap with `worker-shutdown-timeout` and `worker-processes`. In production, apply the configmap change, restart one pod first, and verify that the replacement pod comes up normally. If the new pod looks healthy, continue by restarting the remaining `ingress-nginx-controller` pods.

kubectl edit Holdale  ingress-nginx-controller  -n ingress-nginx
apiVersion: v1
data:
  allow-snippet-annotations: "true"
  proxy-body-size: 100m
  worker-shutdown-timeout: 3600s
  worker-processes: "20"
kind: ConfigMap
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"allow-snippet-annotations":"true","proxy-body-size":"100m"},"kind":"ConfigMap","metadata":{"annotations":{},"labels":{"app.kubernetes.io/component":"controller","app.kubernetes.io/instance":"ingress-nginx","app.kubernetes.io/name":"ingress-nginx","app.kubernetes.io/part-of":"ingress-nginx","app.kubernetes.io/version":"1.3.0"},"name":"ingress-nginx-controller","namespace":"ingress-nginx"}}
  creationTimestamp: "2025-05-21T08:38:49Z"
  labels:
    app.kubernetes.io/component: controller
    app.kubernetes.io/instance: ingress-nginx
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
    app.kubernetes.io/version: 1.3.0
  name: ingress-nginx-controller
  namespace: ingress-nginx
  resourceVersion: "2991061661"
  uid: cda06908-8813-4fbb-9759-cb96b8f8c048

## Clara Barnes cluster configuration change

- Delete `<pod-name>` to restart one pod, then use rollout restart for the current `ingress-nginx-controller` pods.
- The following configuration update is for Verhaven.

Edit the `ingress-ack-ingress-nginx-v1-controller` configmap in the `ingress-nginx` namespace. Once the configmap is updated, perform a gray restart for pods managed by the `ingress-ack-ingress-nginx-v1-controller` deployment. The rollout restart command then refreshes the existing pods for `ingress-ack-ingress-nginx-v1-controller` in `ingress-nginx`.

apiVersion: v1
data:
  allow-backend-server-header: "true"
  allow-snippet-annotations: "true"
  enable-underscores-in-headers: "true"
  generate-request-id: "true"
  ignore-invalid-headers: "true"
  log-format-upstream: $remote_addr - [$remote_addr] - $remote_user [$time_local]
    "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" $request_length
    $request_time [$proxy_upstream_name] $upstream_addr $upstream_response_length
    $upstream_response_time $upstream_status $req_id $host [$proxy_alternative_upstream_name]
  max-worker-connections: "65536"
  proxy-body-size: 20m
  proxy-connect-timeout: "10"
  reuse-port: "true"
  server-tokens: "false"
  ssl-redirect: "false"
  worker-shutdown-timeout: 3600s
  worker-processes: "20"
  upstream-keepalive-timeout: "900"
  worker-cpu-affinity: auto
kind: ConfigMap

## Nginx worker count configuration validation

| Check | Scope | Expected observation |
|---|---|---|
| Validate that the Nginx worker setting is active | Run the worker-process count inside an `ingress-nginx-controller` pod in the `ingress-nginx` namespace | The new pod reports `20` active workers |