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

    def test_showcase_assets_and_language_alternates_exist(self):
        for relative in [
            "assets/showcase/showcase.css",
            "assets/showcase/showcase.js",
            "assets/showcase/nexo/field-service.webp",
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


if __name__ == "__main__":
    unittest.main()
