# Nexo Showcase Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a bilingual, image-led showcase system and a complete fictional Nexo Mantenimiento case that explains an integrated AI workflow to small and medium-sized businesses.

**Architecture:** Extend the existing Python static-site generator with localized showcase data and four generated routes. Keep showcase layout and interaction in isolated CSS and JavaScript files, using progressive enhancement so every stage remains understandable without JavaScript. Use one original project-owned field-service image and HTML/CSS interface mockups for the workflow visuals.

**Tech Stack:** Python 3 static generation, semantic HTML, CSS Grid, vanilla JavaScript, Python `unittest`, Node.js syntax checks, Cloudflare Workers static assets.

**Spec:** `docs/superpowers/specs/2026-09-17-nexo-showcase-design.md`

## Global Constraints

- Preserve the existing pearl, charcoal, restrained-blue, Manrope, and DM Sans brand system.
- Label Nexo visibly as `Caso ficticio` in Spanish and `Fictional case` in English.
- Do not claim a real engagement, testimonial, production deployment, or measured result.
- Show human review before scheduling, reporting, or invoicing is final.
- Support hover, keyboard focus, and touch without requiring automatic animation.
- Keep all content readable without JavaScript and respect `prefers-reduced-motion`.
- Do not add a framework, API, analytics service, persistent state, or third-party brand artwork.
- Preserve existing product dialogs, contact behaviour, articles, protected routes, and deployment exclusions.
- Do not stage or commit the separate untracked flyer files while implementing this feature.

---

### Task 1: Localized showcase model and generated routes

**Files:**
- Create: `tests/test_showcase_build.py`
- Modify: `scripts/build-studio.py`
- Generate: `showcase/index.html`
- Generate: `en/showcase/index.html`
- Generate: `showcase/nexo-mantenimiento/index.html`
- Generate: `en/showcase/nexo-maintenance/index.html`
- Generate: `index.html`
- Generate: `en/index.html`

**Interfaces:**
- Consumes: existing `COPY`, shared home header/footer generation, and `ROOT` in `scripts/build-studio.py`.
- Produces: `SHOWCASE` localized content, four static routes, and one homepage preview per language.

- [ ] **Step 1: Write the route and copy test**

```python
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ShowcaseBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["python3", "scripts/build-studio.py"], cwd=ROOT, check=True)

    def test_showcase_routes_have_localized_metadata_and_six_stages(self):
        cases = [
            ("showcase/index.html", "Demostraciones", "Caso ficticio"),
            ("en/showcase/index.html", "Showcase", "Fictional case"),
            ("showcase/nexo-mantenimiento/index.html", "Nexo Mantenimiento", "Caso ficticio"),
            ("en/showcase/nexo-maintenance/index.html", "Nexo Maintenance", "Fictional case"),
        ]
        for relative, heading, label in cases:
            html = (ROOT / relative).read_text()
            self.assertIn(heading, html)
            self.assertIn(label, html)
            self.assertIn('rel="canonical"', html)
        for relative in [
            "showcase/nexo-mantenimiento/index.html",
            "en/showcase/nexo-maintenance/index.html",
        ]:
            html = (ROOT / relative).read_text()
            self.assertEqual(html.count('class="stage-control"'), 6)

    def test_homepages_link_to_the_matching_showcase(self):
        self.assertIn('href="/showcase/nexo-mantenimiento/"', (ROOT / "index.html").read_text())
        self.assertIn('href="/en/showcase/nexo-maintenance/"', (ROOT / "en/index.html").read_text())
```

- [ ] **Step 2: Run the test and verify the missing routes fail**

Run: `python3 -m unittest tests/test_showcase_build.py -v`

Expected: FAIL because the four showcase files and homepage links do not exist.

- [ ] **Step 3: Add localized content and route builders**

Add a `SHOWCASE` mapping in `scripts/build-studio.py` with Spanish and English values for metadata, navigation labels, index copy, Nexo hero copy, the six named stages, before/after copy, integration labels, CTA, and route pairs. Add helper functions with these signatures:

```python
def shared_head(lang: str, title: str, description: str, canonical: str, alternate: str, image: str) -> str:
    """Return localized metadata and shared CSS/JS links."""


def showcase_mosaic(lang: str, context: str) -> str:
    """Return the progressive-enhancement mosaic for `home`, `index`, or `case`."""


def build_showcase_page(lang: str) -> str:
    """Return the localized showcase index document."""


def build_nexo_page(lang: str) -> str:
    """Return the localized six-stage Nexo case document."""
```

Generate the four routes and insert the homepage preview after the process section. Add `Demos` or `Showcase` to desktop, mobile, and footer navigation. Preserve contextual language switching between matching routes.

- [ ] **Step 4: Run the build tests**

Run: `python3 -m unittest tests/test_showcase_build.py -v`

Expected: PASS for all route, localization, stage-count, and homepage-link assertions.

- [ ] **Step 5: Commit the route foundation**

```bash
git add tests/test_showcase_build.py scripts/build-studio.py index.html en/index.html showcase en/showcase
git commit -m "Add bilingual Nexo showcase routes"
```

---

### Task 2: Original Nexo visual and showcase layout

**Files:**
- Create: `assets/showcase/showcase.css`
- Create: `assets/showcase/nexo/field-service.webp`
- Modify: `scripts/build-studio.py`
- Regenerate: the six generated homepage and showcase documents from Task 1

**Interfaces:**
- Consumes: `.showcase-mosaic`, `.stage-control`, `.showcase-panel`, and localized text emitted by Task 1.
- Produces: responsive image-led layouts and the project-owned hero image used by metadata and visible panels.

- [ ] **Step 1: Generate and inspect the original field-service image**

Use the image generation tool with this art direction:

```text
Editorial documentary photograph for a premium technology consultancy website. A fictional small property-maintenance company in a bright contemporary commercial space in Tenerife. A field technician in neutral workwear, seen from the side with no identifiable face, inspecting plumbing beneath a clean sink while a tablet rests nearby. Architectural daylight, pale stone, brushed metal, subtle utility details, quiet competent mood. Mostly monochrome with restrained cool blue-grey accents. Wide 3:2 composition with clear negative space for a software interface overlay. No logos, no text, no existing brand marks, no dramatic leak, no sci-fi effects.
```

Save the selected asset as `assets/showcase/nexo/field-service.webp`, confirm it is at least 1440 px wide, and inspect the full-resolution image for text artifacts, malformed tools, extra limbs, and visible faces.

- [ ] **Step 2: Create the showcase stylesheet**

Implement these concrete layout units in `assets/showcase/showcase.css`:

```css
.showcase-mosaic { display:grid; grid-template-columns:minmax(0,1.65fr) minmax(250px,.7fr); gap:12px; }
.showcase-panel { position:relative; min-height:620px; overflow:hidden; background:#dfe3e6; }
.showcase-stage-list { display:grid; grid-template-rows:repeat(3,1fr); gap:12px; }
.stage-control { position:relative; min-height:190px; border:1px solid transparent; overflow:hidden; }
.stage-control[aria-current="step"] { border-color:var(--ink); }
```

Complete the desktop, tablet, 390 px, and 320 px layouts. Use the existing CSS variables. Keep stage captions visible on touch widths, provide visible `:focus-visible` styles, and disable transforms and transitions in reduced-motion mode.

- [ ] **Step 3: Build the interface artwork in semantic HTML**

Update `showcase_mosaic()` so the large panel contains the field-service image and six absolutely aligned interface layers. Use plain elements for a customer message, transcript, work order, schedule, evidence checklist, report, and invoice draft. Each layer must contain only the data needed to explain its stage and a visible human-review marker where relevant.

- [ ] **Step 4: Rebuild and render the pages**

Run:

```bash
python3 scripts/build-studio.py
python3 -m unittest tests/test_showcase_build.py -v
```

Expected: all tests pass and every generated page references `/assets/showcase/showcase.css` plus the project-owned WebP asset.

- [ ] **Step 5: Commit the visual system**

```bash
git add assets/showcase scripts/build-studio.py index.html en/index.html showcase en/showcase
git commit -m "Build the Nexo showcase visual system"
```

---

### Task 3: Progressive interactive stages

**Files:**
- Create: `assets/showcase/showcase.js`
- Create: `tests/showcase-interaction.test.cjs`
- Modify: `scripts/build-studio.py`
- Regenerate: the six generated homepage and showcase documents

**Interfaces:**
- Consumes: every `.showcase-mosaic[data-showcase]` and its six `.stage-control[data-stage]` elements.
- Produces: `activateStage(root, stageId)` behaviour expressed through `root.dataset.activeStage`, `aria-current="step"`, and `.showcase-status` text.

- [ ] **Step 1: Write the interaction test**

Create a dependency-free test that evaluates `assets/showcase/showcase.js` in a Node `vm` with a small mock document. Assert that initialisation selects the first control, `pointerenter`, `focus`, and `click` select their target stage, only the active control has `aria-current="step"`, and status text follows the active control's `data-status`.

Run: `node tests/showcase-interaction.test.cjs`

Expected: FAIL because `assets/showcase/showcase.js` does not exist.

- [ ] **Step 2: Implement the interaction module**

Use this public shape in `assets/showcase/showcase.js`:

```javascript
const activateStage = (root, stageId) => {
  const controls = [...root.querySelectorAll('.stage-control[data-stage]')];
  const selected = controls.find(control => control.dataset.stage === stageId) || controls[0];
  root.dataset.activeStage = selected.dataset.stage;
  controls.forEach(control => {
    if (control === selected) control.setAttribute('aria-current', 'step');
    else control.removeAttribute('aria-current');
  });
  const status = root.querySelector('.showcase-status');
  if (status) status.textContent = selected.dataset.status;
};
```

Initialise each showcase root, then bind `pointerenter`, `focus`, and `click` to its controls. Do not add timers or automatic rotation.

- [ ] **Step 3: Load the script only where needed**

Update generated homepage and showcase documents to load `/assets/showcase/showcase.js` with `defer`. Keep article and product-only pages free of showcase assets.

- [ ] **Step 4: Run interaction and build checks**

Run:

```bash
node --check assets/showcase/showcase.js
node tests/showcase-interaction.test.cjs
python3 -m unittest tests/test_showcase_build.py -v
```

Expected: all commands pass.

- [ ] **Step 5: Commit the interaction**

```bash
git add assets/showcase/showcase.js tests/showcase-interaction.test.cjs scripts/build-studio.py index.html en/index.html showcase en/showcase
git commit -m "Add accessible showcase interactions"
```

---

### Task 4: Content, accessibility, and responsive review

**Files:**
- Modify: `scripts/build-studio.py`
- Modify: `assets/showcase/showcase.css`
- Modify: `assets/showcase/showcase.js` only if browser review finds an interaction defect
- Regenerate: all files produced by `scripts/build-studio.py`

**Interfaces:**
- Consumes: the complete showcase system from Tasks 1-3.
- Produces: review-ready Spanish and English pages across desktop and mobile.

- [ ] **Step 1: Run structural validation**

Run the generator, unit tests, JavaScript syntax check, interaction test, `git diff --check`, and the repository's local route/asset validator. Confirm all four showcase routes, images, stylesheets, scripts, anchors, and language alternates resolve.

- [ ] **Step 2: Review Spanish desktop and mobile**

Use browser automation at normal desktop width, 390 px, and 320 px. Verify page order, hover state, keyboard state, tap state, visible fictional-case labels, menu closure, focus visibility, no horizontal overflow, and no console errors.

- [ ] **Step 3: Review English desktop and mobile**

Repeat the same checks for `/en/`, `/en/showcase/`, and `/en/showcase/nexo-maintenance/`. Check that the English reads naturally and does not retain Spanish labels or routes.

- [ ] **Step 4: Tighten only observed defects**

Adjust copy, spacing, typography, crop positions, or interaction code only where the rendered review shows a defect. Regenerate and rerun the affected checks after each change.

- [ ] **Step 5: Commit the reviewed result**

```bash
git add scripts/build-studio.py assets/showcase index.html en/index.html showcase en/showcase tests
git commit -m "Polish the bilingual Nexo showcase"
```

---

### Task 5: Release and production verification

**Files:**
- Modify: `docs/BRAND.md`
- Verify: `wrangler.jsonc`
- Verify: `.assetsignore`

**Interfaces:**
- Consumes: the reviewed committed showcase snapshot.
- Produces: GitHub `main` and the matching Cloudflare production deployment.

- [ ] **Step 1: Document the showcase build**

Update `docs/BRAND.md` with the four routes, the `SHOWCASE` content source, the dedicated asset directory, and the fictional-case rule.

- [ ] **Step 2: Run the complete pre-release check**

Run:

```bash
python3 scripts/build-studio.py
python3 -m unittest tests/test_showcase_build.py -v
node --check assets/showcase/showcase.js
node tests/showcase-interaction.test.cjs
git diff --check
```

Expected: all checks pass. Confirm the only remaining untracked files are the separate flyer campaign and output files.

- [ ] **Step 3: Commit the release state**

```bash
git add docs/BRAND.md scripts/build-studio.py assets/showcase tests index.html en/index.html showcase en/showcase articles en/articles
git commit -m "Document the AI showcase system"
```

- [ ] **Step 4: Push the committed main branch**

Run: `git push origin main`

Expected: `origin/main` advances to the local release commit without force-pushing.

- [ ] **Step 5: Deploy the exact commit**

Create a clean temporary directory with `git archive HEAD`, extract it, and run `npx --yes wrangler@4.133.0 deploy` from that directory. Record the Cloudflare version ID.

- [ ] **Step 6: Verify production**

Compare live bytes for the Spanish and English homepages, all four showcase routes, the showcase CSS, JavaScript, and hero image against the committed archive. Confirm `/lab/`, `/cleaning-windows/`, and `/api/bookings` still return `401`; confirm `/brand/`, `/docs/`, `/scripts/`, and `/grow/` remain unavailable. Open the live Spanish and English cases in a browser and verify the six-stage interaction and responsive layout.
