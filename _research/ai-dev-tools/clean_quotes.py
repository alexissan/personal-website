"""Remove the Nov 2026 Ask HN questionnaire text that commenters paste back into their answers,
so tool names suggested by the question itself don't count as mentions."""
import json, re
QUOTED = [
    r"\(?Claude,\s*ChatGPT/Codex,\s*Cursor,?\s*etc\.?\)?",
    r"pay-as-you-go APIs,?\s*OpenRouter,?\s*or locally hosted models\.?",
    r"Are you sticking with the default CLIs or IDE integrations,?\s*or using alternatives like OpenCode,?\s*Pi,?\s*Aider,?\s*Muse Code,?\s*or custom-built harnesses\??",
    r"alternatives like OpenCode,?\s*Pi,?\s*Aider,?\s*Muse Code,?\s*or custom-built harnesses\??",
    r"For example,?\s*Munder Difflin,?\s*Gas Town,?\s*Ruflo,?\s*or something custom\.?",
    r"Munder Difflin,?\s*Gas Town,?\s*Ruflo",
    r"broader agent platforms like OpenClaw\s*/\s*Hermes Agent\s*/\s*Grok bot\s*/\s*Dots\s*/\s*Muse\??",
    r"OpenClaw\s*/\s*Hermes Agent\s*/\s*Grok bot\s*/\s*Dots\s*/\s*Muse",
]
QRX = [re.compile(q, re.I) for q in QUOTED]
d = json.load(open("raw/hn_ask_comments.json"))
n = 0
for c in d["comments"]:
    t = re.sub(r"\s+", " ", c["text"])
    for q in QRX:
        t, k = q.subn(" [question] ", t); n += k
    c["text"] = t
json.dump(d, open("raw/hn_ask_comments_clean.json", "w"))
print("stripped", n, "quoted fragments")
