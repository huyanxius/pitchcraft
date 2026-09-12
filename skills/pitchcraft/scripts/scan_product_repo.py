#!/usr/bin/env python3
"""Create a read-only product, evidence, asset, and visual-token inventory."""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import subprocess
import tempfile
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".git", ".next", ".nuxt", ".parcel-cache", ".pytest_cache", ".venv",
    "build", "coverage", "dist", "generated", "jobs", "library", "logs",
    "node_modules", "out", "target", "temp", "vendor", "__pycache__",
}
DOC_NAMES = {
    "agents.md", "handoff.md", "tasks.md", "readme.md", "contributing.md",
    "architecture.md", "product.md", "prd.md", "pitch.md", "roadmap.md",
    "changelog.md", "license", "license.md",
}
DOC_HINTS = ("pitch", "roadshow", "competition", "product", "architecture", "workflow", "design", "brand")
ASSET_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".avif", ".mp4", ".mov"}
STYLE_EXTS = {".css", ".scss", ".sass", ".less", ".tsx", ".ts", ".jsx", ".js", ".json", ".html"}
HEX_RE = re.compile(r"(?<![\w-])#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![0-9a-fA-F])")
CSS_VAR_RE = re.compile(r"(--[a-zA-Z0-9_-]+)\s*:\s*([^;}{]{1,120})")
FONT_RE = re.compile(r"font-family\s*:\s*([^;}{]{1,160})", re.IGNORECASE)
SECRET_NAME_RE = re.compile(r"(^|[._-])(env|secret|credential|token|api[-_]?key)([._-]|$)", re.IGNORECASE)


def is_github_url(value: str) -> bool:
    return bool(re.match(r"^(?:https://|git@)github\.com[/:]", value))


def github_clone_spec(source: str) -> tuple[str, int | None]:
    match = re.match(
        r"^https://github\.com/([^/]+)/([^/]+?)(?:\.git)?(?:/pull/(\d+))?/?$",
        source,
    )
    if not match:
        return source, None
    owner, repo, pull_number = match.groups()
    return f"https://github.com/{owner}/{repo}.git", int(pull_number) if pull_number else None


def resolve_source(source: str) -> tuple[Path, tempfile.TemporaryDirectory[str] | None]:
    path = Path(source).expanduser()
    if path.exists():
        return path.resolve(), None
    if not is_github_url(source):
        raise SystemExit(f"Source is neither an existing path nor a GitHub URL: {source}")
    clone_url, pull_number = github_clone_spec(source)
    temp = tempfile.TemporaryDirectory(prefix="competition-roadshow-")
    clone_dir = Path(temp.name) / "repo"
    command = ["git", "clone", "--depth", "1", "--filter=blob:limit=20m", clone_url, str(clone_dir)]
    result = subprocess.run(command, text=True, capture_output=True)
    if result.returncode != 0:
        temp.cleanup()
        raise SystemExit("Unable to clone the repository. Use an authenticated local checkout for private repositories.\n" + result.stderr.strip())
    if pull_number is not None:
        ref = f"pull/{pull_number}/head"
        branch = f"roadshow-pr-{pull_number}"
        fetch = subprocess.run(
            ["git", "-C", str(clone_dir), "fetch", "--depth", "1", "origin", f"{ref}:{branch}"],
            text=True,
            capture_output=True,
        )
        checkout = subprocess.run(
            ["git", "-C", str(clone_dir), "checkout", branch],
            text=True,
            capture_output=True,
        ) if fetch.returncode == 0 else fetch
        if fetch.returncode != 0 or checkout.returncode != 0:
            temp.cleanup()
            detail = fetch.stderr.strip() or checkout.stderr.strip()
            raise SystemExit(f"Unable to fetch GitHub PR #{pull_number}.\n{detail}")
    return clone_dir, temp


def walk_files(root: Path, max_files: int) -> Iterable[Path]:
    count = 0
    for current, dirs, files in os.walk(root):
        current_path = Path(current)
        if current_path != root and ".git" in files:
            # A nested Git worktree/repository needs its own explicit scan. Mixing it
            # into the parent would pollute both product truth and visual tokens.
            dirs[:] = []
            continue
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith(".cache"))
        for name in sorted(files):
            path = Path(current) / name
            rel = path.relative_to(root)
            if SECRET_NAME_RE.search(name) or path.is_symlink():
                continue
            try:
                if path.stat().st_size > 20 * 1024 * 1024:
                    continue
            except OSError:
                continue
            yield rel
            count += 1
            if count >= max_files:
                return


def read_text(path: Path, limit: int = 500_000) -> str:
    try:
        data = path.read_bytes()[:limit]
        return data.decode("utf-8", errors="ignore")
    except OSError:
        return ""


def rank_doc(rel: Path) -> tuple[int, int, str]:
    lower = rel.name.lower()
    direct = 0 if lower in DOC_NAMES else 1
    hinted = 0 if any(h in str(rel).lower() for h in DOC_HINTS) else 1
    return direct, hinted, str(rel)


def is_style_candidate(rel: Path) -> bool:
    suffix = rel.suffix.lower()
    if suffix not in STYLE_EXTS:
        return False
    if suffix != ".json":
        return True
    lower = str(rel).lower()
    return any(hint in lower for hint in ("theme", "token", "tailwind", "design", "style", "manifest"))


def git_summary(root: Path) -> dict[str, str | list[str]]:
    def run(*args: str) -> str:
        result = subprocess.run(["git", "-C", str(root), *args], text=True, capture_output=True)
        return result.stdout.strip() if result.returncode == 0 else ""

    remotes = [line for line in run("remote", "-v").splitlines() if "(fetch)" in line]
    return {
        "branch": run("branch", "--show-current"),
        "commit": run("rev-parse", "--short", "HEAD"),
        "latest_commit": run("log", "-1", "--format=%cs %h %s"),
        "remotes": remotes,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", help="Local repository path or GitHub URL")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument("--max-files", type=int, default=25_000)
    args = parser.parse_args()

    root, temp = resolve_source(args.source)
    try:
        files = list(walk_files(root, args.max_files))
        docs = sorted(
            [p for p in files if p.suffix.lower() == ".md" or p.name.lower() in DOC_NAMES],
            key=rank_doc,
        )[:120]
        assets = [p for p in files if p.suffix.lower() in ASSET_EXTS]
        style_files = [p for p in files if is_style_candidate(p)]

        colors: collections.Counter[str] = collections.Counter()
        fonts: collections.Counter[str] = collections.Counter()
        css_vars: collections.Counter[str] = collections.Counter()
        scanned_style_files = 0
        for rel in style_files[:1500]:
            full = root / rel
            text = read_text(full)
            if not text:
                continue
            scanned_style_files += 1
            colors.update(value.upper() for value in HEX_RE.findall(text))
            fonts.update(value.strip().strip('"\'') for value in FONT_RE.findall(text))
            css_vars.update(f"{name}: {value.strip()}" for name, value in CSS_VAR_RE.findall(text))

        asset_groups = collections.Counter(p.suffix.lower() for p in assets)
        top_dirs = collections.Counter((p.parts[0] if len(p.parts) > 1 else ".") for p in files)
        payload = {
            "source": args.source,
            "resolved_root": str(root) if temp is None else "temporary shallow clone",
            "git": git_summary(root),
            "counts": {
                "files_scanned": len(files),
                "documents_found": len(docs),
                "assets_found": len(assets),
                "style_files_scanned": scanned_style_files,
            },
            "top_level_distribution": top_dirs.most_common(30),
            "documents": [str(p) for p in docs],
            "assets": [str(p) for p in assets[:500]],
            "asset_types": asset_groups.most_common(),
            "visual_tokens": {
                "colors": colors.most_common(40),
                "font_families": fonts.most_common(30),
                "css_variables": css_vars.most_common(80),
            },
            "warnings": [
                "This is an inventory, not a final product or visual judgment.",
                "Review AGENTS/HANDOFF/TASKS and separate current product truth from legacy or livedemo material.",
                "Secret-like filenames, symlinks, dependency folders, build outputs, and files over 20 MB were skipped.",
            ],
        }

        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "repo_scan.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        lines = [
            "# Repository Scan",
            "",
            f"- Source: `{payload['source']}`",
            f"- Resolved root: `{payload['resolved_root']}`",
            f"- Branch: `{payload['git']['branch']}`",
            f"- Commit: `{payload['git']['commit']}`",
            f"- Files scanned: {len(files)}",
            f"- Documents found: {len(docs)}",
            f"- Assets found: {len(assets)}",
            "",
            "## Candidate product documents",
            *[f"- `{p}`" for p in docs[:60]],
            "",
            "## Candidate visual assets",
            *[f"- `{p}`" for p in assets[:120]],
            "",
            "## Frequent color tokens",
            *[f"- `{token}` — {count}" for token, count in colors.most_common(30)],
            "",
            "## Frequent font-family declarations",
            *[f"- `{token}` — {count}" for token, count in fonts.most_common(20)],
            "",
            "## Candidate CSS variables",
            *[f"- `{token}` — {count}" for token, count in css_vars.most_common(40)],
            "",
            "## Warnings",
            *[f"- {warning}" for warning in payload["warnings"]],
        ]
        (args.out / "repo_scan.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"repo_scan_json={args.out / 'repo_scan.json'}")
        print(f"repo_scan_markdown={args.out / 'repo_scan.md'}")
        print(f"files_scanned={len(files)}")
        print(f"assets_found={len(assets)}")
        print(f"colors_found={len(colors)}")
    finally:
        if temp is not None:
            temp.cleanup()


if __name__ == "__main__":
    main()
