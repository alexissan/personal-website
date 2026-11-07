"""Discover AI developer tools on Hacker News via the public Algolia API.
Pulls high-signal stories (Show HN + launches + discussions) since 2025-01-01."""
import json, time, urllib.parse, urllib.request, sys
UA = {"User-Agent": "alexissantos.dev ai-dev-tools research (static analysis script)"}
SINCE = int(time.mktime((2025, 1, 1, 0, 0, 0, 0, 0, 0)))
QUERIES = ["coding agent","AI agent","Claude Code","Codex","Cursor","LLM","MCP","Model Context Protocol",
 "agentic","copilot","AI code review","local LLM","inference","evals","LLM observability","sandbox agents",
 "browser agent","agent framework","prompt","vibe coding","AI IDE","terminal agent","open source agent",
 "worktree","subagents","context engineering","RAG","embeddings","llama.cpp","Ollama","AI SDK","Gemini CLI",
 "agent harness","AI pair programming","code generation","autonomous coding","spec driven","AI testing","Show HN AI"]
def get(url):
    for i in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + i * 2)
    return {"hits": []}
stories = {}
for q in QUERIES:
    for tags in ["show_hn", "story"]:
        for page in range(3):
            p = urllib.parse.urlencode({"query": q, "tags": tags, "hitsPerPage": 100, "page": page,
                "numericFilters": f"created_at_i>{SINCE},points>{40 if tags=='show_hn' else 150}"})
            d = get("https://hn.algolia.com/api/v1/search?" + p)
            for h in d.get("hits", []):
                stories[h["objectID"]] = {k: h.get(k) for k in ("objectID","title","url","points","num_comments","created_at","author")}
                stories[h["objectID"]]["show_hn"] = tags == "show_hn" or (h.get("title") or "").startswith("Show HN")
            if page + 1 >= d.get("nbPages", 0): break
    print(q, len(stories), file=sys.stderr)
json.dump(sorted(stories.values(), key=lambda s: -s["points"]), open("raw/hn_stories.json", "w"), indent=1)
print(len(stories))
