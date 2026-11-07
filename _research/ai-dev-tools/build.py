"""Render ai-dev-tools/index.html + tools.json from scored signals, tone/verdict reviews and editorial copy."""
import glob, html, json, re
from registry import CATEGORIES
from editorial import FINDINGS, CATEGORY_NOTES, KNOWN_OSS, SOURCES, PROPOSED, CAVEATS, WEIGHTS

E = html.escape
OUT = "../../ai-dev-tools"
scored = json.load(open("raw/scored.json"))
meta = json.load(open("raw/meta.json"))
harness = json.load(open("raw/harness_share.json"))
trend = json.load(open("raw/trend.json"))
licenses = json.load(open("raw/licenses.json"))
reviews = {}
for f in sorted(glob.glob("raw/verdicts_*.json")):
    for cat, items in json.load(open(f)).items():
        for r in items:
            reviews[r["name"]] = r
overrides = json.load(open("overrides.json")) if glob.glob("overrides.json") else {}
for old, new in overrides.get("_rename", {}).items():
    if old in reviews: reviews[new] = reviews.pop(old)

def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def hn_item(i): return f"https://news.ycombinator.com/item?id={i}"
def fmt(n):
    if n >= 1_000_000: return f"{n/1_000_000:.1f}M".replace(".0M", "M")
    if n >= 10_000: return f"{n/1000:.0f}k"
    if n >= 1_000: return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)

# ---- final score: data score, discounted for false matches, nudged by tone ----
for t in scored:
    r = reviews.get(t["name"], {})
    judged = sum(r.get(k, 0) for k in ("pos", "neg", "mixed", "neutral"))
    false = r.get("false", 0)
    t["false_rate"] = round(false / (judged + false), 2) if judged + false else 0
    t["tone"] = round((r.get("pos", 0) - r.get("neg", 0)) / judged, 2) if judged >= 4 else 0
    t["final"] = min(100.0, round(t["score"] * (1 - 0.5 * t["false_rate"]) + 6 * t["tone"], 1))
    t["what"] = overrides.get(t["name"], {}).get("what") or r.get("what_it_is", "")
    t["verdict"] = overrides.get(t["name"], {}).get("verdict") or r.get("verdict", "")
    t["cite"] = [c for c in r.get("cite", []) if str(c).isdigit()]
    tags = []
    lic = licenses.get(t["name"])
    if (lic and lic not in ("none", "NOASSERTION")) or t["name"] in KNOWN_OSS: tags.append("Open source")
    if (t.get("gh_created") or "") >= "2026" or t["name"] in overrides.get("_new_in_2026", []): tags.append("New in 2026")
    tr = trend.get(t["name"], {})
    if tr.get("l", 0) >= 8 and tr["late"] >= 2 * max(tr["early"], 0.1) and "New in 2026" not in tags: tags.append("Rising")
    if tr.get("e", 0) >= 8 and tr["late"] <= 0.5 * tr["early"]: tags.append("Fading")
    t["tags"] = tags

def tool_row(rank, t):
    s = t["sig"]
    ask_total = t["ask_authors_recent"] + t["ask_authors_old"]
    facts = []
    if ask_total: facts.append(f'<span title="Distinct people naming it in 24 Ask HN threads about AI tooling"><b>{ask_total}</b> HN devs</span>')
    if s["comments"] >= 20: facts.append(f'<span title="HN comments mentioning it in the last 12 months"><b>{fmt(s["comments"])}</b> comments/yr</span>')
    if t.get("gh_stars"): facts.append(f'<span title="GitHub stars"><b>{fmt(t["gh_stars"])}</b> stars</span>')
    if s["downloads"] >= 1000: facts.append(f'<span title="npm + PyPI downloads, last month"><b>{fmt(s["downloads"])}</b> downloads/mo</span>')
    story = t.get("hn_top_story")
    if story and (story["points"] or 0) >= 100 and t["name"] not in overrides.get("_hide_story", []):
        facts.append(f'<a class="story" href="{hn_item(story["id"])}" title="Biggest HN thread about it: {E(story["title"])}"><span class="hn" aria-hidden="true">Y</span>{fmt(story["points"])}-point thread</a>')
    if t["cite"]:
        facts.append(f'<a class="cite" href="{hn_item(t["cite"][0])}">what people said ↗</a>')
    tags = "".join(f'<span class="tag tag-{slugify(x)}">{E(x)}</span>' for x in t["tags"])
    what = f'<b>{E(t["what"].rstrip("."))}.</b> ' if t["what"] else ""
    return f'''<li class="tool" id="{slugify(t["name"])}">
  <span class="rank">{rank:02d}</span>
  <div class="body">
    <h3><a href="{E(t["url"] or "#")}" rel="noopener">{E(t["name"])}</a>{tags}</h3>
    <p>{what}{E(t["verdict"])}</p>
    <div class="facts">{"".join(facts)}</div>
  </div>
  <div class="score"><span class="score-n" aria-label="Score {t["final"]:.0f} out of 100">{t["final"]:.0f}</span><span class="score-bar" aria-hidden="true"><i style="width:{max(3, min(100, t["final"])):.0f}%"></i></span></div>
</li>'''

def ranked(cat):
    ts = [t for t in scored if t["cat"] == cat and t["name"] not in overrides.get("_exclude", [])]
    return sorted(ts, key=lambda t: -t["final"])

def category_section(i, cat, title, dek):
    ts = ranked(cat)
    top, rest = ts[:10], ts[10:]
    rows = "\n".join(tool_row(r, t) for r, t in enumerate(top, 1))
    also = ('<p class="also"><span>Also scored</span> ' + ", ".join(f'<a href="{E(t["url"] or "#")}">{E(t["name"])}</a>' for t in rest) + "</p>") if rest else ""
    note = f'<p class="note">{CATEGORY_NOTES[cat]}</p>' if cat in CATEGORY_NOTES else ""
    return f'''<section class="cat" id="{cat}" aria-labelledby="h-{cat}">
  <header class="cat-head">
    <span></span>
    <div><span class="cat-num">{i:02d} / {len(CATEGORIES)}</span><h2 id="h-{cat}">{E(title)}</h2><p class="dek">{E(dek)}</p>{note}</div>
  </header>
  <ol class="tools">
{rows}
  </ol>
  {also}
</section>'''

def harness_chart():
    rows, total = harness["rows"], harness["authors"]
    mx = max(r["authors"] for r in rows)
    items = "".join(
        f'<li title="{r["authors"]} of {total} people"{' class="muted"' if r["name"].startswith("Their own") else ""}><span class="hc-name">{E(r["name"])}</span>'
        f'<span class="hc-track" aria-hidden="true"><i style="width:{100 * r["authors"] / mx:.1f}%"></i></span>'
        f'<span class="hc-val">{100 * r["authors"] / total:.0f}%</span><span class="sr-only"> ({r["authors"]} of {total} people)</span></li>'
        for r in rows)
    return f'''<figure class="harness" aria-labelledby="harness-cap">
  <figcaption id="harness-cap"><b>Who gets named for the harness seat.</b> Share of the {total} people answering
  <a href="{hn_item(harness["thread"])}">“Ask HN: What’s your current AI agentic setup?”</a> (November 2026) who mention each tool. Most name more than one.</figcaption>
  <ol class="hc">{items}</ol>
</figure>'''

toc = '<nav class="toc" aria-label="Categories"><ol>' + "".join(
    f'<li><a href="#{c}"><span>{i:02d}</span>{E(t)}</a></li>' for i, (c, t, _) in enumerate(CATEGORIES, 1)) + "</ol></nav>"
src = lambda rows: "".join(f'<li><b>{E(a)}</b><span class="mono">{E(b)}</span><small>{E(c)}</small></li>' for a, b, c in rows)

page = (open("template.html").read()
        .replace("{{STATS}}", "".join(f"<div><dt>{E(k)}</dt><dd>{E(v)}</dd></div>" for k, v in meta["stats"]))
        .replace("{{FINDINGS}}", "".join(f"<li><h3>{E(h)}</h3><p>{E(b)}</p></li>" for h, b in FINDINGS))
        .replace("{{HARNESS}}", harness_chart())
        .replace("{{TOC}}", toc)
        .replace("{{SECTIONS}}", "\n".join(category_section(i, c, t, d) for i, (c, t, d) in enumerate(CATEGORIES, 1)))
        .replace("{{SOURCES}}", src(SOURCES))
        .replace("{{PROPOSED}}", src(PROPOSED))
        .replace("{{WEIGHTS}}", "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td></tr>" for a, b in WEIGHTS))
        .replace("{{CAVEATS}}", CAVEATS)
        .replace("{{UPDATED}}", meta["updated"]))
assert "{{" not in page, re.findall(r"\{\{\w+\}\}", page)
open(f"{OUT}/index.html", "w").write(page)

export = {"edition": meta["updated"], "method": "https://alexissantos.dev/ai-dev-tools#method", "categories": []}
for c, title, dek in CATEGORIES:
    export["categories"].append({"id": c, "title": title, "tools": [{
        "rank": i, "name": t["name"], "url": t["url"], "score": t["final"], "what": t["what"], "verdict": t["verdict"], "tags": t["tags"],
        "signals": {"hn_devs": t["ask_authors_recent"] + t["ask_authors_old"], "hn_comments_12m": t["sig"]["comments"],
                    "hn_title_points": t["sig"]["titles"], "lobsters": t["lobsters_count"], "devto_posts": t["devto_count"],
                    "github_stars": t.get("gh_stars"), "downloads_month": t["sig"]["downloads"] or None, "tone": t["tone"]},
    } for i, t in enumerate(ranked(c), 1)]})
json.dump(export, open(f"{OUT}/tools.json", "w"), indent=1)
print("wrote", f"{OUT}/index.html", len(page) // 1024, "KB;", sum(len(c["tools"]) for c in export["categories"]), "tools")
