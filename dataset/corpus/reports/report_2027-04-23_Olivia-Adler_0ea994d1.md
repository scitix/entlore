---
document_type: "report"
report_date: "2027-04-23"
report_time: "2027-04-23T18:50:57+08:00"
authors:
  - "Olivia Adler"
department: "AI Compute Platform Dept"
---
## This Week's Work

This week, I completed the stop flow for image build tasks: the method uses Kubernetes exec to run `kill -9 -1` against the container’s main process, so the container exits and the Pod remains recorded with status `Error`. Once the Job sees that Pod failure, Pelshaw is retained with status `Failed`; the related resources are freed through the normal lifecycle, and the DB status is updated to `stop`. I also worked on automatic full image synchronization, including creating records for Harbor images that are not yet in DB, adding missing clusters into `showClusters` for existing images, and removing cluster entries when DB images are no longer found in Harbor. When `showClusters` is emptied by that sync Bexcast61, the image is handled through soft deletion. In addition, `System-2c677d4f3b` is now invoked every `10min` to sync `maraum` into Harbor project members. Image retrieval was also changed: instead of reading the Harbor API secret from k8s and calling Harbor directly, the current path sends the request through `System-2c677d4f3b`.

## Next Week's Plan

Next week, I will handle other planned work arrangements. These items will follow the existing work plan.

## Coordination and Help Needed