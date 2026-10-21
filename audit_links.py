#!/usr/bin/env python3
"""Link-domain audit for the Canva mirror.

Answers "is anything under www.canva.dev missing?" independently of the crawler:

  1. scans every local Markdown page for internal canva.dev URLs
  2. diffs them against docs/_index.jsonl
  3. for each referenced-but-unmirrored URL, checks live HTTP:
       - redirect (301/302/307/308)  -> alias; target must already be mirrored
       - 200 direct                 -> LIVE GAP (exit code 1)
       - 404/other                  -> dead link (reported)

With --write it refreshes docs/_redirects.json (alias URL -> canonical URL), the
accounting record of the site's redirect surface.

Usage:
  python3 audit_links.py
  python3 audit_links.py --write
"""
import argparse, json, re, sys
from pathlib import Path

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent))
import crawl_canva as C

DOCS = C.OUT_ROOT
PAT = re.compile(r'https?://(?:www\.)?canva\.dev/[^\s)\]"\'<>]+')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="refresh docs/_redirects.json with alias -> canonical map")
    a = ap.parse_args()

    idx = {json.loads(l)["url"] for l in open(DOCS / "_index.jsonl") if l.strip()}
    links, files = set(), 0
    for p in DOCS.rglob("*.md"):
        if p.name.startswith("_"):
            continue
        files += 1
        for m in PAT.findall(p.read_text(errors="replace")):
            n = C.normalize_url(m.rstrip(".,;:`"))
            if n:
                links.add(n)

    missing = sorted(links - idx)
    aliases, live, dead = {}, [], []
    with httpx.Client(follow_redirects=True, timeout=25,
                      headers={"User-Agent": "Mozilla/5.0"}) as c:
        for u in missing:
            try:
                r = c.get(u)
            except Exception as e:
                dead.append((u, f"ERR {str(e)[:60]}")); continue
            eff = str(r.url)
            if eff.rstrip("/") != u.rstrip("/"):
                tgt = C.normalize_url(eff)
                if r.status_code == 200 and tgt and tgt in idx:
                    aliases[u] = tgt
                elif r.status_code == 200:
                    live.append((u, f"redirects to unmirrored {eff}"))
                else:
                    dead.append((u, f"redirect -> HTTP {r.status_code}"))
            elif r.status_code == 200:
                live.append((u, "200 direct"))
            else:
                dead.append((u, f"HTTP {r.status_code}"))

    print(f"scanned {files} files | referenced internal URLs: {len(links)} | mirrored: {len(idx)}")
    print(f"referenced-but-unmirrored: {len(missing)} "
          f"-> aliases {len(aliases)}, live gaps {len(live)}, dead {len(dead)}")
    for u, why in live[:20]:
        print(f"  LIVE GAP: {u} ({why})")
    for u, why in dead[:20]:
        print(f"  dead: {u} ({why})")

    if a.write and aliases:
        out = DOCS / "_redirects.json"
        prev = {}
        if out.exists():
            try:
                prev = json.loads(out.read_text())
            except Exception:
                prev = {}
        prev.update(aliases)
        out.write_text(json.dumps(prev, indent=1, sort_keys=True))
        print(f"wrote {out} ({len(prev)} aliases)")

    sys.exit(1 if live else 0)


if __name__ == "__main__":
    main()
