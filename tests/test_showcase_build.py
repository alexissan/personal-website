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
            ("showcase/mesa-clara/index.html", "Mesa Clara", "Caso ficticio"),
            ("en/showcase/mesa-clara/index.html", "Mesa Clara", "Fictional case"),
            ("showcase/ladera-norte/index.html", "Ladera Norte", "Caso ficticio"),
            ("en/showcase/ladera-norte/index.html", "Ladera Norte", "Fictional case"),
        ]
        for relative, heading, label in cases:
            html = (ROOT / relative).read_text()
            self.assertIn(heading, html)
            self.assertIn(label, html)
            self.assertIn('rel="canonical"', html)
        for relative in [
            "showcase/nexo-mantenimiento/index.html",
            "en/showcase/nexo-maintenance/index.html",
            "showcase/mesa-clara/index.html",
            "en/showcase/mesa-clara/index.html",
            "showcase/ladera-norte/index.html",
            "en/showcase/ladera-norte/index.html",
        ]:
            html = (ROOT / relative).read_text()
            self.assertEqual(html.count('class="stage-control"'), 6)

    def test_homepages_link_to_the_matching_showcase(self):
        spanish_home = (ROOT / "index.html").read_text()
        english_home = (ROOT / "en/index.html").read_text()
        spanish_showcase = (ROOT / "showcase/index.html").read_text()
        english_showcase = (ROOT / "en/showcase/index.html").read_text()
        self.assertIn('href="/showcase/"', spanish_home)
        self.assertIn('href="/en/showcase/"', english_home)
        self.assertIn('href="/showcase/mesa-clara/"', spanish_home)
        self.assertIn('href="/en/showcase/mesa-clara/"', english_home)
        self.assertIn('href="/showcase/ladera-norte/"', spanish_home)
        self.assertIn('href="/en/showcase/ladera-norte/"', english_home)
        self.assertIn('href="/showcase/nexo-mantenimiento/"', spanish_showcase)
        self.assertIn('href="/en/showcase/nexo-maintenance/"', english_showcase)
        self.assertIn('href="/showcase/mesa-clara/"', spanish_showcase)
        self.assertIn('href="/en/showcase/mesa-clara/"', english_showcase)
        self.assertIn('href="/showcase/ladera-norte/"', spanish_showcase)
        self.assertIn('href="/en/showcase/ladera-norte/"', english_showcase)

    def test_showcase_is_second_in_navigation(self):
        spanish = (ROOT / "index.html").read_text()
        english = (ROOT / "en/index.html").read_text()
        self.assertLess(spanish.index('href="#solutions"'), spanish.index('href="/showcase/"'))
        self.assertLess(spanish.index('href="/showcase/"'), spanish.index('href="#projects"'))
        self.assertLess(english.index('href="#solutions"'), english.index('href="/en/showcase/"'))
        self.assertLess(english.index('href="/en/showcase/"'), english.index('href="#projects"'))

    def test_showcase_assets_and_language_alternates_exist(self):
        for relative in [
            "assets/showcase/showcase.css",
            "assets/showcase/showcase.js",
            "assets/showcase/nexo/field-service.webp",
            "assets/showcase/nexo/evidence-before.webp",
            "assets/showcase/nexo/evidence-after.webp",
            "assets/showcase/mesa-clara/restaurant.webp",
            "assets/showcase/ladera-norte/finance-desk.webp",
        ]:
            self.assertTrue((ROOT / relative).is_file(), relative)
        spanish = (ROOT / "showcase/nexo-mantenimiento/index.html").read_text()
        english = (ROOT / "en/showcase/nexo-maintenance/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/en/showcase/nexo-maintenance/"', spanish)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/showcase/nexo-mantenimiento/"', english)
        for html in [spanish, english]:
            self.assertIn('/assets/showcase/showcase.css', html)
            self.assertIn('/assets/showcase/showcase.js', html)
            self.assertIn('/assets/showcase/nexo/field-service.webp', html)
            self.assertIn('/assets/showcase/nexo/evidence-before.webp', html)
            self.assertIn('/assets/showcase/nexo/evidence-after.webp', html)
            self.assertIn('class="desktop-device"', html)
            self.assertIn('class="phone-device"', html)

        spanish_restaurant = (ROOT / "showcase/mesa-clara/index.html").read_text()
        english_restaurant = (ROOT / "en/showcase/mesa-clara/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/en/showcase/mesa-clara/"', spanish_restaurant)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/showcase/mesa-clara/"', english_restaurant)
        for html in [spanish_restaurant, english_restaurant]:
            self.assertIn('/assets/showcase/mesa-clara/restaurant.webp', html)
            self.assertIn('class="restaurant-desktop"', html)
            self.assertIn('class="booking-phone"', html)

        spanish_invoice = (ROOT / "showcase/ladera-norte/index.html").read_text()
        english_invoice = (ROOT / "en/showcase/ladera-norte/index.html").read_text()
        self.assertIn('hreflang="en" href="https://alexissantos.dev/en/showcase/ladera-norte/"', spanish_invoice)
        self.assertIn('hreflang="es" href="https://alexissantos.dev/showcase/ladera-norte/"', english_invoice)
        for html, review_label in [(spanish_invoice, 'REVISIÓN HUMANA'), (english_invoice, 'HUMAN REVIEW')]:
            self.assertIn('/assets/showcase/ladera-norte/finance-desk.webp', html)
            self.assertIn('class="invoice-desktop"', html)
            self.assertIn('class="approval-phone"', html)
            self.assertIn(review_label, html)


if __name__ == "__main__":
    unittest.main()
