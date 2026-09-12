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
        "file": str(p.as_posix()),
    }


def main(data_dir: str, dst: str) -> int:
    root = Path(data_dir)
    conts = sorted((root / "continents").glob("*.yaml"))
    ctry = sorted((root / "countries").glob("*.yaml"))
    out = {"continents": [load(p) for p in conts], "countries": [load(p) for p in ctry]}
    for c in out["countries"]:
        for b in c["band"]:
            if b not in BAND_ORDER:
                raise SystemExit(f"{c['id']}: bad band {b}")
        if not c["parent_id"]:
            raise SystemExit(f"{c['id']}: missing parent_id")
    out["generated_from"] = f"{len(conts)} continent + {len(ctry)} country YAML files under {data_dir}/"
    Path(dst).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {dst}: {len(out['continents'])} continents, {len(out['countries'])} countries")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data", sys.argv[2] if len(sys.argv) > 2 else "site/entities.json"))
