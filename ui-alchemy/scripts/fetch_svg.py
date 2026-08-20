#!/usr/bin/env python3
"""UI Alchemy: download accessible open-source SVG icons and brand logos.

Sources and licenses (verify before shipping):
  simple-icons  CC0       https://cdn.simpleicons.org/{slug}[/{color}]
  tabler        MIT       https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/{name}.svg
  phosphor      MIT       https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/{weight}/{name}.svg
  heroicons     MIT       https://cdn.jsdelivr.net/npm/heroicons@latest/{size}/{style}/{name}.svg
  remix         Apache-2  https://cdn.jsdelivr.net/npm/remixicon@latest/icons/{name}.svg

Usage:
  python fetch_svg.py --source simple-icons --name github --out assets/icons
  python fetch_svg.py --source tabler --name heart --variant outline --out assets/icons
  python fetch_svg.py --source phosphor --name palette --variant bold --out assets/icons
  python fetch_svg.py --source heroicons --name academic-cap --variant outline --out assets/icons
  python fetch_svg.py --source simple-icons --name github --color 181717 --alt "GitHub logo" --manifest assets/manifest.json
  python fetch_svg.py --selftest
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


SOURCES = {
    "simple-icons": {
        "license": "CC0",
        "url": "https://cdn.simpleicons.org/{slug}{color}",
    },
    "tabler": {
        "license": "MIT",
        "url": "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/{name}.svg",
    },
    "phosphor": {
        "license": "MIT",
        "url": "https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/{variant}/{name}.svg",
    },
    "heroicons": {
        "license": "MIT",
        "url": "https://cdn.jsdelivr.net/npm/heroicons@latest/24/{variant}/{name}.svg",
    },
    "remix": {
        "license": "Apache-2.0",
        "url": "https://cdn.jsdelivr.net/npm/remixicon@latest/icons/{name}.svg",
    },
}

DEFAULTS = {"phosphor": {"variant": "regular"}, "heroicons": {"variant": "outline"}}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_SVG_BYTES = 2 * 1024 * 1024


def validate_slug(slug: str, source: str) -> None:
    if not slug or not SLUG_RE.match(slug) or len(slug) > 80:
        raise ValueError(
            f"invalid slug for {source}: {slug!r}. Use lowercase letters, digits, hyphens; no dots or separators."
        )


def url_for(source: str, name: str, variant: str | None, color: str | None) -> str:
    cfg = SOURCES[source]
    template = cfg["url"]
    if source == "simple-icons":
        color_part = f"/{color}" if color else ""
        return template.format(slug=name, color=color_part)
    v = variant or DEFAULTS.get(source, {}).get("variant", "")
    return template.format(name=name, variant=v)


def download_svg(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "ui-alchemy-fetch-svg/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read(MAX_SVG_BYTES + 1)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} for {url}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"network error for {url}: {exc.reason}") from exc
    if len(data) > MAX_SVG_BYTES:
        raise RuntimeError(f"response too large ({len(data)} bytes) for {url}")
    text = data.decode("utf-8", errors="replace").lstrip("\ufeff \t\r\n")
    if not text.lower().startswith("<svg"):
        raise RuntimeError(f"response is not an SVG: {url}")
    return text.encode("utf-8")


def write_manifest(manifest_path: Path, entry: dict) -> None:
    entries: list[dict] = []
    if manifest_path.exists():
        try:
            loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
            entries = loaded if isinstance(loaded, list) else loaded.get("assets", [])
        except (json.JSONDecodeError, OSError):
            entries = []
    entries.append(entry)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps({"assets": entries}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def selftest() -> int:
    validate_slug("github", "simple-icons")
    validate_slug("academic-cap", "heroicons")
    for bad in ("../etc", "a/b", "a b", "UPPER", ""):
        try:
            validate_slug(bad, "simple-icons")
        except ValueError:
            pass
        else:
            raise AssertionError(f"slug should be rejected: {bad!r}")
    assert url_for("simple-icons", "github", None, None) == "https://cdn.simpleicons.org/github"
    assert url_for("simple-icons", "github", None, "181717") == "https://cdn.simpleicons.org/github/181717"
    assert url_for("tabler", "heart", "outline", None) == "https://cdn.jsdelivr.net/npm/@tabler/icons@latest/icons/heart.svg"
    assert url_for("phosphor", "palette", "bold", None) == "https://cdn.jsdelivr.net/npm/@phosphor-icons/core@latest/assets/bold/palette.svg"
    assert url_for("heroicons", "academic-cap", None, None) == "https://cdn.jsdelivr.net/npm/heroicons@latest/24/outline/academic-cap.svg"
    assert url_for("remix", "heart-line", None, None) == "https://cdn.jsdelivr.net/npm/remixicon@latest/icons/heart-line.svg"
    print("selftest OK: slug validation and source URLs correct")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", choices=sorted(SOURCES), help="icon library")
    parser.add_argument("--name", help="icon slug/name inside the library")
    parser.add_argument("--variant", help="library variant (phosphor weight, heroicons outline/solid, tabler outline/filled)")
    parser.add_argument("--color", help="hex color without '#' (simple-icons only)")
    parser.add_argument("--out", default="assets/icons", help="output directory (default: assets/icons)")
    parser.add_argument("--manifest", help="path to assets/manifest.json to append")
    parser.add_argument("--alt", help="accessibility alt text for the icon")
    parser.add_argument("--purpose", help="where the icon is used (nav, empty state, social proof...)")
    parser.add_argument("--selftest", action="store_true", help="run offline assertions")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    if not args.source or not args.name:
        parser.error("--source and --name are required (or use --selftest)")

    try:
        validate_slug(args.name, args.source)
        if args.source == "simple-icons" and args.color and not re.fullmatch(r"[0-9a-fA-F]{3,6}", args.color):
            parser.error("--color must be a hex value without '#' (e.g. 181717)")
        url = url_for(args.source, args.name, args.variant, args.color)
        data = download_svg(url)
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{args.source}-{args.name}.svg"
        target = out_dir / filename
        target.write_bytes(data)
    except (ValueError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    entry = {
        "file": str(target),
        "source": args.source,
        "license": SOURCES[args.source]["license"],
        "url": url,
        "name": args.name,
        "variant": args.variant,
        "alt": args.alt or "",
        "purpose": args.purpose or "",
        "downloaded_at": datetime.now(timezone.utc).isoformat(),
    }
    if args.manifest:
        write_manifest(Path(args.manifest), entry)
    print(f"OK {target} ({len(data)} bytes) license={entry['license']}")
    print(f"manifest={args.manifest or 'not written'} alt={entry['alt'] or '(add alt text)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
