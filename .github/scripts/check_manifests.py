#!/usr/bin/env python3
"""Check the manifests for the things a broken corpus looks like.

This is deliberately not the audit. The audit lives in papers-reader and runs
over the content; this runs over the manifests alone, needs nothing but Python
and PyYAML, and exists so a bad edit to papers.yaml fails in the pull request
that made it rather than in the next pipeline run.
"""

import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]

FIELDS = {
    "theory", "algorithms", "languages", "systems",
    "networks", "databases", "architecture", "security",
    "ai-ml", "graphics", "hci", "software",
}

ACCESS = {"public-domain", "open", "permissive", "restricted", "unknown"}
STATUS = {"listed", "fetched", "extracted", "translated", "done"}
ID = re.compile(r"^[a-z][a-z0-9]*-[0-9]{4}-[a-z0-9]+$")

problems = []


def bad(where, message):
    problems.append(f"{where}: {message}")


def load(name):
    path = ROOT / "manifests" / name
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_papers():
    papers = load("papers.yaml")["papers"]
    ids, numbers = set(), {}
    for p in papers:
        pid = p.get("id", "")
        where = f"papers.yaml[{pid or '?'}]"
        if not ID.match(pid):
            bad(where, "id is not <surname>-<year>-<keyword> in lowercase ASCII")
        if pid in ids:
            bad(where, "duplicate id")
        ids.add(pid)
        for key in ("title", "authors", "year", "venue", "field", "status"):
            if not p.get(key):
                bad(where, f"missing {key}")
        if p.get("field") not in FIELDS:
            bad(where, f"field {p.get('field')!r} is not one of the twelve")
        if p.get("status") not in STATUS:
            bad(where, f"status {p.get('status')!r} is not a known status")
        if p.get("expect") and p["expect"] not in ACCESS:
            bad(where, f"expect {p['expect']!r} is not an access class")
        year = p.get("year")
        if not isinstance(year, int) or not 1930 <= year <= 2100:
            bad(where, f"year {year!r} is not plausible")
        elif pid and pid.split("-")[1] != str(year):
            bad(where, "the year in the id and the year field disagree")
        difficulty = p.get("difficulty")
        if difficulty is not None and difficulty not in (1, 2, 3, 4, 5):
            bad(where, f"difficulty {difficulty!r} is not 1 to 5")
        number = p.get("number")
        if number is not None:
            if number in numbers:
                bad(where, f"number {number} is already taken by {numbers[number]}")
            numbers[number] = pid
    for p in papers:
        for req in p.get("prerequisites", []) or []:
            if req not in ids:
                bad(f"papers.yaml[{p.get('id')}]",
                    f"prerequisite {req!r} is not a paper in this corpus")
    if numbers and sorted(numbers) != list(range(1, len(numbers) + 1)):
        bad("papers.yaml", "the numbered papers are not a run from 1")
    return ids


def check_collections(ids):
    for c in load("collections.yaml")["collections"]:
        where = f"collections.yaml[{c.get('id')}]"
        members = c.get("members")
        if isinstance(members, str):
            if members not in ("all", "all-with-number"):
                bad(where, f"members {members!r} is not all or all-with-number")
            continue
        for m in members or []:
            if m not in ids:
                bad(where, f"member {m!r} is not a paper in this corpus")


def check_sources(ids):
    for s in load("sources.yaml").get("sources") or []:
        where = f"sources.yaml[{s.get('id')}]"
        if s.get("id") not in ids:
            bad(where, "not a paper in this corpus")
        if s.get("access") not in ACCESS:
            bad(where, f"access {s.get('access')!r} is not an access class")


def check_no_pdfs():
    tracked = subprocess.run(
        ["git", "ls-files", "--", "*.pdf", "pdf/"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout.split()
    for path in tracked:
        bad(path, "a PDF is tracked in a repository that commits no PDFs")


def main():
    ids = check_papers()
    check_collections(ids)
    check_sources(ids)
    check_no_pdfs()
    if problems:
        for p in problems:
            print(p, file=sys.stderr)
        print(f"\n{len(problems)} problem(s)", file=sys.stderr)
        return 1
    print(f"manifests are consistent: {len(ids)} papers")
    return 0


if __name__ == "__main__":
    sys.exit(main())
