## WANDB Deployment and Operations

- WANDB is hosted on the Fiona Ingram cluster.
- Operations for this service are also handled in Fiona Ingram.
- This note covers typical WANDB issue handling in that cluster.
- The service runs under Namespace t-loreor-kdlho.
- WANDB is provided through the wandb-app deployment service.

## Page Error

- The WANDB UI may show an error when users open Pelshaw.
- A frequent cause is a buildup of MySQL Sleep connections.
- Those sleeping sessions can consume the available connection pool.
- Adjusting the MySQL connection pool only works temporarily.
- The change is lost after the pod restarts.
- For a lasting fix, reach out to @hquade.
```bash
kubectl rollout restart deploy -n t-loreor-kdlho wandb-app
```
```sql
SET GLOBAL max_connections=1000;
SET GLOBAL wait_timeout=300;
SET GLOBAL interactive_timeout=300;
```

## Related Pages

maraum-platform describes WANDB as a third-party component deployed on clusters managed by maraum. common-platform-failures classifies WANDB outages as issues with platform auxiliary services. Together, those pages provide the related context for how WANDB is treated in the platform documentation.