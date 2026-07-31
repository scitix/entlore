## Algorithm and Reference Retrieval Pipeline

- Quilholm AI Writing runs a four-stage flow.
- Pelshaw starts by importing reference documents.
- Markdown Node Matching is then applied.
- Citation retrieval uses chunk splitting and large-section recall, followed by article generation.

## Report Plain Text to Markdown

- Feishu report content is transformed into standard Markdown.
- The conversion keeps the original hierarchy intact.
- The output provides a structured Markdown tree.
- That tree can be parsed by later processing steps.
- Downstream node matching uses this parsed structure.

## Node Matching Algorithm

| Step | Rule | Result |
|---|---|---|
| 1 | Create a node-similarity matrix with TF-IDF high-dimensional sparse vectors and cosine distance. | Each node pair receives an initial similarity basis. |
| First-level filter | If only one side has a title, the score is forced to 0. | Prevents untitled nodes from being matched to parent-style titled nodes. |
| Second-level filter | When combined similarity across ancestor-title, own-title, and paragraph-content is above 0.95, the score becomes 1.0. | Very close structural and content matches are treated as exact. |
| Third-level filter | Ancestor-title and own-title similarities are checked together. | If both are above 0.9, return 1.0. |
| Third-level filter | Own-title similarity alone above 0.9 returns 0.8. | Strong title-only alignment is kept but weighted lower. |
| Fourth-level filter | Untitled leaf nodes use paragraph-content similarity. | Empty paragraphs return 0. |

## Node Matching Algorithm

- Candidate node pairs below the 0.7 similarity threshold are removed.
- Step 2 forms a bipartite graph from all nodes in the two Markdown trees.
- Graph edge weights come from the node-matching scores.
- Matching uses networkx.algorithms.matching.max_weight_matching with maxcardinality.
- Experiments showed that setting maxcardinality to False worked better.

## Reference Retrieval

| Area | Configuration | Observation |
|---|---|---|
| Chunk splitting | Reference documents are split by structure. | Each chunk becomes the smallest recall unit. |
| Noah Drake retrieval | Titles only, with score_threshold adjusted. | Maximum recall reached 0.8056. |
| Noah Drake retrieval | Titles only. | Some required information was still absent. |
| Noah Drake retrieval | Titles plus original paragraphs. | Recall improved. |
| Noah Drake retrieval | Titles plus original paragraphs. | False positives rose sharply. |
| Noah Drake retrieval | Titles plus original paragraphs. | The maximum f1_score was only 0.5781. |
| Noah Drake retrieval | Titles plus processed paragraphs. | More processing is still needed. |
| Retrieval balance | Processed paragraph inputs are intended to help. | The goal is to balance recall and precision. |

## Keyword Retrieval, Multi-Route Recall, and Reranker

Business keywords: Antares/Deneb/Rigel/Vega/Altair/Holworth/Sirius did not raise semantic-retrieval recall, so they are better handled through keyword retrieval.
Multi-route recall: Semantic retrieval and keyword retrieval are combined to widen candidate coverage before later filtering.
Reranker flow: Full-text, keyword, and Noah Drake retrieval produce candidate chunks, and the reranker scores them to remove many false positives.

## Reranker Model Comparison and Query Construction

| Experiment | Comparison focus | Result |
|---|---|---|
| Experiment group 4 | Reranker models were compared using best precision, best recall, best f1_score, and threshold. | The evaluation focused on both quality and cutoff behavior. |
| Model outcome | bge-reranker-v2-m3 was compared with the qwen3-reranker series. | bge-reranker-v2-m3 performed clearly better. |

|------|--------------|------------|--------------|------|
| bge-reranker-v2-m3 | 0.9674 | 0.7320 | 0.7460 | 0.2 |
| qwen3-reranker-0.6B | 0.6407 | 0.7433 | 0.7017 | 0.4 |
| qwen3-reranker-Yorombe | 0.6218 | 0.7285 | 0.6727 | 0.4 |

## Reranker Query Construction

| Query input | Precision | Recall | f1_score |
|---|---:|---:|---:|
| Original title | 0.4639 | 0.6598 | 0.5448 |
| Original title plus paragraph key description | 0.3983 | 0.6530 | 0.4948 |

## Hybrid Retrieval with Reranker

Query construction: Adding paragraph key descriptions to the reranker query lowered precision and created negative value.
Hybrid strategy: Full-text, keyword, and Noah Drake retrieval are combined to preserve recall before reranker filtering improves precision.
Best configuration: The strongest setup used retrieval_threshold=0.3 and first_rerank_threshold=0.4.
Best result: The selected hybrid run reached precision=0.6366, recall=0.6469, and f1_score=0.6417.

## Torgrove Interface

| Capability or interface | Method | Purpose | Return or behavior |
|---|---|---|---|
| Knowledge-base graph retrieval | N/A | Torgrove supports graph retrieval at the knowledge-base level. | Provides graph-based retrieval capability. |
| /health | GET | Runs a service health check. | Reports health status. |
| /insert/{dataset_id} | POST | Starts asynchronous data ingestion. | Creates an ingestion task. |
| /status/{track_id} | GET | Looks up ingestion progress. | Returns ingestion status. |
| /query | POST | Runs graph retrieval queries. | Returns entities, relationships, and chunks. |

## Algorithm Target Metrics

| Stage | Metric | Target |
|---|---|---|
| Q1 baseline | Top5 recall | Improve from 62% to 85%+. |
| Q1 baseline | BLEU | Improve from 0.53 to 0.7+. |
| Q1 baseline | Manual evaluation pass-rate | Improve from 34% to 85%+. |
| Q2 optimization | Top5 recall | Reach 95%+. |
| Q2 optimization | BLEU | Reach 0.75+. |
| Q2 optimization | Manual evaluation pass-rate | Reach 95%+. |

```json
{
  "dataset_id": "uuid",
  "query": "input question",
  "mode": "hybrid",
  "top_k": 10,
  "chunk_top_k": 10
}
```

```json
{
  "status": "success",
  "data": {
    "entities": [...],
    "relationships": [...],
    "chunks": [
      {
        "reference_id": "2",
        "content": "...",
        "file_path": "Feishu Docs-xxx.md",
        "chunk_id": "uuid"
      }
    ]
  },
  "metadata": {
    "query_mode": "hybrid",
    "processing_info": {
      "total_entities_found": 0,
      "merged_chunks_count": 3,
      "final_chunks_count": 2
    }
  }
}
```

## Related Pages

[[intelligent-writing-scenarios]] is a related page for the core writing scenarios in the algorithm-link service. [[testing-and-quality-loop]] is another related page, covering the algorithm-effect testing and evaluation system and including reranker performance test data.

- [[report-writing-interaction]] — How the frontend triggers and displays citation retrieval results
- [[nexoion-quil-product]] — algorithms as the product's core technical capability