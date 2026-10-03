"""First-pass screen: rank royalty/milestone streams by monetizability.

Heuristic only -- the final top-20 in reports/ is curated by hand on top of this.
score = stage x royalty_visibility x licensee_credit x territory x structure
Excluded: terminated/returned/failed assets and streams already sold.
"""
import re

import pandas as pd

d = pd.read_csv("data/china_outlicensing_2023_2026.csv")

BIG = r"pfizer|merck|msd|astrazeneca|novartis|roche|genentech|gsk|glaxo|sanofi|abbvie|bristol|bms|lilly|novo nordisk|takeda|amgen|gilead|regeneron|boehringer|bayer|biogen|vertex|j&j|johnson|janssen|daiichi|astellas|otsuka|eisai|ipsen|merck kgaa|biontech|ucb|servier|menarini|santen|madrigal|neurocrine|alkermes|travere|jazz|incyte|summit"
DEAD = r"extinguish|futility|terminat|returned|discontinu|fail|deprioriti|rights revert|ended"
SOLD = r"royalty pharma|sold (?:its|the) royalty|royalty sale|synthetic royalty|monetiz"


def stage(s):
    s = str(s).lower()
    if re.search(r"approv|launch|marketed", s):
        return 5.0
    if re.search(r"bla|nda|maa|filed|pdufa|submitted", s):
        return 4.0
    if re.search(r"ph(?:ase)?\s*3|ph(?:ase)?\s*iii|registrational|pivotal", s):
        return 3.0
    if re.search(r"ph(?:ase)?\s*2|ph(?:ase)?\s*ii", s):
        return 1.5
    if re.search(r"ph(?:ase)?\s*1|ph(?:ase)?\s*i\b|ind", s):
        return 0.7
    return 0.3


def row(r):
    status = f"{r.status_2026} {r.stage_at_deal}"
    st = max(stage(r.status_2026), stage(r.stage_at_deal))
    vis = {"exact": 1.0, "range": 1.0, "qualitative": 0.7}.get(str(r.royalty_disclosed_level).lower(), 0.4)
    credit = 1.0 if re.search(BIG, str(r.licensee).lower()) else 0.55
    terr = str(r.territory_licensed).lower()
    t = 1.0 if re.search(r"global|ex-china|ex-greater|worldwide|outside", terr) else (0.6 if "us" in terr else 0.35)
    struct = str(r.deal_structure).lower()
    s = 0.5 if re.search(r"newco|asset sale|acquisition|buy-?back", struct) else 1.0
    dead = bool(re.search(DEAD, str(r.status_2026).lower()))
    sold = bool(re.search(SOLD, str(r.monetization_flag).lower())) and "none" not in str(r.monetization_flag).lower()[:12]
    return pd.Series({"stage_score": st, "score": 0 if (dead or sold) else round(st * vis * credit * t * s, 2),
                      "excluded": "dead" if dead else ("sold" if sold else "")})


d = pd.concat([d, d.apply(row, axis=1)], axis=1).sort_values("score", ascending=False)
d.to_csv("data/screen_ranked.csv", index=False, encoding="utf-8-sig")
cols = ["announce_date", "licensor", "licensee", "asset", "status_2026", "royalty_terms", "score", "excluded"]
with pd.option_context("display.max_colwidth", 40, "display.width", 250):
    print(d[cols].head(60).to_string(index=False))
