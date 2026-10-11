#!/usr/bin/env python
import argparse
import fnmatch
import json
import shutil
import subprocess
import sys
from datetime import datetime
from urllib.parse import quote


USERS = {
    # "UKlimowicz": "Urszula Klimowicz",
    "ewaschoen": "Ewa Schoen",
    "Kinga-cz": "Kinga Czoków",
    "kruczykm": "Mateusz Kruczyk",
    "ErnestP79": "Ernest Pisarek",
    "emiliadyrek": "Emilia Dyrek",
    "Michal-02": "Michał Strąk",
    "aawchimkow-debug": "Aleksy Maj-Pyszyński",
    # "h4rdstyler96": "Krzysztof Bednarczyk",
    "lesniewski-praca": "Łukasz Leśniewski",
    "training-jj": "Joanna Janowska",
    "johnslavik": "Bartosz Sławecki",
}


def get_latest_repo(username: str) -> dict | None:
    result = subprocess.run(
        [
            "gh",
            "api",
            f"users/{username}/repos",
            "--method",
            "GET",
            "-f",
            "type=owner",
            "-f",
            "sort=created",
            "-f",
            "direction=desc",
            "-F",
            "per_page=1",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        message = result.stderr.strip() or "GitHub API request failed"
        raise RuntimeError(message)

    repos = json.loads(result.stdout)
    return repos[0] if repos else None


def get_matching_file_urls(repo: dict, pattern: str) -> list[str]:
    branch = quote(repo["default_branch"], safe="")
    result = subprocess.run(
        [
            "gh",
            "api",
            f"repos/{repo['full_name']}/git/trees/{branch}",
            "--method",
            "GET",
            "-F",
            "recursive=1",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        message = result.stderr.strip() or "GitHub API request failed"
        raise RuntimeError(message)

    tree = json.loads(result.stdout)
    if tree.get("truncated"):
        raise RuntimeError("GitHub returned a truncated repository tree")

    patterns = [pattern]
    if pattern.startswith("**/"):
        patterns.append(pattern[3:])

    paths = sorted(
        item["path"]
        for item in tree["tree"]
        if item["type"] == "blob"
        and any(fnmatch.fnmatchcase(item["path"], glob) for glob in patterns)
    )
    return [
        f"{repo['html_url']}/blob/{branch}/{quote(path, safe='/')}" for path in paths
    ]


def format_created_at(created_at: str) -> str:
    created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    return created.astimezone().strftime("%Y-%m-%d %H:%M %Z")


def was_created_today(created_at: str) -> bool:
    created = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    return created.astimezone().date() == datetime.now().astimezone().date()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--glob",
        metavar="PATTERN",
        help="find files matching PATTERN on each repository's default branch",
    )
    args = parser.parse_args(argv)

    if shutil.which("gh") is None:
        print("Error: GitHub CLI (gh) is not installed.", file=sys.stderr)
        return 1

    rows = []
    for username, full_name in USERS.items():
        student = f"{full_name} ({username})"

        try:
            repo = get_latest_repo(username)
        except (RuntimeError, json.JSONDecodeError) as error:
            print(f"{student}: {error}", file=sys.stderr)
            rows.append((student, "", "", "", ""))
            continue

        if repo is None or not was_created_today(repo["created_at"]):
            rows.append((student, "", "", "", ""))
            continue

        glob_result = ""
        if args.glob:
            try:
                urls = get_matching_file_urls(repo, args.glob)
                glob_result = ", ".join(urls) if urls else "NOT FOUND"
            except (RuntimeError, json.JSONDecodeError, KeyError) as error:
                print(f"{student}: glob check failed: {error}", file=sys.stderr)
                glob_result = "ERROR"

        rows.append(
            (
                student,
                repo["name"],
                format_created_at(repo["created_at"]),
                repo["html_url"],
                glob_result,
            )
        )

    user_width = max([len("STUDENT (GITHUB)"), *(len(row[0]) for row in rows)])
    repo_width = max([len("REPOSITORY"), *(len(row[1]) for row in rows)])

    if args.glob:
        url_width = max([len("URL"), *(len(row[3]) for row in rows)])
        header = (
            f"{'STUDENT (GITHUB)':<{user_width}}  "
            f"{'REPOSITORY':<{repo_width}}  "
            f"{'CREATED (LOCAL)':<22}  "
            f"{'URL':<{url_width}}  GLOB RESULT"
        )
        print(header)
        print("-" * len(header))
    else:
        print(
            f"{'STUDENT (GITHUB)':<{user_width}}  "
            f"{'REPOSITORY':<{repo_width}}  "
            f"{'CREATED (LOCAL)':<22}  URL"
        )
        print("-" * (user_width + repo_width + 51))

    for student, repo_name, created_at, url, glob_result in rows:
        if args.glob:
            print(
                f"{student:<{user_width}}  "
                f"{repo_name:<{repo_width}}  "
                f"{created_at:<22}  "
                f"{url:<{url_width}}  {glob_result}"
            )
        else:
            print(
                f"{student:<{user_width}}  "
                f"{repo_name:<{repo_width}}  "
                f"{created_at:<22}  {url}"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
