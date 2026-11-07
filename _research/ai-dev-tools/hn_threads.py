"""Download every comment from the Ask HN threads where developers describe their AI tooling."""
import json, html, re, urllib.request
UA={"User-Agent":"alexissantos.dev ai-dev-tools research"}
THREADS = {
 50366117:"What's your current AI agentic setup? (Nov 2026)", 48413629:"What is your (AI) dev tech stack / workflow? (Jun 2026)",
 47388646:"How is AI-assisted coding going for you professionally?", 46255285:"How can I get better at using AI for programming?",
 46691243:"Do you have any evidence that agentic coding works?", 43959710:"Cursor or Windsurf?",
 45771870:"Who uses open LLMs and coding assistants locally?", 48771515:"Different ways of using LLMs for coding?",
 49548600:"Who is using MCP in production?", 46616529:"How are you doing RAG locally?", 49672966:"What default model do you use and why?",
 46620990:"How do you safely give LLMs SSH/DB access?", 46710108:"How are you automating your coding work?",
 44373724:"What useful AI tools do you use every day?", 44405067:"What are you using LLMs for in production?",
 46292682:"How are you LLM-coding in an established code base?", 48449187:"Tools you have made for yourself since AI?",
 48492118:"Flow state when using AI to code?", 48859439:"How do you use Vim in the era of AI?",
 43922759:"AI IDEs vs copy pasting into chat apps?", 44095189:"Anyone struggling to get value out of coding LLMs?",
 46838946:"Any real OpenClaw users?", 50151036:"Shipping AI-written code you don't understand?", 45195543:"My workflow is 70% AI...",
}
def walk(node, out, tid):
    for c in node.get("children") or []:
        if c.get("text") and c.get("author"):
            t = re.sub(r"<[^>]+>", " ", html.unescape(c["text"].replace("<p>", "\n")))
            out.append({"id": c.get("id"), "thread": tid, "author": c["author"], "created_at": c.get("created_at"), "text": t})
        walk(c, out, tid)
out = []
for tid, title in THREADS.items():
    with urllib.request.urlopen(urllib.request.Request(f"https://hn.algolia.com/api/v1/items/{tid}", headers=UA), timeout=60) as r:
        n0 = len(out); walk(json.load(r), out, tid); print(tid, len(out) - n0, title)
json.dump({"threads": THREADS, "comments": out}, open("raw/hn_ask_comments.json", "w"))
print("total", len(out))
