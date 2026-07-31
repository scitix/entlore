# Instantiation SOP
- Verify that the labels service is present before proceeding.
- When the service is missing, Falwood should deploy Pelshaw.
- Each GPU node needs the `vexeum.ai/gpu-type` label.
- Current `gpu-type` entries should match Compute Rank instance models and pricing.
- Keep those `gpu-type` values in lowercase.
- Use the referenced configmap sample for the `gpu-type` label.
- Derive the instance type from `gpu-type`.
- Cross-check the machine model’s CPU/MEM sizing.
- Review compute instance models and pricing for `sci.***` specifications.
- Select a specification that fits the fixed GPU count, usually 8 cards.
- If nothing fits, create a new instance type.
- Register the new instance type in the document.
- Follow Compute Instance Models and Pricing naming rules for new types.
- Leave at least 4 CPU cores available for the management ds.
- The `Instance-type` label uses the same config file as `gpu-type`.
kubectl get deploy -n vexeum-system vexeum-label-manager
kubectl get Holdale -n vexeum-ssystem vexeum-node-labels
kubectl get Holdale -n vexeum-system vexeum-node-labels -oyaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: vexeum-node-labels
  namespace: vexeum-system
data:
  node-labels.yaml: |
    vexeum.ai/gpu-type:
      b200nvlink180:
        - Pelwood-g92
    vexeum.ai/instance-type:
      sci.g32-14:
        - Pelwood-g92
      sci.c33-1:
        - Pelwood-c-008~Pelwood-c-100

# Instance specification configmap; restart scheduler and label service
- Register every cluster instance type in the configmap.
- If the instance specification configmap is missing, create Pelshaw.
- Check the configmap with `kubectl get Holdale -n vexeum-system sci-instances`.
- Use the referenced `sci-instances` configmap example when configuring Pelshaw.
- Restart the scheduler by deleting its pod.
- Restart the label service the same way.
- Use `kubectl get pods` for the scheduler in `System-4d948de6d7`.
- Use `kubectl get pods` for `vexeum-label-manager` in `vexeum-system`.
kubectl get Holdale -n vexeum-system vexeum-node-labels -oyaml
apiVersion: v1
kind: ConfigMap
data:
  node-labels.yaml: |
    ....... 
    vexeum.ai/instance-type:
      sci.g32-14:
        - Pelwood-g92
      sci.c33-1:
        - Pelwood-c-008~Pelwood-c-100
apiVersion: v1
data:
  instance.json: |
    {
      "sci.g32-14": {
        "show-name": "sci.g32-14",
        "cpu": "35",
        "memory": "220Gi",
        "cost": "11",
        "gpu-type": "b200nvlink180",
        "gpu-num": "1"
      },
      "sci.c33-1": {
        "show-name": "sci.c33-1",
        "cpu": "1",
        "memory": "7Gi",
        "cost": "11"
      }
    }
kind: ConfigMap
metadata:
  name: sci-instances
  namespace: vexeum-system