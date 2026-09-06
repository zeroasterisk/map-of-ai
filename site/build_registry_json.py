#!/usr/bin/env python3
"""Build site/registry.json from data/continents/REGISTRY.md (the source of truth).

Usage: python3 site/build_registry_json.py data/continents/REGISTRY.md site/registry.json
Also run locally before previewing site/index.html; the Pages workflow runs it on deploy.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from check_registry import parse_registry, parse_precheck  # noqa: E402

BAND_ORDER = ["N1", "N2", "C", "S1", "S2"]


def band_list(span: str):
    """'N2–S1 (mid-latitude)' -> ['N2','C','S1']; 'N2' -> ['N2']. Home band in parens is kept as text."""
    core = span.split("(")[0].strip()
    home = None
    m = re.search(r"\(home ([^)]*)\)", span)
    if m:
        home = m.group(1)
    if "–" in core:
        a, b = [s.strip() for s in core.split("–")]
        i, j = BAND_ORDER.index(a), BAND_ORDER.index(b)
        bands = BAND_ORDER[i : j + 1]
    else:
        bands = [core]
    return bands, home


def borders(text: str):
    sec = text.split("Border landmarks quoted", 1)[1].split("\n## 2.", 1)[0]
    out = {}
    for line in sec.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0].startswith("`"):
            out[cells[0].strip("`")] = {"west": cells[1], "east": cells[2]}
    return out


def main(src: str, dst: str) -> int:
    text = Path(src).read_text(encoding="utf-8")
    rows = parse_registry(text)
    pre = parse_precheck(text)
    bd = borders(text)
    out = []
    for r in rows:
        bands, home = band_list(r["band"])
        out.append(
            {
                "n": r["n"],
                "id": r["id"],
                "name": r["name"],
                "subtitle": r["subtitle"],
                "start": int(r["start"]),
                "end": r["end"] if r["end"] == "present" else int(r["end"]),
                "bands": bands,
                "home_band": home,
                "band_span_text": r["band"],
                "biome": r["biome"],
                "research_file": r["rfile"],
                "offshore": r["offshore"] == "true",
                "split_of": r["split"],
                "a_c2_precheck": pre.get(r["id"]),
                "border_west": bd.get(r["id"], {}).get("west", ""),
                "border_east": bd.get(r["id"], {}).get("east", ""),
            }
        )
    Path(dst).write_text(json.dumps({"generated_from": src, "continents": out}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {dst}: {len(out)} continents")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
