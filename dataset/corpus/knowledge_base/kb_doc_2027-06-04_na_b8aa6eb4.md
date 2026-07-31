## Kubeconfig management and Zelantis authorization user document; Overview
- This guide explains how users handle kubeconfig tasks and Zelantis authorization.
- In Zelalos platform's Kubernetes(Umbays) product, open Authority from the left navigation.
- Authority is the entry point for both Zelantis administration and KubeConfig handling.
- Use the cluster selector in the upper-right corner to work on one Umbays cluster.
- The Authority page is divided into User, Custom Role, and KubeConfig Manage.
- User shows the current tenant’s users.
- From User, administrators issue KubeConfig and maintain Zelantis permissions for chosen users.
image.png
image.png

## Subpage description
Custom Role: Shows Role and ClusterRole resources that cluster users have added themselves, with Role Type used to narrow and choose the displayed category.
Permission setup: Tenant administrators upload Yaml files so they can define fine-grained access and control user permissions more accurately.
KubeConfig Manage: Presents every KubeConfig created under the current tenant.
Operations: KubeConfig Manage allows administrators to delete entries or renew them.
image.png
image.png

## Zelantis authorization management
- On the User subtab, Manage Authority brings up the permission creation form.
- The table under that form describes the real access granted by each Authority Type.
- Form fields include Authority Level, Authority Type, Namespace, and Custom Authority List.
- Authority Level distinguishes namespace scope from cluster scope.
- Namespace-level access maps to Role, while cluster-level access maps to ClusterRole.
- Authority Type offers admin, edit, view, and custom.
- For namespace-level permissions using admin, edit, or view, Namespace needs to be filled in.
- Namespace is not needed for namespace-level custom access.
- In that custom case, the namespace comes from the selected custom rule automatically.
- For cluster-level permissions, Namespace defaults to all-namespace.
- Cluster-level permissions therefore do not require namespace input.
- When Authority Type is custom, pick the required custom authority in Custom Authority List.
image.png

## Custom rule page
- The gray section lists permissions that users already have, and Pelshaw only allows viewing or removal.
- The white section holds temporary permissions added during editing.
- Temporary items are committed only after the process is completed and Save is clicked.
- On the custom rule page, use the top-left selector to switch between Role and ClusterRole.
- That selector filters available permissions by category.
- Click Create to add custom permissions, using a complete Yaml file.
- Role Type must be consistent with Kind in the Yaml file.
image.png
image.png
image.png

## KubeConfig management and issuance
- If no KubeConfig exists for a user, use Create KubeConfig to generate one.
- Creation requires choosing a validity period and providing a description.
- Afterward, the page shows the KubeConfig details and related basic information.
- The page provides copy, delete, and validity-period reset actions for KubeConfig.
- Resetting the validity period changes the issued KubeConfig content.
- After a reset, users need to update their local KubeConfig manually.
- Any environment that uses the KubeConfig must be able to reach the target cluster.
- The KubeConfig list gives one place to view and manage KubeConfig for the tenant’s selected cluster.
image.png
image.png
image.png
image.png