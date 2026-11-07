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
            ("es/showcase/index.html", "Demostraciones", "Caso ficticio"),
            ("showcase/index.html", "Showcase", "Fictional case"),
            ("es/showcase/nexo-mantenimiento/index.html", "Nexo Mantenimiento", "Caso ficticio"),
            ("showcase/nexo-maintenance/index.html", "Nexo Maintenance", "Fictional case"),
            ("es/showcase/mesa-clara/index.html", "Mesa Clara", "Caso ficticio"),
            ("showcase/mesa-clara/index.html", "Mesa Clara", "Fictional case"),
            ("es/showcase/ladera-norte/index.html", "Ladera Norte", "Caso ficticio"),
            ("showcase/ladera-norte/index.html", "Ladera Norte", "Fictional case"),
            ("es/showcase/cerrajeria-faro/index.html", "Cerrajería Faro", "Caso ficticio"),
            ("showcase/cerrajeria-faro/index.html", "Cerrajería Faro", "Fictional case"),
        ]
        for relative, heading, label in cases:
            html = (ROOT / relative).read_text()
            self.assertIn(heading, html)
            self.assertIn(label, html)
            self.assertIn('rel="canonical"', html)
        for relative in [
            "es/showcase/nexo-mantenimiento/index.html",
            "showcase/nexo-maintenance/index.html",
            "es/showcase/mesa-clara/index.html",
            "showcase/mesa-clara/index.html",
            "es/showcase/ladera-norte/index.html",
            "showcase/ladera-norte/index.html",
            "es/showcase/cerrajeria-faro/index.html",
            "showcase/cerrajeria-faro/index.html",
        ]:
            html = (ROOT / relative).read_text()
            self.assertEqual(html.count('class="stage-control"'), 6)

    def test_homepages_link_to_the_matching_showcase(self):
        spanish_home = (ROOT / "es/index.html").read_text()
        english_home = (ROOT / "index.html").read_text()
        spanish_showcase = (ROOT / "es/showcase/index.html").read_text()
        english_showcase = (ROOT / "showcase/index.html").read_text()
        self.assertIn('href="/es/showcase/"', spanish_home)
        self.assertIn('href="/showcase/"', english_home)
        self.assertIn('href="/es/showcase/mesa-clara/"', spanish_home)
        self.assertIn('href="/showcase/mesa-clara/"', english_home)
        self.assertIn('href="/es/showcase/ladera-norte/"', spanish_home)
        self.assertIn('href="/showcase/ladera-norte/"', english_home)
        self.assertIn('href="/es/showcase/cerrajeria-faro/"', spanish_home)
        self.assertIn('href="/showcase/cerrajeria-faro/"', english_home)
        self.assertIn('href="/es/showcase/nexo-mantenimiento/"', spanish_showcase)
        self.assertIn('href="/showcase/nexo-maintenance/"', english_showcase)
        self.assertIn('href="/es/showcase/mesa-clara/"', spanish_showcase)
        self.assertIn('href="/showcase/mesa-clara/"', english_showcase)
        self.assertIn('href="/es/showcase/ladera-norte/"', spanish_showcase)
        self.assertIn('href="/showcase/ladera-norte/"', english_showcase)
        self.assertIn('href="/es/showcase/cerrajeria-faro/"', spanish_showcase)
        self.assertIn('href="/showcase/cerrajeria-faro/"', english_showcase)

    def test_showcase_is_second_in_navigation(self):
        spanish = (ROOT / "es/index.html").read_text()
        english = (ROOT / "index.html").read_text()
        self.assertLess(spanish.index('href="#solutions"'), spanish.index('href="/es/showcase/"'))
        self.assertLess(spanish.index('href="/es/showcase/"'), spanish.index('href="#studio"'))
        self.assertLess(english.index('href="#solutions"'), english.index('href="/showcase/"'))
        self.assertLess(english.index('href="/showcase/"'), english.index('href="#studio"'))

    def test_grow_book_is_published_and_linked(self):
        spanish = (ROOT / "es/index.html").read_text()
        english = (ROOT / "index.html").read_text()
        book = (ROOT / "grow/index.html").read_text()
        ignored_assets = (ROOT / ".assetsignore").read_text().splitlines()
        sitemap = (ROOT / "sitemap.xml").read_text()

        self.assertGreaterEqual(spanish.count('href="/grow/"'), 3)
        self.assertGreaterEqual(english.count('href="/grow/"'), 3)
        self.assertIn('class="about-book" href="/grow/"', spanish)
        self.assertIn('class="about-book" href="/grow/"', english)
        self.assertNotIn("grow", ignored_assets)
        self.assertIn("Build It. Then Grow It.", book)
        self.assertEqual(book.count('class="part-divider"'), 6)
        self.assertEqual(book.count('class="chapter"'), 28)
        self.assertIn("Chapter 1", book)
        self.assertIn("Chapter 28", book)
        self.assertIn("https://alexissantos.dev/grow/", sitemap)

    def test_showcase_assets_and_language_alternates_exist(self):
        for relative in [
            "assets/showcase/showcase.css",
            "assets/showcase/showcase.js",
            "assets/showcase/nexo/field-service.webp",
            "assets/showcase/nexo/evidence-before.webp",
            "assets/showcase/nexo/evidence-after.webp",
            "assets/showcase/mesa-clara/restaurant.webp",
            "assets/showcase/ladera-norte/finance-desk.webp",
            "assets/showcase/cerrajeria-faro/door-assessment.webp",
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)
        spanish = (ROOT / "es/showcase/nexo-mantenimiento/index.html").read_text()
        english = (ROOT / "showcase/nexo-maintenance/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/showcase/nexo-maintenance/"', spanish)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/es/showcase/nexo-mantenimiento/"', english)
        for html in [spanish, english]:
            self.assertIn('/assets/showcase/showcase.css', html)
            self.assertIn('/assets/showcase/showcase.js', html)
            self.assertIn('/assets/showcase/nexo/field-service.webp', html)
            self.assertIn('/assets/showcase/nexo/evidence-before.webp', html)
            self.assertIn('/assets/showcase/nexo/evidence-after.webp', html)
            self.assertIn('class="desktop-device"', html)
            self.assertIn('class="phone-device"', html)

        spanish_restaurant = (ROOT / "es/showcase/mesa-clara/index.html").read_text()
        english_restaurant = (ROOT / "showcase/mesa-clara/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/showcase/mesa-clara/"', spanish_restaurant)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/es/showcase/mesa-clara/"', english_restaurant)
        for html in [spanish_restaurant, english_restaurant]:
            self.assertIn('/assets/showcase/mesa-clara/restaurant.webp', html)
            self.assertIn('class="restaurant-desktop"', html)
            self.assertIn('class="booking-phone"', html)

        spanish_invoice = (ROOT / "es/showcase/ladera-norte/index.html").read_text()
        english_invoice = (ROOT / "showcase/ladera-norte/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/showcase/ladera-norte/"', spanish_invoice)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/es/showcase/ladera-norte/"', english_invoice)
        for html, review_label in [(spanish_invoice, 'REVISIÓN HUMANA'), (english_invoice, 'HUMAN REVIEW')]:
            self.assertIn('/assets/showcase/ladera-norte/finance-desk.webp', html)
            self.assertIn('class="invoice-desktop"', html)
            self.assertIn('class="approval-phone"', html)
            self.assertIn(review_label, html)

        for relative in ["es/showcase/cerrajeria-faro/index.html", "showcase/cerrajeria-faro/index.html"]:
            html = (ROOT / relative).read_text()
            self.assertIn('/assets/showcase/cerrajeria-faro/door-assessment.webp', html)
            self.assertIn('class="quote-desktop"', html)
            self.assertIn('class="quote-phone"', html)
            self.assertIn('IGIC · 7%', html)

    def test_english_is_the_primary_language(self):
        english = (ROOT / "index.html").read_text()
        spanish = (ROOT / "es/index.html").read_text()
        self.assertIn('<html lang="en">', english)
        self.assertIn('<html lang="es">', spanish)
        for html in [english, spanish]:
            self.assertIn('hreflang="en" href="https://alexissantos.dev/"', html)
            self.assertIn('hreflang="es" href="https://alexissantos.dev/es/"', html)
            self.assertIn('hreflang="x-default" href="https://alexissantos.dev/"', html)
        self.assertIn('<html lang="en"', (ROOT / "articles/index.html").read_text())
        self.assertIn('<html lang="es"', (ROOT / "es/articles/index.html").read_text())
        self.assertIn('<html lang="en"', (ROOT / "articles/mcp-at-work/index.html").read_text())
        self.assertFalse((ROOT / "en").exists())

    def test_no_page_links_to_the_retired_en_prefix(self):
        for page in ROOT.rglob("index.html"):
            if any(part in page.parts for part in ("_research", "lab", "docs", "brand", "tests", ".git")):
                continue
            self.assertNotRegex(page.read_text(), r'(href|src)="/en(/|")', str(page))

    def test_sitemap_lists_both_languages(self):
        sitemap = (ROOT / "sitemap.xml").read_text()
        for path in ["/", "/es/", "/articles/", "/es/articles/", "/showcase/nexo-maintenance/", "/es/showcase/nexo-mantenimiento/", "/ai-dev-tools/"]:
            self.assertIn(f"<loc>https://alexissantos.dev{path}</loc>", sitemap)
        self.assertNotIn("alexissantos.dev/en/", sitemap)

    def test_legacy_urls_redirect(self):
        script = """
const fs = require('fs');
const src = fs.readFileSync('_worker.js', 'utf8');
const body = src.slice(src.indexOf('const SPANISH_ONLY_ROOT_PATHS'), src.indexOf('function legacyRedirect'))
  + src.slice(src.indexOf('function legacyRedirect')).split('\\n}\\n')[0] + '\\n}';
const legacyRedirect = new Function(body + '; return legacyRedirect;')();
const cases = process.argv.slice(1);
console.log(JSON.stringify(cases.map(u => legacyRedirect(new URL(u)))));
"""
        urls = [
            "https://alexissantos.dev/en/",
            "https://alexissantos.dev/en",
            "https://alexissantos.dev/en/showcase/nexo-maintenance/?ref=x",
            "https://alexissantos.dev/en/articles/mcp-at-work/",
            "https://alexissantos.dev/showcase/nexo-mantenimiento/",
            "https://alexissantos.dev/showcase/mesa-clara/",
            "https://alexissantos.dev/entropy/",
        ]
        out = subprocess.run(["node", "-e", script, *urls], cwd=ROOT, check=True, capture_output=True, text=True).stdout
        import json
        self.assertEqual(json.loads(out), [
            "https://alexissantos.dev/",
            "https://alexissantos.dev/",
            "https://alexissantos.dev/showcase/nexo-maintenance/?ref=x",
            "https://alexissantos.dev/articles/mcp-at-work/",
            "https://alexissantos.dev/es/showcase/nexo-mantenimiento/",
            None,
            None,
        ])


if __name__ == "__main__":
    unittest.main()
