#!/usr/bin/env python3
"""check_research.py — mechanical part of SPEC.md §4.1 for research files.

Checks R-01, R-02 (status value + consistency with R-03…R-07 where mechanical),
R-04, R-05, R-06, and R-07 (existence + ≥10 dispositions in the review report).
R-03 (links) is delegated to scripts/check_links.sh unless --no-links.

Usage: scripts/check_research.py research/01-*.md [more files] [--no-links]
Prints PASS/FAIL per criterion per file; exit 1 on any FAIL.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE_HEADINGS = [
    "## One-paragraph summary",
    "## Timeline of key events",
    "## Key people",
    "## Key papers / artifacts",
    "## Schools of thought / sub-clusters",
    "## Map notes",
    "## Sources",
]


def section(text: str, heading: str) -> str:
    m = re.search(r"^" + re.escape(heading) + r"\s*$", text, flags=re.M)
    if not m:
        return ""
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, flags=re.M)
    return rest[: nxt.start()] if nxt else rest


def check(path: Path, do_links: bool) -> list[tuple[str, bool, str]]:
    text = path.read_text(encoding="utf-8")
    out: list[tuple[str, bool, str]] = []

    # R-01 heading order
    positions = []
    missing = []
    for h in TEMPLATE_HEADINGS:
        m = re.search(r"^" + re.escape(h) + r"\s*$", text, flags=re.M)
        if m:
            positions.append(m.start())
        else:
            missing.append(h)
    ordered = positions == sorted(positions)
    out.append(("R-01", not missing and ordered,
                f"missing {missing}" if missing else ("headings out of order" if not ordered else "all template headings present, in order")))

    # R-02 status value
    sm = re.search(r"^\>\s*\*\*Status:\*\*\s*(\w+)", text, flags=re.M)
    status = sm.group(1) if sm else None
    status_ok = status in ("draft", "verified", "reviewed")

    # R-04
    body_wo_sources = text[: text.find("## Sources")] if "## Sources" in text else text
    used = set(re.findall(r"\[([a-h]?\d+)\]", body_wo_sources))  # [12] or [a3] (research/09 style)
    src = section(text, "## Sources")
    defined = set(re.findall(r"^\[([a-h]?\d+)\]", src, flags=re.M))
    undefined = sorted(used - defined)
    unreferenced = sorted(defined - used)
    # timeline rows must have a non-empty Source cell
    tl = section(text, "## Timeline of key events")
    rows = [r for r in tl.splitlines() if r.startswith("|") and not re.match(r"^\|\s*-", r) and not re.match(r"^\|\s*Year", r)]
    empty_src_rows = []
    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 4 or not cells[-1]:
            empty_src_rows.append(r[:60])
    r04 = not undefined and not unreferenced and not empty_src_rows
    msg = []
    if undefined:
        msg.append(f"cited but undefined: {undefined}")
    if unreferenced:
        msg.append(f"defined but never cited: {unreferenced}")
    if empty_src_rows:
        msg.append(f"{len(empty_src_rows)} timeline rows without Source")
    out.append(("R-04", r04, "; ".join(msg) if msg else f"{len(rows)} timeline rows sourced; {len(defined)} sources all cited"))

    # R-05 every source entry has URL + accessed date
    bad05 = []
    for line in src.splitlines():
        m = re.match(r"^\[([a-h]?\d+)\]", line)
        if not m:
            continue
        if not re.search(r"https?://", line) or not re.search(r"\(accessed \d{4}-\d{2}-\d{2}\)", line):
            bad05.append(m.group(1))
    out.append(("R-05", not bad05, f"entries lacking URL or (accessed date): {bad05}" if bad05 else "every source has URL + accessed date"))

    # R-06 schools ≥3 bullets each with borders:
    sc = section(text, "## Schools of thought / sub-clusters")
    bullets = [b for b in sc.splitlines() if re.match(r"^\s*[-*]\s+\*\*", b)]
    no_borders = [b[:50] for b in bullets if "borders:" not in b]
    out.append(("R-06", len(bullets) >= 3 and not no_borders,
                f"{len(bullets)} bullets; without borders: {no_borders}" if (len(bullets) < 3 or no_borders) else f"{len(bullets)} school bullets, all with borders:"))

    # R-03 links
    if do_links:
        res = subprocess.run(["bash", str(REPO / "scripts/check_links.sh"), str(path)], capture_output=True, text=True, check=False)
        last = res.stdout.strip().splitlines()[-1] if res.stdout.strip() else "no output"
        out.append(("R-03", "failed=0" in last, last))
    else:
        out.append(("R-03", True, "skipped (--no-links)"))

    # R-07 review report exists with ≥10 dispositions
    stem = path.name[:2]
    reports = sorted((REPO / "data/reviews").glob(f"*-research-{stem}.md")) if (REPO / "data/reviews").is_dir() else []
    r07 = False
    r07msg = "no review report data/reviews/*-research-%s.md" % stem
    if reports:
        rt = reports[-1].read_text(encoding="utf-8")
        n = len(re.findall(r"\|\s*(added|folded|rejected)\s*\|", rt))
        r07 = n >= 10
        r07msg = f"{reports[-1].relative_to(REPO)}: {n} dispositions"
    out.append(("R-07", r07, r07msg))

    # R-02 consistency
    core = all(ok for rid, ok, _ in out if rid in ("R-03", "R-04", "R-05", "R-06"))
    if status == "reviewed":
        ok02 = core and r07
    elif status == "verified":
        ok02 = core
    else:
        ok02 = status_ok
    out.insert(1, ("R-02", ok02, f"Status: {status!r}" + ("" if ok02 else " inconsistent with R-03…R-07 results")))
    return out


def main(argv: list[str]) -> int:
    do_links = "--no-links" not in argv
    files = [Path(a) for a in argv if not a.startswith("--")]
    rc = 0
    for f in files:
        print(f"== {f}")
        for rid, ok, msg in check(f, do_links):
            print(f"  {'PASS' if ok else 'FAIL'} {rid}: {msg}")
            if not ok:
                rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
