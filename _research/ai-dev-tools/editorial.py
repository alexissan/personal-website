"""Human-written copy for the page. Numbers here come from raw/harness_share.json and raw/trend.json."""

FINDINGS = [
    ("Three harnesses won the terminal.",
     "In the November 2026 “what’s your setup” thread, 26% of the 538 people answering name Claude Code, 24% Codex and 17% OpenCode. "
     "Codex roughly tripled its share of commenters since 2025. Most people run two of them and switch by subscription."),
    ("One in nine built their own.",
     "58 of those 538 describe a harness, agent loop or orchestrator they wrote themselves, more than name Pi, Cursor or Copilot. "
     "The harness is becoming what dotfiles were: personal, forked, and shared as a gist."),
    ("The IDE is no longer the centre.",
     "Cursor went from 8.7% of commenters in 2025 threads to 2.2% in the second half of 2026. Windsurf, Continue and Roo Code all but disappear. "
     "Zed is the one editor whose share went up."),
    ("The most popular orchestrator is tmux.",
     "94 people in recent threads describe tmux panes plus git worktrees. Of the dedicated tools, Herdr is the breakout, from zero mentions to 41 in a few months."),
    ("Cheap plans plus open harnesses is a real lane now.",
     "OpenRouter went from 0.4% to 3.3% of commenters, and 32 people mention OpenCode Go. The pattern: DeepSeek, GLM or Qwen through a $10 plan, driven by OpenCode or Pi."),
    ("GitHub stars stopped meaning much.",
     "Several 2026 repos sit at 80k to 440k stars with almost no discussion anywhere. cc-switch has 152k stars and three HN comments in a year. "
     "So stars count for little here: what people say they use counts for most."),
]

CATEGORY_NOTES = {
    "orchestration": "“tmux + git worktrees” isn’t a product, but it’s what most people actually describe, so it stays in the ranking.",
    "frameworks": "The weakest HN signal of any category: people mostly talk about agents they use, not ones they build. Downloads carry more weight here.",
    "evals": "Thin on HN too. Treat this list as a shortlist to try, not a verdict.",
    "review": "Most review here happens inside the harness (a second model reviewing the first). Dedicated review bots get surprisingly few mentions.",
}

# Licences that NOASSERTION hides but are open source at the core.
KNOWN_OSS = {"Zed", "bubblewrap", "LiteLLM", "Langfuse", "Mastra", "Vercel AI SDK"}

SOURCES = [
    ("Hacker News: Ask HN threads", "6,323 comments",
     "24 threads where developers describe their AI setups, May 2025 to Nov 2026. The core signal: distinct people naming a tool."),
    ("Hacker News: stories and comments", "3,229 stories",
     "Front-page pull since Jan 2025, plus each tool’s comment volume over the last 12 months via the Algolia API, typo tolerance off, checked against a 100-comment sample."),
    ("Lobsters", "2,979 stories",
     "Story titles from the ai, vibecoding, programming, devops, release and show tags since Jan 2025."),
    ("dev.to", "42,357 posts",
     "Top posts of the last year across 12 tags. Practitioner blogging, title mentions weighted by reactions."),
    ("GitHub", "120 repos",
     "Stars, last push and licence for every tool with a public repo."),
    ("npm and PyPI", "monthly downloads",
     "Last-month downloads from the npm registry and pypistats."),
]

PROPOSED = [
    ("Reddit", "not scraped",
     "r/LocalLLaMA, r/ClaudeAI and r/ChatGPTCoding are where local-model and harness talk is densest. Reddit blocks anonymous scripts, so this needs a registered OAuth app. First thing I’d add."),
    ("OpenRouter rankings", "usage, not opinion",
     "A public leaderboard of tokens routed per app. The closest thing to real usage share for open-model harnesses."),
    ("VS Code Marketplace and Open VSX", "install counts",
     "Hard numbers for editor extensions (Cline, Roo, Kilo, Continue), which HN underweights."),
    ("Bluesky and X", "builder chatter",
     "Bluesky’s firehose is open and easy to sample. X has the launches but its API is paid."),
    ("Discord servers", "needs consent",
     "Where support questions and complaints actually happen. Private by default: only with a bot the server admins approve."),
    ("Newsletters and podcasts", "editorial cross-check",
     "Simon Willison, Latent Space, The Pragmatic Engineer, Interconnects. Low volume, high signal, good for catching what HN misses."),
    ("Stack Overflow Developer Survey", "yearly",
     "Huge sample, slow cadence. Best for the enterprise defaults this page underrates."),
]

CAVEATS = """
<p>Hacker News skews senior, terminal-first and sceptical. Enterprise defaults like Copilot and JetBrains are underrepresented, and tools popular in China or on Reddit get less credit than they deserve.</p>
<p>Names collide: Pi, Cursor, Muse, Phoenix. Every tool has a context-aware pattern, every comment count was checked against a sample, and comments that turned out to be about something else are discounted. The November thread’s questionnaire named several tools, so quoted question text was stripped before counting.</p>
<p>Each tool’s HN comments were also read for tone, which moves its score by up to six points. A tool HN uses but complains about still ranks, with the complaint in its write-up.</p>
<p>This is a snapshot from 7 November 2026. A third of these tools didn’t exist a year ago.</p>
"""

WEIGHTS = [
    ("HN devs naming it in Ask HN threads", "40"),
    ("HN comment volume, last 12 months", "20"),
    ("Adoption: GitHub stars or package downloads", "16"),
    ("HN front-page points on stories about it", "12"),
    ("Lobsters stories", "7"),
    ("dev.to reactions", "5"),
    ("Tone of HN comments", "±6"),
]
