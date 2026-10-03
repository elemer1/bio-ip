# bio-ip

Research on China biopharma out-licensing (2023–2026) and unmonetized royalty / milestone rights.

- `data/raw/*.jsonl` — per-window deal records collected from press releases, HKEX/SSE announcements and licensee SEC filings (each with source URLs)
- `data/overrides.json` — hand-verified status corrections
- `data/china_outlicensing_2023_2026.{csv,xlsx}` — merged, deduplicated dataset (290 deals)
- `data/screen_ranked.csv` — heuristic monetizability score (first pass)
- `reports/top20_unmonetized_royalties.md` — curated top-20 shortlist and thesis
- `reports/monetization_exclusions_and_context.md` — known royalty sales by China licensors, pricing and regulatory context

Rebuild: `pip install pandas openpyxl && python3 scripts/build_dataset.py data/raw && python3 scripts/screen.py`
