#!/usr/bin/env python3
"""Monthly Refresh CLI for Map of AI — The 2036 Textbook Atlas.

Designed to make monthly catalog refreshes (new frontier models, agent protocols,
or historical revisions) a painless, single-command workflow without manual
coordinate math.

Usage:
  # 1. Inspect current catalog statistics and recent Eastern Frontier entries:
  python3 scripts/refresh.py --status

  # 2. Scaffold or append a new milestone to any province in data/events/*.yaml:
  python3 scripts/refresh.py --add \\
    --country generative-ai-continent-transformers-foundation-models \\
    --id gemini-4-5-ultra \\
    --name "Gemini 4.5 Ultra" \\
    --year 2026.9 \\
    --lod 3 \\
    --one-line "Native multi-hour autonomous verification and world-model synthesis" \\
    --source-url "https://blog.google/technology/ai/" \\
    --source-title "Google DeepMind 2026 — Gemini 4.5 Technical Report"

  # 3. Rebuild entities, validate schema, render multi-scale tiles (z=0..4), and run all gates:
  python3 scripts/refresh.py --build
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SITE_DIR = ROOT / "site"


def load_catalog_summary():
    entities_path = SITE_DIR / "entities.json"
    if not entities_path.exists():
        subprocess.run([sys.executable, str(SITE_DIR / "build_entities_json.py"), str(DATA_DIR), str(entities_path)], check=True)
    data = json.loads(entities_path.read_text(encoding="utf-8"))
    continents = data.get("continents", [])
    countries = data.get("countries", [])
    threads = data.get("threads", [])
    all_events = []
    for c in countries:
        for e in c.get("events", []):
            all_events.append({**e, "country_id": c["id"], "country_name": c["name"], "parent_id": c["parent_id"]})
    thread_ms = sum(len(t.get("milestones", [])) for t in threads)
    return continents, countries, threads, all_events, thread_ms


def cmd_status():
    continents, countries, threads, all_events, thread_ms = load_catalog_summary()
    spatial_countries = [c for c in countries if c.get("spatial")]
    by_lod = {3: 0, 4: 0}
    for e in all_events:
        lod = int(e.get("lod", 4))
        by_lod[lod] = by_lod.get(lod, 0) + 1

    print("=" * 72)
    print("MAP OF AI — 2036 TEXTBOOK ATLAS CATALOG STATUS")
    print("=" * 72)
    print(f"Continents:         {len(continents)}")
    print(f"Provinces:          {len(countries)} ({len(spatial_countries)} spatial)")
    print(f"Province Events:    {len(all_events)} (LOD 3 Syllabus: {by_lod.get(3, 0)} | LOD 4 Archive: {by_lod.get(4, 0)})")
    print(f"Thread Summits:     {thread_ms} across {len(threads)} cross-cutting range(s)")
    print(f"Outlying Islands:   10 (27 historical cul-de-sac / fringe milestones)")
    print(f"Total Milestones:   {len(all_events) + thread_ms + 27}")
    print("-" * 72)
    print("EASTERN FRONTIER (2025.0 – Present) — Latest 25 Milestones:")
    recent = sorted([e for e in all_events if e["year"] >= 2025.0], key=lambda x: (x["year"], x["id"]), reverse=True)[:25]
    for e in recent:
        print(f"  {e['year']:6.1f}  [LOD {e['lod']}]  {e['name']:<28} ({e['country_id']})")
    print("=" * 72)


def find_event_file_for_country(country_id: str) -> Path:
    for ep in sorted((DATA_DIR / "events").glob("*.yaml")):
        doc = yaml.safe_load(ep.read_text(encoding="utf-8")) or {}
        if country_id in (doc.get("countries") or {}):
            return ep
    raise SystemExit(f"Country ID '{country_id}' not found in any data/events/*.yaml file.")


def cmd_add(args):
    words = args.one_line.strip().split()
    if len(words) > 15:
        raise SystemExit(f"Error: --one-line has {len(words)} words (maximum allowed by validate.py is 15 words).")

    ep = find_event_file_for_country(args.country)
    text = ep.read_text(encoding="utf-8")
    doc = yaml.safe_load(text) or {}
    c_spec = doc["countries"][args.country]
    existing_ids = {e["id"] for e in (c_spec.get("events") or [])}
    if args.id in existing_ids:
        raise SystemExit(f"Error: Event ID '{args.id}' already exists in {ep.name} under {args.country}.")

    new_entry = {
        "id": args.id,
        "name": args.name,
        "year": float(args.year),
        "lod": int(args.lod),
        "one_line": args.one_line.strip(),
        "sources": [{"url": args.source_url, "title": args.source_title}],
    }
    c_spec.setdefault("events", []).append(new_entry)
    c_spec["events"].sort(key=lambda x: (float(x["year"]), x["id"]))

    if args.dry_run:
        print(f"[DRY RUN] Would append to {ep.relative_to(ROOT)} under '{args.country}':")
        print(yaml.dump([new_entry], sort_keys=False, allow_unicode=True))
        return

    ep.write_text(yaml.dump(doc, sort_keys=False, allow_unicode=True, width=110), encoding="utf-8")
    print(f"Added '{args.name}' ({args.year}) to {ep.relative_to(ROOT)} under '{args.country}'.")
    print("Validating updated catalog...")
    subprocess.run([sys.executable, str(SITE_DIR / "build_entities_json.py"), str(DATA_DIR), str(SITE_DIR / "entities.json")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py"), "--offline", "--summary"], check=True)


def cmd_build(skip_tiles: bool = False):
    print("1/4 Compiling data/*.yaml -> site/entities.json & site/entities.js...")
    subprocess.run([sys.executable, str(SITE_DIR / "build_entities_json.py"), str(DATA_DIR), str(SITE_DIR / "entities.json")], check=True)

    print("2/4 Running schema & citation validation (scripts/validate.py --offline --summary)...")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py"), "--offline", "--summary"], check=True)

    if not skip_tiles:
        print("3/4 Rendering multi-scale tile pyramid (z=0..4), site/labels.json, and site/atlas_data.js...")
        subprocess.run([sys.executable, str(SITE_DIR / "build_tiles.py")], check=True)

    print("4/4 Running cartographic layout & 100-frame mobile density gates...")
    subprocess.run([sys.executable, str(SITE_DIR / "check_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "tests" / "sample_frames.py")], check=True)
    print("Monthly refresh build and all verification gates PASSED.")


def main():
    parser = argparse.ArgumentParser(description="Monthly Refresh CLI for Map of AI")
    parser.add_argument("--status", action="store_true", help="Print catalog counts and latest Eastern Frontier entries")
    parser.add_argument("--add", action="store_true", help="Add a new milestone to data/events/*.yaml")
    parser.add_argument("--build", action="store_true", help="Run full build and verification pipeline")
    parser.add_argument("--skip-tiles", action="store_true", help="With --build, skip raster tile rendering")
    parser.add_argument("--dry-run", action="store_true", help="With --add, preview YAML snippet without writing")
    parser.add_argument("--country", type=str, help="Target country_id for --add")
    parser.add_argument("--id", type=str, help="Unique kebab-case event id for --add")
    parser.add_argument("--name", type=str, help="Display name (<= 28 chars recommended) for --add")
    parser.add_argument("--year", type=float, help="Decimal year (e.g. 2026.8) for --add")
    parser.add_argument("--lod", type=int, default=3, choices=[3, 4], help="Altitude LOD (3=Syllabus, 4=Archive)")
    parser.add_argument("--one-line", type=str, help="Concise summary (<= 15 words) for --add")
    parser.add_argument("--source-url", type=str, help="Primary citation URL for --add")
    parser.add_argument("--source-title", type=str, help="Primary citation Author Year — Title for --add")

    args = parser.parse_args()
    if args.add:
        required = ["country", "id", "name", "year", "one_line", "source_url", "source_title"]
        missing = [k for k in required if getattr(args, k) is None]
        if missing:
            parser.error(f"--add requires: {', '.join('--' + m.replace('_', '-') for m in missing)}")
        cmd_add(args)
    elif args.build:
        cmd_build(skip_tiles=args.skip_tiles)
    else:
        cmd_status()


if __name__ == "__main__":
    main()
