#!/usr/bin/env python3
"""Refresh public evidence for the living GitHub profile.

Only repositories explicitly allowlisted in data/projects.json are queried. The
collector never enumerates the account, never serializes private repositories,
and fails closed if an allowlisted repository is not public.
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
OUTPUT_PATH = ROOT / "data" / "public-github-state.json"
API = "https://api.github.com"
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "Dossiya-SE")
TOKEN = os.environ.get("GITHUB_TOKEN")


def request_json(path: str, *, allow_404: bool = False):
    req = urllib.request.Request(f"{API}{path}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "Dossiya-SE-living-research-profile")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        raise RuntimeError(f"GitHub API request failed ({exc.code}): {path}") from exc


def latest_commit(repository: str, default_branch: str) -> dict[str, object] | None:
    branch = urllib.parse.quote(default_branch, safe="")
    commits = request_json(f"/repos/{OWNER}/{repository}/commits?sha={branch}&per_page=1")
    if not commits:
        return None
    item = commits[0]
    details = item.get("commit", {})
    actor = details.get("committer") or details.get("author") or {}
    return {
        "sha": str(item.get("sha", ""))[:12],
        "date": actor.get("date"),
        "message": str(details.get("message", "")).splitlines()[0][:160],
    }


def latest_release(repository: str) -> dict[str, object] | None:
    release = request_json(f"/repos/{OWNER}/{repository}/releases/latest", allow_404=True)
    if not release:
        return None
    return {
        "tag": release.get("tag_name"),
        "name": release.get("name"),
        "published_at": release.get("published_at"),
        "url": release.get("html_url"),
    }


def snapshot(project: dict[str, object]) -> dict[str, object]:
    repository = str(project["repository"])
    metadata = request_json(f"/repos/{OWNER}/{repository}")
    visibility = str(metadata.get("visibility") or "")
    if metadata.get("private") or visibility != "public":
        raise RuntimeError(f"refusing to publish non-public repository: {repository}")

    default_branch = str(metadata.get("default_branch") or "main")
    return {
        "repository": repository,
        "display_name": project["name"],
        "short_name": project["short_name"],
        "research_role": project["research_role"],
        "status": project["status"],
        "featured": bool(project.get("featured", False)),
        "profile_order": int(project["profile_order"]),
        "url": metadata.get("html_url"),
        "visibility": visibility,
        "language": metadata.get("language"),
        "default_branch": default_branch,
        "archived": bool(metadata.get("archived")),
        "updated_at": metadata.get("updated_at"),
        "pushed_at": metadata.get("pushed_at"),
        "latest_commit": latest_commit(repository, default_branch),
        "latest_release": latest_release(repository),
    }


def stable_payload(payload: dict[str, object]) -> dict[str, object]:
    return {key: value for key, value in payload.items() if key != "generated_at"}


def main() -> int:
    projects_doc = json.loads(PROJECTS_PATH.read_text(encoding="utf-8"))
    if projects_doc.get("public_only") is not True:
        raise RuntimeError("data/projects.json must set public_only=true")
    if projects_doc.get("owner") != OWNER:
        raise RuntimeError("project allowlist owner does not match workflow owner")

    projects = projects_doc.get("projects")
    if not isinstance(projects, list) or not projects:
        raise RuntimeError("public repository allowlist is empty")

    repositories = [snapshot(project) for project in projects]
    repositories.sort(key=lambda item: int(item["profile_order"]))

    payload: dict[str, object] = {
        "schema_version": "2.0",
        "source": "GitHub REST API",
        "allowlist_source": "data/projects.json",
        "evidence_state": "OBSERVED_PUBLIC_REPOSITORY_METADATA",
        "status": "live",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "observation_scope": "Allowlisted public repository metadata, latest default-branch commit, and latest public release when available.",
        "repositories": repositories,
    }

    if OUTPUT_PATH.exists():
        previous = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stable_payload(previous) == stable_payload(payload):
            print("Public GitHub evidence unchanged; preserving the previous observation timestamp.")
            return 0

    OUTPUT_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Observed {len(repositories)} allowlisted public research repositories.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyError, TypeError, ValueError, RuntimeError, urllib.error.URLError) as exc:
        print(f"PUBLIC PROFILE EVIDENCE: FAIL — {exc}", file=sys.stderr)
        raise SystemExit(1)
