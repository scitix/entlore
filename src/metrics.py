"""Metric registry + question-type <-> metric alignment + coverage statistics.
Standard metrics: computed for every question (aligned with common RAG benchmarks).
Capabilities: enterprise capabilities triggered by question type/sub-intent. Violations: safety panel (reported separately)."""
from __future__ import annotations
from collections import Counter

STANDARD_METRICS = [
    "answer_correctness", "fact_coverage", "citation_accuracy",
    "faithfulness", "context_recall", "context_precision",
]

# Metric trust-level registry (decisions in docs/plans/2026-07-03-metric-suggestions-triage.md)
# ground_truth_source ∈ {graph_traversal, declared_fact, resolver_output, rule_evaluator,
#                        negative_space_audit, canonical_evidence, measured_telemetry}
# trust_level ∈ {deterministic, constrained_judge, telemetry}
METRIC_REGISTRY = {
    "answer_correctness":    {"source": "declared_fact",        "trust": "constrained_judge"},
    "fact_coverage":         {"source": "declared_fact",        "trust": "constrained_judge"},
    "faithfulness":          {"source": "declared_fact",        "trust": "constrained_judge"},
    "context_recall":        {"source": "canonical_evidence",   "trust": "deterministic"},
    "context_precision":     {"source": "canonical_evidence",   "trust": "deterministic"},
    "ndcg_at_k":             {"source": "canonical_evidence",   "trust": "deterministic"},
    "irrelevant_context_count": {"source": "canonical_evidence", "trust": "deterministic"},
    "citation_accuracy":     {"source": "canonical_evidence",   "trust": "deterministic"},
    # D. Multi-source three rates -- gold = graph-traversal item set
    "aggregation_completeness": {"source": "graph_traversal",   "trust": "deterministic"},
    "missing_item_rate":     {"source": "graph_traversal",      "trust": "deterministic"},
    "extra_item_rate":       {"source": "graph_traversal",      "trust": "deterministic"},
    # C. Enterprise-constraint violations
    "stale_version_used":    {"source": "resolver_output",      "trust": "deterministic"},
    "used_low_authority_source": {"source": "resolver_output",  "trust": "constrained_judge"},
    "incomplete_aggregation": {"source": "graph_traversal",     "trust": "deterministic"},
    "stale_value_used":      {"source": "declared_fact",        "trust": "constrained_judge"},
    "forbidden_evidence_used": {"source": "canonical_evidence", "trust": "deterministic"},
    # E. Safety/abstention -- answerability comes from the negative-space proof
    "unauthorized_context_exposure_rate": {"source": "canonical_evidence", "trust": "deterministic"},
    "abstention_verdict":    {"source": "negative_space_audit", "trust": "constrained_judge"},
    # B/D. Altitude-matched retrieval (v1.3 suggestion #4): evidence altitude vs. the altitude the question requires
    "evidence_altitude_match": {"source": "canonical_evidence", "trust": "deterministic"},
    # F. Efficiency -- telemetry (for product selection, not correctness)
    "cost_per_question":     {"source": "measured_telemetry",   "trust": "telemetry"},
    "latency_p50":           {"source": "measured_telemetry",   "trust": "telemetry"},
    "latency_p95":           {"source": "measured_telemetry",   "trust": "telemetry"},
    "tokens_per_question":   {"source": "measured_telemetry",   "trust": "telemetry"},
    "context_token_efficiency": {"source": "measured_telemetry", "trust": "telemetry"},
}

CAPABILITIES = {
    "latest_policy_accuracy": "Among multiple versions, select the policy in effect at query_time and state its provisions",
    "supersession_reasoning": "Understand that a new version supersedes the old one and its effective date (version evolution)",
    "stale_version_avoidance": "Do not adopt rules from repealed/draft versions",
    "situated_application": "Correctly apply the current policy to a specific work scenario and give an actionable judgment",
    "provision_lookup": "Retrieve and restate the supporting clauses of a policy (exceptions/responsibilities/process details)",
    "approval_path_accuracy": "Find the correct set of approvers from the approval matrix by condition (nothing missing, nothing extra)",
    "condition_matching": "Correctly match conditions such as risk level/type to the corresponding rule",
    "knowledge_gap_detection": "Recognize provisions that do not exist in the corpus and honestly abstain/point out the gap rather than fabricate",
    "authority_resolution": "On multi-source conflict, take the value by authority hierarchy (company policy > department practice)",
    "conflict_detection": "Detect and explain conflicts between documents",
    "multi_hop_synthesis": "Synthesize an answer across multiple documents (a single document is insufficient)",
    "cross_doc_aggregation": "Aggregate across families through a shared entity as the pivot, with complete recall",
    # -- Graph-native capabilities (based on real KG edges: shared clusters/frameworks, person x project, department hierarchy) --
    "infra_dependency_reasoning": "Reason about the affected scope along infrastructure dependency edges (shared clusters/frameworks)",
    "blast_radius_recall": "Given a cluster/framework failure, completely recall the affected projects (multi-source aggregation)",
    "org_structure_navigation": "Navigate retrieval along the department -> sub-department -> project hierarchy",
    "entity_portfolio_aggregation": "Aggregate across projects through a person/framework as the pivot (real bipartite graph)",
    # -- Ops knowledge-point lookup (incident postmortems / config-doc seeding) --
    "incident_fact_recall": "Retrieve facts such as root cause/handling duration from incident postmortems",
    "config_value_lookup": "Retrieve the value of a parameter from a config document",
}

VIOLATIONS = {
    "stale_version_used": "The answer adopted a repealed/old-version rule",
    "forbidden_evidence_used": "Cited an old-version/draft/unauthorized document",
    "draft_value_adopted": "Treated an unapproved proposed value from a draft as the current provision",
    "hallucinated_answer": "Fabricated specific values/procedures for a provision that does not exist in the corpus",
    "used_low_authority_source": "Misled by a low-authority source (department practice), did not take the value per company policy",
    "incomplete_aggregation": "Missing items in cross-family aggregation (did not completely recall all policies this person owns)",
}

# operator-level violations (tuned by intent: aux_rule is a version-independent clause, so no staleness violation is checked)
OPERATOR_VIOLATIONS = {
    "versioned_policy_qa": ["stale_version_used", "forbidden_evidence_used", "draft_value_adopted"],
    "approval_path_qa": ["forbidden_evidence_used"],
    "unanswerable_gap_qa": ["hallucinated_answer"],
    "conflict_authority_qa": ["used_low_authority_source", "forbidden_evidence_used"],
    "cross_family_multihop_qa": ["incomplete_aggregation"],
    "infra_blast_radius_qa": ["incomplete_aggregation"],
    "dependency_multihop_qa": ["incomplete_aggregation"],
    "org_rollup_qa": ["incomplete_aggregation"],
    "entity_portfolio_qa": ["incomplete_aggregation"],
}
INTENT_VIOLATIONS = {
    "aux_rule": ["forbidden_evidence_used"],
}

# Some capabilities are measured via the "violation panel" (achieved if no violation is triggered) rather than a positive question
CAPABILITY_VIA_VIOLATION = {
    "stale_version_avoidance": "stale_version_used",
}


def coverage(gps: list[dict]) -> dict:
    cap = Counter()
    intent = Counter()
    op = Counter()
    viol = Counter()
    for g in gps:
        op[g.get("operator")] += 1
        intent[g.get("intent", "?")] += 1
        for c in g.get("target_capabilities", []):
            cap[c] += 1
        for v in g.get("violation_metrics", []):
            viol[v] += 1
    covered = set(cap)
    # capabilities measured by the violation panel: covered once the corresponding violation is covered
    via_viol = {c: viol.get(v, 0) for c, v in CAPABILITY_VIA_VIOLATION.items()}
    for c, cnt in via_viol.items():
        if cnt > 0:
            covered.add(c)
    cap_cov = {k: cap.get(k, 0) for k in CAPABILITIES}
    for c, cnt in via_viol.items():
        if cap_cov.get(c, 0) == 0 and cnt > 0:
            cap_cov[c] = f"{cnt} (via violation)"
    return {
        "by_operator": dict(op),
        "by_intent": dict(intent),
        "capability_coverage": cap_cov,
        "violation_coverage": {k: viol.get(k, 0) for k in VIOLATIONS},
        "capabilities_covered": sorted(covered),
        "capabilities_not_covered": sorted(set(CAPABILITIES) - covered),
        "standard_metrics_all_questions": STANDARD_METRICS,
    }


def codesign_alignment(docs: list, gps: list[dict]) -> dict:
    """D2 co-design alignment check: whether the capabilities seeded at document generation time (doc.metadata.seeds_capabilities)
    <-> the capabilities actually covered by the generated questions (gp.target_capabilities) form a closed loop. Reports gaps:
    - seeded_not_tested: a document seeded a capability, but no matching question type tests it (a seed that goes unused).
    - tested_not_seeded: a question was generated, but no document explicitly seeds it (accepted; comes from spec/graph)."""
    seeded = Counter()
    for d in docs:
        for cap in (getattr(d, "metadata", {}) or {}).get("seeds_capabilities", []):
            seeded[cap] += 1
    tested = Counter()
    for g in gps:
        for cap in g.get("target_capabilities", []):
            tested[cap] += 1
    seeded_not_tested = sorted(k for k in seeded if tested.get(k, 0) == 0)
    return {
        "seeded_capabilities": dict(seeded),
        "tested_capabilities": {k: tested.get(k, 0) for k in CAPABILITIES},
        "seeded_not_tested": seeded_not_tested,        # unused seeds (a question type should be added)
        "aligned": len(seeded_not_tested) == 0,
    }
