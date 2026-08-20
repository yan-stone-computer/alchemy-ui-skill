import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from preflight_check import scan, scan_text, summarize


class PreflightCheckTests(unittest.TestCase):
    def test_detects_hard_tells(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "page.html").write_text(
                """<div class="h-screen" onClick="go()">x</div>
<style>body { background:#000000; } a { transition: all .3s; font-family: Inter; }</style>
<script>window.addEventListener("scroll", fn);</script>
<img src="x.jpg">
<button class="bg-white text-white">hi</button>
<h1>Hello \u2014 world</h1>""",
                encoding="utf-8",
            )
            results = scan(root)
            rules = {f.rule for r in results for f in r.findings}
            for expected in ("em-dash", "pure-black", "h-screen", "transition-all", "scroll-listener", "div-onclick", "invisible-button", "missing-alt"):
                self.assertIn(expected, rules)

    def test_clean_file_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "good.html").write_text(
                """<!doctype html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<main class="min-h-[100dvh]"><button class="bg-zinc-950 text-white">Continue</button>
<img src="x.jpg" alt="Shot" width="1200" height="800"></main>""",
                encoding="utf-8",
            )
            results = scan(root)
            hard, _ = summarize(results)
            self.assertEqual(hard, 0)

    def test_skips_node_modules(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            nm = root / "node_modules" / "pkg"
            nm.mkdir(parents=True)
            (nm / "bad.html").write_text("<h1>x \u2014 y</h1>", encoding="utf-8")
            results = scan(root)
            self.assertEqual(results, [])

    def test_skips_generated_token_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "design-tokens.json").write_text(
                '{"semantic": {"light": {"on-primary": "#FFFFFF"}}}', encoding="utf-8"
            )
            results = scan(root)
            self.assertEqual(results, [])

    def test_line_override_suppresses_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "doc.md").write_text(
                "The banned pattern is `h-screen` and `transition: all`. <!-- ui-alchemy: ignore -->",
                encoding="utf-8",
            )
            results = scan(root)
            hard, _ = summarize(results)
            self.assertEqual(hard, 0)

    def test_ignore_all_suppresses_everything(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "doc.md").write_text(
                "<!-- ui-alchemy: ignore-all -->\n<h1>x \u2014 y</h1>\n<div class=\"h-screen\">z</div>",
                encoding="utf-8",
            )
            results = scan(root)
            hard, _ = summarize(results)
            self.assertEqual(hard, 0)

    def test_h5_platform_checks(self):
        missing = scan_text("<!doctype html><html><body>hi</body></html>", "page.html", "h5")
        self.assertTrue(any(f.rule == "viewport-missing" for f in missing.findings))
        locked = scan_text(
            "<meta name=\"viewport\" content=\"width=device-width, user-scalable=no\">",
            "page.html",
            "h5",
        )
        self.assertTrue(any(f.rule == "zoom-disabled" for f in locked.findings))
        good = scan_text(
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">",
            "page.html",
            "h5",
        )
        self.assertFalse([f for f in good.findings if f.severity == "hard"])

    def test_miniapp_platform_checks(self):
        bad = scan_text(
            "<image src=\"/a.png\"></image>\n<view bindtap=\"go\">tap</view>",
            "index.wxml",
            "miniapp",
        )
        rules = {f.rule for f in bad.findings}
        self.assertIn("miniapp-image-mode", rules)
        self.assertIn("miniapp-view-tap", rules)
        good = scan_text(
            "<image src=\"/a.png\" mode=\"aspectFill\" lazy-load=\"true\"></image>\n<button bindtap=\"go\">Go</button>",
            "index.wxml",
            "miniapp",
        )
        self.assertEqual([f for f in good.findings], [])


if __name__ == "__main__":
    unittest.main()
