import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fetch_svg import url_for, validate_slug, write_manifest


class FetchSvgTests(unittest.TestCase):
    def test_slug_validation(self):
        validate_slug("github", "simple-icons")
        validate_slug("academic-cap", "heroicons")
        for bad in ("../etc", "a/b", "a b", "UPPER", "", "a..b"):
            with self.assertRaises(ValueError):
                validate_slug(bad, "simple-icons")

    def test_url_mapping(self):
        self.assertEqual(url_for("simple-icons", "github", None, None), "https://cdn.simpleicons.org/github")
        self.assertEqual(url_for("simple-icons", "github", None, "181717"), "https://cdn.simpleicons.org/github/181717")
        self.assertEqual(
            url_for("phosphor", "palette", "bold", None),
            "https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/bold/palette.svg",
        )
        self.assertEqual(
            url_for("heroicons", "academic-cap", None, None),
            "https://cdn.jsdelivr.net/npm/heroicons@latest/24/outline/academic-cap.svg",
        )

    def test_manifest_append(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "manifest.json"
            write_manifest(manifest, {"file": "a.svg", "license": "MIT"})
            write_manifest(manifest, {"file": "b.svg", "license": "CC0"})
            data = manifest.read_text(encoding="utf-8")
            self.assertIn("a.svg", data)
            self.assertIn("b.svg", data)
            self.assertEqual(len(__import__("json").loads(data)["assets"]), 2)


if __name__ == "__main__":
    unittest.main()
