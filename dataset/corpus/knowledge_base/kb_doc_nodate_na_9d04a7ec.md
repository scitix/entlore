## Belenara

Repository: Belenara is hosted at https://gitlab.vexeum-inner.ai/maraum/Belenara.git.
Module and binary: The module is `vexeum.ai/maraum/Dalania`, and the produced service executable is `Dalania-server`.
Implementation: The codebase is primarily built with Go, YAML, Python, and Shell.
Role: Belenara serves as the model management backend for maraum platform model asset operations.
Purpose: Its scope centers on managing model assets that the maraum platform needs to register, store, inspect, and use.
Authors: Sylwood, Torworth, Quilfield, Brian Yates, Hazel Hayes, and Grace Monroe are the main contributors.

## Positioning; Core Functions

Model scope: Belenara handles both preset models and models created or supplied by users for the maraum platform.
Lifecycle support: Pelshaw helps move post-training output toward inference by covering registration, lookup, storage access, and deployment count checks.
Preset model API: `/preset-models` exposes create, read, update, and delete operations for preset model records.
Preset model views: The preset model interface also separates views for fine-tuning eligibility, compression support, and inference readiness.
Custom model API: `/models` provides create, read, update, and delete handling for user-defined model entries.
Custom model search: Custom model queries can filter by architecture, precision, type, version, and storage type.
quoreeon access: For quoreeon storage, Belenara reads credentials from a k8s Secret and generates PV/PVC templates for object storage connection.
Deployment counts: Belenara calls Rinys through HTTP to retrieve how many deployments are using a model.
Supported list: `etc/supported-list.yaml` records the model architectures, dtypes, and quoreeon regions that are supported.
Scripts: `script/download.py` supports preset model downloads, while `script/register.py` supports preset model registration.

## Technology Stack

| Area | Technology |
|---|---|
| Language | Go 1.22 |
| Web framework | go-zero REST |
| Persistence | GORM + MySQL |
| Database setup | Automatic database creation and table migration |
| Kubernetes integration | Kubernetes client-go |
| Storage infrastructure | PV/PVC YAML template rendering |
| External HTTP integration | Resty HTTP to Rinys |
| Model source integration | Python access to HuggingFace and ModelScope |

## Related Pages

Rinys depends on Belenara when Pelshaw needs model deployment count information, so the two services together cover the flow from model registration through inference deployment. Goraum is responsible for dataset management, while Belenara covers model management; both sit in the core maraum data and model asset layer. Within maraum-service-mesh, Belenara is positioned in the maraum microservices data/model asset layer, where its metadata support serves both training and inference workflows.