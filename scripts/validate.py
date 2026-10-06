#!/usr/bin/env -S uv run --script --quiet
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6"]
# ///
"""validate.py — mechanical validator for data/**/*.yaml (SPEC.md §3).

Implements every rule V-01 … V-60 as a function named check_V_nn. Prints one
line per violation as ``FAIL <rule> <file> <message>``, a summary, and exits 1
on any FAIL.

Usage:
  scripts/validate.py [DATA_DIR ...] [--offline] [--require-children]
                      [--file PATH ...] [--summary] [--quiet]

  DATA_DIR            root(s) to scan (default: data/). Each root is expected
                      to contain continents/, countries/, cities/, coverage/.
  --file PATH         validate only these files (cross-file rules still load
                      the whole tree for context; FAIL lines are printed only
                      for the named files).
  --offline           skip network rules (V-20 only).
  --require-children  turn on V-32 (every continent ≥ 1 country, every
                      country ≥ 1 city).
  --summary           print entity counts by level and status.
  --quiet             suppress per-rule PASS lines (only FAIL + summary).

Run with ``uv run --script scripts/validate.py`` if the shebang is not
executable on your platform.
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

# --------------------------------------------------------------------------- #
# SPEC.md §2 constants
# --------------------------------------------------------------------------- #

LEVELS = ("continent", "country", "city")
LEVEL_DIR = {"continent": "continents", "country": "countries", "city": "cities"}
DIR_LEVEL = {v: k for k, v in LEVEL_DIR.items()}
BANDS = ["N1", "N2", "C", "S1", "S2"]
BIOMES = {"highland", "grassland", "forest", "jungle", "wetland", "harbour", "mixed"}
CITY_TYPES = {"lab", "system", "paper", "event", "dataset", "institution", "person"}
SOURCE_KINDS = {"wikipedia", "primary", "secondary", "official"}
THREADS = {"rl", "robotics", "safety", "compute", "open-closed", "language", "vision", "games"}
NEIGHBOUR_RELATIONS = {"borders", "bridge", "wall", "river", "road"}
STATUSES = ["draft", "sourced", "verified", "placed"]
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SUBTITLE_RE = re.compile(r"^.+, (\d{4})(?:–(\d{4}|present))?$")
SUMMARY_WORDS = {"continent": (120, 300), "country": (80, 220), "city": (30, 150)}
SOURCE_MIN = {"continent": 3, "country": 2, "city": 1}
VERIFIED_SOURCE_MIN = {"continent": 3, "country": 3, "city": 2}

# field -> (type-check, {level: req}) ; req in R P V O -
# type keys: str,int,bool,list,dict,date(any of int/str/date),list_or_str
SCHEMA: dict[str, tuple[str, dict[str, str]]] = {
    "id": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "level": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "type": ("str", {"continent": "-", "country": "-", "city": "R"}),
    "name": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "subtitle": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "summary": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "time_range": ("dict", {"continent": "R", "country": "R", "city": "R"}),
    "offshore": ("bool", {"continent": "O", "country": "-", "city": "-"}),
    "band": ("band", {"continent": "R", "country": "R", "city": "R"}),
    "band_override_note": ("str", {"continent": "O", "country": "O", "city": "O"}),
    "biome": ("str", {"continent": "R", "country": "R", "city": "O"}),
    "parent_id": ("str", {"continent": "-", "country": "R", "city": "R"}),
    "research_ref": ("dict", {"continent": "R", "country": "R", "city": "O"}),
    "sources": ("list", {"continent": "R", "country": "R", "city": "R"}),
    "threads": ("list", {"continent": "O", "country": "O", "city": "O"}),
    "neighbours": ("list", {"continent": "O", "country": "P", "city": "O"}),
    "adjacent_field": ("dict", {"continent": "-", "country": "O", "city": "O"}),
    "status": ("str", {"continent": "R", "country": "R", "city": "R"}),
    "verified_by": ("dict", {"continent": "V", "country": "V", "city": "V"}),
    "notes": ("str", {"continent": "O", "country": "O", "city": "O"}),
    # P3-RENDER v2 country-layer fields (SPEC §9; render-only hints, no coordinates):
    # sub_band: finer row(s) inside the parent's band rows (N1a N1b N2a N2b Ca Cb S1a S1b S2a S2b S2c), str or list
    # spatial: false -> no polygon; surfaced as a related_facts hover note on another entity
    # related_facts: [{id, note}] extra hover/click content referencing a demoted entity
    "sub_band": ("list_or_str", {"continent": "-", "country": "O", "city": "-"}),
    "spatial": ("bool", {"continent": "-", "country": "O", "city": "O"}),
    "related_facts": ("list", {"continent": "O", "country": "O", "city": "O"}),
}

PRESENT = 10**9  # +infinity for "present"


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #

class Entity:
    def __init__(self, path: Path, root: Path, raw, parse_error: str | None):
        self.path = path
        self.root = root
        self.rel = str(path.relative_to(root.parent)) if root.parent in path.parents else str(path)
        self.raw = raw
        self.parse_error = parse_error
        self.data = raw if isinstance(raw, dict) else {}

    @property
    def id(self):
        return self.data.get("id")

    @property
    def level(self):
        return self.data.get("level")

    @property
    def dir_level(self) -> str | None:
        """Level implied by the directory the file lives in."""
        try:
            first = self.path.relative_to(self.root).parts[0]
        except ValueError:
            return None
        return DIR_LEVEL.get(first)

    def get(self, k, default=None):
        return self.data.get(k, default)


class Context:
    def __init__(self, roots: list[Path], offline: bool, require_children: bool,
                 only: set[Path] | None, repo: Path):
        self.roots = roots
        self.offline = offline
        self.require_children = require_children
        self.only = only
        self.repo = repo
        self.entities: list[Entity] = []
        self.by_id: dict[str, list[Entity]] = defaultdict(list)
        self.fails: list[tuple[str, str, str]] = []
        self.rules_run: list[str] = []

    def fail(self, rule: str, ent: Entity | None, msg: str, path: Path | None = None):
        p = path if path is not None else (ent.path if ent else Path("-"))
        if self.only is not None and p.resolve() not in self.only:
            return
        self.fails.append((rule, str(p), msg))

    def first(self, id_: str) -> Entity | None:
        lst = self.by_id.get(id_)
        return lst[0] if lst else None


def load_tree(roots: list[Path]) -> list[Entity]:
    ents = []
    for root in roots:
        for sub in ("continents", "countries", "cities"):
            d = root / sub
            if not d.is_dir():
                continue
            for p in sorted(d.rglob("*.yaml")) + sorted(d.rglob("*.yml")):
                err = None
                raw = None
                try:
                    raw = yaml.safe_load(p.read_text(encoding="utf-8"))
                except Exception as e:  # noqa: BLE001
                    err = f"YAML parse error: {e.__class__.__name__}: {str(e).splitlines()[0]}"
                ents.append(Entity(p, root, raw, err))
    return ents


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def is_str(v):
    return isinstance(v, str)


def type_ok(kind: str, v) -> bool:
    if kind == "str":
        return isinstance(v, str)
    if kind == "int":
        return isinstance(v, int) and not isinstance(v, bool)
    if kind == "bool":
        return isinstance(v, bool)
    if kind == "list":
        return isinstance(v, list)
    if kind == "dict":
        return isinstance(v, dict)
    if kind == "band":
        return isinstance(v, str) or isinstance(v, list)
    return True


def parse_time(v) -> tuple[int | None, str | None]:
    """Return (ordinal-ish comparable int, error). Accepts int year, 'YYYY-MM',
    'YYYY-MM-DD', datetime.date, or literal 'present'."""
    if v == "present":
        return PRESENT, None
    if isinstance(v, bool):
        return None, f"bad time value {v!r}"
    if isinstance(v, int):
        if 1 <= v <= 9999:
            return v * 10000, None
        return None, f"year out of range {v}"
    if isinstance(v, dt.datetime):
        v = v.date()
    if isinstance(v, dt.date):
        return v.year * 10000 + v.month * 100 + v.day, None
    if isinstance(v, str):
        m = re.fullmatch(r"(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?", v)
        if not m:
            return None, f"bad time format {v!r} (want YYYY, YYYY-MM, YYYY-MM-DD or present)"
        y, mo, d = int(m.group(1)), m.group(2), m.group(3)
        if mo and not 1 <= int(mo) <= 12:
            return None, f"bad month in {v!r}"
        if d:
            try:
                dt.date(y, int(mo), int(d))
            except ValueError:
                return None, f"bad date {v!r}"
        return y * 10000 + (int(mo) if mo else 0) * 100 + (int(d) if d else 0), None
    return None, f"bad time value {v!r}"


def year_of(v) -> int | None:
    t, err = parse_time(v)
    if err or t is None:
        return None
    if t == PRESENT:
        return None
    return t // 10000


def time_span(ent: Entity) -> tuple[int, int] | None:
    tr = ent.get("time_range")
    if not isinstance(tr, dict):
        return None
    s, e1 = parse_time(tr.get("start"))
    e, e2 = parse_time(tr.get("end"))
    if e1 or e2 or s is None or e is None:
        return None
    return s, e


def norm_start(t: int) -> int:
    """Pad a YYYY-only or YYYY-MM start to the earliest possible day."""
    return t


def norm_end(t: int) -> int:
    """Pad a YYYY-only or YYYY-MM end to the latest possible day so that
    a child dated 2012-09-30 lies inside a parent that ends in 2012."""
    if t == PRESENT:
        return t
    y, rest = divmod(t, 10000)
    mo, d = divmod(rest, 100)
    if mo == 0:
        return y * 10000 + 12 * 100 + 31
    if d == 0:
        return y * 10000 + mo * 100 + 31
    return t


def word_count(s: str) -> int:
    return len(re.findall(r"\S+", s or ""))


def sources_section_numbers(path: Path) -> set[int] | None:
    """Return the set of [n] entries in a research file's ## Sources section."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r"^## Sources\s*$", text, flags=re.M)
    if not m:
        return set()
    section = text[m.end():]
    nxt = re.search(r"^## ", section, flags=re.M)
    if nxt:
        section = section[: nxt.start()]
    return {int(n) for n in re.findall(r"^\[(\d+)\]", section, flags=re.M)}


def git_first_author(repo: Path, path: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%an <%ae>", "--", str(path)],
            cwd=repo, capture_output=True, text=True, check=False,
        ).stdout.strip().splitlines()
    except OSError:
        return None
    return out[-1].strip() if out else None


def date_ok(v) -> bool:
    if isinstance(v, dt.date):
        return True
    if isinstance(v, str):
        try:
            dt.date.fromisoformat(v)
            return True
        except ValueError:
            return False
    return False


# --------------------------------------------------------------------------- #
# Rules — one function per row of SPEC.md §3, named check_V_nn
# --------------------------------------------------------------------------- #

def check_V_01(ctx: Context):
    """File parses as YAML mapping; no unknown keys; declared types."""
    for e in ctx.entities:
        if e.parse_error:
            ctx.fail("V-01", e, e.parse_error)
            continue
        if not isinstance(e.raw, dict):
            ctx.fail("V-01", e, f"top level is {type(e.raw).__name__}, expected a mapping")
            continue
        for k, v in e.data.items():
            if k not in SCHEMA:
                ctx.fail("V-01", e, f"unknown field {k!r} (SPEC.md §2.1)")
                continue
            kind, _ = SCHEMA[k]
            if not type_ok(kind, v):
                ctx.fail("V-01", e, f"field {k!r} has type {type(v).__name__}, expected {kind}")
        # sub-structure types
        tr = e.get("time_range")
        if isinstance(tr, dict):
            for k in tr:
                if k not in ("start", "end"):
                    ctx.fail("V-01", e, f"time_range has unknown key {k!r}")
        rr = e.get("research_ref")
        if isinstance(rr, dict):
            for k in rr:
                if k not in ("file", "sources"):
                    ctx.fail("V-01", e, f"research_ref has unknown key {k!r}")
            if "sources" in rr and not isinstance(rr["sources"], list):
                ctx.fail("V-01", e, "research_ref.sources must be a list of ints")
        vb = e.get("verified_by")
        if isinstance(vb, dict):
            for k in vb:
                if k not in ("who", "date", "method"):
                    ctx.fail("V-01", e, f"verified_by has unknown key {k!r}")
        af = e.get("adjacent_field")
        if isinstance(af, dict):
            for k in af:
                if k not in ("field", "fed"):
                    ctx.fail("V-01", e, f"adjacent_field has unknown key {k!r}")


def check_V_02(ctx: Context):
    """Every R field for the level present and non-empty; '-' fields absent."""
    for e in ctx.entities:
        lvl = e.level if e.level in LEVELS else e.dir_level
        if lvl not in LEVELS:
            continue
        for field, (_, reqs) in SCHEMA.items():
            req = reqs[lvl]
            present = field in e.data and e.data[field] not in (None, "", [], {})
            if req == "R" and not present:
                ctx.fail("V-02", e, f"required field {field!r} missing or empty for level {lvl}")
            # '-' fields with a dedicated rule are reported there, not here:
            # type -> V-05, offshore -> V-14, parent_id on a continent -> V-33.
            if req == "-" and field in e.data and field not in ("type", "offshore", "parent_id"):
                ctx.fail("V-02", e, f"field {field!r} not allowed at level {lvl}")
        tr = e.get("time_range")
        if isinstance(tr, dict):
            for k in ("start", "end"):
                if tr.get(k) in (None, ""):
                    ctx.fail("V-02", e, f"time_range.{k} missing")
        rr = e.get("research_ref")
        if isinstance(rr, dict):
            if not rr.get("file"):
                ctx.fail("V-02", e, "research_ref.file missing")
            if not rr.get("sources"):
                ctx.fail("V-02", e, "research_ref.sources missing or empty (need ≥ 1)")


def check_V_03(ctx: Context):
    """id regex, equals basename, unique across data/."""
    seen: dict[str, Entity] = {}
    for e in ctx.entities:
        i = e.id
        if not is_str(i):
            continue
        if not ID_RE.match(i) or len(i) > 48:
            ctx.fail("V-03", e, f"id {i!r} does not match ^[a-z0-9]+(-[a-z0-9]+)*$ / ≤ 48 chars")
        if e.path.stem != i:
            ctx.fail("V-03", e, f"id {i!r} != file basename {e.path.stem!r}")
        if i in seen:
            ctx.fail("V-03", e, f"id {i!r} already defined in {seen[i].rel}")
        else:
            seen[i] = e


def check_V_04(ctx: Context):
    """level matches directory."""
    for e in ctx.entities:
        if not is_str(e.level):
            continue
        if e.level not in LEVELS:
            ctx.fail("V-04", e, f"level {e.level!r} not in {LEVELS}")
        elif e.dir_level != e.level:
            ctx.fail("V-04", e, f"level {e.level!r} but file is under {LEVEL_DIR.get(e.dir_level, '?')}/")


def check_V_05(ctx: Context):
    """type iff city, in enum."""
    for e in ctx.entities:
        t = e.get("type")
        if e.level == "city":
            if t is None:
                ctx.fail("V-05", e, "city missing 'type'")
            elif t not in CITY_TYPES:
                ctx.fail("V-05", e, f"type {t!r} not in {sorted(CITY_TYPES)}")
        elif t is not None and e.level in LEVELS:
            ctx.fail("V-05", e, f"'type' only allowed on cities (level is {e.level})")


def check_V_06(ctx: Context):
    """time_range.start ≤ end; formats valid."""
    for e in ctx.entities:
        tr = e.get("time_range")
        if not isinstance(tr, dict):
            continue
        s, es = parse_time(tr.get("start"))
        en, ee = parse_time(tr.get("end"))
        if es:
            ctx.fail("V-06", e, f"time_range.start: {es}")
        if ee:
            ctx.fail("V-06", e, f"time_range.end: {ee}")
        if s == PRESENT:
            ctx.fail("V-06", e, "time_range.start may not be 'present'")
        if s is not None and en is not None and s != PRESENT and s > norm_end(en):
            ctx.fail("V-06", e, f"time_range.start {tr.get('start')} > end {tr.get('end')}")


def check_V_07(ctx: Context):
    """child time_range within parent's, or notes has 'time-overlap-ok:'."""
    for e in ctx.entities:
        if e.level not in ("country", "city"):
            continue
        parent = ctx.first(e.get("parent_id")) if is_str(e.get("parent_id")) else None
        if parent is None:
            continue
        cs, ps = time_span(e), time_span(parent)
        if cs is None or ps is None:
            continue
        inside = cs[0] >= norm_start(ps[0]) and norm_end(cs[1]) <= norm_end(ps[1])
        if inside:
            continue
        notes = e.get("notes") or ""
        if re.search(r"time-overlap-ok:\s*\S", notes):
            continue
        ctx.fail("V-07", e, f"time_range outside parent {parent.id!r} and no 'time-overlap-ok: <reason>' in notes")


def check_V_08(ctx: Context):
    """band single enum or contiguous list of 2–5 in N1→S2 order."""
    for e in ctx.entities:
        b = e.get("band")
        if b is None:
            continue
        if isinstance(b, str):
            if b not in BANDS:
                ctx.fail("V-08", e, f"band {b!r} not in {BANDS}")
            continue
        if not isinstance(b, list):
            ctx.fail("V-08", e, "band must be a string or a list")
            continue
        if not 2 <= len(b) <= 5:
            ctx.fail("V-08", e, f"band list must have 2–5 entries, has {len(b)}")
            continue
        if any(x not in BANDS for x in b):
            ctx.fail("V-08", e, f"band list contains values outside {BANDS}: {b}")
            continue
        idx = [BANDS.index(x) for x in b]
        if idx != list(range(idx[0], idx[0] + len(idx))):
            ctx.fail("V-08", e, f"band list {b} is not contiguous in N1→N2→C→S1→S2 order")


def check_V_09(ctx: Context):
    """band_override_note ≥ 20 chars if present."""
    for e in ctx.entities:
        n = e.get("band_override_note")
        if n is None:
            continue
        if not is_str(n) or len(n.strip()) < 20:
            ctx.fail("V-09", e, "band_override_note present but shorter than 20 chars")


def check_V_10(ctx: Context):
    """biome in enum; present for continent and country."""
    for e in ctx.entities:
        b = e.get("biome")
        if b is None:
            if e.level in ("continent", "country"):
                ctx.fail("V-10", e, f"biome required for {e.level}")
            continue
        if b not in BIOMES:
            ctx.fail("V-10", e, f"biome {b!r} not in {sorted(BIOMES)}")


def check_V_11(ctx: Context):
    """summary word count within level range."""
    for e in ctx.entities:
        s = e.get("summary")
        if not is_str(s) or e.level not in SUMMARY_WORDS:
            continue
        lo, hi = SUMMARY_WORDS[e.level]
        n = word_count(s)
        if not lo <= n <= hi:
            ctx.fail("V-11", e, f"summary has {n} words; {e.level} range is {lo}–{hi}")


def check_V_12(ctx: Context):
    """continent/country subtitle regex + years equal time_range."""
    for e in ctx.entities:
        if e.level not in ("continent", "country"):
            continue
        st = e.get("subtitle")
        if not is_str(st):
            continue
        m = SUBTITLE_RE.match(st)
        if not m:
            ctx.fail("V-12", e, f"subtitle {st!r} does not match '^.+, YYYY(–(YYYY|present))?$'")
            continue
        tr = e.get("time_range") or {}
        if not isinstance(tr, dict):
            continue
        sy, ey = year_of(tr.get("start")), tr.get("end")
        ey_txt = "present" if ey == "present" else (str(year_of(ey)) if year_of(ey) else None)
        sub_s, sub_e = m.group(1), m.group(2)
        if sy is not None and int(sub_s) != sy:
            ctx.fail("V-12", e, f"subtitle start year {sub_s} != time_range.start {sy}")
        if sub_e is None:
            # single-year subtitle: allowed only when start == end year
            if ey_txt is not None and ey_txt != str(sy):
                ctx.fail("V-12", e, f"subtitle has one year but time_range ends {ey_txt}")
        elif ey_txt is not None and sub_e != ey_txt:
            ctx.fail("V-12", e, f"subtitle end {sub_e!r} != time_range.end {ey_txt!r}")


def check_V_13(ctx: Context):
    """name unique within level."""
    seen: dict[tuple[str, str], Entity] = {}
    for e in ctx.entities:
        n, lvl = e.get("name"), e.level
        if not is_str(n) or lvl not in LEVELS:
            continue
        key = (lvl, n.strip().casefold())
        if key in seen:
            ctx.fail("V-13", e, f"name {n!r} duplicates {seen[key].rel} at level {lvl}")
        else:
            seen[key] = e


def check_V_14(ctx: Context):
    """offshore only on continents; if true, end ≤ 1943."""
    for e in ctx.entities:
        if "offshore" not in e.data:
            continue
        if e.level != "continent":
            ctx.fail("V-14", e, "offshore only allowed on continents")
            continue
        if e.get("offshore") is True:
            tr = e.get("time_range") or {}
            end = tr.get("end") if isinstance(tr, dict) else None
            y = year_of(end)
            if end == "present" or (y is not None and y > 1943):
                ctx.fail("V-14", e, f"offshore continent must end ≤ 1943 (ends {end})")


def check_V_20(ctx: Context):
    """(net) every sources[].url returns < 400 via check_links.sh or is allowlisted."""
    if ctx.offline:
        return
    script = ctx.repo / "scripts" / "check_links.sh"
    files = [e.path for e in ctx.entities if isinstance(e.get("sources"), list)
             and (ctx.only is None or e.path.resolve() in ctx.only)]
    if not files or not script.exists():
        return
    res = subprocess.run(["bash", str(script), *map(str, files)], capture_output=True, text=True, check=False)
    for line in res.stdout.splitlines():
        if line.startswith("FAIL "):
            parts = line.split(maxsplit=3)
            if len(parts) == 4:
                _, code, f, url = parts
                ctx.fail("V-20", None, f"HTTP {code} for {url}", path=Path(f))


def check_V_21(ctx: Context):
    """sources length ≥ level min; each has url/title/kind/accessed."""
    for e in ctx.entities:
        src = e.get("sources")
        if not isinstance(src, list):
            continue
        need = SOURCE_MIN.get(e.level)
        if need and len(src) < need:
            ctx.fail("V-21", e, f"{len(src)} sources; {e.level} minimum is {need}")
        for i, s in enumerate(src):
            if not isinstance(s, dict):
                ctx.fail("V-21", e, f"sources[{i}] is not a mapping")
                continue
            for k in ("url", "title", "kind", "accessed"):
                if s.get(k) in (None, ""):
                    ctx.fail("V-21", e, f"sources[{i}] missing {k!r}")
            if s.get("kind") is not None and s.get("kind") not in SOURCE_KINDS:
                ctx.fail("V-21", e, f"sources[{i}].kind {s.get('kind')!r} not in {sorted(SOURCE_KINDS)}")
            if s.get("accessed") is not None and not date_ok(s.get("accessed")):
                ctx.fail("V-21", e, f"sources[{i}].accessed {s.get('accessed')!r} is not a YYYY-MM-DD date")
            u = s.get("url")
            if is_str(u) and not re.match(r"^https?://", u):
                ctx.fail("V-21", e, f"sources[{i}].url {u!r} is not http(s)")
            extra = set(s) - {"url", "title", "kind", "accessed"}
            if extra:
                ctx.fail("V-21", e, f"sources[{i}] has unknown keys {sorted(extra)}")


def check_V_22(ctx: Context):
    """research_ref.file exists; each int matches a [n] in its ## Sources."""
    cache: dict[Path, set[int] | None] = {}
    for e in ctx.entities:
        rr = e.get("research_ref")
        if not isinstance(rr, dict):
            continue
        f = rr.get("file")
        if not is_str(f):
            continue
        p = (ctx.repo / f)
        if not p.is_file():
            ctx.fail("V-22", e, f"research_ref.file {f!r} does not exist")
            continue
        if p not in cache:
            cache[p] = sources_section_numbers(p)
        nums = cache[p] or set()
        for n in rr.get("sources") or []:
            if not isinstance(n, int) or isinstance(n, bool):
                ctx.fail("V-22", e, f"research_ref.sources entry {n!r} is not an int")
            elif n not in nums:
                ctx.fail("V-22", e, f"research_ref.sources [{n}] not found in {f} ## Sources")


def check_V_30(ctx: Context):
    """parent exists, one level up; cities under data/cities/<continent>/."""
    for e in ctx.entities:
        pid = e.get("parent_id")
        if pid is None or e.level not in ("country", "city"):
            continue
        parent = ctx.first(pid) if is_str(pid) else None
        if parent is None:
            ctx.fail("V-30", e, f"parent_id {pid!r} does not exist")
            continue
        want = "continent" if e.level == "country" else "country"
        if parent.level != want:
            ctx.fail("V-30", e, f"parent {pid!r} is a {parent.level}, expected {want}")
            continue
        if e.level == "city" and e.dir_level == "city":  # wrong top dir is V-04's job
            gp = ctx.first(parent.get("parent_id")) if is_str(parent.get("parent_id")) else None
            if gp is None:
                continue  # parent's own V-30 failure covers it
            try:
                parts = e.path.relative_to(e.root).parts
            except ValueError:
                continue
            if len(parts) < 3 or parts[0] != "cities" or parts[1] != gp.id:
                ctx.fail("V-30", e, f"city must live in cities/{gp.id}/ (found {'/'.join(parts[:-1])}/)")


def check_V_31(ctx: Context):
    """neighbours[].id exists; relation in enum; no self-reference."""
    for e in ctx.entities:
        nb = e.get("neighbours")
        if not isinstance(nb, list):
            continue
        for i, n in enumerate(nb):
            if not isinstance(n, dict):
                ctx.fail("V-31", e, f"neighbours[{i}] is not a mapping")
                continue
            nid = n.get("id")
            if not is_str(nid) or ctx.first(nid) is None:
                ctx.fail("V-31", e, f"neighbours[{i}].id {nid!r} does not exist")
            elif nid == e.id:
                ctx.fail("V-31", e, f"neighbours[{i}] references itself")
            if n.get("relation") not in NEIGHBOUR_RELATIONS:
                ctx.fail("V-31", e, f"neighbours[{i}].relation {n.get('relation')!r} not in {sorted(NEIGHBOUR_RELATIONS)}")
            extra = set(n) - {"id", "relation", "note"}
            if extra:
                ctx.fail("V-31", e, f"neighbours[{i}] has unknown keys {sorted(extra)}")


def check_V_32(ctx: Context):
    """(--require-children) every continent ≥ 1 country, every country ≥ 1 city."""
    if not ctx.require_children:
        return
    children = Counter()
    for e in ctx.entities:
        pid = e.get("parent_id")
        if is_str(pid):
            children[pid] += 1
    for e in ctx.entities:
        if e.level in ("continent", "country") and is_str(e.id) and children[e.id] == 0:
            kind = "country" if e.level == "continent" else "city"
            ctx.fail("V-32", e, f"{e.level} {e.id!r} has no {kind} children")


def check_V_33(ctx: Context):
    """no cycles; parent graph is a forest rooted at continents.

    Each problem is reported once: a continent carrying parent_id is reported
    on the continent itself; a cycle is reported once per distinct cycle."""
    reported_cycles: set[frozenset] = set()
    for e in ctx.entities:
        if not is_str(e.id):
            continue
        if e.level == "continent" and "parent_id" in e.data:
            ctx.fail("V-33", e, f"continent {e.id!r} has a parent_id (continents are roots)")
            continue
        seen = [e.id]
        cur = e
        while True:
            if cur.level == "continent":
                break
            pid = cur.get("parent_id")
            if not is_str(pid):
                break  # V-02 covers the missing parent
            if pid in seen:
                cyc = frozenset(seen[seen.index(pid):] + [pid])
                if cyc not in reported_cycles:
                    reported_cycles.add(cyc)
                    ctx.fail("V-33", e, f"parent cycle: {' -> '.join(seen[seen.index(pid):] + [pid])}")
                break
            nxt = ctx.first(pid)
            if nxt is None:
                break  # V-30 covers the dangling parent
            seen.append(pid)
            cur = nxt
            if len(seen) > 10:
                ctx.fail("V-33", e, "parent chain longer than 10; not a 3-level tree")
                break


def check_V_40(ctx: Context):
    """adjacent_field: field non-empty, fed is an existing id ≠ self."""
    for e in ctx.entities:
        af = e.get("adjacent_field")
        if not isinstance(af, dict):
            continue
        if not is_str(af.get("field")) or not af.get("field").strip():
            ctx.fail("V-40", e, "adjacent_field.field is empty")
        fed = af.get("fed")
        if not is_str(fed) or ctx.first(fed) is None:
            ctx.fail("V-40", e, f"adjacent_field.fed {fed!r} does not exist")
        elif fed == e.id:
            ctx.fail("V-40", e, "adjacent_field.fed references itself")


def check_V_50(ctx: Context):
    """status enum + the requirements of that status (SPEC.md §5.1)."""
    for e in ctx.entities:
        st = e.get("status")
        if st is None:
            continue
        if st not in STATUSES:
            ctx.fail("V-50", e, f"status {st!r} not in {STATUSES}")
            continue
        rank = STATUSES.index(st)
        src = e.get("sources") if isinstance(e.get("sources"), list) else []
        if rank >= STATUSES.index("verified"):
            vb = e.get("verified_by")
            if not isinstance(vb, dict):
                ctx.fail("V-50", e, f"status {st} requires verified_by")
            else:
                who = vb.get("who")
                if not is_str(who) or not who.strip():
                    ctx.fail("V-50", e, "verified_by.who missing")
                if not date_ok(vb.get("date")):
                    ctx.fail("V-50", e, f"verified_by.date {vb.get('date')!r} is not YYYY-MM-DD")
                if not is_str(vb.get("method")) or not vb.get("method").strip():
                    ctx.fail("V-50", e, "verified_by.method missing")
                author = git_first_author(ctx.repo, e.path)
                if author and is_str(who) and who.strip() and (
                    who.strip().casefold() == author.casefold()
                    or who.strip().casefold() == author.split("<")[0].strip().casefold()
                ):
                    ctx.fail("V-50", e, f"verified_by.who {who!r} equals the git author of the file's first commit")
            need = VERIFIED_SOURCE_MIN.get(e.level, 1)
            if len(src) < need:
                ctx.fail("V-50", e, f"status {st} {e.level} needs ≥ {need} sources, has {len(src)}")
            if e.level == "city":
                kinds = {s.get("kind") for s in src if isinstance(s, dict)}
                if not (kinds - {"wikipedia", None}):
                    ctx.fail("V-50", e, f"status {st} city needs ≥ 1 source of kind ≠ wikipedia")
        if rank >= STATUSES.index("placed") and e.level == "country":
            nb = e.get("neighbours")
            if not isinstance(nb, list) or len(nb) < 1:
                ctx.fail("V-50", e, "status placed country needs ≥ 1 neighbour")
        elif st in ("draft", "sourced") and e.get("verified_by") is not None:
            ctx.fail("V-50", e, f"verified_by present but status is {st}")
        if rank >= STATUSES.index("draft") and len(src) < 1:
            ctx.fail("V-50", e, "status draft needs ≥ 1 source")


def check_V_51(ctx: Context):
    """threads in enum, no duplicates."""
    for e in ctx.entities:
        th = e.get("threads")
        if not isinstance(th, list):
            continue
        bad = [t for t in th if t not in THREADS]
        if bad:
            ctx.fail("V-51", e, f"threads {bad} not in {sorted(THREADS)}")
        dup = [t for t, c in Counter(th).items() if c > 1]
        if dup:
            ctx.fail("V-51", e, f"duplicate threads {dup}")


def check_V_60(ctx: Context):
    """coverage matrices: every city id listed exists; every city appears."""
    ids = {e.id for e in ctx.entities if is_str(e.id)}
    cities_by_cont: dict[str, set[str]] = defaultdict(set)
    for e in ctx.entities:
        if e.level == "city" and is_str(e.id):
            try:
                parts = e.path.relative_to(e.root).parts
            except ValueError:
                continue
            if len(parts) >= 3:
                cities_by_cont[parts[1]].add(e.id)
    for root in ctx.roots:
        cov = root / "coverage"
        matrices: dict[str, Path] = {}
        if cov.is_dir():
            for p in sorted(cov.glob("*.md")):
                if p.stem.upper() == "README":
                    continue
                matrices[p.stem] = p
                text = p.read_text(encoding="utf-8")
                # city decisions: a table cell "city" followed by an id cell
                for m in re.finditer(r"\|\s*city\s*\|\s*`?([a-z0-9][a-z0-9-]*)`?\s*\|", text):
                    cid = m.group(1)
                    if cid not in ids:
                        ctx.fail("V-60", None, f"coverage matrix names city id {cid!r} which does not exist", path=p)
        for cont, cids in cities_by_cont.items():
            mp = matrices.get(cont)
            if mp is None:
                for cid in sorted(cids):
                    ctx.fail("V-60", ctx.first(cid), f"city {cid!r} has no coverage matrix {cov / (cont + '.md')}")
                continue
            text = mp.read_text(encoding="utf-8")
            for cid in sorted(cids):
                if not re.search(r"(?<![a-z0-9-])" + re.escape(cid) + r"(?![a-z0-9-])", text):
                    try:
                        mp_disp = str(mp.resolve().relative_to(ctx.repo))
                    except ValueError:
                        mp_disp = str(mp)
                    ctx.fail("V-60", ctx.first(cid), f"city {cid!r} not listed in {mp_disp}")


RULES = [check_V_01, check_V_02, check_V_03, check_V_04, check_V_05, check_V_06,
         check_V_07, check_V_08, check_V_09, check_V_10, check_V_11, check_V_12,
         check_V_13, check_V_14, check_V_20, check_V_21, check_V_22, check_V_30,
         check_V_31, check_V_32, check_V_33, check_V_40, check_V_50, check_V_51,
         check_V_60]


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #

def find_repo(start: Path) -> Path:
    p = start.resolve()
    for cand in [p, *p.parents]:
        if (cand / "SPEC.md").exists() and (cand / "scripts").is_dir():
            return cand
    return Path.cwd()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roots", nargs="*", help="data root(s); default data/")
    ap.add_argument("--file", action="append", default=[], help="validate only this file (repeatable)")
    ap.add_argument("--offline", action="store_true", help="skip V-20 (network)")
    ap.add_argument("--require-children", action="store_true", help="enable V-32")
    ap.add_argument("--summary", action="store_true", help="print counts by level/status")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    repo = find_repo(Path(__file__).parent)
    only: set[Path] | None = None
    roots: list[Path] = []
    if args.file:
        only = set()
        for f in args.file:
            p = Path(f).resolve()
            if not p.exists():
                print(f"FAIL V-01 {f} file does not exist")
                return 1
            only.add(p)
            # root = the directory two above continents/ countries/ cities/
            for anc in p.parents:
                if anc.name in ("continents", "countries", "cities"):
                    r = anc.parent
                    if r not in roots:
                        roots.append(r)
                    break
    for r in args.roots:
        rp = Path(r).resolve()
        if rp not in roots:
            roots.append(rp)
    if not roots:
        roots = [repo / "data"]

    ctx = Context(roots, args.offline, args.require_children, only, repo)
    ctx.entities = load_tree(roots)
    for e in ctx.entities:
        if is_str(e.id):
            ctx.by_id[e.id].append(e)

    for rule in RULES:
        rule(ctx)
        ctx.rules_run.append(rule.__name__.replace("check_", "").replace("_", "-"))

    def sort_key(t):
        rule, f, _ = t
        return (f, rule)

    for rule, f, msg in sorted(ctx.fails, key=sort_key):
        try:
            f_disp = str(Path(f).resolve().relative_to(repo))
        except ValueError:
            f_disp = f
        print(f"FAIL {rule} {f_disp} {msg}")

    n_files = len(ctx.entities) if only is None else len(only)
    skipped = " (V-20 skipped: --offline)" if args.offline else ""
    v32 = "" if args.require_children else " (V-32 off; use --require-children)"
    print(f"validate.py: files={n_files} rules={len(RULES)} fails={len(ctx.fails)}{skipped}{v32}")
    if args.summary:
        c = Counter((e.level, e.get("status")) for e in ctx.entities)
        for lvl in LEVELS:
            row = ", ".join(f"{st}={c[(lvl, st)]}" for st in STATUSES if c[(lvl, st)])
            tot = sum(v for (l, _), v in c.items() if l == lvl)
            print(f"  {lvl:9s} total={tot} {row}")
    return 1 if ctx.fails else 0


if __name__ == "__main__":
    sys.exit(main())
