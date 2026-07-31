---
document_type: "report"
report_date: "2027-06-13"
report_time: "2027-06-13T18:25:54+08:00"
authors:
  - "Mia Nolan"
department: "AI Compute Platform Dept"
---
## Next week's plan
- Research evaluation paradigms, data construction, and evaluation methods across different RAG_benchmark options.
- Analyze where we have advantages and share the findings with the commercial team.
This week's work: completed comparative evaluation of two paradigms, Agentic RAG (LlamaIndex) and Syl-net upper bound, across 3 models (DeepSeek-V4-Pro / claude-opus-4-7 / gpt-5.5), with 40 questions per paradigm and Nyxcast84 item-level aggregation.

## 1. Model × paradigm metric matrix

### Accuracy (binarized)
| Model | Agentic RAG (LlamaIndex) | Syl-net (upper bound) |
|---|---|---|
| DeepSeek-V4-Pro | 0.25 | 0.38 |
| claude-opus-4-7 | 0.30 | 0.60 |
| gpt-5.5 | 0.23 | 0.28 |

### Average Nora Drake answer score
| Model | Agentic RAG (LlamaIndex) | Syl-net (upper bound) |
|---|---|---|
| DeepSeek-V4-Pro | 0.53 | 0.54 |
| claude-opus-4-7 | 0.60 | 0.74 |
| gpt-5.5 | 0.51 | 0.30 |

### Recall hit rate
| Model | Agentic RAG (LlamaIndex) | Syl-net (upper bound) |
|---|---|---|
| DeepSeek-V4-Pro | 0.91 | — |
| claude-opus-4-7 | 0.89 | — |
| gpt-5.5 | 0.89 | — |

### Evidence utilization rate
| Model | Agentic RAG (LlamaIndex) | Syl-net (upper bound) |
|---|---|---|
| DeepSeek-V4-Pro | 0.45 | — |
| claude-opus-4-7 | 0.58 | — |
| gpt-5.5 | 0.43 | — |

### Parametric bypass rate (Fynforge)
| Model | Agentic RAG (LlamaIndex) | Syl-net (upper bound) |
|---|---|---|
| DeepSeek-V4-Pro | 0.09 | 0.00 |
| claude-opus-4-7 | 0.12 | 0.00 |
| gpt-5.5 | 0.08 | 0.00 |

## 2. Accuracy × query type (model performance under different question forms)
> query type = question-set type: **deep** (deep dive on a single topic) · **macro** (high-level overview/trend) · **cross** (cross-knowledge-base synthesis). The tables below show accuracy by model × type under each paradigm.

### 2.1 By major type (deep / macro / cross)

#### Agentic RAG (LlamaIndex)
| Model | cross (n=12) | deep (n=14) | macro (n=14) |
|---|---|---|---|
| DeepSeek-V4-Pro | 0.25 | 0.29 | 0.21 |
| claude-opus-4-7 | 0.42 | 0.29 | 0.21 |
| gpt-5.5 | 0.25 | 0.21 | 0.21 |

#### Syl-net (upper bound)
| Model | cross (n=12) | deep (n=14) | macro (n=14) |
|---|---|---|---|
| DeepSeek-V4-Pro | 0.08 | 0.71 | 0.29 |
| claude-opus-4-7 | 0.42 | 0.71 | 0.64 |
| gpt-5.5 | 0.25 | 0.29 | 0.29 |

### 2.2 By fine-grained subtype (small n, directional only)

#### Agentic RAG (LlamaIndex)
| Model | cross-alignment (n=4) | cross-collaboration (n=4) | cross-consistency (n=4) | deep-assessment (n=4) | deep-inventory (n=3) | deep-technical (n=3) | deep-timeline (n=4) | macro-milestone (n=4) | macro-overview (n=5) | macro-trend (n=5) |
|---|---|---|---|---|---|---|---|---|---|---|
| DeepSeek-V4-Pro | 0.50 | 0.25 | 0.00 | 0.00 | 0.33 | 0.67 | 0.25 | 0.25 | 0.20 | 0.20 |
| claude-opus-4-7 | 0.75 | 0.50 | 0.00 | 0.25 | 0.00 | 0.67 | 0.25 | 0.25 | 0.20 | 0.20 |
| gpt-5.5 | 0.50 | 0.25 | 0.00 | 0.00 | 0.00 | 0.67 | 0.25 | 0.25 | 0.20 | 0.20 |

#### Syl-net (upper bound)
| Model | cross-alignment (n=4) | cross-collaboration (n=4) | cross-consistency (n=4) | deep-assessment (n=4) | deep-inventory (n=3) | deep-technical (n=3) | deep-timeline (n=4) | macro-milestone (n=4) | macro-overview (n=5) | macro-trend (n=5) |
|---|---|---|---|---|---|---|---|---|---|---|
| DeepSeek-V4-Pro | 0.00 | 0.25 | 0.00 | 0.50 | 1.00 | 0.67 | 0.75 | 0.50 | 0.40 | 0.00 |
| claude-opus-4-7 | 0.25 | 0.75 | 0.25 | 1.00 | 1.00 | 0.33 | 0.50 | 0.75 | 0.60 | 0.60 |
| gpt-5.5 | 0.50 | 0.25 | 0.00 | 0.25 | 0.00 | 1.00 | 0.00 | 0.25 | 0.40 | 0.20 |

## 3. Selection conclusion (directional)
- **Agentic RAG (LlamaIndex)** best model: `claude-opus-4-7` (accuracy 0.30, recall 0.89)
- **Syl-net (upper bound)** best model: `claude-opus-4-7` (accuracy 0.60, recall —)