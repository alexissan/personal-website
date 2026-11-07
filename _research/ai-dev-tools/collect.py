"""Collect per-tool signals from public sources. Cached in raw/ so reruns are cheap.

Sources
  HN Ask threads  distinct commenters who mention the tool (raw/hn_ask_comments.json)
  HN titles       stories since 2025-01 whose title mentions the tool (Algolia)
  HN comments     comment volume over the last 12 months, precision-checked by regex (Algolia)
  Lobsters        story titles in ai / vibecoding tags since 2025-01
  dev.to          top articles of the last year, title mentions
  GitHub          stars + last push (gh api)
  npm / PyPI      last-month downloads
"""
import json, os, re, subprocess, sys, time, urllib.parse, urllib.request
from registry import T

UA = {"User-Agent": "alexissantos.dev ai-dev-tools research (static analysis script)"}
SINCE_2025 = int(time.mktime((2025, 1, 1, 0, 0, 0, 0, 0, 0)))
LAST_12M = int(time.time()) - 365 * 86400
os.makedirs("raw/cache", exist_ok=True)

def get(url, cache=None):
    path = f"raw/cache/{cache}.json" if cache else None
    if path and os.path.exists(path):
        return json.load(open(path))
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                d = json.load(r)
            if path: json.dump(d, open(path, "w"))
            return d
        except urllib.error.HTTPError as e:
            if e.code == 404: return None
            time.sleep(3 * (i + 1))
        except Exception:
            time.sleep(3 * (i + 1))
    return None

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def rx_of(t): return re.compile(t["rx"], 0 if t["cs"] else re.I)

# ---------- corpora loaded once ----------
ask = json.load(open("raw/hn_ask_comments_clean.json"))
RECENT_THREADS = {50366117, 48413629, 48771515, 49548600, 49672966, 48449187, 48492118, 48859439, 50151036}

def lobsters_corpus():
    path = "raw/lobsters.json"
    if os.path.exists(path): return json.load(open(path))
    out = {}
    for tag in ["ai", "vibecoding", "programming", "devops", "release", "show"]:
        for page in range(1, 120):
            d = get(f"https://lobste.rs/t/{tag}/page/{page}.json")
            if not d: break
            for s in d:
                out[s["short_id"]] = {k: s.get(k) for k in ("title", "url", "score", "comment_count", "created_at", "tags")}
            if d[-1]["created_at"] < "2025-01-01": break
            time.sleep(0.6)
        print("lobsters", tag, len(out), file=sys.stderr)
    out = [v for v in out.values() if v["created_at"] >= "2025-01-01"]
    json.dump(out, open(path, "w"))
    return out

def devto_corpus():
    path = "raw/devto.json"
    if os.path.exists(path): return json.load(open(path))
    out = {}
    for tag in ["ai", "llm", "claude", "mcp", "agents", "programming", "webdev", "productivity", "opensource", "devops", "python", "javascript"]:
        for page in range(1, 6):
            d = get(f"https://dev.to/api/articles?tag={tag}&top=365&per_page=1000&page={page}")
            if not d: break
            for a in d:
                out[a["id"]] = {"title": a["title"], "reactions": a.get("public_reactions_count", 0), "url": a["url"], "published_at": a["published_at"]}
            if len(d) < 1000: break
        print("devto", tag, len(out), file=sys.stderr)
    out = list(out.values())
    json.dump(out, open(path, "w"))
    return out

LOB = lobsters_corpus()
DEV = devto_corpus()

def gh_repo(full):
    path = f"raw/cache/gh-{slug(full)}.json"
    if os.path.exists(path): return json.load(open(path))
    r = subprocess.run(["gh", "api", f"repos/{full}", "--jq", "{full_name, stargazers_count, pushed_at, created_at, html_url, description, archived}"], capture_output=True, text=True)
    d = json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None
    json.dump(d, open(path, "w"))
    return d

results = []
for t in T:
    rx = rx_of(t)
    s = {"name": t["name"], "cat": t["cat"]}

    # 1. Ask HN: distinct authors, recency-weighted, keep evidence ids
    authors_recent, authors_old, evidence = set(), set(), []
    for c in ask["comments"]:
        m = rx.search(c["text"])
        if not m: continue
        (authors_recent if c["thread"] in RECENT_THREADS else authors_old).add(c["author"])
        a, b = max(0, m.start() - 220), min(len(c["text"]), m.end() + 260)
        evidence.append({"id": c.get("id"), "thread": c["thread"], "author": c["author"], "snippet": c["text"][a:b].replace("\n", " ")})
    s["ask_authors_recent"] = len(authors_recent)
    s["ask_authors_old"] = len(authors_old - authors_recent)
    s["evidence"] = evidence[:40]

    q = t["q"]
    s["hn_title_points"] = s["hn_title_count"] = s["hn_comments_12m"] = 0
    s["hn_top_story"] = None
    if q:
        # 2. titles
        p = urllib.parse.urlencode({"query": q, "restrictSearchableAttributes": "title", "tags": "story", "hitsPerPage": 200, "typoTolerance": "false", "numericFilters": f"created_at_i>{SINCE_2025}"})
        d = get("https://hn.algolia.com/api/v1/search?" + p, cache=f"title-nt-{slug(q)}") or {"hits": []}
        hits = [h for h in d["hits"] if rx.search(h.get("title") or "")]
        s["hn_title_points"] = sum(h["points"] or 0 for h in hits)
        s["hn_title_count"] = len(hits)
        if hits:
            top = max(hits, key=lambda h: h["points"] or 0)
            s["hn_top_story"] = {"title": top["title"], "points": top["points"], "id": top["objectID"], "url": top.get("url")}
        # 3. comment volume, precision-checked
        p = urllib.parse.urlencode({"query": q, "tags": "comment", "hitsPerPage": 100, "typoTolerance": "false", "numericFilters": f"created_at_i>{LAST_12M}"})
        d = get("https://hn.algolia.com/api/v1/search?" + p, cache=f"comments-nt-{slug(q)}") or {"hits": [], "nbHits": 0}
        sample = d["hits"]
        prec = (sum(1 for h in sample if rx.search(re.sub("<[^>]+>", " ", h.get("comment_text") or ""))) / len(sample)) if sample else 0
        s["hn_comments_12m"] = round(d.get("nbHits", 0) * prec)
        s["hn_comment_precision"] = round(prec, 2)
        time.sleep(0.25)

    # 4. Lobsters / 5. dev.to
    lob = [x for x in LOB if rx.search(x["title"] or "")]
    s["lobsters_count"], s["lobsters_score"] = len(lob), sum(x["score"] for x in lob)
    dev = [x for x in DEV if rx.search(x["title"] or "")]
    s["devto_count"], s["devto_reactions"] = len(dev), sum(x["reactions"] for x in dev)

    # 6. GitHub
    if t["gh"]:
        g = gh_repo(t["gh"])
        if g:
            s["gh_stars"], s["gh_pushed"], s["gh_created"], s["gh_url"] = g["stargazers_count"], g["pushed_at"], g["created_at"], g["html_url"]
            s["gh_archived"] = g.get("archived")
    # 7. downloads
    if t["npm"]:
        d = get(f"https://api.npmjs.org/downloads/point/last-month/{t['npm']}", cache=f"npm-{slug(t['npm'])}")
        s["npm_month"] = (d or {}).get("downloads")
    if t["pypi"]:
        d = get(f"https://pypistats.org/api/packages/{t['pypi']}/recent", cache=f"pypi-{slug(t['pypi'])}")
        s["pypi_month"] = ((d or {}).get("data") or {}).get("last_month")
        time.sleep(1.2)  # pypistats is rate-limited
    s.update({k: t[k] for k in ("url", "gh", "npm", "pypi", "aka")})
    results.append(s)
    print(f"{t['cat']:13s} {t['name']:32s} ask={s['ask_authors_recent']:3d}/{s['ask_authors_old']:3d} titles={s['hn_title_count']:3d}/{s['hn_title_points']:6d} cm12={s['hn_comments_12m']:5d}(p{s.get('hn_comment_precision',0)}) lob={s['lobsters_count']:2d} dev={s['devto_count']:3d} gh={s.get('gh_stars','-')} npm={s.get('npm_month','-')} pypi={s.get('pypi_month','-')}", file=sys.stderr)

json.dump(results, open("raw/signals.json", "w"), indent=1)
