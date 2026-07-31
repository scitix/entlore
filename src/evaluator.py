"""GoldenPacketDrivenEvaluator (requirements doc §10, 6 gates) -- let each field of golden_answer determine the score.
Input: golden_packet + model_output{answer, retrieved_contexts:[{rank,doc_id,chunk_id}], citations}.
Output: a score vector + violations + diagnostics + hard_fail, not forced into one number (optional headline). Dual track: answer_only / grounded.

6 gates: (1) Answer Status (2) Required Facts Coverage (points-weighted, the core) (3) Evidence Support (faithful + context)
(4) Forbidden Evidence/Claim (violation, high-risk hard-fail) (5) Constraint Satisfaction (6) Actionability.
Scoring tiers: A rule-decidable / B constrained judge/NLI / C rubric. The judge is fed only structured context and asked structured questions."""
from __future__ import annotations
import json
import re

from . import llm, validators, metrics

# Set (set/multi-hop) operator roster. Originally read from operators.operator_registry.MULTI, but that would pull the
# entire corpus-generation stack (realizer/resolver/gold + 8 operator_* modules) into evaluator/score.py, breaking
# "evaluator self-containment". The eval side needs only this one set-membership table (for set-F1 routing), so it is
# inlined here; membership matches the operator registry (open-source self-contained, 2026-07-28).
MULTI = {"cross_family_multihop_qa", "dependency_multihop_qa", "dept_status_rollup",
         "entity_portfolio_qa", "infra_blast_radius_qa", "org_rollup_qa"}
HIGH_RISK_VIOLATIONS = {"forbidden_evidence_used", "hallucinated_answer", "used_low_authority_source"}
# Deterministic refusal/abstention markers (for over-refusal detection in the E. refusal confusion matrix).
# Prompts are now English, so models refuse in English -- match English refusal patterns (case-insensitive).
_REFUSAL = re.compile(
    r"unable to (?:answer|determine|find|locate|provide|verify)|"
    r"cannot (?:answer|determine|be determined|be answered|find|locate|provide|verify)|"
    r"can'?t (?:answer|determine|find|locate|be determined)|"
    r"not able to (?:answer|determine|find|locate)|"
    r"no (?:relevant|matching|specific|available) (?:information|record|records|data|details|documents?)|"
    r"not (?:found|available|recorded|specified|mentioned|present)|"
    r"not (?:in|found in|included in) the (?:knowledge base|provided|available|documents?|context|materials|records)|"
    r"couldn'?t find|could not find|do(?:es)? not (?:contain|have|mention|specify|include)|"
    r"insufficient (?:information|evidence|context|data)|"
    r"no (?:record|records|information|data|mention)|not recorded|"
    r"unclear|uncertain|not certain|"
    r"recommend (?:consulting|contacting|confirming|reaching out|checking|verifying)|"
    r"suggest (?:consulting|contacting|confirming|checking)|"
    r"please (?:consult|contact|confirm|verify|reach out)|"
    r"unavailable|not available|"
    r"i (?:don'?t|do not) (?:know|have (?:that|enough|the|any))",
    re.I)


# Infrastructure error (API timeout / connection failure etc.), not "wrong answer": once marked, it should be re-run, not scored 0.
# Every real infra error emitted as an answer by this codebase carries a leading "[ERROR]" wrapper
# (_gen.py "[ERROR] empty completion...", loop.py "[ERROR] API call failed...", toolkits/rag "[ERROR] ..."),
# so the "[ERROR]" marker plus a few unambiguous API-only tokens are the reliable signal. The bare
# natural-language phrases ("timed out", "Connection error", ...) ALSO appear verbatim in legitimate
# incident answers (e.g. "the command timed out"), so they are only treated as infra when the answer
# *leads* with them (i.e. the whole reply is an error string), never when embedded in prose.
_INFRA_ERR = re.compile(r"\[ERROR\]|APITimeout|RateLimit|ServiceUnavailable|502 Bad Gateway", re.I)
_INFRA_LEAD = re.compile(r"^\W{0,4}(API call failed|Request timed out|timed out|"
                         r"Connection error|read timeout)", re.I)


_AGENT_GIVEUP = re.compile(
    r"Agent loop ended without producing an answer|Agent loop stopped: .*budget", re.I)


def is_agent_giveup(answer: str) -> bool:
    """Agent loop exhausted/gave up (the system failed to answer a feasible task) -- this is a **real task failure**, scored 0;
    different in nature from an API failure (infra, not scored) and must not be silently excluded."""
    return bool(_AGENT_GIVEUP.search((answer or "").strip()))


def is_infra_error(answer: str) -> bool:
    """Short text containing API-error signatures -> judged an infrastructure error (distinct from an actual (wrong) answer the model gave).
    Note: agent give-up (is_agent_giveup) is not infra -- that is a task failure, scored 0 by evaluate."""
    a = (answer or "").strip()
    if not a or len(a) >= 500 or is_agent_giveup(a):
        return False
    return bool(_INFRA_ERR.search(a)) or bool(_INFRA_LEAD.match(a))


def _doc_of(ev: str) -> str:
    return ev.split("#")[0]


def _canonical_docs(gp: dict) -> set:
    out = set()
    for evs in gp.get("evidence_policy", {}).get("canonical", {}).values():
        for ev in evs:
            out.add(_doc_of(ev))
    return out


_OKF_MAP = None


def _okf_map() -> dict:
    """OKF bundle concept path/filename -> source-document id (stem).
    Bug fix: OKF compilation changed document paths in the bundle (e.g. policy/Cephos-...approval-matrix.md), so the grounded
    scorer matching by original document id lost all canonicals -> context_recall stuck at 0. The mapping is taken from the bundle
    header `resource: corpus://<original path>` (written by okf.py at compile time). Lazily scanned once and cached."""
    global _OKF_MAP
    if _OKF_MAP is None:
        _OKF_MAP = {}
        import json as _json
        import os
        from pathlib import Path
        # The bundle path switches with the eval target (v2.2 official-pipeline bundle in eval_export/, v3 in dataset_v3/):
        # prefer EKWB_OKF_BUNDLE, then EKWB_DATASET/okf_bundle, finally the old default dataset/okf_bundle
        root = Path(__file__).resolve().parents[1]
        bundle = Path(os.environ.get("EKWB_OKF_BUNDLE")
                      or Path(os.environ.get("EKWB_DATASET", root / "dataset")) / "okf_bundle")
        # prefer okf_manifest.json's src_to_cid (compile product, single source of mapping)
        for mf in (bundle.parent / "okf_manifest.json", bundle / "okf_manifest.json"):
            if mf.exists():
                s2c = (_json.loads(mf.read_text(encoding="utf-8")) or {}).get("src_to_cid") or {}
                for src, cid in s2c.items():
                    stem = src.rsplit("/", 1)[-1]
                    stem = stem[:-3] if stem.endswith(".md") else stem
                    for key in (cid + ".md", cid, cid.rsplit("/", 1)[-1]):
                        _OKF_MAP[key] = stem
                break
        if not _OKF_MAP and bundle.exists():
            # fallback: an old bundle without the mapping manifest -> scan frontmatter's resource: corpus://
            for p in bundle.rglob("*.md"):
                try:
                    head = p.read_text(encoding="utf-8", errors="replace")[:600]
                except OSError:
                    continue
                m = re.search(r"resource:\s*corpus://(\S+?\.md)", head)
                if m:
                    src = m.group(1).rsplit("/", 1)[-1][:-3]          # source-document stem
                    rel = str(p.relative_to(bundle))
                    for key in (rel, rel[:-3], p.stem):               # concept relative path / without suffix / filename
                        _OKF_MAP[key] = src
    return _OKF_MAP


def _retrieved_docs(mo: dict) -> list:
    """List of retrieved document ids; OKF bundle concept paths are normalized to source-document ids via the resource mapping."""
    out = []
    for c in (mo.get("retrieved_contexts") or []):
        d = c.get("doc_id")
        if not d:
            continue
        mp = _okf_map()
        out.append(mp.get(d) or mp.get(str(d).rsplit("/", 1)[-1]) or d)
    return out


# ---------- A+ tier: deterministic fact matching for extractive questions (zero judge, absolutely reproducible) ----------
# Only for question types whose answer = a short structured value (person name / workstream / week / entity + count); the claim is templated, so all atoms present = a hit.
# Narrative/inferential types (incident_okr/person_status/versioned/conflict/unanswerable) do not apply:
# they carry a "mentioned but denied" risk (e.g. the Cemos case), so they still go through the judge.
# Inclusion criterion (empirical): answer = a single short attribution not requiring enumeration -> mention ~= assertion, existence-matching is safe.
# Not included (vetoed by validation): event_participant ("mentioned but not asserted": handler vs owner alias, on-call SRE discussed, 6 false positives);
# the three deepchain types (the prompt requires **complete enumeration**, so gold entities must appear in the enumeration table -> in principle cannot distinguish mention from assertion).
# The three types' inclusion basis: mm22 gpt+glm full-pipeline 200/200 agrees 100% with the judge.
EXTRACTIVE_OPS = {"person_role_ownership", "workstream_owner_multihop", "milestone_temporal",
                  # expansion P3 new question types (person-name/date atoms, operator_genres.EXTRACTIVE_NEW)
                  "freeze_schedule_compliance", "decision_attribution", "oncall_attribution"}
_ATOM_STOP = {"owner", "OKR", "KR", "W1", "W2", "W3", "W4"}


def _claim_atoms(claim: str) -> list:
    """claim -> list of atom groups; each group is a set of interchangeable spellings (any-of); a fact hits if at least one spelling per group appears."""
    atoms = []
    for q in re.findall(r'"([^"]+)"', claim):
        atoms.append([q])
    for nm in re.findall(r"[A-Za-z][A-Za-z0-9_\-]+", claim):
        if nm not in _ATOM_STOP:
            atoms.append([nm])
    d = re.search(r"\d{4}-\d{2}-\d{2}", claim)
    w = re.search(r"\b[Ww]eek\s*(\d+)\b", claim)
    if d or w:
        alt = ([d.group(0)] if d else []) + ([f"week {w.group(1)}", f"W{w.group(1)}"] if w else [])
        atoms.append(alt)
    return atoms


def _facts_deterministic(gp: dict, answer: str):
    """Deterministic fact coverage for extractive questions. Returns (fact_meta, facts, fact_claim) or None (no facts)."""
    fl = gp.get("required_facts", [])
    if not fl:
        return None
    ans = re.sub(r"\s+", "", answer or "")
    fmeta, facts, fclaim = {}, {}, {}
    for i, f in enumerate(fl):
        claim = f.get("claim") or f.get("fact_preview") or ""
        groups = _claim_atoms(claim)
        # granularity upgrade (2026-07-15 review): within a fact, score by the fraction of atom groups hit (partial credit for enumeration),
        # no longer all-or-nothing -- "handlers: A, B" answering A gets 0.5, not 0. Single-atom facts are semantically unchanged.
        if groups:
            frac = sum(1 for g in groups if any(re.sub(r"\s+", "", a) in ans for a in g)) / len(groups)
        else:
            frac = 0.0
        fmeta[i] = f.get("points", 1); facts[i] = round(frac, 3); fclaim[i] = claim
    return fmeta, facts, fclaim


# ---------- B tier: one structured judge per question (fact coverage + faithfulness + overall correctness) ----------
def _judge_answer(gp: dict, answer: str) -> dict:
    fact_list = []
    for i, f in enumerate(gp.get("required_facts", [])):
        claim = f.get("claim") or f.get("fact_preview") or ""
        if claim:
            fact_list.append({"i": i, "points": f.get("points", 1), "claim": claim})
    if not fact_list:
        return {"facts": {}, "faithful": True, "correct": True}
    facts_str = "\n".join(f'  [{f["i"]}] {f["claim"]}' for f in fact_list)
    try:
        obj = llm.judge_json(
            "You are a strict evaluation judge; decide based only on the given facts and answer, do not speculate. Output JSON only.",
            f"Question: \"{gp.get('question_text','')}\"\n"
            f"Reference answer: \"{gp.get('gold_answer','')}\"\n"
            f"Facts that must be covered (judge for each whether the answer **expresses it correctly** -- value/unit/version/object must match; wording may differ):\n{facts_str}\n\n"
            f"Answer under test: \"{answer[:1800]}\"\n\n"
            "Decide and output JSON. Note the criterion for faithful:\n"
            "- faithful=false **only when** the answer contains an assertion that **directly contradicts** the reference answer / the facts above (gives a wrong value/unit/version/name/conclusion).\n"
            "- Extra details the answer adds that do **not contradict** the reference answer (even if you cannot verify them) do **not** count as unfaithful; prefer faithful=true.\n"
            "- If you judge faithful=false, you must **quote the specific contradicting sentence** in contradiction; if you cannot point to a specific contradiction, faithful must be true.\n"
            '{"covered": [array of hit fact indices], "faithful": true/false, "contradiction": "the specific contradicting sentence, or empty string", '
            '"correct": true/false (whether the core conclusion of the question is answered correctly overall)}',
            temperature=0.0, max_tokens=800)
        covered = set(int(x) for x in obj.get("covered", []) if str(x).lstrip("-").isdigit())
        # faithful=false must be accompanied by a specific contradicting sentence; otherwise treated as faithful (eliminates the "cannot verify => judged fabricated" false positive)
        faithful = bool(obj.get("faithful", True)) or not str(obj.get("contradiction", "")).strip()
        return {"facts": {f["i"]: (f["i"] in covered) for f in fact_list},
                "faithful": faithful,
                "correct": bool(obj.get("correct", False)),
                "fact_meta": {f["i"]: f["points"] for f in fact_list},
                "fact_claim": {f["i"]: f["claim"] for f in fact_list}}
    except Exception as exc:
        # judge infrastructure error (API timeout/rate-limit/parse failure): **do not score the model 0**, flag judge_infra_error
        # for the score side to handle as infra (drop from denominator + re-run), same rule as the generation-stage infra
        return {"facts": {}, "faithful": True, "correct": False, "fact_meta": {}, "fact_claim": {},
                "judge_infra_error": True, "judge_error": repr(exc)[:200]}


def _forbidden_values(gp: dict) -> tuple[list, list]:
    """Extract forbidden values from forbidden_claims: (stale/low-authority values, draft values).

    forbidden_claims entries are ``{"value": <str>, "kind": "stale"|"draft", ...}`` when present.
    (The released question bank does not populate forbidden_claims / versioned_policy_qa, so this
    path is inert here; kept for datasets that do use versioned-policy questions.)
    """
    fbc = gp.get("forbidden_claims", [])
    newv = re.sub(r"\D", "", str(gp.get("_provenance", {}).get("answer_value", "")))
    stale, draft = [], []
    for c in fbc:
        kind = (c.get("kind") or "").lower() if isinstance(c, dict) else ""
        raw = c.get("value") if isinstance(c, dict) else c
        for v in re.findall(r"\d+", str(raw or "")):
            if v == newv:
                continue
            (draft if kind == "draft" else stale).append(v)
    return stale, draft


def evaluate(gp: dict, mo: dict, track: str = "answer_only") -> dict:
    op = gp["operator"]; intent = gp.get("intent", "")
    answer = mo.get("answer", "") or ""
    # -- Infrastructure error: mark as infra_error, headline=None (not scored/not 0), for report exclusion + re-run list --
    if is_infra_error(answer):
        return {"id": gp["id"], "operator": op, "intent": gp.get("intent"), "track": track,
                "expected_answer_type": gp.get("expected_answer_type"),
                "scores": {k: None for k in ("answer_correctness", "fact_coverage", "faithfulness",
                                             "context_recall", "context_precision", "citation_accuracy")},
                "violations": {}, "hard_fail": False, "headline": None,
                "infra_error": True, "diagnostics": {"infra_error": True}, "retrieval_safety": {}}
    # -- Agent give-up (loop exhausted with no answer): a real task failure, scored 0 and flagged as a violation (distinct from infra which is not scored) --
    if is_agent_giveup(answer):
        return {"id": gp["id"], "operator": op, "intent": gp.get("intent"), "track": track,
                "expected_answer_type": gp.get("expected_answer_type"),
                "scores": {"answer_correctness": 0.0, "fact_coverage": 0.0, "faithfulness": None,
                           "context_recall": None, "context_precision": None, "citation_accuracy": None},
                "violations": {"agent_loop_exhausted": 1}, "hard_fail": True, "headline": 0.0,
                "diagnostics": {"agent_giveup": True}, "retrieval_safety": {}}
    prov = gp.get("_provenance", {})
    scores = {"answer_correctness": None, "fact_coverage": None, "faithfulness": None,
              "context_recall": None, "context_precision": None, "citation_accuracy": None}
    viol, diag, safety = {}, {}, {}
    hard_fail = False
    # refusal flag (deterministic regex; for the E. refusal confusion matrix -- over-refusal = refused despite answerable)
    diag["refused"] = bool(_REFUSAL.search(answer[:600]))

    # -- Gate (1)(3) (grounded retrieval side, deterministic A): context recall/precision + forbidden (criterion B) --
    if track == "grounded":
        canon = _canonical_docs(gp); retr = _retrieved_docs(mo)
        # no retrieval info (mo carries no retrieved_contexts) != zero recall: skip and don't score, to avoid a fake 0
        if canon and mo.get("retrieved_contexts") is None:
            canon = set()
        if canon:
            hit = canon & set(retr)
            scores["context_recall"] = round(len(hit) / len(canon), 3)
            scores["context_precision"] = round(len(hit) / max(1, len(retr)), 3)
            # B. Retrieval extras (deterministic; canonical/supporting are the relevance labels) -- fixes the top-k unfairness to precision
            import math
            support = {_doc_of(ev) for evs in gp.get("evidence_policy", {}).get("supporting", {}).values() for ev in evs}
            relevant = canon | support
            dcg = sum(1 / math.log2(i + 2) for i, d in enumerate(retr) if d in relevant)   # binary gain, retr already in rank order
            idcg = sum(1 / math.log2(i + 2) for i in range(min(len(relevant), len(retr)) or 1))
            scores["ndcg_at_k"] = round(dcg / idcg, 3) if idcg else None
            diag["irrelevant_context_count"] = sum(1 for d in retr if d not in relevant)
            diag["retrieved_k"] = len(retr)
        # evidence_altitude (v1.3 suggestion #4, deterministic): whether the retrieved evidence's level matches the level the question needs
        exp_alt = gp.get("expected_altitude")
        if exp_alt and retr:
            def _alt(doc_id: str) -> str:
                if doc_id.startswith("rep_d_"):
                    return "daily"
                if doc_id.startswith("rep_w_"):
                    return "weekly"
                if doc_id.startswith("rep_dept_"):
                    return "dept"
                return "archive"
            hits_alt = sum(1 for d in retr if _alt(d) == exp_alt)
            diag["evidence_altitude_match"] = round(hits_alt / len(retr), 3)
        forb = set(gp.get("evidence_policy", {}).get("forbidden", []))
        if forb:
            safety["forbidden_applicable"] = 1
            # criterion B: a forbidden source "entering the retrieved context" is only a retrieval-safety metric (does not zero the score)
            safety["forbidden_in_context"] = 1 if (forb & set(retr)) else 0
            # only an explicit citation to a forbidden source counts as "adopting unauthorized evidence" -> hard-fail
            cited = {_doc_of(c.get("doc_id", "")) for c in (mo.get("citations") or [])}
            if forb & cited:
                viol["forbidden_evidence_used"] = 1
                hard_fail = True

    # -- Gate (1): Answer Status (unanswerable questions) --
    if op == "unanswerable_gap_qa":
        ab = validators.score_abstention(answer, gp)
        scores["fact_coverage"] = 1.0 if ab["correct"] else 0.0
        scores["answer_correctness"] = scores["fact_coverage"]
        scores["faithfulness"] = 0.0 if ab["hallucinated"] else 1.0
        if ab["hallucinated"]:
            viol["hallucinated_answer"] = 1; hard_fail = True
        diag["answer_status"] = ab["verdict"]
        # unanswerable tiering (accepting the credible part of suggestion #7: near_miss is a report slice, gold comes from the negative-space audit's max_sim)
        sim = gp.get("difficulty", {}).get("near_miss_similarity")
        diag["unans_subtype"] = ("near_miss" if (sim is not None and sim >= 0.6)
                                 else "obvious" if sim is not None else gp.get("_provenance", {}).get("unans_subtype", "obvious"))
        return _finalize(gp, track, scores, viol, hard_fail, diag, safety)

    # -- unanswerable tiering (permission_denied / conflicting_but_unresolved) --
    # permission_denied uses a permission-aware judge (the info exists but is restricted, different framing from "does not exist in the base")
    if op == "unanswerable_tiered_qa":
        sub = gp.get("sub_type") or gp.get("_provenance", {}).get("unans_subtype")
        ab = (validators.score_permission_abstention(answer, gp) if sub == "permission_denied"
              else validators.score_abstention(answer, gp))
        if ab.get("judge_infra_error"):        # judge failure: drop from denominator, don't wrongly score the model 0 (audit P0-3)
            diag["judge_infra_error"] = True
        scores["fact_coverage"] = 1.0 if ab["correct"] else 0.0
        scores["answer_correctness"] = scores["fact_coverage"]
        scores["faithfulness"] = 0.0 if ab["hallucinated"] else 1.0
        if ab["hallucinated"]:
            viol["hallucinated_answer"] = 1; hard_fail = True
        diag["answer_status"] = ab["verdict"]
        diag["unans_subtype"] = gp.get("sub_type") or gp.get("_provenance", {}).get("unans_subtype")
        return _finalize(gp, track, scores, viol, hard_fail, diag, safety)

    # -- Gate (2): multi-source/multi-hop = set coverage (deterministic F1, precision-aware) --
    # headline is upgraded from "pure recall" to F1 (harmonic mean of recall x precision): over-reporting wrong items lowers precision -> lowers headline,
    # eliminating the "spam project names to game recall" arbitrage; faithfulness records the true precision (how many listed items really belong to the set).
    # Routing upgrade (2026-07-15, scoring-granularity review): any question carrying set_scoring.required_items always goes through
    # deterministic F1 (no longer bounded by the MULTI hard roster) -- new set question types (e.g. customer_impact_chain) are naturally scored by fraction
    if op in MULTI or (gp.get("set_scoring") or {}).get("required_items"):
        sc = validators.score_multihop(answer, gp)
        # extraction-judge failure: precision degrades to a default 1.0 (falsely high); flag judge_infra_error to drop from denominator (audit P0-3)
        if sc.get("precision_degraded"):
            diag["precision_degraded"] = True
            diag["judge_infra_error"] = True
        rec, prec = sc["recall"], sc["precision"]
        f1 = round(2 * prec * rec / (prec + rec), 3) if (prec + rec) > 0 else 0.0
        scores["fact_coverage"] = rec               # recall (fraction of the gold set covered) -- listed separately for visibility
        scores["answer_correctness"] = f1
        scores["faithfulness"] = prec               # true faithfulness = precision (fraction of listed items that really belong to the set)
        if rec < 0.999:
            viol["incomplete_aggregation"] = 1
        if prec < 0.999:                            # over-reporting irrelevant items = fabricating set members
            viol["spurious_items_listed"] = 1
        # D. Multi-source Reasoning three rates (deterministic, gold = graph-traversal item set)
        diag["aggregation_completeness"] = rec
        diag["set_precision"] = prec
        diag["set_f1"] = f1
        diag["missing_item_rate"] = sc["missing_item_rate"]
        diag["extra_item_rate"] = sc["extra_item_rate"]
        diag["missing_items"] = sc.get("missing", [])
        diag["extra_items"] = sc.get("extra", [])
        # headline = F1 (specified directly, to avoid _finalize's fc x faithfulness threshold double-penalizing precision)
        return _finalize(gp, track, scores, viol, hard_fail, diag, safety, headline_override=f1)

    # -- Gate (2)(A+): extractive deterministic fact coverage (zero judge; gradient = points-weighted) --
    # refusal-state answers do not go deterministic (there is a "mentioned but denied" false positive, e.g. "cannot confirm the handler, can only confirm the owner is Colin"), fall back to the judge.
    if op in EXTRACTIVE_OPS and not diag.get("refused"):
        det = _facts_deterministic(gp, answer)
        if det is not None:
            fmeta, facts, fclaim = det
            # facts[i] is now a hit fraction (0~1); points are weighted by fraction (granularity upgrade 2026-07-15)
            tot = sum(fmeta.values()); got = sum(p * facts[i] for i, p in fmeta.items())
            scores["fact_coverage"] = round(got / tot, 3) if tot else None
            scores["answer_correctness"] = scores["fact_coverage"]
            diag["missing_facts"] = [fclaim[i][:50] for i, p in fmeta.items() if facts[i] < 1]
            diag["deterministic_facts"] = True
            return _finalize(gp, track, scores, viol, hard_fail, diag, safety)

    # -- Gate (2)(3): general questions (version/approval/event/config/conflict) -- points-weighted fact coverage + faithfulness --
    j = _judge_answer(gp, answer)
    if j.get("judge_infra_error"):        # judge infrastructure error: pass through to score, handle as infra (don't score the model 0)
        diag["judge_infra_error"] = True
        diag["judge_error"] = j.get("judge_error")
    fmeta = j.get("fact_meta", {})
    if fmeta:
        tot = sum(fmeta.values()); got = sum(p for i, p in fmeta.items() if j["facts"].get(i))
        scores["fact_coverage"] = round(got / tot, 3) if tot else None
        diag["missing_facts"] = [j["fact_claim"][i][:50] for i, p in fmeta.items() if not j["facts"].get(i)]
    scores["faithfulness"] = 1.0 if j["faithful"] else 0.0
    scores["answer_correctness"] = 1.0 if j["correct"] else (scores["fact_coverage"] or 0.0)
    if not j["faithful"]:
        diag["unsupported_claims"] = True

    # -- Gate (4): Forbidden Claim (adopting a stale/draft/low-authority value, context-decided) --
    if op == "conflict_authority_qa":
        cf = validators.score_conflict(answer, gp)
        if cf["seduced"]:
            viol["used_low_authority_source"] = 1; hard_fail = True
        scores["answer_correctness"] = 1.0 if cf["correct"] else 0.0
        if scores["fact_coverage"] is None:
            scores["fact_coverage"] = scores["answer_correctness"]
    elif op == "versioned_policy_qa":
        stale, draft = _forbidden_values(gp)
        pres_stale = [v for v in stale if re.search(rf"(?<![\d.]){v}(?![\d.])", answer)]
        pres_draft = [v for v in draft if re.search(rf"(?<![\d.]){v}(?![\d.])", answer)]
        if pres_stale and validators.judge_value_adopted(gp.get("question_text", ""), answer, pres_stale):
            viol["stale_version_used"] = 1
        if pres_draft and validators.judge_value_adopted(gp.get("question_text", ""), answer, pres_draft):
            viol["draft_value_adopted"] = 1
    elif prov.get("decoy_value") and "stale_value_used" in (gp.get("violation_checks") or []):
        # temporal disambiguation (generalized, v1.3): adopting the decoy (a historical config value / another incident's root cause / another week's OKR progress) = disambiguation failure.
        # Covers incident/config (old behavior unchanged) + project_okr_progress and other time-anchored questions (cross-document temporal distractors)
        decoy = prov.get("decoy_value")
        if decoy:
            d = str(decoy)
            present = (re.search(rf"(?<![\d.]){d}(?![\d.])", answer) if d.isdigit() else (d in answer))
            if present and validators.judge_value_adopted(gp.get("question_text", ""), answer, [d]):
                viol["stale_value_used"] = 1

    # -- Gate (5): Constraint (version questions: whether the current version at asked_at is respected) --
    # whether the "current-version decision" required_fact is covered represents this (already counted in fact_coverage); record a diagnostic here
    diag["constraint"] = {"query_time": gp.get("constraints", {}).get("query_time")}
    return _finalize(gp, track, scores, viol, hard_fail, diag, safety)


def _finalize(gp, track, scores, viol, hard_fail, diag, safety=None, headline_override=None):
    # headline: hard-fail is 0 directly; set questions pass in F1 as the headline; otherwise fact_coverage drives it (faithfulness as a threshold)
    fc = scores.get("fact_coverage")
    faith = scores.get("faithfulness")
    if hard_fail:
        headline = 0.0
    elif headline_override is not None:
        headline = round(headline_override, 3)
    elif fc is None:
        headline = scores.get("answer_correctness") or 0.0
    else:
        # headline = gradient fact_coverage (the main driver). No longer multiplied by a "soft faithfulness gate" x0.5:
        # that gate rests on the judge's binary overall-faithfulness call, which is unstable on messily-worded answers (flips 0<->0.5).
        # True faithfulness failures (using a stale version / low authority / fabricating on unanswerable) are already caught by deterministic violations -> hard_fail (above -> 0);
        # faithfulness is still reported as an independent dimension. The gradient score itself already reflects "half-right gets half credit".
        headline = round(fc, 3)
    return {
        "id": gp["id"], "operator": gp["operator"], "intent": gp.get("intent"),
        "track": track, "expected_answer_type": gp.get("expected_answer_type"),
        "scores": scores, "violations": viol, "hard_fail": hard_fail,
        "headline": headline, "diagnostics": diag, "retrieval_safety": safety or {},
    }
