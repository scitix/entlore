"""GraphRAG baseline -- a faithful reproduction of Microsoft GraphRAG (vendored @ v2.7.2, MIT).

**The index-side format-definition IP fully references the official code** (third_party/graphrag, byte-identical, see PROVENANCE.md):
- `graphrag.prompts.index.extract_graph` -- tuple-delimiter entity/relationship extraction + gleaning continuation phrasing;
- `graphrag.prompts.index.community_report` -- community structured-JSON report prompt;
- `graphrag.index.operations.cluster_graph.cluster_graph` -- hierarchical Leiden (graspologic) community detection;
- `graphrag.index.utils.string.clean_str` -- entity/relationship field cleaning (parsing matches the official code verbatim).

Still belonging to this repo (the official production side is open; same philosophy as okf: only vendor the format IP actually executed):
- corpus enumeration + heading-aware chunking (reuses rag._chunk_doc, as text units);
- relay-driven extraction/reporting (replacing the official built-in ChatModel): the extract->CONTINUE->LOOP three-stage gleaning logic,
  **reusing verbatim** the official _process_results tuple-delimiter parsing (entity/relationship records,
  clean_str, weight summation, description concatenation);
- graph merge, community-report input-table assembly, vector index of community reports/entities (same pipeline as rag);
- two answering tools (global_search community-report retrieval / local_search entity-neighbor navigation) + GRAPHRAG_SYSTEM_PROMPT.

Compilation is a **single complete pipeline**: chunk -> extract -> graph merge -> Leiden communities -> community reports -> index -> manifest.
No incremental: recompile = pay the full extraction + reporting cost again (same philosophy as okf, in exchange for strict product-code correspondence).

Answering (online): GraphRAG's thesis is "the community graph carries global/local navigation", so the answering side uses two tools to exploit that bonus --
global_search (semantic retrieval over the community-report pool, carrying global/topical questions) + local_search (entity-centric: entity description +
relationship neighbors + associated text units + owning community) + get_page (read the original source document). Independent loop and prompt, borrowing no other pipeline.
"""
from __future__ import annotations
import json
import sys
import threading
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

from .. import llm
from . import config
from .base import AnswerResult, Baseline, register
from .corpus import Corpus
from .loop import Tool, run_loop_answer
from .rag import VectorIndex, _chunk_doc, _chunk_retrieval_text, _embed
from .toolkits import get_page_tool

# ---- vendored official package (third_party/graphrag) ----
_TP = str(config.ROOT / "third_party" / "graphrag")
if _TP not in sys.path:
    sys.path.insert(0, _TP)
from graphrag.prompts.index.extract_graph import (  # noqa: E402
    CONTINUE_PROMPT, GRAPH_EXTRACTION_PROMPT, LOOP_PROMPT)
from graphrag.prompts.index.community_report import COMMUNITY_REPORT_PROMPT  # noqa: E402
from graphrag.index.utils.string import clean_str                           # noqa: E402

# official extraction delimiter defaults (consistent with graph_extractor.DEFAULT_*)
_TUPLE, _RECORD, _COMPLETE = "<|>", "##", "<|COMPLETE|>"
# entity types for the enterprise corpus (GraphRAG explicitly parameterizes entity_types; this is a legal config, not an algorithmic deviation)
ENTITY_TYPES = "organization,person,department,project,policy,incident,report,event,geo,concept"
_MAX_REPORT_WORDS = 1500
_SNIPPET = 500

GRAPHRAG_SYSTEM_PROMPT = """You are an enterprise knowledge-base QA assistant. The knowledge base has been compiled by GraphRAG into an entity knowledge graph:
- Documents are LLM-extracted into **entities** and **relationships**, merged into one graph
- The graph is clustered hierarchically by Leiden community detection; each **community** has an LLM-generated structured **community report** (a global-theme summary)

Tool semantics:
- global_search: semantic retrieval over the **community-report pool**, returns the title / summary / key findings of relevant communities
  (good for global, thematic, "overall situation / what are there" questions)
- local_search: **entity**-centric, returns the entity description + relationship neighbors + associated original text snippets + owning community
  (good for specific entity / relationship / detail questions)
- get_page: read the full text of the **original source document** by its exact relative path (verify details / gather evidence)
- submit_answer: submit the final answer

First use global_search to grasp the whole picture, or local_search to anchor an entity, then get_page to verify against the source as needed --
how to combine them is entirely up to you.

## Answer requirements
- **Use only retrieved/read information**; do not fabricate or speculate about facts not present in the graph or documents
- When information is insufficient, state clearly what is missing

## Citation format (must follow)
After each key factual assertion, cite its source: `[source: group/path]`, where path is the source-document path you actually read via get_page;
if the information comes only from a community report / entity graph with no specific source document, mark it as `[source: community report]` or `[source: knowledge graph]`,
and for information whose source is uncertain, mark it as `[source: inferred]` rather than fabricating a path.

Available knowledge-base groups: {groups}"""


# ==================== extraction: relay-driven gleaning (replacing the official ChatModel) ====================
def _chat_turns(messages: list, model: str, max_tokens: int) -> str:
    """One multi-turn chat completion (dual-protocol); appends the assistant reply in place into messages and returns its text.
    Extraction uses config.CHAT_MODEL (cheap), not counted in TCO (same as okf enrichment; prepare cost is not in the answering budget)."""
    if model.lower().startswith("claude"):
        r = llm._anthropic_client().messages.create(model=model, max_tokens=max_tokens,
                                                     messages=messages)
        text = "".join(getattr(b, "text", "") for b in r.content).strip()
        messages.append({"role": "assistant", "content": text})
        return text
    kwargs = dict(model=model, messages=messages)
    if model.lower().startswith("gpt-5"):
        kwargs["extra_body"] = {"max_completion_tokens": max_tokens}
    else:
        kwargs["temperature"] = 0.0
        kwargs["max_tokens"] = max_tokens
    llm.apply_no_think(kwargs, model)
    r = llm.next_client().chat.completions.create(**kwargs)
    text = (r.choices[0].message.content or "").strip()
    messages.append({"role": "assistant", "content": text})
    return text


def _extract_one(job) -> tuple[str, str]:
    """Extract on a single text unit; returns (chunk_id, concatenated extraction-record string). Includes the official three-stage gleaning logic:
    first extraction -> up to N CONTINUE rounds, with LOOP between rounds asking whether more remains (continue only on 'Y')."""
    chunk_id, text, model, max_glean = job
    prompt = GRAPH_EXTRACTION_PROMPT.format(
        entity_types=ENTITY_TYPES, tuple_delimiter=_TUPLE, record_delimiter=_RECORD,
        completion_delimiter=_COMPLETE, input_text=text)
    messages = [{"role": "user", "content": prompt}]
    try:
        out = _chat_turns(messages, model, max_tokens=4096)
    except Exception:
        return chunk_id, ""
    for i in range(max_glean):
        try:
            messages.append({"role": "user", "content": CONTINUE_PROMPT})
            out += _chat_turns(messages, model, max_tokens=4096)
            if i >= max_glean - 1:
                break
            messages.append({"role": "user", "content": LOOP_PROMPT})
            if _chat_turns(messages, model, max_tokens=4).strip() != "Y":
                break
        except Exception:
            break
    return chunk_id, out


def _parse_records(extractions: dict[str, str]) -> "tuple[dict, dict]":
    """Reuse the official _process_results logic verbatim to parse extraction strings into entities / relationships.
    entities[name] = {type, description (concatenated), source_ids (set)};
    relationships[(s,t)] = {description (concatenated), weight (summed), source_ids (set)}."""
    entities: dict[str, dict] = {}
    rels: dict[tuple, dict] = {}
    for chunk_id, blob in extractions.items():
        for record in (r.strip() for r in blob.split(_RECORD)):
            record = record.strip()
            if record.startswith("(") and record.endswith(")"):
                record = record[1:-1]
            attrs = record.split(_TUPLE)
            if attrs and attrs[0] == '"entity"' and len(attrs) >= 4:
                name = clean_str(attrs[1].upper())
                if not name:
                    continue
                etype = clean_str(attrs[2].upper())
                desc = clean_str(attrs[3])
                e = entities.setdefault(name, {"type": etype or "", "descs": set(), "source_ids": set()})
                if desc:
                    e["descs"].add(desc)
                if etype:
                    e["type"] = etype
                e["source_ids"].add(chunk_id)
            elif attrs and attrs[0] == '"relationship"' and len(attrs) >= 5:
                s = clean_str(attrs[1].upper())
                t = clean_str(attrs[2].upper())
                if not s or not t:
                    continue
                desc = clean_str(attrs[3])
                try:
                    w = float(attrs[-1])
                except ValueError:
                    w = 1.0
                for n in (s, t):
                    entities.setdefault(n, {"type": "", "descs": set(), "source_ids": set()})["source_ids"].add(chunk_id)
                key = (s, t)
                r = rels.setdefault(key, {"description": set(), "weight": 0.0, "source_ids": set()})
                r["weight"] += w
                if desc:
                    r["description"].add(desc)
                r["source_ids"].add(chunk_id)
    # finalize: concatenate descriptions into multiple lines, sort source_ids
    for e in entities.values():
        e["description"] = "\n".join(sorted(e.pop("descs")))
        e["source_ids"] = sorted(e["source_ids"])
    for r in rels.values():
        r["description"] = "\n".join(sorted(r["description"]))
        r["source_ids"] = sorted(r["source_ids"])
    return entities, rels


# ==================== community reports ====================
def _community_input_text(nodes: list[str], entities: dict, rels: dict,
                          eid: dict, rid: dict) -> str:
    """Assemble the community report's Real Data (entities / relationships tables, with numeric ids for Data references)."""
    ent_lines = ["-----Entities-----", "id,entity,type,description"]
    nodeset = set(nodes)
    for n in nodes:
        e = entities.get(n, {})
        d = (e.get("description") or "").replace("\n", " ")[:400]
        ent_lines.append(f"{eid[n]},{n},{e.get('type','')},{d}")
    rel_lines = ["-----Relationships-----", "id,source,target,description,weight"]
    for (s, t), r in rels.items():
        if s in nodeset and t in nodeset:
            d = (r.get("description") or "").replace("\n", " ")[:300]
            rel_lines.append(f"{rid[(s,t)]},{s},{t},{d},{r['weight']:.1f}")
    return "\n".join(ent_lines) + "\n\n" + "\n".join(rel_lines)


def _report_one(job) -> dict:
    """Generate a structured report for a single community (vendored COMMUNITY_REPORT_PROMPT -> JSON)."""
    community_id, level, input_text, model = job
    prompt = COMMUNITY_REPORT_PROMPT.format(input_text=input_text, max_report_length=_MAX_REPORT_WORDS)
    try:
        obj = llm.chat_json("You are an AI assistant that writes community reports as strict JSON.",
                            prompt, max_tokens=2000, model=model)
    except Exception:
        obj = {}
    if not isinstance(obj, dict):     # chat_json may return a JSON string/array literal (not an object) -> count as an empty report (tolerated by the <=1% gate), don't crash the whole build
        obj = {}
    findings = obj.get("findings") or []
    if not isinstance(findings, list):
        findings = []
    title = str(obj.get("title") or f"Community {community_id}").strip()
    summary = str(obj.get("summary") or "").strip()
    full = summary + "\n\n" + "\n".join(
        f"- {f.get('summary','')}: {f.get('explanation','')}" for f in findings
        if isinstance(f, dict))
    return {"community_id": community_id, "level": level, "title": title, "summary": summary,
            "rating": obj.get("rating"), "rating_explanation": obj.get("rating_explanation"),
            "findings": findings, "full_text": full.strip()}


def _save_vindex(index_dir: Path, records: list[dict], embed_texts: list[str], log) -> None:
    """Save records + their embeddings as the three files that rag.VectorIndex can load directly."""
    index_dir.mkdir(parents=True, exist_ok=True)
    emb = _embed(embed_texts) if embed_texts else np.zeros((0, 1), dtype=np.float32)
    np.save(index_dir / "embeddings.npy", emb)
    with open(index_dir / "chunks.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    (index_dir / "index_meta.json").write_text(json.dumps(
        {"embedding_model": config.RAG_EMBED_MODEL,
         "embedding_dim": int(emb.shape[1]) if emb.size else 0,
         "total_chunks": len(records)}, ensure_ascii=False, indent=2), encoding="utf-8")


@register("graphrag")
class GraphRAGBaseline(Baseline):
    def __init__(self, corpus: Corpus | None = None, model: str | None = None, index_dir=None):
        self.corpus = corpus or Corpus()
        self.model = model or config.SUT_MODEL
        self.dir = Path(index_dir or config.GRAPHRAG_DIR)
        self._loaded = False
        self._reports_vx: VectorIndex | None = None
        self._entities_vx: VectorIndex | None = None
        self._rels: dict | None = None            # name -> [(other, desc, weight)]
        self._ent_comm: dict | None = None         # name -> community_id (finest)
        self._comm_title: dict | None = None       # community_id -> title
        self._text_units: dict | None = None       # chunk_id -> {source_file, heading_path, text}
        self._ent_rec: dict | None = None          # name -> full entity record
        self._ent_src: dict | None = None          # name -> [chunk_id]
        self._load_lock = threading.Lock()          # guard against concurrent _load (multiple workers each loading a 3.6GB index -> OOM)

    # ---------------- offline: single complete compile pipeline ----------------
    def prepare(self, log=print) -> None:
        t0 = time.time()
        build_model = llm.config.CHAT_MODEL
        self.dir.mkdir(parents=True, exist_ok=True)
        # Directory-level exclusive lock: prevent the same graph directory from being written by two build processes concurrently
        # (the child process spawned later by the driver + a manual parallel build share this lock -- each build is a brand-new child
        # process loading the current on-disk code, so this lock is effective for both). flock auto-releases on process exit/crash
        # (no residual deadlock); it releases as soon as build's prepare() returns. Blocking wait: if another process is building the same dir, queue up.
        import fcntl
        self._build_lockf = open(self.dir / ".build.lock", "w")
        fcntl.flock(self._build_lockf, fcntl.LOCK_EX)
        # After acquiring the lock, re-check: if already built by a concurrent process (valid manifest), skip and don't rebuild (idempotent)
        _mf = self.dir / "graphrag_manifest.json"
        if _mf.exists():
            try:
                _gm = json.loads(_mf.read_text(encoding="utf-8"))
                if _gm.get("text_units_unique") is True and _gm.get("text_units") == 18025:
                    log(f"[graphrag.build] {self.dir} already built by a concurrent process (text_units={_gm.get('text_units')}), skipping rebuild")
                    return
            except Exception:
                pass
        # Delete the old manifest before starting: during a rebuild, leave no half-baked product that could be mistaken for "ready" (recheck P0-3); the manifest is written last = the completion marker
        (self.dir / "graphrag_manifest.json").unlink(missing_ok=True)
        # 1) chunking (text units)
        docs = self.corpus.docs()
        units: list[dict] = []
        for p in docs:
            rel = self.corpus.rel(p)
            for c in _chunk_doc(rel, self.corpus.read(rel) or "",
                                self.corpus.group, config.CHUNK_SIZE, config.CHUNK_OVERLAP):
                units.append(c)   # {id, text, source_file, heading_path, group, char_count}
        # hard assertion of chunk-id uniqueness: duplicates -> dict merge drops chunks (audit P1-1). Should always hold after fixing _make_chunk_id.
        _uids = [u["id"] for u in units]
        if len(_uids) != len(set(_uids)):
            from collections import Counter as _C
            dup = {k: c for k, c in _C(_uids).items() if c > 1}
            raise RuntimeError(f"[graphrag.build] text-unit chunk id not unique ({len(_uids)-len(set(_uids))} duplicates, "
                               f"examples {list(dup)[:3]}); fix _make_chunk_id and rebuild")
        log(f"[graphrag.build] {len(docs)} docs -> {len(units)} text units (all ids unique); extracting (model={build_model})...")

        # 2) entity/relationship extraction (gleaning; concurrent) -- extraction input includes metadata (on par with RAG/BM25, recheck P1-1:
        #    otherwise authors/report_date/department are only in frontmatter, graphrag can't extract them -> metadata questions suffer)
        jobs = [(u["id"], _chunk_retrieval_text(u), build_model, config.GRAPHRAG_MAX_GLEAN) for u in units]
        extractions = dict(llm.pmap(_extract_one, jobs))
        # targeted retry of failed (empty) chunks <=2 rounds (transient-jitter convergence, makes the zero-failure gate reachable; recheck P0-3)
        job_by = {j[0]: j for j in jobs}
        for _r in range(2):
            fails = [cid for cid, v in extractions.items() if not str(v).strip()]
            if not fails:
                break
            log(f"[graphrag.build] retrying {len(fails)} failed extraction chunks (round {_r+1})")
            for cid, v in dict(llm.pmap(_extract_one, [job_by[c] for c in fails])).items():
                extractions[cid] = v
        n_extract_fail = sum(1 for v in extractions.values() if not str(v).strip())
        log(f"[graphrag.build] extraction-failed (empty) chunks: {n_extract_fail}/{len(units)}")
        entities, rels = _parse_records(extractions)
        log(f"[graphrag.build] extracted {len(entities)} entities / {len(rels)} relationships; building graph + Leiden communities...")
        if not entities:
            raise RuntimeError("[graphrag.build] extracted 0 entities; check the corpus and CHAT_MODEL")

        # 3) graph merge -> networkx
        import networkx as nx
        g = nx.Graph()
        for name, e in entities.items():
            g.add_node(name, description=e["description"], type=e["type"],
                       source_id=", ".join(e["source_ids"]))
        for (s, t), r in rels.items():
            g.add_edge(s, t, weight=r["weight"], description=r["description"],
                       source_id=", ".join(r["source_ids"]))

        # 4) community detection (vendored official hierarchical_leiden; lazy import graspologic)
        try:
            from graphrag.index.operations.cluster_graph import cluster_graph
        except ImportError as e:
            raise RuntimeError(
                "graphrag community detection needs graspologic: pip install -r requirements.txt (graspologic>=3.3)") from e
        communities = cluster_graph(g, max_cluster_size=config.GRAPHRAG_MAX_CLUSTER,
                                    use_lcc=True, seed=0xDEADBEEF)   # [(level,cluster,parent,[nodes])]
        log(f"[graphrag.build] {len(communities)} communities (across levels); generating reports per community...")

        # numeric ids (for community-report Data references)
        eid = {n: i for i, n in enumerate(sorted(entities))}
        rid = {k: i for i, k in enumerate(sorted(rels))}

        # 5) community reports (concurrent)
        rep_jobs = []
        comm_meta = []
        for level, cluster, parent, nodes in communities:
            cid = f"{level}-{cluster}"
            it = _community_input_text(nodes, entities, rels, eid, rid)
            rep_jobs.append((cid, level, it, build_model))
            comm_meta.append({"community_id": cid, "level": level, "cluster": cluster,
                              "parent": parent, "entities": nodes})
        reports = llm.pmap(_report_one, rep_jobs)
        # targeted retry of empty-report communities <=2 rounds (recheck P0-3)
        for _r in range(2):
            idx_fail = [i for i, rp in enumerate(reports) if not str(rp.get("full_text") or "").strip()]
            if not idx_fail:
                break
            log(f"[graphrag.build] retrying {len(idx_fail)} empty reports (round {_r+1})")
            redo = dict(zip(idx_fail, llm.pmap(_report_one, [rep_jobs[i] for i in idx_fail])))
            for i, rp in redo.items():
                reports[i] = rp
        n_report_fail = sum(1 for r in reports if not str(r.get("full_text") or "").strip())
        log(f"[graphrag.build] empty-report communities: {n_report_fail}/{len(reports)}")

        # 6) persist + index
        d = self.dir
        d.mkdir(parents=True, exist_ok=True)
        with open(d / "entities.jsonl", "w", encoding="utf-8") as f:
            for n in sorted(entities):
                e = entities[n]
                f.write(json.dumps({"id": eid[n], "name": n, "type": e["type"],
                                    "description": e["description"], "source_ids": e["source_ids"],
                                    "degree": g.degree(n) if n in g else 0},
                                   ensure_ascii=False) + "\n")
        with open(d / "relationships.jsonl", "w", encoding="utf-8") as f:
            for (s, t), r in rels.items():
                f.write(json.dumps({"id": rid[(s, t)], "source": s, "target": t,
                                    "description": r["description"], "weight": r["weight"],
                                    "source_ids": r["source_ids"]}, ensure_ascii=False) + "\n")
        with open(d / "communities.jsonl", "w", encoding="utf-8") as f:
            for c in comm_meta:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")
        with open(d / "community_reports.jsonl", "w", encoding="utf-8") as f:
            for r in reports:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with open(d / "text_units.jsonl", "w", encoding="utf-8") as f:
            for u in units:
                f.write(json.dumps({"id": u["id"], "source_file": u["source_file"],
                                    "heading_path": u.get("heading_path", ""),
                                    "text": _chunk_retrieval_text(u)},   # includes metadata (recheck P1-1)
                                   ensure_ascii=False) + "\n")

        # community-report vector index (global_search data plane)
        rep_records = [{"community_id": r["community_id"], "level": r["level"], "title": r["title"],
                        "summary": r["summary"], "findings": r["findings"], "text": r["full_text"]}
                       for r in reports if r["full_text"]]
        _save_vindex(d / "reports_index", rep_records,
                     [f"{r['title']}\n{r['text']}" for r in rep_records], log)
        # entity vector index (local_search data plane)
        ent_records = [{"name": n, "type": entities[n]["type"],
                        "description": entities[n]["description"], "source_ids": entities[n]["source_ids"],
                        "text": f"{n}: {entities[n]['description']}"} for n in sorted(entities)]
        _save_vindex(d / "entities_index", ent_records, [r["text"] for r in ent_records], log)

        # manifest
        # failure gate (pushed down into prepare): tolerate <=10% (catch API meltdown/systemic crash, not a weak model's legitimately sparse graph).
        # A per-model graph should reflect the model's extraction ability: a weak model (e.g. Flash) has more empty chunks -> sparser graph -> lower graphrag score,
        # which is a valid result, not a bad build. A hard 1% would wrongly kill DeepSeek-Flash (a legitimate graph with 4% empty chunks / 51k entities). True failure rate goes into the manifest.
        _ef_tol = max(1, int(0.10 * len(units))); _rf_tol = max(1, int(0.10 * max(len(rep_records), 1)))
        if n_extract_fail > _ef_tol or n_report_fail > _rf_tol:
            raise RuntimeError(f"[graphrag.build] build unqualified: extract_fail={n_extract_fail} (tolerance {_ef_tol}) "
                               f"empty_report={n_report_fail} (tolerance {_rf_tol}); refusing to write manifest")
        import hashlib as _hl
        _corpus_mf = Path(self.corpus.root) / "_manifest.json"
        (d / "graphrag_manifest.json").write_text(json.dumps(
            {"graphrag_version": "0.1", "compiler": "microsoft@v2.7.2", "build_model": build_model,
             "docs": len(docs), "text_units": len(units), "entities": len(entities),
             "relationships": len(rels), "communities": len(comm_meta),
             "reports": len(rep_records), "embedding_model": config.RAG_EMBED_MODEL,
             "entity_types": ENTITY_TYPES,
             # audit P2-2: failures visible + corpus hash binding
             "text_units_unique": len(units) == len(set(_uids)),
             "extract_fail_blocks": n_extract_fail, "empty_report_communities": n_report_fail,
             # recheck P1-3: offline build cost visible (wall clock + estimated LLM call count; tokens not counted per call, estimated by count x unit price)
             "build_wall_s": round(time.time() - t0, 1),
             "build_llm_calls_est": len(units) * (1 + config.GRAPHRAG_MAX_GLEAN) + len(rep_records),
             "corpus_manifest_sha256": (
                 _hl.sha256(_corpus_mf.read_bytes()).hexdigest() if _corpus_mf.exists() else None)},
            ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"[graphrag.build] DONE {len(entities)} entities / {len(rels)} relationships / {len(comm_meta)} communities / "
            f"{len(rep_records)} reports, {time.time()-t0:.0f}s -> {d}")

    # ---------------- online: two-tool navigation loop ----------------
    def _load(self) -> None:
        if self._loaded:
            return
        with self._load_lock:                       # double-checked lock: only one thread loads, the rest wait and reuse (review #5)
            if self._loaded:
                return
            self._load_locked()

    def _load_locked(self) -> None:
        if not (self.dir / "graphrag_manifest.json").exists():
            raise FileNotFoundError(
                f"GraphRAG index missing: {self.dir} (first run `python -m src.baselines.cli build --baseline graphrag`)")
        self._reports_vx = VectorIndex(self.dir / "reports_index", config.GRAPHRAG_REPORT_TOPK)
        self._entities_vx = VectorIndex(self.dir / "entities_index", config.GRAPHRAG_LOCAL_TOPK)
        self._reports_vx.load(); self._entities_vx.load()
        # relationship adjacency
        self._rels = defaultdict(list)
        for line in open(self.dir / "relationships.jsonl", encoding="utf-8"):
            r = json.loads(line)
            self._rels[r["source"]].append((r["target"], r["description"], r["weight"]))
            self._rels[r["target"]].append((r["source"], r["description"], r["weight"]))
        # entity -> finest-level community; community -> title
        self._comm_title = {r["community_id"]: r["title"]
                            for r in map(json.loads, open(self.dir / "community_reports.jsonl", encoding="utf-8"))}
        self._ent_comm = {}
        for line in open(self.dir / "communities.jsonl", encoding="utf-8"):
            c = json.loads(line)
            for n in c["entities"]:
                prev = self._ent_comm.get(n)
                if prev is None or c["level"] > prev[0]:
                    self._ent_comm[n] = (c["level"], c["community_id"])
        # text units + entity records (name -> full record, incl. source_ids)
        self._text_units = {u["id"]: u for u in map(json.loads, open(self.dir / "text_units.jsonl", encoding="utf-8"))}
        self._ent_rec = {e["name"]: e
                         for e in map(json.loads, open(self.dir / "entities.jsonl", encoding="utf-8"))}
        self._ent_src = {n: e["source_ids"] for n, e in self._ent_rec.items()}
        self._loaded = True

    def _global_search_tool(self) -> Tool:
        def fn(args: dict) -> dict:
            q = (args.get("query") or "").strip()
            if not q:
                return {"content": "[ERROR] query is required", "next_action": "Provide a search query."}
            hits = self._reports_vx.retrieve(q, top_k=config.GRAPHRAG_REPORT_TOPK)
            if not hits:
                return {"content": f"No community reports for '{q}'.", "next_action": "Try local_search for a specific entity."}
            lines = [f"Top {len(hits)} community reports for '{q}':"]
            for r in hits:
                lines.append(f"\n### [{r['community_id']}] {r['title']} (score {r['_score']:.3f})")
                lines.append(r.get("summary", "")[:800])
                for f_ in (r.get("findings") or [])[:5]:
                    if isinstance(f_, dict):
                        lines.append(f"- {f_.get('summary','')}: {f_.get('explanation','')[:300]}")
            return {"content": "\n".join(lines),
                    "next_action": "Drill into entities via local_search, verify via get_page, or submit_answer."}
        return Tool("global_search",
                    "Semantic retrieval over the community-report pool; returns the title/summary/key findings of relevant communities (prefer for global, thematic, overview questions).",
                    {"query": {"type": "string", "description": "Thematic/global query (1-200 chars)"}}, ["query"], fn)

    def _local_search_tool(self) -> Tool:
        def fn(args: dict) -> dict:
            q = (args.get("query") or "").strip()
            if not q:
                return {"content": "[ERROR] query is required", "next_action": "Provide an entity name or query."}
            hits = self._entities_vx.retrieve(q, top_k=config.GRAPHRAG_LOCAL_TOPK)
            # pin exact entity-name matches to the top
            up = q.upper()
            if up in self._ent_rec and not any(h["name"] == up for h in hits):
                hits = [dict(self._ent_rec[up], _score=1.0)] + hits
            if not hits:
                return {"content": f"No entities for '{q}'.", "next_action": "Try global_search for a broad theme."}
            lines = [f"Top {len(hits)} entities for '{q}':"]
            for e in hits[:config.GRAPHRAG_LOCAL_TOPK]:
                name = e["name"]
                lines.append(f"\n## {name} [{e.get('type','')}] (score {e.get('_score',0):.3f})")
                lines.append((e.get("description") or "")[:500])
                comm = self._ent_comm.get(name)
                if comm:
                    lines.append(f"Community: {self._comm_title.get(comm[1], comm[1])}")
                nbrs = self._rels.get(name, [])[:6]
                if nbrs:
                    lines.append("Relationship neighbors:")
                    for other, desc, w in nbrs:
                        lines.append(f"  - {other} (w{w:.0f}): {desc[:160]}")
                for cid in (self._ent_src.get(name) or [])[:1]:
                    u = self._text_units.get(cid)
                    if u:
                        lines.append(f"Source snippet [{u['source_file']}]: {u['text'][:_SNIPPET]}")
            return {"content": "\n".join(lines),
                    "next_action": "get_page a cited source_file to verify, global_search for theme, or submit_answer."}
        return Tool("local_search",
                    "Entity-centric retrieval: returns entity description + relationship neighbors + associated source snippets + owning community (prefer for specific entity/relationship/detail questions).",
                    {"query": {"type": "string", "description": "Entity name or detail query (1-200 chars)"}}, ["query"], fn)

    def answer(self, question: dict) -> AnswerResult:
        self._load()
        tools = [self._global_search_tool(), self._local_search_tool(), get_page_tool(self.corpus)]
        return run_loop_answer(self.model, GRAPHRAG_SYSTEM_PROMPT.format(groups=self.corpus.group),
                               tools, question["question"], "graphrag")
