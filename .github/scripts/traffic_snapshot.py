#!/usr/bin/env python3
"""Snapshot GitHub traffic data into dated CSVs.

GitHub retains only a rolling 14 days of traffic data and exposes no lifetime
total. This appends each day's numbers to CSVs so the history survives.

Rows are keyed by date and the newest reading wins, because the current day's
count is still climbing when we read it. Every run re-reads the whole 14-day
window, so a few failed runs in a row cost nothing.

Usage: traffic_snapshot.py <data-dir>
Env:   GH_TOKEN (needs push access), GH_REPO (owner/name)
"""

import csv
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

API = "https://api.github.com"


def get(path):
    token, repo = os.environ["GH_TOKEN"], os.environ["GH_REPO"]
    req = urllib.request.Request(
        f"{API}/repos/{repo}{path}",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "traffic-snapshot",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as err:
        if err.code in (403, 404):
            sys.exit(
                f"HTTP {err.code} on {path}.\n"
                "The traffic API requires push access, and the default GITHUB_TOKEN\n"
                "is frequently rejected on these endpoints. Add a TRAFFIC_TOKEN secret:\n"
                "  classic PAT with 'repo' scope, or\n"
                "  fine-grained PAT with Administration: read-only on this repo."
            )
        sys.exit(f"HTTP {err.code} on {path}: {err.read().decode()[:300]}")


def merge(path, keys, fields, rows):
    """Upsert rows into a CSV, newest reading wins for a given key."""
    merged = {}
    if os.path.exists(path):
        with open(path, newline="") as f:
            for row in csv.DictReader(f):
                merged[tuple(row[k] for k in keys)] = row
    for row in rows:
        merged[tuple(str(row[k]) for k in keys)] = row
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for key in sorted(merged):
            writer.writerow(merged[key])
    return merged


def timeseries(payload, count_field, unique_field):
    return [
        {
            "date": item["timestamp"][:10],
            count_field: item["count"],
            unique_field: item["uniques"],
        }
        for item in payload.get("clones", payload.get("views", []))
    ]


def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    os.makedirs(data_dir, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    clones = merge(
        os.path.join(data_dir, "clones.csv"),
        ["date"],
        ["date", "clones", "unique_cloners"],
        timeseries(get("/traffic/clones"), "clones", "unique_cloners"),
    )
    views = merge(
        os.path.join(data_dir, "views.csv"),
        ["date"],
        ["date", "views", "unique_visitors"],
        timeseries(get("/traffic/views"), "views", "unique_visitors"),
    )

    # Referrers and paths are point-in-time snapshots with no dates of their
    # own, so we stamp them with the collection date and keep the series.
    merge(
        os.path.join(data_dir, "referrers.csv"),
        ["date", "referrer"],
        ["date", "referrer", "views", "unique_visitors"],
        [
            {
                "date": today,
                "referrer": r["referrer"],
                "views": r["count"],
                "unique_visitors": r["uniques"],
            }
            for r in get("/traffic/popular/referrers")
        ],
    )
    merge(
        os.path.join(data_dir, "paths.csv"),
        ["date", "path"],
        ["date", "path", "views", "unique_visitors"],
        [
            {
                "date": today,
                "path": p["path"],
                "views": p["count"],
                "unique_visitors": p["uniques"],
            }
            for p in get("/traffic/popular/paths")
        ],
    )

    write_summary(data_dir, clones, views, today)


def write_summary(data_dir, clones, views, today):
    total_clones = sum(int(r["clones"]) for r in clones.values())
    total_views = sum(int(r["views"]) for r in views.values())
    # Daily uniques cannot be summed into a distinct-people count: one person
    # cloning on three days is counted three times. Treat it as an upper bound.
    upper_cloners = sum(int(r["unique_cloners"]) for r in clones.values())
    upper_visitors = sum(int(r["unique_visitors"]) for r in views.values())
    days = sorted(set(clones) | set(views))
    span = f"{days[0][0]} to {days[-1][0]}" if days else "no data yet"

    with open(os.path.join(data_dir, "SUMMARY.md"), "w") as f:
        f.write(
            f"""# Traffic totals

Collected daily from the GitHub traffic API, which only retains 14 days.
Covering **{span}** ({len(days)} days). Last updated {today}.

| Metric | Lifetime |
|---|---|
| Clones | {total_clones} |
| Views | {total_views} |
| Unique cloners (upper bound) | {upper_cloners} |
| Unique visitors (upper bound) | {upper_visitors} |

The unique figures are a sum of daily uniques, so someone who clones on three
separate days is counted three times. They are a ceiling on distinct people,
not a headcount. The clone and view totals are exact.

Raw data: `clones.csv`, `views.csv`, `referrers.csv`, `paths.csv`.

Not captured by any GitHub metric: "Download ZIP" from the Code button.
"""
        )


if __name__ == "__main__":
    main()
