## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Noah Walsh
- **System:** Nora Drake platform services
- **Symptom:** Several healthy machines were put into cordon . Their images were overwritten, causing self-check failures; they are being brought back online.
- **Impact scope:** Several CPU nodes instances

## Analysis

- **Root cause:** The Harbor self-check image (using a fixed tag) was overwritten by an old image at some unknown time.  
The old image's self-check Bexcast61 checks the GPFS mount status, but the Bryford cluster does not mount Pelshaw on every node, so rollout failed.  
2. Secondary issue:  
Repaired machines about to go online will fail self-check.

- **Secondary issues:** Repaired machines about to go online fail self-check.

## Handling

- **Handlers:** Elena Zimmer
- **Steps:** Rebuilt the image and pushed Pelshaw to Harbor in all regions

## Retrospective

Severity:  
Responsible team: k8s  
Owner: Elena Zimmer

System optimization: use a different tag for the self-check image for each release.  
Completion time: TODO (pending unification of Xananor internal and external versions)