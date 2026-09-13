#!/usr/bin/env python3
"""Build site/entities.json from data/continents/*.yaml + data/countries/*.yaml (SPEC.md §9 G10).

Usage: python3 site/build_entities_json.py data site/entities.json
Sibling of build_registry_json.py. registry.json (from REGISTRY.md) stays authoritative for continent
ids/spans in the prototype; entities.json carries the COUNTRY layer (P3-RENDER) plus the continent YAML
rows for cross-reference. No coordinates are stored (SPEC §6 item 2) — every position is derived at
render time from time_range / band / parent_id and the parent's drawn polygon.
"""
import json
import sys
from pathlib import Path

import yaml

BAND_ORDER = ["N1", "N2", "C", "S1", "S2"]
SUB_BANDS = {"N1a", "N1b", "N2a", "N2b", "Ca", "Cb", "S1a", "S1b", "S2a", "S2b", "S2c"}   # country-layer rows inside the band rows (N1/N2 added for generative-coast, P3-T10)


def bands(v):
    return v if isinstance(v, list) else [v]


def load(p: Path):
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    tr = d.get("time_range") or {}
    words = " ".join(str(d.get("summary", "")).split()).split(" ")
    return {
        "id": d["id"],
        "level": d.get("level"),
        "name": d["name"],
        "subtitle": d.get("subtitle", ""),
        "parent_id": d.get("parent_id"),
        "start": tr.get("start"),
        "end": tr.get("end"),
        "band": bands(d.get("band")),
        "biome": d.get("biome"),
        "status": d.get("status"),
        "summary60": " ".join(words[:60]) + (" …" if len(words) > 60 else ""),
        "neighbours": [{"id": n.get("id"), "relation": n.get("relation")} for n in (d.get("neighbours") or []) if isinstance(n, dict)],
        "band_override_note": d.get("band_override_note"),
        # P3-RENDER v2: sub_band is ALWAYS a list (["S2a"] or ["Cb","S1a"]) — the renderer unions fine rows, so a
        # 1-row and a 2-row country share one code path. spatial defaults true; false = demoted (no polygon).
        "sub_band": bands(d["sub_band"]) if d.get("sub_band") else None,
        "spatial": d.get("spatial", True) is not False,
        "related_facts": [{"id": f.get("id"), "note": f.get("note")} for f in (d.get("related_facts") or []) if isinstance(f, dict)],
        "file": str(p.as_posix()),
    }


def main(data_dir: str, dst: str) -> int:
    root = Path(data_dir)
    conts = sorted((root / "continents").glob("*.yaml"))
    ctry = sorted((root / "countries").glob("*.yaml"))
    out = {"continents": [load(p) for p in conts], "countries": [load(p) for p in ctry]}
    # LOD events (data/events/<continent>.yaml): per-country z1 hint / z2 tag / z3–z4 named events, rendered into the
    # map by atlas.html. Every event must carry >= 1 source (SOURCING.md); years must lie inside the country's span.
    events_n = 0
    for ep in sorted((root / "events").glob("*.yaml")) if (root / "events").exists() else []:
        ev = yaml.safe_load(ep.read_text(encoding="utf-8")) or {}
        for cid, spec in (ev.get("countries") or {}).items():
            c = next((c for c in out["countries"] if c["id"] == cid), None)
            if not c:
                raise SystemExit(f"{ep}: unknown country {cid}")
            c["hint"] = spec.get("hint")
            c["tag"] = spec.get("tag")
            c["events"] = []
            for e in spec.get("events") or []:
                if not e.get("sources"):
                    raise SystemExit(f"{ep}: event {e.get('id')} has no sources")
                if not (c["start"] - 0.5 <= float(e["year"]) <= c["end"] + 1):
                    raise SystemExit(f"{ep}: event {e['id']} year {e['year']} outside {cid} span {c['start']}–{c['end']}")
                if len(str(e.get("one_line", "")).split()) > 16:
                    raise SystemExit(f"{ep}: event {e['id']} one_line > 15 words")
                c["events"].append({"id": e["id"], "name": e["name"], "year": float(e["year"]), "lod": int(e.get("lod", 4)),
                                    "one_line": e.get("one_line", ""), "sources": [{"url": s["url"], "title": s.get("title", "")} for s in e["sources"]]})
                events_n += 1
    for c in out["countries"]:
        for b in c["band"]:
            if b not in BAND_ORDER:
                raise SystemExit(f"{c['id']}: bad band {b}")
        if not c["parent_id"]:
            raise SystemExit(f"{c['id']}: missing parent_id")
        if c["spatial"] and not c["sub_band"]:
            raise SystemExit(f"{c['id']}: spatial country needs sub_band")
        for sb in c["sub_band"] or []:
            if sb not in SUB_BANDS or sb[:-1] not in c["band"]:
                raise SystemExit(f"{c['id']}: sub_band {sb} not inside band {c['band']}")
    # cross-cutting threads (data/threads/*.yaml, AXES.md §3): linear features (rivers/roads/mountain ranges), NOT
    # regions. Passed through as-is (id, kind, placement, milestones with their research/09 citations); the renderer
    # draws each as a path with year-anchored points, never through the country-polygon machinery.
    threads = []
    for tp in sorted((root / "threads").glob("*.yaml")) if (root / "threads").exists() else []:
        t = yaml.safe_load(tp.read_text(encoding="utf-8"))
        for m in t.get("milestones") or []:
            m["year"] = float(m["year"])
            if not m.get("sources"):
                raise SystemExit(f"{t['id']}: milestone {m['name']} has no sources (every thread milestone must cite research/09)")
        threads.append(t)
    out["threads"] = threads
    out["generated_from"] = f"{len(conts)} continent + {len(ctry)} country YAML files under {data_dir}/" + (f" + {len(threads)} thread(s)" if threads else "")
    Path(dst).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # entities.js: the same payload as a JS global — the page is static (file:// or Pages) and loads it via <script src>
    Path(dst).with_suffix(".js").write_text("window.ENTITIES = " + json.dumps(out, ensure_ascii=False) + ";\n", encoding="utf-8")
    ns = sum(1 for c in out["countries"] if c["spatial"])
    print(f"wrote {dst}: {len(out['continents'])} continents, {len(out['countries'])} countries ({ns} spatial), {events_n} LOD events")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data", sys.argv[2] if len(sys.argv) > 2 else "site/entities.json"))
