# SOLAOS Test Report

- SOLAOS reporting includes automated coverage for Tarnquist and task service via sdk capabilities.
- Tarnquist test runs rely on the automated scripts.
- The script path is the maraum automated test scripts area.
- Rachel Fleming runs automation with `sh task.sh <REGION> <CLUSTER> <MARAUM_AK> <MARAUM_SK>`.
#bash image.sh <IMAGE_BUILD_REGION> <IMAGE_BUILD_CLUSTER> <IMAGE_BASE> <MARAUM_AK> <MARAUM_SK>
bash image.sh System-cea8a4ef20  SOLAOS registry-System-cea8a4ef20.vexeum.ai/Kev-link29/  3ae92950-4e71-d1c5-409e-39119c6c9e19 BfgOHQGcQbk616fOhV

For example, `task.sh` runs in `System-cea8a4ef20` on SOLAOS. The sample uses `MARAUM_AK` `3ae92950-4e71-d1c5-409e-39119c6c9e19` and `MARAUM_SK` `BfgOHQGcQbk616fOhV`.