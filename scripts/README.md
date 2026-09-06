# scripts/

| Script | Purpose |
|---|---|
| `wiki.sh` | Plain-text extract of a Wikipedia article for fact-checking. Cached under `.cache/wiki/`, retries on 429/5xx with back-off. `scripts/wiki.sh "Dartmouth_workshop" [chars]`; `WIKI_NOCACHE=1` bypasses the cache. |
| `check_links.sh` | Every http(s) URL in `.md` files, and every `url:` value in `.yaml` files, must return HTTP < 400 or be listed in `link_allowlist.txt`. Prints `FAIL <code> <file> <url>` lines and `checked=N failed=M allowlisted=K` (N = distinct URLs). Exit 1 on any failure. |
| `link_allowlist.txt` | Exact URLs known to block bots or containing template placeholders; `#` lines are reasons. |
| `validate.py` | Entity validator implementing every rule in `SPEC.md` §3 (V-01 … V-60). |
| `fixtures/` | Validator test fixtures (`valid/` mini data root; `invalid/<rule>/` one violation each; `EXPECTED.txt`; `run.sh`). |

## validate.py

Requires Python ≥ 3.11 and PyYAML; the shebang uses `uv run --script`, which
installs PyYAML into an ephemeral environment on first run.

```
scripts/validate.py                         # validate data/ (network on)
scripts/validate.py --offline               # skip V-20 (link checking)
scripts/validate.py --file data/continents/deep-learning-basin.yaml
scripts/validate.py --require-children      # turn on V-32
scripts/validate.py --summary               # entity counts by level/status
scripts/validate.py some/other/root         # validate a different data root
```

Output: one `FAIL <rule> <file> <message>` line per violation (sorted by
file, then rule), then a summary line `validate.py: files=N rules=25 fails=M`.
Exit code 1 if any FAIL, else 0.

Semantics worth knowing:

- `--file` validates only the named file(s) but loads the whole tree they
  live in, so cross-file rules (V-03 uniqueness, V-30 parents, V-31
  neighbours, V-60 coverage) still see context. Only FAIL lines for the named
  files are printed.
- `--offline` skips **only** V-20. Nothing else touches the network.
- V-20 shells out to `check_links.sh` with every file that has `sources`.
- V-32 is off unless `--require-children` is passed (partial progress
  validates, per `SPEC.md`).
- V-50 compares `verified_by.who` with the git author of the file's first
  commit (`git log --diff-filter=A --follow`). Outside a git checkout that
  comparison is skipped.
- Rules that are the *cause* of another rule's failure are reported once:
  a wrong `type` is V-05 not V-02; `offshore` on a country is V-14; a
  continent with `parent_id` is V-33. Fixtures pin this behaviour.

## Fixtures

```
scripts/fixtures/run.sh            # compare every case with EXPECTED.txt
scripts/fixtures/run.sh --update   # regenerate EXPECTED.txt after a deliberate change
FIXTURE_OFFLINE=1 scripts/fixtures/run.sh   # skip the V-20 (network) case
```

`fixtures/valid/` is the three `SPEC.md` §2.10 worked examples made mutually
consistent (summaries padded to the word-count ranges, spec-example
neighbours that do not exist in the fixture set removed) plus a coverage
matrix stub. `fixtures/invalid/<rule>/` is a copy of `valid/` with exactly
one violation of `<rule>`; `EXPECTED.txt` holds the byte-exact expected FAIL
line per case. A `FLAGS` file in a case directory adds validator flags (V-32
needs `--require-children`). The V-20 case is the only one that runs online.
