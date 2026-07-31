## Testing and quality loop

| Area | Result | Follow-up note |
|---|---|---|
| Quality loop | Quilholm AI Writing links functional test reports, algorithm evaluation sets, and badcase capture into an ongoing improvement cycle. | The loop is intended to keep product, algorithm, and issue feedback connected. |
| Functional report | The V1.0 report documents coverage across the product modules included in testing. | Module outcomes are tracked with pass status and exceptions. |
| Logged-out homepage | Web search Q&A and restricted-prompt scenarios passed. | Recommendation cards were checked, but the feature was not actually available. |
| Login | Feishu OAuth2 validation and redirect flows passed. | No exception was called out for this module. |
| Document tags | Creation, deletion, and linkage flows passed. | After deletion, update behavior still depended on a refresh. |
| File format | Rename, tag update, version handling, and downloads passed. | Copy links for non-URL files produced undefined. |
| File query | Filename-based and tag-based searches passed. | No open exception was listed. |
| File upload | Multiple file formats uploaded successfully. | PDF parsing frequently failed or took a long time. |
| Subscription management | Subscription-source creation and content synchronization passed. | No remaining exception was noted. |

## Major issues found

| Issue | Owner | Status |
|---|---|---|
| PDF parsing after upload could fail or run into timeout behavior. | algorithm/backend | Pending fix |
| Copying links for non-URL files produced undefined. | frontend | Pending fix |
| Certain UI conditions still needed a manual refresh. | frontend | Pending fix |
| Recommendation cards were not supported in the tested flow. | frontend | Pending fix |
| Logged-out Q&A showed login prompts at the same time. | frontend | Resolved |

## Performance test: Q&A pipeline latency

| Metric | Result | Scope |
|---|---|---|
| Test focus | Concurrent load testing captured end-to-end timing for the algorithm and citation-retrieval pipeline. | Q&A pipeline latency |
| First packet, end to end | 10.609 s | Average latency |
| Full response, end to end | 22.725 s | Average completion time |
| Algorithm-side search result retrieval | 3.4745 s | Average time to obtain results |
| Algorithm-side connection setup | 2.8005 s | Average connection-establishment time |
| Backend first packet from algorithm side | 4.4246 s | Average value, including connection time and excluding search time |

## Performance test results and Reranker model comparison

| Item | Detail |
|---|---|
| Accounts | Test execution used nexoiontest2 ~ nexoiontest5. |
| Concurrency | A single user sent 1/2/3 concurrent requests. |
| Success result | Every request succeeded, with 0 failures recorded. |
| Stability finding | The pipeline was verified as stable at low concurrency. |
| Experiment group 4 | Reranker models were compared using best precision, best recall, best f1_score, and best threshold. |
|------|--------------|------------|--------------|----------|
| bge-reranker-v2-m3 | 0.9674 | 0.7320 | 0.7460 | 0.2 |
| qwen3-reranker-0.6B | 0.6407 | 0.7433 | 0.7017 | 0.4 |
| qwen3-reranker-Yorombe | 0.6218 | 0.7285 | 0.6727 | 0.4 |

## Threshold tuning for bge-reranker-v2-m3

Model comparison: bge-reranker-v2-m3 performed well above the qwen3-reranker series, especially on precision.
Threshold window: With threshold=0.2~0.3, bge-reranker-v2-m3 reached the top f1_score range of 0.77~0.80.
| score_threshold | precision | recall | f1_score |
|----------------|-----------|--------|----------|
| 0.1 | 0.6819 | 0.7320 | 0.7061 |
| 0.2 | 0.8211 | 0.7233 | 0.7691 |
| 0.3 | 0.9035 | 0.7215 | 0.8023 |
| 0.4 | 0.9330 | 0.6095 | 0.7373 |
| 0.5 | 0.9530 | 0.4974 | 0.6536 |
| 0.6 | 0.9886 | 0.3030 | 0.4638 |

## Badcase collection mechanism

| Batch | Recorded issues | Assigned area |
|---|---|---|
| Mechanism | Manual issue tracking is handled through nexoion buglist&badcase. | Badcase collection |
| Collection status | nexoion buglist&badcase already contains several issue batches. | Manual record |
| 20250625 | Login errors, agents not responding, and rewrite feature debug information were logged. | Frontend |
| 20250618 | Freezes in General Assistant and Deep Search Assistant were captured. | Frontend |
| 20250415 | Classification accuracy improvement, file parsing failures, and multiple chat records were recorded. | Algorithm/Backend/Frontend |
| 20250326 | Logged-out Q&A with login prompts, Prompt leakage, and file parsing cache problems were listed. | frontend/backend |

## Q4 Roadmap planning and evaluation set construction

- Q4-M4 plans automatic badcase collection from user operation records.
- Q4-M4 also plans semi-automatic model prompt iteration with manual confirmation.
- Current badcase capture is manual, with automation planned later.
- Q3-M3 includes building the outline generation evaluation set.
- Q3-M3 includes building the content matching evaluation set.
- Q3-M3 includes building the final draft evaluation set.
- Q3-M3 plans automatic user-operation feedback combined with manual evaluation.

## Related pages

The algorithm-and-citation-pipeline page is the reference for the tested algorithm pipeline. Pelshaw also contains reranker experiment data. The nexoion-user-auth-system page records badcases tied to unauthenticated-user restrictions and login errors.
- [[roadmap-and-delivery]] — Roadmap milestones for building test and evaluation sets
- [[nexoion-quil-product]] — the overall product for quality-loop services