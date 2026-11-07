"""Turn raw signals into a 0-100 score per tool, normalised within its category.

Weights favour what developers say they use over what gets starred:
  40  HN Ask threads      distinct commenters naming the tool (recent threads 1.0, older 0.5)
  20  HN comment volume   comments in the last 12 months, precision-checked
  12  HN front-page pull  points on stories whose title names the tool (since 2025)
   7  Lobsters            score + stories naming the tool
   5  dev.to              reactions on top-of-year posts naming the tool
  16  adoption            max(GitHub stars, npm + PyPI monthly downloads), log-scaled

Every signal is log-scaled and divided by the category maximum, so a tool is compared with
its neighbours, not with Claude Code. Tools with no repo or package are not penalised:
their adoption weight is redistributed across the HN signals.
"""
import json, math
from collections import defaultdict

# A category's best tool only gets full marks on a signal if it clears these floors,
# so thin categories (3 mentions tops) don't turn noise into a perfect score.
FLOOR = dict(ask=15, comments=300, titles=800, lobsters=40, devto=150)
W = dict(ask=40, comments=20, titles=12, lobsters=7, devto=5, adoption=16)

def signals(t):
    dl = (t.get("npm_month") or 0) + (t.get("pypi_month") or 0)
    return dict(
        ask=t["ask_authors_recent"] + 0.5 * t["ask_authors_old"],
        comments=t["hn_comments_12m"],
        titles=t["hn_title_points"],
        lobsters=t["lobsters_score"] + 5 * t["lobsters_count"],
        devto=t["devto_reactions"],
        stars=t.get("gh_stars") or 0,
        downloads=dl,
    )

def score_all(tools):
    by_cat = defaultdict(list)
    for t in tools:
        t["sig"] = signals(t)
        by_cat[t["cat"]].append(t)
    for cat, ts in by_cat.items():
        mx = {k: max(max(math.log1p(t["sig"][k]) for t in ts), math.log1p(FLOOR.get(k, 0))) or 1 for k in ts[0]["sig"]}
        for t in ts:
            n = {k: math.log1p(v) / mx[k] if mx[k] else 0 for k, v in t["sig"].items()}
            has_adoption = bool(t.get("gh_stars") or t["sig"]["downloads"])
            n["adoption"] = max(n["stars"], n["downloads"])
            if has_adoption:
                total = sum(W[k] * n[k] for k in W)
            else:  # closed-source / hosted: re-weight over the other signals
                hn_w = {k: v for k, v in W.items() if k != "adoption"}
                total = sum(hn_w[k] * n[k] for k in hn_w) * 100 / sum(hn_w.values())
            t["norm"] = {k: round(v, 3) for k, v in n.items()}
            t["score"] = round(total, 1)
        ts.sort(key=lambda t: -t["score"])
    return by_cat

if __name__ == "__main__":
    tools = json.load(open("raw/signals.json"))
    by_cat = score_all(tools)
    for cat, ts in by_cat.items():
        print(f"\n## {cat}")
        for i, t in enumerate(ts, 1):
            s = t["sig"]
            print(f"{i:2d}. {t['score']:5.1f}  {t['name']:30s} ask={t['ask_authors_recent']}/{t['ask_authors_old']} cm={s['comments']} ti={s['titles']} lob={s['lobsters']} dev={s['devto']} ★={s['stars']} dl={s['downloads']}")
    json.dump(tools, open("raw/scored.json", "w"), indent=1)
