"""Merge per-window deal JSONL files into one deduplicated dataset (CSV + XLSX)."""
import glob
import json
import re
import sys
from pathlib import Path

import pandas as pd

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/raw")
OUT = Path("data")

COLS = [
    "id", "announce_date", "licensor", "licensor_ticker", "licensee", "licensee_ticker",
    "asset", "modality", "target_indication", "stage_at_deal", "territory_licensed",
    "deal_structure", "upfront_usd_m", "near_term_usd_m", "milestones_total_usd_m",
    "total_deal_value_usd_m", "royalty_terms", "royalty_disclosed_level", "equity_in_newco",
    "status_2026", "monetization_flag", "sources", "notes",
]


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s).lower())


def num(x):
    if x is None or x == "":
        return None
    if isinstance(x, (int, float)):
        return float(x)
    m = re.search(r"[\d.]+", str(x).replace(",", ""))
    return float(m.group()) if m else None


rows = []
for f in sorted(glob.glob(str(SRC / "*.jsonl"))):
    for i, line in enumerate(open(f, encoding="utf-8")):
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            print(f"skip {f}:{i+1}: {e}", file=sys.stderr)
            continue
        r["_file"] = Path(f).stem
        rows.append(r)

df = pd.DataFrame(rows)
for c in COLS:
    if c not in df:
        df[c] = None
for c in ["upfront_usd_m", "near_term_usd_m", "milestones_total_usd_m", "total_deal_value_usd_m"]:
    df[c] = df[c].map(num)
df["sources"] = df["sources"].map(lambda v: " | ".join(v) if isinstance(v, list) else (v or ""))
# Some records only carry a month ("2023-10" / "2025-06 (approx)"): fall back to the 1st.
df["announce_date"] = df["announce_date"].astype(str).str.extract(r"(\d{4}-\d{2}(?:-\d{2})?)")[0]
df["announce_date"] = pd.to_datetime(df["announce_date"].where(df["announce_date"].str.len() == 10, df["announce_date"] + "-01"), errors="coerce")

# Dedupe on (licensor, asset, month): windows can overlap at boundaries.
df["_key"] = df["licensor"].map(norm).str[:12] + "|" + df["asset"].map(norm).str[:12] + "|" + df["announce_date"].dt.strftime("%Y%m").fillna("")
df["_filled"] = df[COLS].notna().sum(axis=1)
df = df.sort_values("_filled", ascending=False).drop_duplicates("_key").sort_values("announce_date")
df = df[(df["announce_date"] >= "2023-01-01") | df["announce_date"].isna()]

# Hand-verified corrections (see data/overrides.json).
ov_path = OUT / "overrides.json"
if ov_path.exists():
    for rid, fields in json.load(open(ov_path, encoding="utf-8")).items():
        if rid.startswith("_"):
            continue
        m = df["id"] == rid
        for k, v in fields.items():
            if k == "sources_add":
                df.loc[m, "sources"] = df.loc[m, "sources"] + " | " + v
            else:
                df.loc[m, k] = v

out = df[COLS + ["_file"]].rename(columns={"_file": "source_window"})
out["announce_date"] = out["announce_date"].dt.strftime("%Y-%m-%d")
OUT.mkdir(exist_ok=True)
out.to_csv(OUT / "china_outlicensing_2023_2026.csv", index=False, encoding="utf-8-sig")
with pd.ExcelWriter(OUT / "china_outlicensing_2023_2026.xlsx") as xw:
    out.to_excel(xw, sheet_name="deals", index=False)
print(f"{len(out)} deals written")
print(out.groupby(out["announce_date"].str[:4]).size().to_string())
