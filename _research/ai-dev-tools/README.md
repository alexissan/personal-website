# AI dev tools field guide — research pipeline

Builds `/ai-dev-tools` (page, `tools.json`, `cover.png`). Not deployed: `_research` is in `.assetsignore`.

```
python3 -I hn_discover.py      # HN stories since 2025 (Algolia)        -> raw/hn_stories.json
python3 -I hn_threads.py       # every comment in 24 Ask HN setup threads -> raw/hn_ask_comments.json
python3 clean_quotes.py        # strip the Nov 2026 questionnaire text people quoted back
python3 collect.py             # per-tool signals: HN, Lobsters, dev.to, GitHub, npm, PyPI (cached in raw/cache)
python3 score.py               # 0-100 per category                     -> raw/scored.json
python3 build.py               # merges raw/verdicts_*.json + overrides.json + editorial.py -> ../../ai-dev-tools/
```

- `registry.py`: every candidate tool, its category, match regex, search query and package ids.
- `raw/verdicts_*.json`: per-tool tone counts and verdicts, written by reading the comment evidence in `raw/evidence/`.
- `overrides.json`: fact-checked corrections, renames, hidden off-topic story links.
- `cover.html`: the 1200x630 share image, rendered with headless Chrome.
