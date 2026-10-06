#!/usr/bin/env python3
"""check_registry.py — mechanical Check for PLAN.md P2-T1 over data/continents/REGISTRY.md.

Exit 0 = PASS. Prints one line per assertion.
"""
from __future__ import annotations

import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "data" / "continents" / "REGISTRY.md"
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SUB_RE = re.compile(r"^.+, (\d{4})(–(\d{4}|present))?$")


def parse_registry(text: str):
    sec = text.split("## 1. The registry", 1)[1].split("\n## 2.", 1)[0]
    rows = []
    for line in sec.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 11 or cells[0] in ("#", "id") or set(cells[0]) <= {"-"}:
            continue
        if not cells[0].isdigit():
            continue  # second (border) table has 3 cells, filtered by len already
        rows.append(
            dict(
                n=int(cells[0]),
                id=cells[1].strip("`"),
                name=cells[2],
                subtitle=cells[3],
                start=cells[4],
                end=cells[5],
                band=cells[6],
                biome=cells[7],
                rfile=cells[8],
                offshore=cells[9].strip("*").lower(),
                split=cells[10],
            )
        )
    return rows


def parse_precheck(text: str):
    sec = text.split("## 3. A-C2 pre-check", 1)[1].split("\n## 4.", 1)[0]
    ans = {}
    for line in sec.splitlines():
        m = re.match(r"^\|\s*`([a-z0-9-]+)`\s*\|\s*(\w+)", line)
        if m:
            ans[m.group(1)] = m.group(2).lower()
    return ans


def main() -> int:
    text = REG.read_text(encoding="utf-8")
    rows = parse_registry(text)
    fails = 0

    def check(ok: bool, msg: str):
        nonlocal fails
        print(("  PASS " if ok else "  FAIL ") + msg)
        if not ok:
            fails += 1

    n = len(rows)
    check(9 <= n <= 15, f"row count 9 ≤ {n} ≤ 15")

    files = {r["rfile"] for r in rows}
    missing = [f"0{i}" for i in range(1, 9) if f"0{i}" not in files]
    check(not missing, f"every research/0[1-8] is the source of ≥ 1 row (missing: {missing})")
    for f in sorted(files):
        assert (ROOT / "research").glob(f"{f}-*.md"), f

    ids = [r["id"] for r in rows]
    bad = [i for i in ids if not ID_RE.match(i) or len(i) > 48]
    check(not bad, f"ids match V-03 regex and ≤ 48 chars (bad: {bad})")
    check(len(set(ids)) == len(ids), "ids unique")
    names = [r["name"] for r in rows]
    check(len(set(names)) == len(names), "names unique (V-13)")

    this_year = _dt.date.today().year
    sub_bad = []
    for r in rows:
        m = SUB_RE.match(r["subtitle"])
        if not m:
            sub_bad.append((r["id"], "regex"))
            continue
        y0 = m.group(1)
        y1 = m.group(3) or y0
        if y0 != r["start"] or y1 != r["end"]:
            sub_bad.append((r["id"], f"{y0}–{y1} ≠ {r['start']}–{r['end']}"))
    check(not sub_bad, f"subtitles match V-12 regex and equal start/end (bad: {sub_bad})")

    def yr(v: str) -> int:
        return this_year if v == "present" else int(v)

    off_bad = [r["id"] for r in rows if (r["offshore"] == "true") != (yr(r["end"]) <= 1943)]
    check(not off_bad, f"offshore rows ⇔ end ≤ 1943 (V-14) (bad: {off_bad})")
    check(sum(r["offshore"] == "true" for r in rows) == 1, "exactly one archipelago row")

    spans = sorted((yr(r["start"]), yr(r["end"])) for r in rows)
    check(spans[0][0] <= 1943, f"earliest start {spans[0][0]} ≤ 1943")
    check(any(r["end"] == "present" for r in rows), "one row ends at present")
    covered_to = spans[0][1]
    gap = None
    for s, e in spans[1:]:
        if s > covered_to + 1:
            gap = (covered_to + 1, s - 1)
            break
        covered_to = max(covered_to, e)
    check(gap is None and covered_to >= this_year, f"sorted starts tile with no uncovered year (gap: {gap}); covered to {covered_to}")
    print("  spans: " + " · ".join(f"{r['start']}–{r['end']}" for r in sorted(rows, key=lambda r: yr(r['start']))))

    ans = parse_precheck(text)
    no = [i for i in ids if ans.get(i) != "yes"]
    check(not no, f"A-C2 pre-check answered 'yes' for every id (not yes: {no})")

    biomes = {"highland", "grassland", "forest", "jungle", "wetland", "harbour", "mixed"}
    bb = [r["id"] for r in rows if r["biome"] not in biomes]
    check(not bb, f"biome in SPEC §2.6 enum (bad: {bb})")

    print(f"check_registry: rows={n} fails={fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
