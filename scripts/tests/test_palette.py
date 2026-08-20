import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from palette import anchor_step, build, contrast, generate_scale, on_color


class PaletteTest(unittest.TestCase):
    def test_contrast_math(self):
        self.assertAlmostEqual(contrast("#FFFFFF", "#000000"), 21.0, places=2)

    def test_scale_contains_brand(self):
        scale = generate_scale("#F26B21")
        anchor = anchor_step("#F26B21")
        self.assertIn(anchor, scale)
        self.assertEqual(scale[anchor], "#F26B21")

    def test_on_color_flips(self):
        self.assertEqual(on_color("#111111"), "#FFFFFF")
        self.assertEqual(on_color("#F2EBDE"), "#111111")

    def test_palette_passes_contrast(self):
        payload = build("#2B4A33", "#C98244", "Forest")
        self.assertTrue(payload["contrast"]["all_pass"])
        self.assertIn("light", payload["semantic"])
        self.assertIn("dark", payload["semantic"])


if __name__ == "__main__":
    unittest.main()
