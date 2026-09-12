#!/usr/bin/env python3
"""Fetch an allowlisted, public-only GitHub telemetry snapshot for the profile.

The output is intentionally narrow: repository metadata, the latest commit on the
default branch, and the latest release when one exists. Private repositories are
never discovered or serialized because the input repository list is an explicit
public allowlist in data/projects.json.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "data" / "projects.json"
OUTPUT_PATH = ROOT / "data" / "github-state.json"
API = "https://api.github.com"
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "Dossiya-SE")
TOKEN = os.environ.get("GITHUB_TOKEN")


def request_json(path: str, *, allow_404: bool = False):
    request = urllib.request.Request(f"{API}{path}")
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    request.add_header("User-Agent", "Dossiya-SE-living-profile")
    if TOKEN:
        request.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        raise RuntimeError(f"GitHub API request failed ({exc.code}): {path}") from exc


def latest_commit(repository: str, default_branch: str) -> dict[str, object] | None:
    encoded_branch = urllib.parse.quote(default_branch, safe="")
    commits = request_json(
        f"/repos/{OWNER}/{repository}/commits?sha={encoded_branch}&per_page=1"
    )
    if not commits:
        return None
    commit = commits[0]
    details = commit.get("commit", {})
    committer = details.get("committer") or details.get("author") or {}
    message = str(details.get("message", "")).splitlines()[0]
    return {
        "sha": str(commit.get("sha", ""))[:12],
        "date": committer.get("date"),
        "message": message[:160],
    }


def latest_release(repository: str) -> dict[str, object] | None:
    release = request_json(
        f"/repos/{OWNER}/{repository}/releases/latest", allow_404=True
    )
    if not release:
        return None
    return {
        "tag": release.get("tag_name"),
        "name": release.get("name"),
        "published_at": release.get("published_at"),
        "url": release.get("html_url"),
    }


def snapshot_repository(project: dict[str, object]) -> dict[str, object]:
    repository = str(project["repository"])
    metadata = request_json(f"/repos/{OWNER}/{repository}")
    if metadata.get("private") or metadata.get("visibility") != "public":
        raise RuntimeError(f"refusing to publish non-public repository: {repository}")
    default_branch = str(metadata.get("default_branch") or "main")
    return {
        "repository": repository,
        "display_name": project["name"],
        "research_role": project["research_role"],
        "status": project["status"],
        "url": metadata.get("html_url"),
        "language": metadata.get("language"),
        "default_branch": default_branch,
        "archived": bool(metadata.get("archived")),
        "stars": int(metadata.get("stargazers_count", 0)),
        "forks": int(metadata.get("forks_count", 0)),
        "open_issues": int(metadata.get("open_issues_count", 0)),
        "updated_at": metadata.get("updated_at"),
        "pushed_at": metadata.get("pushed_at"),
        "latest_commit": latest_commit(repository, default_branch),
        "latest_release": latest_release(repository),
    }


def stable_payload(payload: dict[str, object]) -> dict[str, object]:
    return {k: v for k, v in payload.items() if k != "generated_at"}


def main() -> int:
    projects_doc = json.loads(PROJECTS_PATH.read_text(encoding="utf-8"))
    if projects_doc.get("public_only") is not True:
        raise RuntimeError("projects.json must explicitly require public_only=true")

    projects = projects_doc.get("projects", [])
    repositories = [snapshot_repository(project) for project in projects]
    repositories.sort(
        key=lambda repo: str(repo.get("pushed_at") or repo.get("updated_at") or ""),
        reverse=True,
    )

    payload: dict[str, object] = {
        "schema_version": "1.0",
        "source": "GitHub REST API",
        "evidence_state": "OBSERVED_PUBLIC_REPOSITORY_METADATA",
        "status": "live",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "repositories": repositories,
    }

    if OUTPUT_PATH.exists():
        old = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stable_payload(old) == stable_payload(payload):
            print("GitHub telemetry unchanged; preserving existing snapshot timestamp.")
            return 0

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote public GitHub telemetry for {len(repositories)} repositories.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, RuntimeError, urllib.error.URLError) as exc:
        print(f"GITHUB TELEMETRY: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
