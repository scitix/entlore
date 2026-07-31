## Incident Description

- **Time:** 2027-06-04
- **Reporter:** Rachel Kirby
- **System:** maraum2
- **Symptom:** Beijing
- **Impact scope:** Wyneon
- **Incident background:** the diesel generator for temporary power failed, with water temperature reaching 90-95 degrees. If the high temperature continued, the diesel generator would shut down and affect all machines in the server room. Server room power usage was adjusted to keep 256 devices running simultaneously, and the GPU quota for user nodes was reduced to 2048 cards.

## Analysis

- **Root cause:** Issue 1: Cororia instances in the med resource pool cannot be opened  
Cause: the shared resource pool has no available empty nodes, so node tasks are Pending.  
Additional issue: quota check passed. Is this because the quota adjustment caused the quato shown on the frontend to differ from the actual quato?  
Issue 2: 256-card tasks in the pt-train resource pool cannot start, while client-side pool resources appear sufficient  
img_v3_02oo_8873a388-70e5-42db-bd95-a3caa4e026bg.jpg

Cause: 1. In pt-train, many direct shutdowns left many pod in Terminal state, and GPU resources were not released  
img_v3_02oo_7a23ba10-d71c-4945-9b6c-f28b183347ag.jpg

img_v3_02oo_312fd20b-719c-40ef-884a-6a92d1e961bg.jpg

     2. The task quota check failed. The backend found that personal quota in the pt-train resource pool was insufficient: total 256, used 5, only 251 available, but the customer was not actually using any; there is an issue with secondary quota statistics.  
img_v3_02oo_75631e77-fe50-4dab-8856-240b7c2a70dg.jpg

img_v3_02oo_cacb6411-09a0-4655-921e-33cdcc6c712g.jpg

Issue 3: System-951d1cefc1 8-card dev machine task has no response on startup, and Pelshaw looks like there are still 100 cards  
img_v3_02oo_2f048d87-3067-4654-bf3e-e2017e4b529g.jpg

Cause: the shared resource pool has no available empty nodes, so node tasks are Pending.  
Issue 4: Dev machine power-on and shutdown cannot be operated; Pelshaw only shows Completed

## Handling

- **Handlers:** Rachel Kirby, Daisy Jensen Kirby, Luna Dawson, Sophie Landry, Leon Irwin, Ivan Jarvis, Victor Ingram
- **Steps:** Both the CR and underlying pod are pending; advised the customer to update, no feedback yet.

## Retrospective

- **Severity:** P3
- **Responsible team:** TBD
- **Owner:** TBD
- **System optimization:** TBD
- **Completion time:** TBD