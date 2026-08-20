#!/usr/bin/env python3
"""UI Alchemy pre-flight scanner.

# ui-alchemy: ignore-all  (this file intentionally contains the banned patterns as scan targets)

Deterministic, dependency-free checks for the most common AI-design tells.
Runs over HTML/JSX/TSX/CSS/SCSS/Markdown source and reports findings per file.

Usage:
    python preflight_check.py <path> [--platform h5|miniapp|app]  # scan a file or directory
    python preflight_check.py <path> --json     # machine-readable output
    python preflight_check.py --selftest        # run inline assertions

Hard violations (em-dash, h-screen, scroll listener, div onClick, missing alt,
pure black/white, transition: all) set the exit code to 1. Soft findings
(Inter default, eyebrow density, un-sized images, en-dash separators) are
advisory: an explicit override comment or a documented brand rule wins.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path


SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", ".nuxt", ".output", "coverage", "vendor"}
SKIP_FILES = {"design-tokens.json"}
TEXT_EXTENSIONS = {
    ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".css", ".scss", ".sass",
    ".less", ".vue", ".svelte", ".astro", ".md", ".mdx", ".json", ".json5",
    ".wxml", ".wxss", ".wxs", ".axml", ".acss",
    ".kt", ".kts", ".ets",
}


@dataclass
class Finding:
    rule: str
    severity: str  # "hard" | "soft"
    message: str
    line: int = 0


@dataclass
class FileResult:
    path: str
    findings: list[Finding] = field(default_factory=list)


EM_DASH_RE = re.compile(r"\u2014")
EN_DASH_RE = re.compile(r"\u2013")
PURE_BLACK_RE = re.compile(r"#000000\b|#000\b", re.IGNORECASE)
PURE_WHITE_RE = re.compile(r"#ffffff\b|#fff\b", re.IGNORECASE)
H_SCREEN_RE = re.compile(r"\bh-screen\b")
TRANSITION_ALL_RE = re.compile(r"transition:\s*all\b|transition-all\b")
SCROLL_LISTENER_RE = re.compile(r'window\.addEventListener\(\s*["\']scroll["\']')
DIV_ONCLICK_RE = re.compile(r"<div\b[^>]*\bon(Click|MouseEnter|MouseDown|KeyDown|DoubleClick)\s*=", re.IGNORECASE)
WHITE_ON_WHITE_1 = re.compile(r'class=["\'][^"\']*bg-white[^"\']*text-white', re.IGNORECASE)
WHITE_ON_WHITE_2 = re.compile(r'class=["\'][^"\']*text-white[^"\']*bg-white', re.IGNORECASE)
INTER_FONT_RE = re.compile(r"font-family\s*:\s*['\"]?Inter\b", re.IGNORECASE)
INTER_CLASS_RE = re.compile(r"\bfont-inter\b", re.IGNORECASE)
IMG_NO_ALT_RE = re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.IGNORECASE)
IMG_NO_DIMENSIONS_RE = re.compile(r"<img\b(?![^>]*\b(?:width|height)\s*=)[^>]*>", re.IGNORECASE)
EYEBROW_RE = re.compile(r"\btracking-widest\b|\btracking-\[0\.(?:1[0-9]|2[0-9])\]|text-\[1[012]px\]\s+uppercase", re.IGNORECASE)
OVERRIDE_RE = re.compile(r"ui-alchemy:? ?(?:ignore-all|ignore|disable)(?:\s|$)|preflight-(?:ignore-all|ignore|disable)(?:\s|$)", re.IGNORECASE)
VIEWPORT_RE = re.compile(r"<meta\b[^>]*name\s*=\s*[\"']viewport[\"']", re.IGNORECASE)
ZOOM_LOCK_RE = re.compile(r"user-scalable\s*=\s*[\"']?no[\"']?|maximum-scale\s*=\s*[\"']?1(?:\.0)?[\"']?", re.IGNORECASE)
MINIAPP_IMAGE_MODE_RE = re.compile(r"<image\b(?![^>]*\bmode\s*=)[^>]*>", re.IGNORECASE)
MINIAPP_VIEW_TAP_RE = re.compile(r"<view\b[^>]*\bbind(?::)?tap\s*=", re.IGNORECASE)


def iter_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix.lower() in TEXT_EXTENSIONS and path.name not in SKIP_FILES else []
    files: list[Path] = []
    for p in sorted(path.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(path)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if p.name in SKIP_FILES:
            continue
        if p.suffix.lower() in TEXT_EXTENSIONS:
            files.append(p)
    return files


def has_override(text: str, line: int) -> bool:
    lines = text.splitlines()
    if any(OVERRIDE_RE.search(l) and "ignore-all" in l for l in lines):
        return True
    window = lines[max(0, line - 2) : line + 1]
    return any(OVERRIDE_RE.search(l) for l in window)


def match_lines(text: str, pattern: re.Pattern[str]) -> list[int]:
    """1-based line numbers of every match."""
    out: list[int] = []
    for i, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            out.append(i)
    return out


def scan_text(text: str, rel_path: str, platform: str = "auto") -> FileResult:
    result = FileResult(path=rel_path)
    full = text
    lines = text.splitlines()
    suffix = Path(rel_path).suffix.lower()
    ignore_all = any(OVERRIDE_RE.search(l) and "ignore-all" in l for l in lines)
    if ignore_all:
        return result

    for lineno, line in enumerate(lines, start=1):
        overridden = has_override(text, lineno)
        if EM_DASH_RE.search(line):
            result.findings.append(Finding("em-dash", "hard", "Em-dash found; use a period, comma, parentheses, or hyphen. This is the #1 AI tell.", lineno))
        if EN_DASH_RE.search(line) and not overridden:
            result.findings.append(Finding("en-dash-separator", "soft", "En-dash used as a separator; date/number ranges use a hyphen.", lineno))
        if PURE_BLACK_RE.search(line) and not overridden:
            result.findings.append(Finding("pure-black", "hard", "Pure #000000 found; use an off-black tint (e.g. zinc-950).", lineno))
        if PURE_WHITE_RE.search(line) and not overridden:
            result.findings.append(Finding("pure-white", "hard", "Pure #ffffff found; use an off-white tint with depth.", lineno))
        if H_SCREEN_RE.search(line) and not overridden:
            result.findings.append(Finding("h-screen", "hard", "h-screen causes mobile viewport jump; use min-h-[100dvh].", lineno))
        if TRANSITION_ALL_RE.search(line) and not overridden:
            result.findings.append(Finding("transition-all", "hard", "transition: all / transition-all animates layout properties; name exact properties.", lineno))
        if SCROLL_LISTENER_RE.search(line) and not overridden:
            result.findings.append(Finding("scroll-listener", "hard", "window scroll listener is jank-prone; use Motion useScroll / GSAP ScrollTrigger / IntersectionObserver / CSS scroll-driven animations.", lineno))
        if DIV_ONCLICK_RE.search(line) and not overridden:
            result.findings.append(Finding("div-onclick", "hard", "Click handler on <div> loses focus/keyboard/semantics; use a <button> or an accessible primitive.", lineno))
        if (WHITE_ON_WHITE_1.search(line) or WHITE_ON_WHITE_2.search(line)) and not overridden:
            result.findings.append(Finding("invisible-button", "hard", "bg-white + text-white on the same element; CTA text must contrast (WCAG AA).", lineno))
        if IMG_NO_ALT_RE.search(line) and not overridden:
            result.findings.append(Finding("missing-alt", "hard", "<img> without alt text; provide alt or alt=\"\" for decorative images.", lineno))

    if platform in ("auto", "h5") and suffix in (".html", ".htm"):
        if not VIEWPORT_RE.search(full):
            result.findings.append(Finding("viewport-missing", "hard", "No viewport meta; mobile H5 must declare width=device-width, initial-scale=1, viewport-fit=cover.", 1))
        zoom_lines = match_lines(full, ZOOM_LOCK_RE)
        if zoom_lines and not all(has_override(text, ln) for ln in zoom_lines):
            result.findings.append(Finding("zoom-disabled", "hard", "user-scalable=no / maximum-scale=1 disables zoom and breaks accessibility; remove it.", zoom_lines[0]))

    if platform in ("auto", "miniapp") and suffix == ".wxml":
        img_lines = match_lines(full, MINIAPP_IMAGE_MODE_RE)
        if img_lines and not all(has_override(text, ln) for ln in img_lines):
            result.findings.append(Finding("miniapp-image-mode", "soft", f"{len(img_lines)} <image> without explicit mode; set aspectFill / widthFix / aspectFit to avoid default stretch.", img_lines[0]))
        tap_lines = match_lines(full, MINIAPP_VIEW_TAP_RE)
        if tap_lines and not all(has_override(text, ln) for ln in tap_lines):
            result.findings.append(Finding("miniapp-view-tap", "soft", f"{len(tap_lines)} <view bindtap>; prefer <button> or add hover-class + role so taps give feedback.", tap_lines[0]))

    full = text
    inter_lines = match_lines(full, INTER_FONT_RE) + match_lines(full, INTER_CLASS_RE)
    if inter_lines and not all(has_override(text, ln) for ln in inter_lines):
        first = inter_lines[0]
        result.findings.append(Finding("inter-default", "soft", "Inter used as default font; pick Geist/Outfit/Satoshi or a brand face unless the brief explicitly wants neutral.", first))

    img_lines = match_lines(full, IMG_NO_DIMENSIONS_RE)
    if img_lines and not all(has_override(text, ln) for ln in img_lines):
        imgs_no_dim = len(img_lines)
        result.findings.append(Finding("unsized-images", "soft", f"{imgs_no_dim} <img> without width/height; reserve space to keep CLS < 0.1.", 0))

    eyebrow_lines = match_lines(full, EYEBROW_RE)
    if len(eyebrow_lines) > 6 and not all(has_override(text, ln) for ln in eyebrow_lines):
        result.findings.append(Finding("eyebrow-density", "soft", f"{len(eyebrow_lines)} eyebrow micro-labels found; keep <= ceil(sectionCount / 3) across the page.", 0))

    return result


def scan(path: Path, platform: str = "auto") -> list[FileResult]:
    results: list[FileResult] = []
    for file in iter_files(path):
        try:
            text = file.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            results.append(FileResult(path=str(file), findings=[Finding("io-error", "hard", f"cannot read: {exc}")]))
            continue
        rel = str(file.relative_to(path)) if path.is_dir() else str(file)
        results.append(scan_text(text, rel, platform))
    return results


def summarize(results: list[FileResult]) -> tuple[int, int]:
    hard = sum(1 for r in results for f in r.findings if f.severity == "hard")
    soft = sum(1 for r in results for f in r.findings if f.severity == "soft")
    return hard, soft


def render_text(results: list[FileResult]) -> str:
    lines = ["UI Alchemy pre-flight scan", "=" * 40]
    for res in results:
        if not res.findings:
            continue
        lines.append(f"\n{res.path}")
        for f in res.findings:
            loc = f"line {f.line}" if f.line else "file"
            lines.append(f"  [{f.severity.upper():4}] {f.rule} ({loc}): {f.message}")
    hard, soft = summarize(results)
    lines.append(f"\n{len(results)} file(s) scanned | {hard} hard | {soft} soft")
    return "\n".join(lines)


def selftest() -> int:
    bad_html = """<!doctype html>
<html><body>
<h1>Hello \u2014 world</h1>
<div class="h-screen bg-white text-white" onClick="go()">Click</div>
<img src="x.jpg">
<style>body { background: #000000; } a { transition: all .3s; font-family: Inter; }</style>
<script>window.addEventListener('scroll', fn);</script>
</body></html>"""
    good_html = """<!doctype html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"></head><body>
<h1>Hello, world</h1>
<main class="min-h-[100dvh]">
  <button class="bg-zinc-950 text-white" onclick="go()">Continue</button>
  <img src="x.jpg" alt="Product shot" width="1200" height="800">
</main>
</body></html>"""

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "bad.html").write_text(bad_html, encoding="utf-8")
        (root / "good.html").write_text(good_html, encoding="utf-8")
        results = scan(root)
        hard, soft = summarize(results)
        by_rule = {f.rule for r in results for f in r.findings}
        expected_hard = {"em-dash", "pure-black", "h-screen", "transition-all", "scroll-listener", "div-onclick", "invisible-button", "missing-alt"}
        assert hard >= len(expected_hard), f"missing hard findings: {expected_hard - by_rule}"
        assert "inter-default" in by_rule, "Inter default should be flagged"
        # The good file must not produce hard findings.
        good = next(r for r in results if r.path.endswith("good.html"))
        assert not [f for f in good.findings if f.severity == "hard"], f"good.html should be clean: {good.findings}"
    print(f"selftest OK: {hard} hard, {soft} soft findings detected")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=None, help="files or directories to scan")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--platform", choices=["auto", "h5", "miniapp", "app"], default="auto", help="platform-specific checks (h5: viewport/zoom; miniapp: image mode/view taps; app: manual checklist only)")
    parser.add_argument("--selftest", action="store_true", help="run inline assertions")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    if not args.paths:
        parser.error("at least one path is required (or use --selftest)")

    results: list[FileResult] = []
    for raw in args.paths:
        target = Path(raw)
        if not target.exists():
            print(f"error: path not found: {target}", file=sys.stderr)
            return 2
        results.extend(scan(target, args.platform))
    hard, soft = summarize(results)
    if args.json:
        payload = {
            "scanned": len(results),
            "hard": hard,
            "soft": soft,
            "findings": [
                {"file": r.path, "rule": f.rule, "severity": f.severity, "line": f.line, "message": f.message}
                for r in results
                for f in r.findings
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_text(results))

    return 1 if hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
