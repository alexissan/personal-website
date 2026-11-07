"""Candidate registry for the AI dev tools field guide.

Every candidate came from at least one of: HN Ask threads, HN Show HN / story titles,
GitHub topic search, Lobsters. `rx` is matched (case-insensitive unless cs=True) against
HN comment text; `q` is the Algolia query used for title + comment volume (None = name is
too generic for a reliable search, so only the regex-matched Ask HN corpus counts).
"""

CATEGORIES = [
    ("terminal", "Terminal agents", "The harness is the product. CLI agents that read, edit, run and loop until the job is done."),
    ("editors", "Editors & IDEs", "Where you still look at the code. Editors with agents built in rather than bolted on."),
    ("orchestration", "Running many agents", "Worktrees, multiplexers and boards for when one agent at a time stops being enough."),
    ("review", "Code review & PR agents", "The second pair of eyes. Agents that read diffs and catch what the first agent missed."),
    ("context", "Context, MCP & skills", "What the agent knows. Docs, code search, memory and the skills that steer it."),
    ("browser", "Browser & web for agents", "Letting agents see and drive the web: debugging, testing, scraping."),
    ("sandbox", "Sandboxes & safety", "Blast-radius control. Run agents in YOLO mode without betting your laptop or prod DB."),
    ("local", "Local models & inference", "Run open weights on your own hardware. Private, offline, and cheaper than you think."),
    ("gateways", "Model access & routing", "One key, every model. Gateways and plans that make switching models cheap."),
    ("frameworks", "Build your own agent", "SDKs and frameworks for shipping agents inside your product."),
    ("evals", "Evals & observability", "Traces, evals and regression tests. How you know the agent got better, not just different."),
    ("assistants", "Always-on agents", "Personal agents that live on a server or a Mac mini and work while you sleep."),
]

T = []
def tool(cat, name, rx, q=None, url=None, gh=None, npm=None, pypi=None, cs=False, aka=None):
    T.append(dict(cat=cat, name=name, rx=rx, q=q if q is not None else name, url=url, gh=gh, npm=npm, pypi=pypi, cs=cs, aka=aka))

# --- Terminal agents -------------------------------------------------------
tool("terminal", "Claude Code", r"claude[ -]?code|\bCC\b", url="https://code.claude.com", gh="anthropics/claude-code", npm="@anthropic-ai/claude-code")
tool("terminal", "Codex CLI", r"\bcodex\b", q="Codex", url="https://developers.openai.com/codex", gh="openai/codex", npm="@openai/codex")
tool("terminal", "OpenCode", r"\bopen ?code\b", url="https://opencode.ai", gh="sst/opencode", npm="opencode-ai")
tool("terminal", "Pi", r"\bpi\b(?=[^.\n]{0,60}(agent|harness|coding|cli|mono|zechner|omp|\bdev\b))|pi\.dev|\bomp\b|oh-my-pi|(?<=\buse )pi\b|(?<=and )pi\b(?= (for|with|as))", q="pi.dev", url="https://pi.dev", gh="earendil-works/pi", npm="@mariozechner/pi-coding-agent", cs=False)
tool("terminal", "Gemini CLI", r"gemini[ -]cli|antigravity cli", q="Gemini CLI", url="https://github.com/google-gemini/gemini-cli", gh="google-gemini/gemini-cli", npm="@google/gemini-cli")
tool("terminal", "Aider", r"\baider\b", url="https://aider.chat", gh="Aider-AI/aider", pypi="aider-chat")
tool("terminal", "Amp", r"\bamp\b(?=[^.\n]{0,40}(code|agent|cli|sourcegraph))|ampcode|sourcegraph amp", cs=False, q="ampcode", url="https://ampcode.com")
tool("terminal", "Goose", r"\bgoose\b", q="goose agent", url="https://block.github.io/goose", gh="block/goose")
tool("terminal", "Qwen Code", r"qwen[ -]code", url="https://github.com/QwenLM/qwen-code", gh="QwenLM/qwen-code", npm="@qwen-code/qwen-code")
tool("terminal", "DeepSeek Harness", r"deepseek[ -]?harness|\bDSH\b", url="https://deepseek.com/harness/en/", gh="deepseek-ai/deepseek-harness")
tool("terminal", "Crush", r"\bcrush\b(?=[^.\n]{0,40}(charm|agent|cli|terminal))|charm(bracelet)?'?s? crush", q="charmbracelet crush", url="https://github.com/charmbracelet/crush", gh="charmbracelet/crush")
tool("terminal", "Droid", r"\bdroid\b|factory\.ai", q="Factory Droid", url="https://factory.ai")
tool("terminal", "Copilot CLI", r"copilot[ -]cli", url="https://github.com/features/copilot/cli", gh="github/copilot-cli", npm="@github/copilot")
tool("terminal", "Kimi CLI", r"kimi[ -]cli|kimi code", url="https://github.com/MoonshotAI/kimi-cli", gh="MoonshotAI/kimi-cli")
tool("terminal", "Muse Code", r"muse (code|cli)", url="https://ai.meta.com/muse/")
tool("terminal", "Zerostack", r"zerostack", url="https://github.com/gi-dellav/zerostack", gh="gi-dellav/zerostack")
tool("terminal", "Codewhale", r"codewhale", url="https://github.com/codewhale-hq/Codewhale", gh="codewhale-hq/Codewhale")
tool("terminal", "Mistral Vibe", r"mistral vibe|vibe cli", url="https://mistral.ai/news/devstral-2-vibe-cli", gh="mistralai/mistral-vibe")
tool("terminal", "Kiro CLI", r"kiro[ -]cli", url="https://kiro.dev/cli/")
tool("terminal", "Plandex", r"plandex", url="https://plandex.ai", gh="plandex-ai/plandex")
tool("terminal", "jcode", r"\bjcode\b", url="https://github.com/1jehuang/jcode", gh="1jehuang/jcode")
tool("terminal", "Open Interpreter", r"open[ -]interpreter", url="https://github.com/openinterpreter/openinterpreter", gh="openinterpreter/openinterpreter")

# --- Editors & IDEs ---------------------------------------------------------
tool("editors", "Cursor", r"\bcursor\b(?! (position|key|movement|blink))", q="Cursor", url="https://cursor.com")
tool("editors", "Zed", r"\bzed\b", url="https://zed.dev", gh="zed-industries/zed")
tool("editors", "VS Code + Copilot", r"github copilot|\bcopilot\b(?![ -]cli)", q="GitHub Copilot", url="https://code.visualstudio.com/docs/copilot/overview", aka="VS Code agent mode")
tool("editors", "Windsurf", r"windsurf", url="https://windsurf.com")
tool("editors", "Antigravity", r"antigravity(?! cli)", url="https://antigravity.google")
tool("editors", "JetBrains Junie", r"\bjunie\b|jetbrains ai", q="JetBrains Junie", url="https://www.jetbrains.com/junie/")
tool("editors", "Kiro", r"\bkiro\b(?![ -]cli)", url="https://kiro.dev")
tool("editors", "Neovim (CodeCompanion / avante)", r"codecompanion|avante|neovim", q="codecompanion", url="https://github.com/olimorris/codecompanion.nvim", gh="olimorris/codecompanion.nvim")
tool("editors", "Emacs gptel", r"gptel", url="https://github.com/karthink/gptel", gh="karthink/gptel")
tool("editors", "Cline", r"\bcline\b", url="https://cline.bot", gh="cline/cline")
tool("editors", "Roo Code", r"roo ?code|\broo\b", q="Roo Code", url="https://roocode.com", gh="RooCodeInc/Roo-Code")
tool("editors", "Kilo Code", r"kilo ?code", url="https://kilocode.ai", gh="Kilo-Org/kilocode")
tool("editors", "Continue", r"continue\.dev|continuedev", q="continue.dev", url="https://continue.dev", gh="continuedev/continue")
tool("editors", "Whiteboard", r"whiteboard(?=[^.\n]{0,30}(ide|yc))", q="Whiteboard IDE", url="https://github.com/devdotfast/whiteboard", gh="devdotfast/whiteboard")
tool("editors", "Void", r"void (editor|ide)", url="https://voideditor.com", gh="voideditor/void")

# --- Orchestration ----------------------------------------------------------
tool("orchestration", "Herdr", r"herdr", url="https://herdr.dev", gh="ogulcancelik/herdr")
tool("orchestration", "Conductor", r"conductor", q="conductor.build", url="https://conductor.build")
tool("orchestration", "Paseo", r"paseo", url="https://github.com/getpaseo/paseo", gh="getpaseo/paseo")
tool("orchestration", "T3 Code", r"t3[ .]?code", url="https://t3.codes", gh="pingdotgg/t3code")
tool("orchestration", "Orca", r"\borca\b", q="stablyai orca", url="https://github.com/stablyai/orca", gh="stablyai/orca")
tool("orchestration", "Claude Squad", r"claude[ -]squad", url="https://github.com/smtg-ai/claude-squad", gh="smtg-ai/claude-squad")
tool("orchestration", "Vibe Kanban", r"vibe[ -]?kanban", url="https://www.vibekanban.com", gh="BloopAI/vibe-kanban", npm="vibe-kanban")
tool("orchestration", "workmux", r"workmux", url="https://github.com/raine/workmux", gh="raine/workmux")
tool("orchestration", "tmux + git worktrees", r"\btmux\b|worktree", q=None, url="https://git-scm.com/docs/git-worktree")
tool("orchestration", "Omnara", r"omnara", url="https://github.com/omnara-ai/omnara", gh="omnara-ai/omnara")
tool("orchestration", "Superset", r"superset\.sh|superset(?=[^.\n]{0,30}(agent|terminal|worktree))", q="superset.sh", url="https://superset.sh", gh="superset-sh/superset")
tool("orchestration", "Sculptor", r"sculptor", url="https://imbue.com/sculptor/")
tool("orchestration", "Juggler", r"juggler", url="https://github.com/juggler-ai/juggler", gh="juggler-ai/juggler")
tool("orchestration", "qm", r"\bqm\b(?=[^.\n]{0,40}(harness|agent|yc))|yc-software/qm", q="qm harness", url="https://github.com/yc-software/qm", gh="yc-software/qm")
tool("orchestration", "AX (Agent Executor)", r"agentexecutor|\bAX\b(?=[^.\n]{0,40}(orchestrat|google))", q="agentexecutor", url="https://agentexecutor.io", cs=True)
tool("orchestration", "oh-my-claudecode", r"oh[ -]my[ -]claude ?code", url="https://github.com/Yeachan-Heo/oh-my-claudecode", gh="Yeachan-Heo/oh-my-claudecode")
tool("orchestration", "Crystal", r"crystal(?=[^.\n]{0,30}(worktree|claude|agent))", q="stravu crystal", url="https://github.com/stravu/crystal", gh="stravu/crystal")
tool("orchestration", "Ralph loop", r"\bralph\b(?=[^.\n]{0,30}(loop|wiggum|technique))|ralph wiggum", q="Ralph Wiggum loop", url="https://ghuntley.com/ralph/")
tool("orchestration", "Gas Town", r"gas ?town", url="https://github.com/gastownhall/gastown", gh="gastownhall/gastown")
tool("orchestration", "Munder Difflin", r"munder ?difflin", url="https://munderdiffl.in")
tool("orchestration", "Ruflo", r"ruflo|claude[ -]flow", url="https://github.com/ruvnet/ruflo", gh="ruvnet/ruflo")
tool("orchestration", "Beads",r"\bbeads\b", url="https://github.com/steveyegge/beads", gh="steveyegge/beads")

# --- Code review ------------------------------------------------------------
tool("review", "CodeRabbit", r"code ?rabbit", url="https://coderabbit.ai")
tool("review", "Greptile", r"greptile", url="https://greptile.com")
tool("review", "Copilot code review", r"copilot (code )?reviews?|copilot review", q="Copilot code review", url="https://docs.github.com/en/copilot/concepts/agents/code-review")
tool("review", "Cursor Bugbot", r"bugbot", url="https://cursor.com/bugbot")
tool("review", "Claude Code review", r"claude (code )?(github action|review)|/review|claude-code-action|code review (with|by|from) claude", q="Claude Code review", url="https://code.claude.com/docs/en/code-review", gh="anthropics/claude-code-action")
tool("review", "Codex code review", r"codex (code )?review|@codex review", q="Codex review", url="https://developers.openai.com/codex/integrations/github")
tool("review", "Graphite", r"graphite(?! diamond)|graphite\.dev|diamond", q="Graphite", url="https://graphite.com")
tool("review", "Qodo", r"\bqodo\b", url="https://www.qodo.ai", gh="qodo-ai/pr-agent")
tool("review", "Sourcery", r"sourcery", url="https://sourcery.ai")
tool("review", "Open Code Review (Alibaba)", r"open[ -]code[ -]review", url="https://github.com/alibaba/open-code-review", gh="alibaba/open-code-review")
tool("review", "Sphinx", r"\bsphinx\b(?=[^.\n]{0,40}(quiz|hook))", q="Sphinx quizzes", url="https://sphinx-six-theta.vercel.app/")
tool("review", "Codex Security", r"codex security|aardvark", url="https://openai.com/index/codex-security/")

# --- Context, MCP, skills ---------------------------------------------------
tool("context", "Context7", r"context7", url="https://context7.com", gh="upstash/context7", npm="@upstash/context7-mcp")
tool("context", "Agent Skills", r"\bskills?\b(?=[^.\n]{0,30}(md|file|claude|agent))|skill\.md|agentskills", q="Agent Skills", url="https://agentskills.io")
tool("context", "AGENTS.md", r"agents\.md|claude\.md", q="AGENTS.md", url="https://agents.md")
tool("context", "Superpowers", r"superpowers", url="https://github.com/obra/superpowers", gh="obra/superpowers")
tool("context", "Serena", r"\bserena\b", url="https://github.com/oraios/serena", gh="oraios/serena", pypi="serena-agent")
tool("context", "GitHub MCP server", r"github mcp", url="https://github.com/github/github-mcp-server", gh="github/github-mcp-server")
tool("context", "Spec Kit", r"spec[ -]kit", url="https://github.com/github/spec-kit", gh="github/spec-kit")
tool("context", "claude-mem", r"claude[ -]mem\b", url="https://github.com/thedotmack/claude-mem", gh="thedotmack/claude-mem")
tool("context", "rtk", r"\brtk\b", q="rtk token", url="https://github.com/rtk-ai/rtk", gh="rtk-ai/rtk")
tool("context", "context-mode", r"context[ -]mode", url="https://github.com/mksglu/context-mode", gh="mksglu/context-mode")
tool("context", "Semble", r"semble", url="https://github.com/MinishLab/semble", gh="MinishLab/semble")
tool("context", "Repomix", r"repomix", url="https://repomix.com", gh="yamadashy/repomix", npm="repomix")
tool("context", "codebase-memory-mcp", r"codebase[ -]memory", url="https://github.com/DeusData/codebase-memory-mcp", gh="DeusData/codebase-memory-mcp")
tool("context", "Graphify", r"graphify", url="https://github.com/Graphify-Labs/graphify", gh="Graphify-Labs/graphify")
tool("context", "Figma MCP", r"figma mcp|figma dev mode mcp", q="Figma MCP", url="https://www.figma.com/developers/mcp")
tool("context", "Sentry MCP", r"sentry mcp", url="https://docs.sentry.io/product/sentry-mcp/", gh="getsentry/sentry-mcp")
tool("context", "Linear MCP", r"linear mcp", url="https://linear.app/docs/mcp")
tool("context", "Impeccable", r"impeccable", url="https://github.com/pbakaus/impeccable", gh="pbakaus/impeccable")
tool("context", "headroom", r"headroom(?=[^.\n]{0,30}(token|compress|proxy))", q="headroom tokens", url="https://github.com/headroomlabs-ai/headroom", gh="headroomlabs-ai/headroom")

# --- Browser ----------------------------------------------------------------
tool("browser", "Playwright MCP", r"playwright", q="Playwright MCP", url="https://github.com/microsoft/playwright-mcp", gh="microsoft/playwright-mcp", npm="@playwright/mcp")
tool("browser", "Chrome DevTools MCP", r"(chrome )?devtools mcp|chrome-devtools-mcp", q="Chrome DevTools MCP", url="https://github.com/ChromeDevTools/chrome-devtools-mcp", gh="ChromeDevTools/chrome-devtools-mcp", npm="chrome-devtools-mcp")
tool("browser", "browser-use", r"browser[ -]use", url="https://browser-use.com", gh="browser-use/browser-use", pypi="browser-use")
tool("browser", "Stagehand", r"stagehand", url="https://www.stagehand.dev", gh="browserbase/stagehand", npm="@browserbasehq/stagehand")
tool("browser", "Browserbase", r"browserbase", url="https://www.browserbase.com")
tool("browser", "Vibium", r"vibium", url="https://github.com/VibiumDev/vibium", gh="VibiumDev/vibium")
tool("browser", "agent-browser", r"agent[ -]browser", url="https://github.com/vercel-labs/agent-browser", gh="vercel-labs/agent-browser", npm="agent-browser")
tool("browser", "Lightpanda", r"lightpanda", url="https://lightpanda.io", gh="lightpanda-io/browser")
tool("browser", "Firecrawl", r"firecrawl", url="https://firecrawl.dev", gh="firecrawl/firecrawl")
tool("browser", "Browser MCP", r"browser ?mcp", q="Browser MCP", url="https://browsermcp.io", gh="BrowserMCP/mcp")
tool("browser", "Claude in Chrome", r"claude (in|for) chrome", url="https://claude.com/chrome")
tool("browser", "Jina Reader", r"jina", q="Jina Reader", url="https://jina.ai/reader")
tool("browser", "Scrapling", r"scrapling", url="https://github.com/D4Vinci/Scrapling", gh="D4Vinci/Scrapling", pypi="scrapling")

# --- Sandbox ----------------------------------------------------------------
tool("sandbox", "Docker Sandboxes", r"docker sandbox", url="https://www.docker.com/products/docker-sandboxes/")
tool("sandbox", "Agent Safehouse", r"safehouse", url="https://agent-safehouse.dev")
tool("sandbox", "Dev containers", r"dev ?containers?|devcontainer", q="devcontainer agent", url="https://containers.dev")
tool("sandbox", "Apple container", r"apple container", url="https://github.com/apple/container", gh="apple/container")
tool("sandbox", "OpenShell", r"openshell", url="https://github.com/NVIDIA/OpenShell", gh="NVIDIA/OpenShell")
tool("sandbox", "container-use", r"container[ -]use", url="https://github.com/dagger/container-use", gh="dagger/container-use")
tool("sandbox", "E2B", r"\be2b\b", q="e2b sandbox", url="https://e2b.dev", gh="e2b-dev/E2B")
tool("sandbox", "Daytona", r"daytona", url="https://www.daytona.io", gh="daytonaio/daytona")
tool("sandbox", "Sprites (Fly.io)", r"sprites?(?=[^.\n]{0,30}(fly|sandbox|vm))|sprites\.dev", q="Fly.io Sprites", url="https://sprites.dev")
tool("sandbox", "smolvm", r"smolvm", url="https://github.com/smol-machines/smolvm", gh="smol-machines/smolvm")
tool("sandbox", "nono", r"\bnono\b(?=[^.\n]{0,30}(sandbox|agent))", q="nono sandbox", url="https://github.com/nolabs-ai/nono", gh="nolabs-ai/nono")
tool("sandbox", "bubblewrap", r"bubblewrap|\bbwrap\b", url="https://github.com/containers/bubblewrap", gh="containers/bubblewrap")
tool("sandbox", "Modal Sandboxes", r"\bmodal\b(?=[^.\n]{0,30}(sandbox|gpu|\.com))", q="Modal sandbox", url="https://modal.com/docs/guide/sandboxes")
tool("sandbox", "Vercel Sandbox", r"vercel sandbox", url="https://vercel.com/docs/vercel-sandbox")
tool("sandbox", "Lume", r"\blume\b", q="lume vm", url="https://github.com/trycua/cua", gh="trycua/cua")
tool("sandbox", "yoloai", r"yoloai", url="https://github.com/kstenerud/yoloai", gh="kstenerud/yoloai")
tool("sandbox", "Ardent", r"tryardent|\bardent\b", url="https://tryardent.com")

# --- Local models -----------------------------------------------------------
tool("local", "llama.cpp", r"llama\.?cpp|llama-server|llama\.app", url="https://github.com/ggml-org/llama.cpp", gh="ggml-org/llama.cpp")
tool("local", "Ollama", r"ollama(?!ya)", url="https://ollama.com", gh="ollama/ollama")
tool("local", "LM Studio", r"lm ?studio", url="https://lmstudio.ai")
tool("local", "MLX", r"\bmlx\b", q="MLX", url="https://github.com/ml-explore/mlx", gh="ml-explore/mlx", pypi="mlx-lm")
tool("local", "vLLM", r"\bvllm\b", url="https://github.com/vllm-project/vllm", gh="vllm-project/vllm", pypi="vllm")
tool("local", "Lemonade", r"lemonade", q="Lemonade AMD", url="https://lemonade-server.ai", gh="lemonade-sdk/lemonade")
tool("local", "SGLang", r"sglang", url="https://github.com/sgl-project/sglang", gh="sgl-project/sglang", pypi="sglang")
tool("local", "Open WebUI", r"open[ -]?webui", url="https://openwebui.com", gh="open-webui/open-webui")
tool("local", "Jan", r"\bjan\b(?=[^.\n]{0,20}(ai|app|\.ai))|jan\.ai", q="jan.ai", url="https://jan.ai", gh="janhq/jan")
tool("local", "llama-swap", r"llama[ -]swap", url="https://github.com/mostlygeek/llama-swap", gh="mostlygeek/llama-swap")
tool("local", "Unsloth", r"unsloth", url="https://unsloth.ai", gh="unslothai/unsloth", pypi="unsloth")
tool("local", "KoboldCpp", r"kobold", url="https://github.com/LostRuins/koboldcpp", gh="LostRuins/koboldcpp")
tool("local", "Apfel", r"\bapfel\b", url="https://github.com/Arthur-Ficial/apfel", gh="Arthur-Ficial/apfel")

# --- Gateways ---------------------------------------------------------------
tool("gateways", "OpenRouter", r"open ?router", url="https://openrouter.ai")
tool("gateways", "LiteLLM", r"litellm", url="https://github.com/BerriAI/litellm", gh="BerriAI/litellm", pypi="litellm")
tool("gateways", "Vercel AI Gateway", r"(vercel )?ai gateway", q="Vercel AI Gateway", url="https://vercel.com/ai-gateway")
tool("gateways", "OpenCode Go / Zen", r"opencode (go|zen)", url="https://opencode.ai/go")
tool("gateways", "llm (Simon Willison)", r"simonw/llm|\bllm cli\b|llm\.datasette|simon willison'?s? llm|\bllm\b tool", q="llm.datasette.io", url="https://llm.datasette.io", gh="simonw/llm", pypi="llm")
tool("gateways", "AWS Bedrock", r"bedrock", url="https://aws.amazon.com/bedrock/")
tool("gateways", "Cloudflare AI Gateway", r"cloudflare ai gateway|workers ai", url="https://developers.cloudflare.com/ai-gateway/")
tool("gateways", "cc-switch", r"cc[ -]switch", url="https://github.com/farion1231/cc-switch", gh="farion1231/cc-switch")
tool("gateways", "Claude Code Router", r"claude[ -]code[ -]router", url="https://github.com/musistudio/claude-code-router", gh="musistudio/claude-code-router")
tool("gateways", "OmniRoute", r"omniroute", url="https://github.com/cheaper-inference/OmniRoute", gh="cheaper-inference/OmniRoute")
tool("gateways", "Portkey", r"portkey", url="https://portkey.ai", gh="Portkey-AI/gateway")
tool("gateways", "Synthetic", r"synthetic\.new", url="https://synthetic.new")
tool("gateways", "Chutes", r"\bchutes\b", url="https://chutes.ai")

# --- Frameworks -------------------------------------------------------------
tool("frameworks", "Claude Agent SDK", r"(claude )?agent sdk|claude-agent-sdk", q="Claude Agent SDK", url="https://docs.claude.com/en/docs/agent-sdk/overview", npm="@anthropic-ai/claude-agent-sdk")
tool("frameworks", "OpenAI Agents SDK", r"(openai )?agents sdk", q="OpenAI Agents SDK", url="https://openai.github.io/openai-agents-python/", gh="openai/openai-agents-python", pypi="openai-agents")
tool("frameworks", "Vercel AI SDK", r"(vercel )?ai[ -]sdk", q="Vercel AI SDK", url="https://ai-sdk.dev", gh="vercel/ai", npm="ai")
tool("frameworks", "Pydantic AI", r"pydantic[ -]?ai", url="https://ai.pydantic.dev", gh="pydantic/pydantic-ai", pypi="pydantic-ai")
tool("frameworks", "LangGraph", r"langgraph", url="https://langchain-ai.github.io/langgraph/", gh="langchain-ai/langgraph", pypi="langgraph")
tool("frameworks", "LangChain", r"langchain", url="https://www.langchain.com", gh="langchain-ai/langchain", pypi="langchain")
tool("frameworks", "Mastra", r"mastra", url="https://mastra.ai", gh="mastra-ai/mastra", npm="@mastra/core")
tool("frameworks", "DSPy", r"\bdspy\b", url="https://dspy.ai", gh="stanfordnlp/dspy", pypi="dspy")
tool("frameworks", "smolagents", r"smolagents", url="https://github.com/huggingface/smolagents", gh="huggingface/smolagents", pypi="smolagents")
tool("frameworks", "Google ADK", r"\badk\b|agent development kit", q="Google ADK", url="https://google.github.io/adk-docs/", gh="google/adk-python", pypi="google-adk")
tool("frameworks", "Strands Agents", r"strands", q="Strands Agents", url="https://strandsagents.com", gh="strands-agents/sdk-python", pypi="strands-agents")
tool("frameworks", "BAML", r"\bbaml\b", url="https://boundaryml.com", gh="BoundaryML/baml")
tool("frameworks", "Pi agent toolkit", r"pi-ai|pi-agent|pi (sdk|toolkit|library)", q="pi-ai", url="https://github.com/earendil-works/pi", aka="pi-ai")
tool("frameworks", "MCP SDKs", r"mcp (python |typescript )?sdk|fastmcp", q="FastMCP", url="https://modelcontextprotocol.io", gh="modelcontextprotocol/python-sdk", pypi="mcp")
tool("frameworks", "Microsoft Agent Framework", r"agent framework|autogen|semantic kernel", q="Microsoft Agent Framework", url="https://github.com/microsoft/agent-framework", gh="microsoft/agent-framework")
tool("frameworks", "Jido", r"\bjido\b", url="https://github.com/agentjido/jido", gh="agentjido/jido")
tool("frameworks", "CrewAI", r"crew ?ai", url="https://www.crewai.com", gh="crewAIInc/crewAI", pypi="crewai")

# --- Evals ------------------------------------------------------------------
tool("evals", "Langfuse", r"langfuse", url="https://langfuse.com", gh="langfuse/langfuse", pypi="langfuse")
tool("evals", "promptfoo", r"promptfoo", url="https://www.promptfoo.dev", gh="promptfoo/promptfoo", npm="promptfoo")
tool("evals", "Braintrust", r"braintrust", url="https://www.braintrust.dev", pypi="braintrust")
tool("evals", "Arize Phoenix", r"phoenix(?=[^.\n]{0,30}(arize|trac|eval))|arize", q="Arize Phoenix", url="https://phoenix.arize.com", gh="Arize-ai/phoenix", pypi="arize-phoenix")
tool("evals", "LangSmith", r"langsmith", url="https://www.langchain.com/langsmith")
tool("evals", "Inspect AI", r"inspect[ _-]ai|inspect evals|\binspect\b(?=[^.\n]{0,20}(aisi|uk ai))", q="Inspect AI", url="https://inspect.aisi.org.uk", gh="UKGovernmentBEIS/inspect_ai", pypi="inspect-ai")
tool("evals", "DeepEval", r"deepeval", url="https://deepeval.com", gh="confident-ai/deepeval", pypi="deepeval")
tool("evals", "Logfire", r"logfire", url="https://pydantic.dev/logfire", gh="pydantic/logfire", pypi="logfire")
tool("evals", "Opik", r"\bopik\b", url="https://www.comet.com/site/products/opik/", gh="comet-ml/opik", pypi="opik")
tool("evals", "Helicone", r"helicone", url="https://www.helicone.ai", gh="Helicone/helicone")
tool("evals", "MLflow", r"mlflow", url="https://mlflow.org", gh="mlflow/mlflow", pypi="mlflow")
tool("evals", "Laminar", r"\blaminar\b|lmnr", q="Laminar lmnr", url="https://www.lmnr.ai", gh="lmnr-ai/lmnr")
tool("evals", "OpenTelemetry GenAI", r"opentelemetry|\botel\b|openllmetry", q="OpenTelemetry LLM", url="https://opentelemetry.io/docs/specs/semconv/gen-ai/")
tool("evals", "Weights & Biases Weave", r"\bweave\b(?=[^.\n]{0,30}(w&b|wandb|trac))|wandb weave", q="W&B Weave", url="https://wandb.ai/site/weave/", pypi="weave")
tool("evals", "garak", r"\bgarak\b", url="https://github.com/NVIDIA/garak", gh="NVIDIA/garak", pypi="garak")

# --- Always-on assistants ---------------------------------------------------
tool("assistants", "OpenClaw", r"open ?claw|clawd ?bot|molt ?bot", url="https://openclaw.ai", gh="openclaw/openclaw")
tool("assistants", "Hermes Agent", r"hermes(?! \d)(?=[^.\n]{0,40}(agent|setup|mac|running|cron)|\b)", q="Hermes Agent", url="https://github.com/NousResearch/hermes-agent", gh="NousResearch/hermes-agent")
tool("assistants", "Claude Cowork", r"cowork", url="https://claude.com/product/cowork")
tool("assistants", "Dots", r"\bdots\b(?=[^.\n]{0,40}(agent|openai|always|duet))|openai dots", q="OpenAI Dots", url="https://openai.com/index/introducing-dots/", cs=False)
tool("assistants", "Muse", r"\bmuse\b(?! (code|cli|spark))", q="Meta Muse agent", url="https://ai.meta.com/muse/")
tool("assistants", "NanoClaw", r"nanoclaw", url="https://github.com/qwibitai/nanoclaw", gh="qwibitai/nanoclaw")
tool("assistants", "nanobot", r"nanobot", url="https://github.com/HKUDS/nanobot", gh="HKUDS/nanobot")
tool("assistants", "Claude Code Routines", r"routines?(?=[^.\n]{0,30}claude)|claude code routines", q="Claude Code Routines", url="https://code.claude.com/docs/en/routines")
tool("assistants", "Claude Duet", r"\bduet\b", q="Claude Duet", url="https://claude.com/product/claude-duet")
tool("assistants", "Paperclip", r"paperclip(?=[^.\n]{0,30}(agent|ai))|paperclipai", q="paperclipai", url="https://github.com/paperclipai/paperclip", gh="paperclipai/paperclip")
tool("assistants", "Eigent", r"eigent", url="https://github.com/eigent-ai/eigent", gh="eigent-ai/eigent")
tool("assistants", "Home Assistant + LLM", r"home assistant", q="Home Assistant LLM", url="https://www.home-assistant.io/integrations/conversation/")
tool("assistants", "n8n", r"\bn8n\b", url="https://n8n.io", gh="n8n-io/n8n")
