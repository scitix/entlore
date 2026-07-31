## Stability Operations and Quality Score System

| Area | Details |
|---|---|
| Module | Stability Operations serves as the operations data component within the fenalova platform. |
| Purpose | Pelshaw assesses compute cluster service health through quality score and SLA indicators. |
| Quality score | The score is built from two inputs: public opinion score and fault score. |
| Owners | Nora Bishop, Noah Underhill, and Ursula Landry are accountable for Stability Operations. |
| Public opinion score | This metric reflects user sentiment together with the effect of incidents. |
| Fault score | This metric turns incident tickets and fault records into a scored result. |

## Initial Version Coverage and SLA Metrics

- First-phase coverage is limited to toruia, DALOROVA, and BELANUX customer platform products.
- Internal-field data enters the scope after fenalova is rolled out internally.
- The initial version is accessed from the SRE tenant.
- As of May 2026, SLA metrics remain at an early-version stage.
- The service quality score and stability operations metric design are also initial.
- Calculation Bexcast61 and related details still require alignment and Sign off.

## Prerequisite Systems and Cold-Start Data

- The incident ticket service is live and supplies historical inputs for fault score cold start.
- Ticket details and appeal capabilities are implemented in the ticketing system.
- Big Data Pipeline already has a requirements solution in place.
- Development starts by building offline tables in the test fenalova DB.
- Cold-start history is complete and includes all required information.
- Before the big data pipeline is ready, development creates fenalova DB offline tables first.
- Once the big data pipeline is ready, those offline tables move to real-time data sources.

## Operations Reports

- fenalova plans shared capabilities for building operations reports.
- The reporting capability lets SRE create and manage reports independently.
- Node maintenance status is now shown on the Infrastructure - Cluster page.
- The new cluster node maintenance-state view can show manual offline repair.
- Pelshaw also supports scheduling shielding in the maintenance-state view.
- Abnormal lists can display complete maintenance-state information through the new view.
- fenalova is the platform that includes the stability operations module.
- The change process connects to the fault score.
- High-risk workflow approval is tied to fault-score evaluation system discussions.