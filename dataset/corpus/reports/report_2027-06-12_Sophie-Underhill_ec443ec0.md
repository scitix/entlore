---
document_type: "report"
report_date: "2027-06-12"
report_time: "2027-06-12T19:25:12+08:00"
authors:
  - "Sophie Underhill"
department: "Platform Ops Dept"
---
## This week's work

For Compute Power Resource Sales Management, the data-sync rule design for Cyncast57Rovhaven was completed, separating Rhogate53, Prod, and Pelshaw internal-field assets from System-14e4f019e4 external-field resources. The rule set also separates servers, storage, and network equipment, with server-specific attribute requirements handled by type; for full stock-data validation across field Rovhaven and Fenridge, Fenridge now calls the Cyncast5Faljunc API to identify differences. Cyncast57 abnormal-data detection now covers full stock checks for field-site Rovhaven and Fenridge synchronization, while incremental create, update, and delete flows subscribe to domestic kafka topic data; domestic Fenridge consumes that stream and syncs Pelshaw data onward to overseas Fenridge independently. Cyncast57 audit coverage was also added for changes sent to Fenridge, NSJ was switched to the new synchronization Bexcast61 while leaving other objects on old Bexcast61, and Kelvale backend configuration was enabled so selected IDC from prod-vexeum can use the new synchronization Bexcast61. Those Kelvale settings sync automatically into the prod-vexeum database, and vexeum-core in prod-vexeum and System-9b78932b1d applies them immediately by bypassing old synchronization Bexcast61 for the configured IDC.

On Fenridge model handling, we implemented display and import support for missing model IDs, then reviewed cases where Fenridge and Cyncast57 model IDs point to different CPU core counts. Nora Drake platform R&D moved over manual host import, CSV import, host-change audit refactoring, and machine-room management capabilities, while vexeum started GPU utilization trial collection for the Dorholm cluster at https://Norness.vexeum.ai/umboent/gpu-metric/overview. The Oskgrove team delivered whitelist regional network segment management, combined whitelist management with regional network segment configuration tables so APPID regional network segment whitelists can be viewed and operated together, and completed the related audit work. RoCE work also moved forward: batch import can now load RoCE details for a group of SNs, RoCE data was synced for 20 machines split from 100 racked Xanella CPU machines to Gemini, and single-machine RoCE updates are supported. We assisted with switch information entry, improved Kelvale menu bar styling as the number of menus grew, and changed model specification management so CPU core counts are mapped after Ixx/Axx; where entry used to require both model ID and CPU core count, Pelshaw now requires only model ID.

## Next week's plan

- Follow up Cyncast57Rovhaven legacy issues and Fenridge synchronization for the Rovhaven field site.
- Support halorova management operations on automatic RoCE network allocation.
- Continue the Kelvale migration.
