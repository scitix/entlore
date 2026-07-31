## Intelligent writing algorithm optimization
- Scope includes importing reference documents and parsing the resulting document structure.
- Stage 1 turns report plain text into Markdown text.
- Stage 2 handles matching between Markdown nodes.
- Step 1 builds similarity scores for every node pair.
- Text scoring uses tfidf vectors for the two texts, with cosine distance treated as the similarity.
- The first node filter assigns 0 when exactly one side has a title.
- That first rule stops titleless nodes from pairing with nodes that really belong with their parents.
- The second rule builds a comparison string from ancestor titles, the node title, and paragraph text.
- When that combined comparison is above 0.95, the second rule outputs 1.0.
- The third rule evaluates ancestor-title similarity separately from the node-title similarity.
- If both title scores are above 0.9, the third rule outputs 1.0.
- If only the node-title score is above 0.9, the third rule outputs 0.8.
- The fourth rule treats nodes without titles as leaves.
- For those titleless nodes, the fourth rule uses paragraph-text similarity.
- If either paragraph body is empty, the fourth rule gives 0.
- Final matches discard node pairs below the 0.7 similarity threshold.

- Step 2 derives the best matching from the node similarity matrix.
- The implementation creates a bipartite graph across the two Markdown trees.
- Graph edges carry the matching weight between two candidate nodes.
- Each vertex CAN be attached to no more than one edge.
- Matching uses networkx.algorithms.matching.max_weight_matching.
- The selected result maximizes the sum of edge weights.
- maxcardinality is the main setting that changes the output.
image.png

## Experiment records
- This experiment group focuses on ways to score similarity between nodes.
- The goal is a reliable scoring flow for section-node matching.
- Experiments 1 and 2 both confirm that titles matter a lot.
- Because titles are short, mixing them with paragraph text sharply lowers their influence.
- Lower title influence CAN lead to incorrect matches.
- The conclusion is to match titles and paragraphs through separate checks.

- The experiment table records number, method settings, results, and notes.
- Experiment 1 joins all ancestor titles with the node title before title scoring.
- If title similarity is >= 0.8, Experiment 1 returns that title score directly.
- If title similarity is < 0.8, Pelshaw scores text from title, paragraph, and child content.
- Under that lower-title-score path, Experiment 1 returns the text similarity.
- When the two articles are close, titled nodes are matched fairly accurately.
- Untitled leaf nodes are still easy to confuse with parent or sibling nodes.

- Experiment 2 gives 0 when only one of the two compared nodes has a title.
- That rule cuts some unnecessary similarity work and reduces compute time.
- Pelshaw also builds a high-similarity filter from ancestor titles, node title, and paragraph text.
- If the combined score is greater than 0.95, Experiment 2 returns 1.0.
- Ancestor-title and self-title similarities are then calculated separately.
- When both title scores are greater than 0.9, the result is 1.0.
- When only the self-title score is greater than 0.9, the result is 0.8.
- Nodes with no title use paragraph-content similarity instead.
- If either paragraph is empty, the score is 0, so empty paragraphs do not match each other.

- Two test datasets showed better Jynkit42 matching accuracy and recall.
- Large-scale timing factors were not tested.
- Future evaluation will pull more data from log.
- Another experiment group works on optimal matching from the similarity matrix.
- Its goal is to pick the best node-matching algorithm and parameters from the current section-node matrix.
- No conclusion is provided for that experiment.
- Its table also records experiment number, parameters, results, and notes.

- Experiment 1 applies networkx.algorithms.matching.max_weight_matching() for maximum-weight matching.
- Experiment 1 uses maxcardinality = True.
- Matches below 0.7 matching degree are filtered out.
- Experiment 2 also uses networkx.algorithms.matching.max_weight_matching().
- Experiment 2 sets maxcardinality = False.
- Pelshaw applies the same below-0.7 match filter.

## Reference citation retrieval
- Reference citation retrieval includes a test set.
- Stage 1 splits content into chunks.
- Stage 2 performs citation recall at the large-section level.
- Experiment group 1 evaluates Noah Drake-retrieval query design and large-section recall parameters.
- Noah Drake retrieval CAN connect semantically similar queries and chunks.
- Pelshaw also brings in many false positives.
- The experiment needs a score_threshold that keeps recall high without too many false positives.
- Later reranker processing is expected to handle false positives that cannot be avoided.
- Large-section recall may draw queries from titles, paragraphs, and template content.
- The tests compare which query source and extraction strategy work best.
- Thresholds are adjusted and then checked against precision and recall on a labeled test set.
- Experiments 1-1 and 1-2 show title-only semantic retrieval reaches a maximum Overall recall of 0.8056.
- Even with a low threshold, title-only semantic retrieval does not provide enough query detail.
- Adding raw paragraph text raises Overall recall, but false positives also increase.
- Raw paragraph query content reaches a maximum Overall f1_score of only 0.5781.
- Paragraphs should still be used as query inputs, but they require more processing.
- Experiments 1-1 and 1-3 show no recall gain from adding Antares, Deneb, Rigel, Vega, Altair, Holworth, Sirius, Torombe.
- Those terms fit keyword retrieval better than semantic retrieval.
- score_threshold is the Noah Drake semantic-recall matching score threshold.

- Experiment 1-1 uses large-section titles as queries for large-section nodes.
- If source text lacks a title, the first list item is treated as the title.
- For leaf nodes outside large sections, ancestor titles and the current title are joined as the query.
- Each leaf-node query is added into the query source for its large section.
- Non-leaf node titles are left out of large-section recall queries.
- Query post-processing strips Markdown formatting marks.
- Pelshaw also removes @ person names.
- Escape symbols are deleted, along with the special symbols “【” and “】”.
- “This Week's Work”, “Next Week's Plan”, “KR1”, and “KR2” are also removed.
- Experiment 1-1 does not apply filtering after recall.
reranking_enable: false
embedding_model_name=lororys2-qwen3-embedding-0-6b-v1
weights=null
top_k=50, score_threshold=0.1～0.9

- Iris Otis results are provided in an associated data block.
- Kara Holt results are also provided in an associated data block.
- Experiment 1-1 uses only concatenated raw titles for semantic recall.
- Experiment 1-2 changes the query source to titles plus extracted key paragraph descriptions.
- Other conditions in Experiment 1-2 stay aligned with Experiment 1-1.
- Its semantic recall queries therefore combine titles with key paragraph descriptions.
- Experiment 1-3 merges the query sources from Experiment 1-1 and Experiment 1-2.
- Other conditions in Experiment 1-3 also follow Experiment 1-1.
Overall Metrics:
score_threshold=0.1: precision=0.158 recall=0.8493 f1_score=0.2664
score_threshold=0.2: precision=0.1583 recall=0.8493 f1_score=0.2669
score_threshold=0.3: precision=0.1706 recall=0.8493 f1_score=0.2841
score_threshold=0.4: precision=0.2164 recall=0.742 f1_score=0.3351
score_threshold=0.5: precision=0.3891 recall=0.5525 f1_score=0.4566
score_threshold=0.6: precision=0.5263 recall=0.3196 f1_score=0.3977
score_threshold=0.7: precision=0.3445 recall=0.0936 f1_score=0.1472
score_threshold=0.8: precision=0.2258 recall=0.016 f1_score=0.0299
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.1894 recall=0.8221 f1_score=0.3079
score_threshold=0.2: precision=0.1894 recall=0.8221 f1_score=0.3079
score_threshold=0.3: precision=0.2001 recall=0.8221 f1_score=0.3219
score_threshold=0.4: precision=0.2538 recall=0.7709 f1_score=0.3819
score_threshold=0.5: precision=0.414 recall=0.6038 f1_score=0.4912
score_threshold=0.6: precision=0.5466 recall=0.3639 f1_score=0.4369
score_threshold=0.7: precision=0.3694 recall=0.1105 f1_score=0.1701
score_threshold=0.8: precision=0.25 recall=0.0189 f1_score=0.0351
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.0899 recall=1.0 f1_score=0.165
score_threshold=0.2: precision=0.0905 recall=1.0 f1_score=0.166
score_threshold=0.3: precision=0.102 recall=1.0 f1_score=0.1851
score_threshold=0.4: precision=0.104 recall=0.5821 f1_score=0.1765
score_threshold=0.5: precision=0.2222 recall=0.2687 f1_score=0.2432
score_threshold=0.6: precision=0.2632 recall=0.0746 f1_score=0.1163
score_threshold=0.7: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
New data result:
Overall Metrics:
score_threshold=0.1: precision=0.1542 recall=0.879 f1_score=0.2624
score_threshold=0.2: precision=0.1546 recall=0.879 f1_score=0.263
score_threshold=0.3: precision=0.1626 recall=0.8767 f1_score=0.2743
score_threshold=0.4: precision=0.2044 recall=0.742 f1_score=0.3205
score_threshold=0.5: precision=0.3531 recall=0.5708 f1_score=0.4363
score_threshold=0.6: precision=0.5036 recall=0.3219 f1_score=0.3928
score_threshold=0.7: precision=0.3566 recall=0.105 f1_score=0.1622
score_threshold=0.8: precision=0.2121 recall=0.016 f1_score=0.0298
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.1816 recall=0.8571 f1_score=0.2997
score_threshold=0.2: precision=0.1816 recall=0.8571 f1_score=0.2997
score_threshold=0.3: precision=0.186 recall=0.8544 f1_score=0.3055
score_threshold=0.4: precision=0.2375 recall=0.7709 f1_score=0.3631
score_threshold=0.5: precision=0.3694 recall=0.6253 f1_score=0.4644
score_threshold=0.6: precision=0.5211 recall=0.3666 f1_score=0.4304
score_threshold=0.7: precision=0.377 recall=0.124 f1_score=0.1866
score_threshold=0.8: precision=0.2258 recall=0.0189 f1_score=0.0349
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.0899 recall=1.0 f1_score=0.165
score_threshold=0.2: precision=0.0905 recall=1.0 f1_score=0.166
score_threshold=0.3: precision=0.102 recall=1.0 f1_score=0.1851
score_threshold=0.4: precision=0.101 recall=0.5821 f1_score=0.1721
score_threshold=0.5: precision=0.225 recall=0.2687 f1_score=0.2449
score_threshold=0.6: precision=0.2632 recall=0.0746 f1_score=0.1163
score_threshold=0.7: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Overall Metrics:
score_threshold=0.1: precision=0.1491 recall=0.5776 f1_score=0.237
score_threshold=0.2: precision=0.1547 recall=0.6027 f1_score=0.2462
score_threshold=0.3: precision=0.1543 recall=0.5936 f1_score=0.2449
score_threshold=0.4: precision=0.157 recall=0.5571 f1_score=0.245
score_threshold=0.5: precision=0.1936 recall=0.3744 f1_score=0.2552
score_threshold=0.6: precision=0.2846 recall=0.1644 f1_score=0.2084
score_threshold=0.7: precision=0.125 recall=0.0228 f1_score=0.0386
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.1807 recall=0.6442 f1_score=0.2822
score_threshold=0.2: precision=0.1864 recall=0.6712 f1_score=0.2918
score_threshold=0.3: precision=0.1847 recall=0.6631 f1_score=0.2889
score_threshold=0.4: precision=0.1828 recall=0.6226 f1_score=0.2826
score_threshold=0.5: precision=0.2086 recall=0.4178 f1_score=0.2783
score_threshold=0.6: precision=0.2918 recall=0.1833 f1_score=0.2252
score_threshold=0.7: precision=0.1316 recall=0.027 f1_score=0.0448
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.0374 recall=0.209 f1_score=0.0634
score_threshold=0.2: precision=0.0404 recall=0.2239 f1_score=0.0684
score_threshold=0.3: precision=0.0397 recall=0.209 f1_score=0.0667
score_threshold=0.4: precision=0.0448 recall=0.194 f1_score=0.0728
score_threshold=0.5: precision=0.0865 recall=0.1343 f1_score=0.1052
score_threshold=0.6: precision=0.2 recall=0.0597 f1_score=0.092
score_threshold=0.7: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0

- Experiment 1-3 uses raw titles plus paragraph-derived key descriptions for semantic recall queries.
- Experiment group 2 evaluates full-text retrieval query design and large-section recall parameters.
- Unlike embedding-based semantic retrieval, full-text retrieval CAN hit exact keywords.
- Pelshaw CAN also reduce false positives caused by broad semantic matching.
- To avoid too many false positives, each large section needs distinctive keywords.
- One construction method sends the full Markdown tree to a large model for unique keyword analysis.
- Another method asks a large model to extract keywords for each large section separately.
- The comparison covers pure keyword retrieval and TF-IDF retrieval.
- Pure keyword retrieval depends on exact hits but cannot return scores for threshold filtering.
- TF-IDF retrieval gives each query a score, but short queries usually score low.
- Short TF-IDF queries score low because their TF-IDF vectors are too sparse.
- The experiment needs a final scoring approach with Jynkit42 discrimination.
- Pelshaw also needs to decide whether one method is better or whether the methods should fill each other’s recall gaps.
- Special title keywords Antares, Deneb, Rigel, Vega, Altair, Holworth, Sirius, and Torombe retrieve with high accuracy.
- Results from those special title keywords do not require another reranker pass.
- Experiment 2-3 shows special-keyword title recall is contained within title-keyword recall.
- Special-keyword recall is still needed because Pelshaw avoids the risk of reranker filtering correct recalls.
- Experiment 2-5 shows body keywords improve recall by about 5%.
- The same experiment shows precision drops by 11%.
- Body keywords introduce far more false-recall noise than title keywords.
- They remain useful when later reranker processing CAN remove false recalls.
Overall Metrics:
score_threshold=0.1: precision=0.1589 recall=0.8836 f1_score=0.2694
score_threshold=0.2: precision=0.1597 recall=0.8881 f1_score=0.2707
score_threshold=0.3: precision=0.1716 recall=0.8881 f1_score=0.2876
score_threshold=0.4: precision=0.2152 recall=0.7945 f1_score=0.3387
score_threshold=0.5: precision=0.3611 recall=0.6826 f1_score=0.4723
score_threshold=0.6: precision=0.4806 recall=0.621 f1_score=0.5419
score_threshold=0.7: precision=0.5048 recall=0.605 f1_score=0.5504
score_threshold=0.8: precision=0.5693 recall=0.6096 f1_score=0.5888
score_threshold=0.9: precision=0.6606 recall=0.6329 f1_score=0.6465
Metrics of easy:
score_threshold=0.1: precision=0.1895 recall=0.8625 f1_score=0.3107
score_threshold=0.2: precision=0.1901 recall=0.8679 f1_score=0.3119
score_threshold=0.3: precision=0.2002 recall=0.8679 f1_score=0.3254
score_threshold=0.4: precision=0.2502 recall=0.8329 f1_score=0.3848
score_threshold=0.5: precision=0.3813 recall=0.7493 f1_score=0.5054
score_threshold=0.6: precision=0.5 recall=0.6927 f1_score=0.5808
score_threshold=0.7: precision=0.5216 recall=0.6819 f1_score=0.5911
score_threshold=0.8: precision=0.5939 recall=0.6819 f1_score=0.6349
score_threshold=0.9: precision=0.7076 recall=0.7626 f1_score=0.7341
Metrics of hard:
score_threshold=0.1: precision=0.0897 recall=1.0 f1_score=0.1646
score_threshold=0.2: precision=0.0903 recall=1.0 f1_score=0.1656
score_threshold=0.3: precision=0.1017 recall=1.0 f1_score=0.1846
score_threshold=0.4: precision=0.1021 recall=0.5821 f1_score=0.1737
score_threshold=0.5: precision=0.2121 recall=0.3134 f1_score=0.253
score_threshold=0.6: precision=0.2885 recall=0.2239 f1_score=0.2521
score_threshold=0.7: precision=0.3 recall=0.1791 f1_score=0.2243
score_threshold=0.8: precision=0.3256 recall=0.209 f1_score=0.2546
score_threshold=0.9: precision=0.3684 recall=0.209 f1_score=0.2667

- Experiment 2-1 builds query sources by joining the title of a large section with all subsection titles.
- When list nodes have titles, those list-node titles are concatenated as well.
- The full-text retrieval keywords are Antares, Deneb, Rigel, Vega, Altair, Holworth, Sirius, and Torombe.
- Experiment 2-1 applies those keywords when they are present in the query source.
search_method: full_text_search
reranking_enable: false
top_k=50

- Experiment 2-1 relies only on title keywords Antares, Deneb, Rigel, Vega, Altair, Holworth, Sirius, and Torombe for full-text recall.
- Experiment 2-2 uses a model during query post-processing to extract keywords.
- Other conditions in Experiment 2-2 remain the same as Experiment 2-1.
- Experiment 2-2 extracts title keywords and then recalls through full-text retrieval.
- Experiment 2-3 is introduced later for query Qelsys40.
Overall Metrics:
precision=0.9638 recall=0.4863 f1_score=0.6464
Metrics of easy:
precision=0.9638 recall=0.5741 f1_score=0.7196
Metrics of hard:
precision=0.0 recall=0.0 f1_score=0.0
Overall Metrics:
precision=0.5959 recall=0.5959 f1_score=0.5959
Metrics of easy:
precision=0.6195 recall=0.6846 f1_score=0.6504
Metrics of hard:
precision=0.25 recall=0.1045 f1_score=0.1474

- Experiment 2-3 combines the queries from Experiment 2-1 and Experiment 2-2.
- Its other conditions follow Experiment 2-1.
- Recall in Experiment 2-3 uses both special keywords and title keywords.
- Experiment 2-4 takes leaf-node paragraph content as the query source.
- Pelshaw uses a model for keyword extraction during query post-processing.
- Other conditions in Experiment 2-4 stay the same as Experiment 2-1.
- Experiment 2-4 performs recall with paragraph keywords.
- Experiment 2-5 merges queries from Experiment 2-2 and Experiment 2-4.
Overall Metrics:
score_threshold=0.1: precision=0.605 recall=0.605 f1_score=0.605
Metrics of easy:
score_threshold=0.1: precision=0.6225 recall=0.6846 f1_score=0.6521
Metrics of hard:
score_threshold=0.1: precision=0.3667 recall=0.1642 f1_score=0.2268
Overall Metrics:
score_threshold=0.1: precision=0.2923 recall=0.1895 f1_score=0.2299
Metrics of easy:
score_threshold=0.1: precision=0.2878 recall=0.2102 f1_score=0.243
Metrics of hard:
score_threshold=0.1: precision=0.3846 recall=0.0746 f1_score=0.125

- Experiment 2-5 keeps the remaining conditions aligned with Experiment 2-1.
- Pelshaw recalls with a combination of title keywords and paragraph keywords.
- Experiment group 3 studies mixed coarse-recall strategies across semantic and full-text retrieval.
- The group aims to raise precision while still prioritizing recall.
- The method first sets the semantic retrieval threshold at a relatively accurate level.
- Pelshaw then adds each keyword retrieval query and checks which parts help.
- After required keyword queries are fixed, the semantic threshold is lowered until recall gains are no longer Jynkit42.
- Experiment 3-1 shows special-keyword recall plus raw-title semantic recall greatly raises f1-score.
- The same result indicates special keywords and raw-title semantic recall complement each other.
- Experiments 3-3 and 3-4 show substring queries CAN be dropped when covered by another query.
- Removing substring queries during recall has little effect.
Overall Metrics:
score_threshold=0.1: precision=0.4807 recall=0.653 f1_score=0.5538
Metrics of easy:
score_threshold=0.1: precision=0.4927 recall=0.7251 f1_score=0.5867
Metrics of hard:
score_threshold=0.1: precision=0.3469 recall=0.2537 f1_score=0.2931

- Experiment 3-1 merges strategies from Experiment 2-1 and Experiment 1-1.
- Pelshaw uses raw titles for semantic recall.
- Pelshaw uses special keywords for keyword recall.
- Experiment 3-2 combines the strategies from Experiment 2-1 and Experiment 2-2.
- Experiment 3-2 recalls with special keywords plus model-extracted title keywords.
- Experiment 3-3 combines strategies from Experiment 1-1, Experiment 1-2, Experiment 2-1, Experiment 2-2, and Experiment 2-4.
Overall Metrics:
score_threshold=0.1: precision=0.1603 recall=0.8653 f1_score=0.2705
score_threshold=0.2: precision=0.1606 recall=0.8653 f1_score=0.2709
score_threshold=0.3: precision=0.173 recall=0.8653 f1_score=0.2883
score_threshold=0.4: precision=0.2338 recall=0.8462 f1_score=0.3664
score_threshold=0.5: precision=0.4126 recall=0.6142 f1_score=0.4936
score_threshold=0.6: precision=0.6331 recall=0.516 f1_score=0.5686
score_threshold=0.7: precision=0.7167 recall=0.4909 f1_score=0.5827
score_threshold=0.8: precision=0.873 recall=0.4863 f1_score=0.6246
score_threshold=0.9: precision=0.9509 recall=0.4863 f1_score=0.6435
Metrics of easy:
score_threshold=0.1: precision=0.1926 recall=0.841 f1_score=0.3134
score_threshold=0.2: precision=0.1926 recall=0.841 f1_score=0.3134
score_threshold=0.3: precision=0.2034 recall=0.841 f1_score=0.3276
score_threshold=0.4: precision=0.3076 recall=0.9269 f1_score=0.4619
score_threshold=0.5: precision=0.4396 recall=0.6765 f1_score=0.5329
score_threshold=0.6: precision=0.6538 recall=0.5957 f1_score=0.6234
score_threshold=0.7: precision=0.7363 recall=0.5795 f1_score=0.6486
score_threshold=0.8: precision=0.8838 recall=0.5741 f1_score=0.6961
score_threshold=0.9: precision=0.9509 recall=0.5741 f1_score=0.7159
Metrics of hard:
score_threshold=0.1: precision=0.0899 recall=1.0 f1_score=0.165
score_threshold=0.2: precision=0.0905 recall=1.0 f1_score=0.166
score_threshold=0.3: precision=0.102 recall=1.0 f1_score=0.1851
score_threshold=0.4: precision=0.104 recall=0.5821 f1_score=0.1765
score_threshold=0.5: precision=0.2222 recall=0.2687 f1_score=0.2432
score_threshold=0.6: precision=0.2632 recall=0.0746 f1_score=0.1163
score_threshold=0.7: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Overall Metrics:
precision=0.6014 recall=0.5959 f1_score=0.5986
Metrics of easy:
precision=0.6256 recall=0.6846 f1_score=0.6538
Metrics of hard:
precision=0.25 recall=0.1045 f1_score=0.1474

- Experiment 3-3 uses original titles, title key descriptions, and paragraph key descriptions for semantic recall.
- Its keyword recall uses title keywords, paragraph keywords, and special keywords.
- Experiment 3-4 reviews all queries based on Experiment 3-3.
- If a query has a parent-string query, Experiment 3-4 keeps only the parent-string version.
- Semantic recall in Experiment 3-4 still uses title originals, title key descriptions, and paragraph key descriptions.
- Keyword recall in Experiment 3-4 still uses title keywords, paragraph keywords, and special keywords.
- During query processing, Experiment 3-4 removes all substring queries.
Overall Metrics:
score_threshold=0.1: precision=0.1429 recall=0.9292 f1_score=0.2477
score_threshold=0.2: precision=0.1443 recall=0.9338 f1_score=0.25
score_threshold=0.3: precision=0.151 recall=0.9315 f1_score=0.2599
score_threshold=0.4: precision=0.1735 recall=0.8927 f1_score=0.2905
score_threshold=0.5: precision=0.2448 recall=0.7534 f1_score=0.3695
score_threshold=0.6: precision=0.3702 recall=0.6804 f1_score=0.4795
score_threshold=0.7: precision=0.4153 recall=0.6712 f1_score=0.5131
score_threshold=0.8: precision=0.4474 recall=0.6507 f1_score=0.5302
score_threshold=0.9: precision=0.47 recall=0.6621 f1_score=0.5498
Metrics of easy:
score_threshold=0.1: precision=0.1654 recall=0.9164 f1_score=0.2802
score_threshold=0.2: precision=0.1665 recall=0.9218 f1_score=0.2821
score_threshold=0.3: precision=0.1725 recall=0.9191 f1_score=0.2905
score_threshold=0.4: precision=0.1981 recall=0.9003 f1_score=0.3247
score_threshold=0.5: precision=0.2579 recall=0.7951 f1_score=0.3895
score_threshold=0.6: precision=0.3838 recall=0.752 f1_score=0.5082
score_threshold=0.7: precision=0.4284 recall=0.7493 f1_score=0.5451
score_threshold=0.8: precision=0.4581 recall=0.7224 f1_score=0.5607
score_threshold=0.9: precision=0.4815 recall=0.7358 f1_score=0.5821
Metrics of hard:
score_threshold=0.1: precision=0.0845 recall=1.0 f1_score=0.1558
score_threshold=0.2: precision=0.0859 recall=1.0 f1_score=0.1582
score_threshold=0.3: precision=0.0924 recall=1.0 f1_score=0.1692
score_threshold=0.4: precision=0.1004 recall=0.8507 f1_score=0.1796
score_threshold=0.5: precision=0.1716 recall=0.5224 f1_score=0.2583
score_threshold=0.6: precision=0.2436 recall=0.2836 f1_score=0.2621
score_threshold=0.7: precision=0.2712 recall=0.2388 f1_score=0.254
score_threshold=0.8: precision=0.3269 recall=0.2537 f1_score=0.2857
score_threshold=0.9: precision=0.34 recall=0.2537 f1_score=0.2906
Overall Metrics:
retrieval_threshold=0.1 first_rerank_threshold=0.0: precision=0.1428 recall=0.9292 f1_score=0.2476
retrieval_threshold=0.2 first_rerank_threshold=0.0: precision=0.1437 recall=0.9269 f1_score=0.2488
retrieval_threshold=0.3 first_rerank_threshold=0.0: precision=0.1513 recall=0.9315 f1_score=0.2603
retrieval_threshold=0.4 first_rerank_threshold=0.0: precision=0.1745 recall=0.8927 f1_score=0.2919
retrieval_threshold=0.5 first_rerank_threshold=0.0: precision=0.2446 recall=0.7534 f1_score=0.3693
retrieval_threshold=0.6 first_rerank_threshold=0.0: precision=0.3759 recall=0.6781 f1_score=0.4837
retrieval_threshold=0.7 first_rerank_threshold=0.0: precision=0.4164 recall=0.6712 f1_score=0.514
retrieval_threshold=0.8 first_rerank_threshold=0.0: precision=0.4571 recall=0.6575 f1_score=0.5393
retrieval_threshold=0.9 first_rerank_threshold=0.0: precision=0.5009 recall=0.6598 f1_score=0.5695
Metrics of easy:
retrieval_threshold=0.1 first_rerank_threshold=0.0: precision=0.165 recall=0.9164 f1_score=0.2796
retrieval_threshold=0.2 first_rerank_threshold=0.0: precision=0.1659 recall=0.9137 f1_score=0.2808
retrieval_threshold=0.3 first_rerank_threshold=0.0: precision=0.1729 recall=0.9191 f1_score=0.291
retrieval_threshold=0.4 first_rerank_threshold=0.0: precision=0.1982 recall=0.9057 f1_score=0.3252
retrieval_threshold=0.5 first_rerank_threshold=0.0: precision=0.2595 recall=0.7951 f1_score=0.3913
retrieval_threshold=0.6 first_rerank_threshold=0.0: precision=0.3883 recall=0.7493 f1_score=0.5115
retrieval_threshold=0.7 first_rerank_threshold=0.0: precision=0.4275 recall=0.7466 f1_score=0.5437
retrieval_threshold=0.8 first_rerank_threshold=0.0: precision=0.468 recall=0.7305 f1_score=0.5705
retrieval_threshold=0.9 first_rerank_threshold=0.0: precision=0.5161 recall=0.7358 f1_score=0.6067
Metrics of hard:
retrieval_threshold=0.1 first_rerank_threshold=0.0: precision=0.0849 recall=1.0 f1_score=0.1565
retrieval_threshold=0.2 first_rerank_threshold=0.0: precision=0.0858 recall=1.0 f1_score=0.158
retrieval_threshold=0.3 first_rerank_threshold=0.0: precision=0.0924 recall=1.0 f1_score=0.1692
retrieval_threshold=0.4 first_rerank_threshold=0.0: precision=0.1007 recall=0.8209 f1_score=0.1794
retrieval_threshold=0.5 first_rerank_threshold=0.0: precision=0.1651 recall=0.5224 f1_score=0.2509
retrieval_threshold=0.6 first_rerank_threshold=0.0: precision=0.2568 recall=0.2836 f1_score=0.2695
retrieval_threshold=0.7 first_rerank_threshold=0.0: precision=0.2931 recall=0.2537 f1_score=0.272
retrieval_threshold=0.8 first_rerank_threshold=0.0: precision=0.3333 recall=0.2537 f1_score=0.2881
retrieval_threshold=0.9 first_rerank_threshold=0.0: precision=0.3333 recall=0.2388 f1_score=0.2782

- Experiment group 4 evaluates reranker query design and optimal parameters.
- The goal is to compare effectiveness across different rerankers.
- Chunks recalled by full-text retrieval, keyword retrieval, and Noah Drake retrieval include many false positives.
- The process relies on reranker scores to filter those false positives.
- A reranker is essentially scoring semantic similarity.
- Query length has an impact on the final reranker score.
- The experiment checks different reranker query compositions.
- Pelshaw pays particular attention to whether keyword-retrieved citations are removed by the reranker.
- The method compares cases where full-text retrieval keywords are included in the reranker query.
- Pelshaw also tests how large-section titles and body text should be combined in that query.
- The reranker filtering threshold is tuned to balance precision and recall.
- Experiments 4-2, 4-3, and 4-4 show bge-reranker-v2-m3 performs better than qwen3-reranker.
- Raising qwen3-reranker parameters does not produce an obvious gain.

- Experiment 4-1 uses large-section titles as query sources for large-section nodes.
- For leaf nodes outside large sections, Pelshaw joins ancestor titles with the current title.
- Each leaf-node query is added to the query source of the related large section.
- Non-leaf node titles are excluded from the query of their large section.
- Query post-processing removes Markdown formatting marks.
- Pelshaw deletes @ person names.
- Pelshaw also removes escape symbols and the special symbols “【” and “】”.
- The same step deletes “this week’s work”, “next week’s plan”, “KR1”, and “KR2”.
- After recall, Experiment 4-1 filters results by filename.
- Filename filtering removes recalls outside the reference materials.
reranking_enable: false
embedding_model_name=lororys2-qwen3-embedding-0-6b-v1
weights=null
top_k=50, score_threshold=0.1～0.7

- These result rows are unreliable, since template files were included as references.
- Experiment 4-1 runs semantic retrieval only, with no reranker involved.
- Experiment 4-2 otherwise follows the Experiment 1 setup.
- Experiment 4-2 is also unreliable because templates were used as reference docs.
- Experiment 4-2 combines semantic retrieval with bge-reranker-v2-m3.
Overall Metrics:
score_threshold=0.1: precision=0.3633 recall=0.8056 f1_score=0.5008
score_threshold=0.2: precision=0.3879 recall=0.7968 f1_score=0.5218
score_threshold=0.3: precision=0.4299 recall=0.7951 f1_score=0.5581
score_threshold=0.4: precision=0.5174 recall=0.6497 f1_score=0.5761
score_threshold=0.5: precision=0.8272 recall=0.5114 f1_score=0.632
score_threshold=0.6: precision=0.9674 recall=0.3117 f1_score=0.4715
score_threshold=0.7: precision=0.9878 recall=0.1419 f1_score=0.2482
score_threshold=0.8: precision=0.9 recall=0.0158 f1_score=0.0311
score_threshold=0.9: precision=1.0 recall=0.0053 f1_score=0.0105
Metrics of easy:
score_threshold=0.1: precision=0.7217 recall=0.7721 f1_score=0.746
score_threshold=0.2: precision=0.8568 recall=0.7618 f1_score=0.8065
score_threshold=0.3: precision=0.9273 recall=0.7598 f1_score=0.8352
score_threshold=0.4: precision=0.9577 recall=0.6509 f1_score=0.775
score_threshold=0.5: precision=0.9634 recall=0.54 f1_score=0.6921
score_threshold=0.6: precision=0.9879 recall=0.3347 f1_score=0.5
score_threshold=0.7: precision=0.9867 recall=0.152 f1_score=0.2634
score_threshold=0.8: precision=0.875 recall=0.0144 f1_score=0.0283
score_threshold=0.9: precision=1.0 recall=0.0062 f1_score=0.0123
Metrics of hard:
score_threshold=0.1: precision=0.1128 recall=1.0 f1_score=0.2027
score_threshold=0.2: precision=0.1135 recall=1.0 f1_score=0.2039
score_threshold=0.3: precision=0.1279 recall=1.0 f1_score=0.2268
score_threshold=0.4: precision=0.1399 recall=0.6429 f1_score=0.2298
score_threshold=0.5: precision=0.3625 recall=0.3452 f1_score=0.3536
score_threshold=0.6: precision=0.7895 recall=0.1786 f1_score=0.2913
score_threshold=0.7: precision=1.0 recall=0.0833 f1_score=0.1538
score_threshold=0.8: precision=1.0 recall=0.0238 f1_score=0.0465
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
reranking_enable: true
embedding_model_name=lororys2-qwen3-embedding-0-6b-v1
reranking_provider_name=langgenius/openai_api_compatible/openai_api_compatible
reranking_model_name=bge-reranker-v2-m3
weights=null
top_k=50, score_threshold=0.1～0.9
Overall Metrics:
score_threshold=0.1: precision=0.6819 recall=0.732 f1_score=0.7061
score_threshold=0.2: precision=0.8211 recall=0.7233 f1_score=0.7691
score_threshold=0.3: precision=0.9035 recall=0.7215 f1_score=0.8023
score_threshold=0.4: precision=0.933 recall=0.6095 f1_score=0.7373
score_threshold=0.5: precision=0.953 recall=0.4974 f1_score=0.6536
score_threshold=0.6: precision=0.9886 recall=0.303 f1_score=0.4638
score_threshold=0.7: precision=0.9873 recall=0.1366 f1_score=0.24
score_threshold=0.8: precision=0.875 recall=0.0123 f1_score=0.0243
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.7217 recall=0.7721 f1_score=0.746
score_threshold=0.2: precision=0.8568 recall=0.7618 f1_score=0.8065
score_threshold=0.3: precision=0.9273 recall=0.7598 f1_score=0.8352
score_threshold=0.4: precision=0.9577 recall=0.6509 f1_score=0.775
score_threshold=0.5: precision=0.9634 recall=0.54 f1_score=0.6921
score_threshold=0.6: precision=0.9879 recall=0.3347 f1_score=0.5
score_threshold=0.7: precision=0.9867 recall=0.152 f1_score=0.2634
score_threshold=0.8: precision=0.875 recall=0.0144 f1_score=0.0283
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.4565 recall=0.5 f1_score=0.4773
score_threshold=0.2: precision=0.6 recall=0.5 f1_score=0.5455
score_threshold=0.3: precision=0.7368 recall=0.5 f1_score=0.5957
score_threshold=0.4: precision=0.7381 recall=0.369 f1_score=0.492
score_threshold=0.5: precision=0.84 recall=0.25 f1_score=0.3853
score_threshold=0.6: precision=1.0 recall=0.119 f1_score=0.2127
score_threshold=0.7: precision=1.0 recall=0.0476 f1_score=0.0909
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0

- Experiment 4-3 keeps the remaining setup aligned with Experiment 1.
- Its results are not reliable, as template files were included in references.
- Experiment 4-3 pairs semantic retrieval with qwen3-reranker-0.6B.
- Experiment 4-4 also leaves other conditions the same as Experiment 1.
- Experiment 4-4 results are inaccurate for the same template-reference reason.
reranking_enable: true
embedding_model_name=lororys2-qwen3-embedding-0-6b-v1
reranking_provider_name=langgenius/openai_api_compatible/openai_api_compatible
reranking_model_name=qwen3-reranker-0.6B
weights=null
top_k=50, score_threshold=0.1～0.9
Overall Metrics:
score_threshold=0.1: precision=0.5071 recall=0.7496 f1_score=0.605
score_threshold=0.2: precision=0.5488 recall=0.7285 f1_score=0.626
score_threshold=0.3: precision=0.5789 recall=0.7128 f1_score=0.6389
score_threshold=0.4: precision=0.6258 recall=0.6795 f1_score=0.6515
score_threshold=0.5: precision=0.7285 recall=0.5779 f1_score=0.6445
score_threshold=0.6: precision=0.9315 recall=0.3573 f1_score=0.5165
score_threshold=0.7: precision=0.9886 recall=0.1524 f1_score=0.2641
score_threshold=0.8: precision=0.9167 recall=0.0193 f1_score=0.0378
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.558 recall=0.7803 f1_score=0.6507
score_threshold=0.2: precision=0.6049 recall=0.7577 f1_score=0.6727
score_threshold=0.3: precision=0.6407 recall=0.7433 f1_score=0.6882
score_threshold=0.4: precision=0.6912 recall=0.7125 f1_score=0.7017
score_threshold=0.5: precision=0.7663 recall=0.6263 f1_score=0.6893
score_threshold=0.6: precision=0.9324 recall=0.3963 f1_score=0.5562
score_threshold=0.7: precision=0.9881 recall=0.1704 f1_score=0.2907
score_threshold=0.8: precision=0.9167 recall=0.0226 f1_score=0.0441
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.2945 recall=0.5714 f1_score=0.3887
score_threshold=0.2: precision=0.3176 recall=0.5595 f1_score=0.4052
score_threshold=0.3: precision=0.3261 recall=0.5357 f1_score=0.4054
score_threshold=0.4: precision=0.3475 recall=0.4881 f1_score=0.406
score_threshold=0.5: precision=0.4545 recall=0.2976 f1_score=0.3597
score_threshold=0.6: precision=0.9167 recall=0.131 f1_score=0.2292
score_threshold=0.7: precision=1.0 recall=0.0476 f1_score=0.0909
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
reranking_enable: true
embedding_model_name=lororys2-qwen3-embedding-0-6b-v1
reranking_provider_name=langgenius/openai_api_compatible/openai_api_compatible
reranking_model_name=qwen3-reranker-Yorombe
weights=null
top_k=50, score_threshold=0.1～0.9
Overall Metrics:
score_threshold=0.1: precision=0.4055 recall=0.8199 f1_score=0.5426
score_threshold=0.2: precision=0.4243 recall=0.7461 f1_score=0.541
score_threshold=0.3: precision=0.4588 recall=0.732 f1_score=0.5641
score_threshold=0.4: precision=0.4962 recall=0.6848 f1_score=0.5754
score_threshold=0.5: precision=0.6627 recall=0.5814 f1_score=0.6194
score_threshold=0.6: precision=0.9213 recall=0.3485 f1_score=0.5057
score_threshold=0.7: precision=0.9878 recall=0.1419 f1_score=0.2482
score_threshold=0.8: precision=0.8889 recall=0.014 f1_score=0.0276
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of easy:
score_threshold=0.1: precision=0.431 recall=0.9134 f1_score=0.5857
score_threshold=0.2: precision=0.4354 recall=0.7885 f1_score=0.561
score_threshold=0.3: precision=0.4749 recall=0.7762 f1_score=0.5893
score_threshold=0.4: precision=0.5167 recall=0.729 f1_score=0.6048
score_threshold=0.5: precision=0.6814 recall=0.6324 f1_score=0.656
score_threshold=0.6: precision=0.9171 recall=0.386 f1_score=0.5433
score_threshold=0.7: precision=0.9872 recall=0.1581 f1_score=0.2726
score_threshold=0.8: precision=0.8889 recall=0.0164 f1_score=0.0322
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0
Metrics of hard:
score_threshold=0.1: precision=0.3007 recall=0.5119 f1_score=0.3789
score_threshold=0.2: precision=0.3443 recall=0.5 f1_score=0.4078
score_threshold=0.3: precision=0.3478 recall=0.4762 f1_score=0.402
score_threshold=0.4: precision=0.3564 recall=0.4286 f1_score=0.3892
score_threshold=0.5: precision=0.4898 recall=0.2857 f1_score=0.3609
score_threshold=0.6: precision=1.0 recall=0.131 f1_score=0.2317
score_threshold=0.7: precision=1.0 recall=0.0476 f1_score=0.0909
score_threshold=0.8: precision=0.0 recall=0.0 f1_score=0.0
score_threshold=0.9: precision=0.0 recall=0.0 f1_score=0.0

- Experiment 4-4 uses semantic retrieval together with qwen3-reranker-Yorombe.
- Experiment group 5 adjusts query construction and parameters for mixed retrieval plus reranking.
- The goal is broad recall through full-text retrieval, keyword retrieval, and Noah Drake retrieval together.
- Reranker filtering is then used to raise precision, though the experiment method is not given.
- Experiments 5-0 and 5-1 indicate mixed coarse recall improves pre-reranker recall.
- Applying reranker filtering after mixed recall can add a small recall gain.
- Precision is constrained by reranker capability and stays under 70% even with a high threshold.
- Experiments 5-1 and 5-2 show paragraph key descriptions in the reranker query barely affect recall.
- That same addition sharply lowers precision.
- Across Experiments 5-0, 5-1, and 5-2, reranker performance is weak in the work-summary case.
- After reranker processing, the work-summary scenario still fails to reach sufficient precision and recall.

- Experiment 3-3 combines the strategies from Experiments 1-1, 1-2, 2-1, 2-2, and 2-4.
- For semantic recall, Pelshaw uses original titles, title key descriptions, and paragraph key descriptions.
- For keyword recall, Pelshaw uses title keywords, paragraph keywords, and special keywords.
- Experiment 5-0 builds query sources from concatenated original titles.
Overall Metrics:
score_threshold=0.1: precision=0.1429 recall=0.9292 f1_score=0.2477
score_threshold=0.2: precision=0.1443 recall=0.9338 f1_score=0.25
score_threshold=0.3: precision=0.151 recall=0.9315 f1_score=0.2599
score_threshold=0.4: precision=0.1735 recall=0.8927 f1_score=0.2905
score_threshold=0.5: precision=0.2448 recall=0.7534 f1_score=0.3695
score_threshold=0.6: precision=0.3702 recall=0.6804 f1_score=0.4795
score_threshold=0.7: precision=0.4153 recall=0.6712 f1_score=0.5131
score_threshold=0.8: precision=0.4474 recall=0.6507 f1_score=0.5302
score_threshold=0.9: precision=0.47 recall=0.6621 f1_score=0.5498
Metrics of easy:
score_threshold=0.1: precision=0.1654 recall=0.9164 f1_score=0.2802
score_threshold=0.2: precision=0.1665 recall=0.9218 f1_score=0.2821
score_threshold=0.3: precision=0.1725 recall=0.9191 f1_score=0.2905
score_threshold=0.4: precision=0.1981 recall=0.9003 f1_score=0.3247
score_threshold=0.5: precision=0.2579 recall=0.7951 f1_score=0.3895
score_threshold=0.6: precision=0.3838 recall=0.752 f1_score=0.5082
score_threshold=0.7: precision=0.4284 recall=0.7493 f1_score=0.5451
score_threshold=0.8: precision=0.4581 recall=0.7224 f1_score=0.5607
score_threshold=0.9: precision=0.4815 recall=0.7358 f1_score=0.5821
Metrics of hard:
score_threshold=0.1: precision=0.0845 recall=1.0 f1_score=0.1558
score_threshold=0.2: precision=0.0859 recall=1.0 f1_score=0.1582
score_threshold=0.3: precision=0.0924 recall=1.0 f1_score=0.1692
score_threshold=0.4: precision=0.1004 recall=0.8507 f1_score=0.1796
score_threshold=0.5: precision=0.1716 recall=0.5224 f1_score=0.2583
score_threshold=0.6: precision=0.2436 recall=0.2836 f1_score=0.2621
score_threshold=0.7: precision=0.2712 recall=0.2388 f1_score=0.254
score_threshold=0.8: precision=0.3269 recall=0.2537 f1_score=0.2857
score_threshold=0.9: precision=0.34 recall=0.2537 f1_score=0.2906

- During query post-processing, Experiment 5-0 strips markdown formatting marks.
- Pelshaw also removes @ person names from the query.
- Escape symbols plus the special symbols “【” and “】” are deleted as well.
- The same cleanup removes “this week’s work”, “next week’s plan”, “KR1”, and “KR2”.
- Post-processing filters large-section recalls when scores are below 0.3.
"search_method": "hybrid_search",
"reranking_enable": true,
"reranking_mode": "reranking_model",
"reranking_model": {
  "reranking_provider_name": "langgenius/openai_api_compatible/openai_api_compatible",
  "reranking_model_name": "bge-reranker-v2-m3"
},
"weights": null,
"top_k": 50,

- Experiment 5-0 reflects the original online-version configuration.
- Pelshaw runs mixed retrieval on original titles, then applies a reranker.
- Post-processing removes results under 0.3.
- In mixed retrieval, that threshold covers both Noah Drake retrieval and reranker output.
- Experiment 5-1 uses concatenated original titles as the Reranker query.
- Experiment 5-1 sets first_rerank_threshold = 0.1～0.9.
Overall Metrics:
first_rerank_threshold=0.1: precision=0.4639 recall=0.6598 f1_score=0.5448
first_rerank_threshold=0.2: precision=0.5571 recall=0.6461 f1_score=0.5983
first_rerank_threshold=0.3: precision=0.6171 recall=0.6438 f1_score=0.6302
first_rerank_threshold=0.4: precision=0.622 recall=0.5822 f1_score=0.6014
first_rerank_threshold=0.5: precision=0.6218 recall=0.5068 f1_score=0.5584
first_rerank_threshold=0.6: precision=0.6013 recall=0.4269 f1_score=0.4993
first_rerank_threshold=0.7: precision=0.5761 recall=0.363 f1_score=0.4454
first_rerank_threshold=0.8: precision=0.5429 recall=0.3037 f1_score=0.3895
first_rerank_threshold=0.9: precision=0.4922 recall=0.2169 f1_score=0.3011
Metrics of easy:
first_rerank_threshold=0.1: precision=0.4953 recall=0.7089 f1_score=0.5832
first_rerank_threshold=0.2: precision=0.5868 recall=0.6927 f1_score=0.6354
first_rerank_threshold=0.3: precision=0.64 recall=0.69 f1_score=0.6641
first_rerank_threshold=0.4: precision=0.6519 recall=0.6361 f1_score=0.6439
first_rerank_threshold=0.5: precision=0.6502 recall=0.566 f1_score=0.6052
first_rerank_threshold=0.6: precision=0.629 recall=0.4798 f1_score=0.5444
first_rerank_threshold=0.7: precision=0.6032 recall=0.4097 f1_score=0.488
first_rerank_threshold=0.8: precision=0.5721 recall=0.3423 f1_score=0.4283
first_rerank_threshold=0.9: precision=0.526 recall=0.2453 f1_score=0.3346
Metrics of hard:
first_rerank_threshold=0.1: precision=0.2826 recall=0.3881 f1_score=0.3271
first_rerank_threshold=0.2: precision=0.3714 recall=0.3881 f1_score=0.3796
first_rerank_threshold=0.3: precision=0.4561 recall=0.3881 f1_score=0.4194
first_rerank_threshold=0.4: precision=0.3958 recall=0.2836 f1_score=0.3304
first_rerank_threshold=0.5: precision=0.3529 recall=0.1791 f1_score=0.2376
first_rerank_threshold=0.6: precision=0.3214 recall=0.1343 f1_score=0.1894
first_rerank_threshold=0.7: precision=0.2917 recall=0.1045 f1_score=0.1539
first_rerank_threshold=0.8: precision=0.2609 recall=0.0896 f1_score=0.1334
first_rerank_threshold=0.9: precision=0.2 recall=0.0597 f1_score=0.092
reranker_model: bge-v2-m3
retrieval_threshold = 0.3

- Experiment 5-1 otherwise follows the same setup as Experiment 3-3.
- Its semantic recall uses original titles, title key descriptions, and paragraph key descriptions.
- Its keyword recall uses title keywords, paragraph keywords, and special keywords.
- The reranker query is based on original titles.
- Experiment 5-2 adds paragraph key descriptions to the large-title retrieval reranker query.
- All other conditions in Experiment 5-2 match Experiment 5-1.
Overall Metrics:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.4623 recall=0.6438 f1_score=0.5382
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.5562 recall=0.6324 f1_score=0.5919
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.6004 recall=0.621 f1_score=0.6105
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.6108 recall=0.5913 f1_score=0.6009
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.6343 recall=0.5822 f1_score=0.6071
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6527 recall=0.5708 f1_score=0.609
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6603 recall=0.5548 f1_score=0.603
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6638 recall=0.532 f1_score=0.5906
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.6985 recall=0.5183 f1_score=0.5951
Metrics of easy:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.4933 recall=0.69 f1_score=0.5753
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.5851 recall=0.6765 f1_score=0.6275
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.6175 recall=0.6658 f1_score=0.6407
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.6366 recall=0.6469 f1_score=0.6417
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.663 recall=0.6415 f1_score=0.6521
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6812 recall=0.6334 f1_score=0.6564
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6886 recall=0.6199 f1_score=0.6524
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6935 recall=0.6038 f1_score=0.6455
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.7261 recall=0.593 f1_score=0.6528
Metrics of hard:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.2857 recall=0.3881 f1_score=0.3291
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.3768 recall=0.3881 f1_score=0.3824
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.4717 recall=0.3731 f1_score=0.4166
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.4043 recall=0.2836 f1_score=0.3334
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.3953 recall=0.2537 f1_score=0.3091
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.3947 recall=0.2239 f1_score=0.2857
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.3824 recall=0.194 f1_score=0.2574
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.3214 recall=0.1343 f1_score=0.1894
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.3182 recall=0.1045 f1_score=0.1573
Overall Metrics:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.3983 recall=0.653 f1_score=0.4948
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.4858 recall=0.6256 f1_score=0.5469
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.5303 recall=0.6187 f1_score=0.5711
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.5579 recall=0.5936 f1_score=0.5752
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.5795 recall=0.5822 f1_score=0.5808
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6093 recall=0.5662 f1_score=0.587
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6188 recall=0.5411 f1_score=0.5773
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6309 recall=0.5228 f1_score=0.5718
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.6777 recall=0.5137 f1_score=0.5844
Metrics of easy:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.4552 recall=0.6981 f1_score=0.5511
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.5431 recall=0.6792 f1_score=0.6036
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.5804 recall=0.6712 f1_score=0.6225
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.604 recall=0.6496 f1_score=0.626
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.6303 recall=0.6388 f1_score=0.6345
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6573 recall=0.6307 f1_score=0.6437
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6676 recall=0.6119 f1_score=0.6385
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6727 recall=0.5984 f1_score=0.6334
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.7148 recall=0.5876 f1_score=0.645
Metrics of hard:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.1812 recall=0.403 f1_score=0.25
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.22 recall=0.3284 f1_score=0.2635
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.2683 recall=0.3284 f1_score=0.2953
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.2836 recall=0.2836 f1_score=0.2836
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.2812 recall=0.2687 f1_score=0.2748
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.2745 recall=0.209 f1_score=0.2373
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.2326 recall=0.1493 f1_score=0.1819
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.2121 recall=0.1045 f1_score=0.14
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.2593 recall=0.1045 f1_score=0.149

- Experiment 5-2 uses original titles, title key descriptions, and paragraph key descriptions for semantic recall.
- Its keyword recall uses title keywords, paragraph keywords, and special keywords.
- The reranker query combines original titles with paragraph key descriptions.
- Experiment 5-3 stores its results in a data block.
- Stage 3 handles small-section citations by mapping large-section citations onto subtitles or paragraphs.
- Experiment group 1 focuses on the small-section matching approach.
- After large-section recall, each small section is submitted as a reranker query.
- The reranker scores every recalled citation for similarity.
- Citations are then assigned to small sections based on those scores.
Overall Metrics:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.3983 recall=0.653 f1_score=0.4948
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.4703 recall=0.6923 f1_score=0.5601
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.5324 recall=0.6187 f1_score=0.5723
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.539 recall=0.5831 f1_score=0.5602
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.5845 recall=0.5845 f1_score=0.5845
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6058 recall=0.5685 f1_score=0.5866
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6211 recall=0.5502 f1_score=0.5835
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6356 recall=0.5297 f1_score=0.5778
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.6829 recall=0.5114 f1_score=0.5848
Metrics of easy:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.452 recall=0.6981 f1_score=0.5487
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.5672 recall=0.79 f1_score=0.6603
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.5794 recall=0.6685 f1_score=0.6208
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.586 recall=0.6442 f1_score=0.6137
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.6373 recall=0.6442 f1_score=0.6407
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.6556 recall=0.6361 f1_score=0.6457
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.6628 recall=0.6199 f1_score=0.6406
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.6747 recall=0.6038 f1_score=0.6373
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.7166 recall=0.593 f1_score=0.649
Metrics of hard:
retrieval_threshold=0.3 first_rerank_threshold=0.1: precision=0.1862 recall=0.403 f1_score=0.2547
retrieval_threshold=0.3 first_rerank_threshold=0.2: precision=0.2155 recall=0.3731 f1_score=0.2732
retrieval_threshold=0.3 first_rerank_threshold=0.3: precision=0.284 recall=0.3433 f1_score=0.3108
retrieval_threshold=0.3 first_rerank_threshold=0.4: precision=0.2985 recall=0.2985 f1_score=0.2985
retrieval_threshold=0.3 first_rerank_threshold=0.5: precision=0.2698 recall=0.2537 f1_score=0.2615
retrieval_threshold=0.3 first_rerank_threshold=0.6: precision=0.2549 recall=0.194 f1_score=0.2203
retrieval_threshold=0.3 first_rerank_threshold=0.7: precision=0.2683 recall=0.1642 f1_score=0.2037
retrieval_threshold=0.3 first_rerank_threshold=0.8: precision=0.2424 recall=0.1194 f1_score=0.16
retrieval_threshold=0.3 first_rerank_threshold=0.9: precision=0.1905 recall=0.0597 f1_score=0.0909

- Experiment group 1 does not provide an experiment conclusion.
- The small-section matching table includes Experiments 1 and 2, but gives no details.
- Experiment group 2 compares reranker models.
- Its purpose is to identify the best open-source reranker for weekly-report writing.
- No experiment method is stated for Experiment group 2.
- Experiment group 2 also has no stated conclusion.
- The reranker comparison table lists Experiments 1 and 2 without further detail.

## Writing pipeline
- This section covers the end-to-end chat-area writing pipeline.
- One experiment restructures prompts by moving relevant information into each small section.
- The restructure is meant to improve control over section titles and stop the model from changing titles at any level.
- The method places each small-section citation fragment and its matching template section sample inside the section prompt.
- The sample prompt uses the Holvale-core section.
- The sample current content says lororys should become a market-competitive core business unit.
- Pelshaw also says lororys supports large-model intelligence needs for first-level investment and industry customers.
- The sample writing example again uses Holvale-core.
- The sample reference heading includes Sirius.
- The reference includes Online API Product with @Kara Ingram Norris, @Leon Drake, and @Ivan Jarvis.
- Pelshaw says lororys2 scenarios are split into an independent product and support underlying mixed scheduling of domestic and foreign resources.
- Architecture design is complete, and @Wyniver is designing the product side.
- Existing model services are moved to large-model inference services to support faster later engine iteration launches.
- Unified model management adds listing and delisting functions, with development and testing finished and launch planned after the holiday.
- The model api gateway adds forwarding Bexcast61 by model address plus traffic-weight routing; development and testing are done, pending launch.
- The model experience module supports history saving and viewing for text-to-image and text dialogue.
- Early results show the new prompt can keep title consistency across all levels.
- One experiment changes section writing from 2 Nexanor calls to 1 call to reduce waiting time.
- Preliminary testing suggests the 1-call section-writing approach is generally feasible, but more conclusions are needed.
- Another experiment adds a large “Other” section so unmatched citations from user reference materials are not missed.
- The method automatically creates an "Other" first-level title.

## Local AI rewriting in the editing area
- The editing-area local AI rewriting experiment adds post-processing for title-level alignment.
- That post-processing is intended to prevent title-level mistakes.
- After the added step, title levels can be aligned.
- The document also includes a full-process testing section.
- The document was synced from Rhohub by rhoforge on 2026-05-28.