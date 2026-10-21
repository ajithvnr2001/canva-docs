#!/usr/bin/env python3
"""Incremental update for the whole www.canva.dev site (docs + blog + all sections).

Three refresh lanes:
  1. NEW      - live sitemap/build-manifest URL not indexed yet
  2. STALE    - sitemap <lastmod> newer than our last verification
  3. MISSING  - indexed pages with no sitemap lastmod or absent from the live union
                (current rotation pool: 271 pages), refreshed oldest-first up to ROTATION_CAP

Content-aware: a refreshed page is only rewritten when its Markdown body actually
changed, so unchanged confirmations don't create 200-file commits. Verification
timestamps live in docs/_verified.json (committed, so GitHub Actions is stateless).

Usage:
  python3 update_incremental.py --check-only
  python3 update_incremental.py
  python3 update_incremental.py --limit 5            # smoke test
  python3 update_incremental.py --force URL          # refetch one page
"""
import argparse, json, os, re, pathlib, asyncio, sys
from datetime import datetime, timezone
from urllib.parse import urlparse, urljoin, urldefrag
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import crawl_canva as C

DOCS = C.OUT_ROOT
STATE = C.STATE_FILE
VERIFIED = DOCS / "_verified.json"
REFRESH_CAP = 1000   # max lastmod-stale refetches per run (newest first)
ROTATION_CAP = 300   # max no-lastmod / not-in-inventory pages re-verified per run (oldest first)

FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n\n?", re.S)

def iso(s):
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except Exception:
        return None

def body_of(text):
    m = FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text

async def live_sitemaps():
    import httpx, xml.etree.ElementTree as ET
    urls, lastmod = set(), {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        r = await c.get(C.SITEMAP_URL, timeout=30)
        r.raise_for_status()
        text = r.text
    try:
        root = ET.fromstring(text)
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for el in root.findall("s:url", ns):
            loc = el.find("s:loc", ns)
            if loc is None or not loc.text:
                continue
            n = C.normalize_url(loc.text)
            if not n:
                continue
            urls.add(n)
            lm = el.find("s:lastmod", ns)
            if lm is not None and lm.text:
                lastmod[n] = lm.text.strip()
    except Exception as e:
        print(f"[sitemap] ET parse failed ({e}); regex fallback")
        for u, d in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>(?:\s*<lastmod>\s*([^<]+?)\s*</lastmod>)?", text, re.S):
            n = C.normalize_url(u)
            if n:
                urls.add(n)
                if d:
                    lastmod[n] = d
    return {"docs": sorted(urls)}, lastmod

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--force", default=None)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=10)
    a = ap.parse_args()

    idx = [json.loads(l) for l in open(DOCS / "_index.jsonl")] if (DOCS / "_index.jsonl").exists() else []
    by_url = {r["url"]: r for r in idx}
    verified = {}
    if VERIFIED.exists():
        try:
            verified = json.loads(VERIFIED.read_text())
        except Exception as e:
            print(f"[verified] unreadable, rebuilding: {e}")
    # backfill verification times from page metadata on first run after upgrade
    for mfile in (DOCS / "_meta").rglob("*.json"):
        try:
            m = json.loads(mfile.read_text())
        except Exception:
            continue
        u, fa = m.get("url"), m.get("fetched_at")
        if u and fa and u not in verified:
            verified[u] = fa

    live, lastmod = await live_sitemaps()
    sitemap_urls = set(live["docs"])
    manifest_urls = set(await C.load_build_manifest_urls())
    live_urls = sitemap_urls | manifest_urls
    print(f"sitemap in-scope={len(sitemap_urls)} | build-manifest={len(manifest_urls)} | "
          f"live-union={len(live_urls)} | indexed={len(by_url)} | verified-known={len(verified)}")

    # 1) new — in sitemap or build manifest, not indexed yet
    new = sorted(live_urls - set(by_url))
    # 2) stale by sitemap lastmod
    stale = []
    for u in by_url:
        lm, va = lastmod.get(u), verified.get(u)
        lmd, vad = iso(lm) if lm else None, iso(va) if va else None
        if lmd and vad and lmd > vad:
            stale.append((lmd, u))
    stale.sort(reverse=True)
    refresh = [u for _, u in stale[:REFRESH_CAP]]
    # 3) pages with no sitemap lastmod (extensions, Preview API, type declarations,
    #    plus anything absent from both sources) — oldest verification first
    pool = [u for u in by_url if u not in lastmod or u not in live_urls]
    pool.sort(key=lambda u: verified.get(u, ""))
    rotate = [u for u in pool if u not in set(new)][:ROTATION_CAP]

    print(f"new={len(new)} stale={len(stale)} (refresh {len(refresh)}) | "
          f"no-lastmod pool={len(pool)} (rotate {len(rotate)})")
    for u in new[:20]:
        print(f"  NEW: {u}")
    for _, u in stale[:10]:
        print(f"  STALE: {u}")

    targets = [a.force] if a.force else new + refresh + rotate
    if a.limit:
        targets = targets[:a.limit]

    if not a.check_only:
        now = datetime.now(timezone.utc)
        stamp = {"date": now.strftime("%F"), "at": now.isoformat(),
                 "new": len(new), "stale_total": len(stale), "refreshed_stale": len(refresh),
                 "manifest_urls": len(manifest_urls), "no_lastmod_pool": len(pool),
                 "rotated": len(rotate), "targets": len(targets), "total_index": len(by_url)}
        (DOCS / "_last_verified.json").write_text(json.dumps(stamp, indent=2))
        try:
            mp = DOCS / "_manifest.json"
            m = json.loads(mp.read_text()) if mp.exists() else {}
            m["last_verified"] = stamp["date"]
            m["generated_at"] = stamp["at"]
            mp.write_text(json.dumps(m, indent=2))
        except Exception as e:
            print("stamp manifest skip:", e)
        try:  # keep README verification date fresh
            rp = C.REPO_ROOT / "README.md"
            if rp.exists():
                t = rp.read_text()
                t2 = re.sub(r"Last verified: \d{4}-\d{2}-\d{2}", f"Last verified: {stamp['date']}", t)
                t2 = re.sub(r"## Results \(verified \d{4}-\d{2}-\d{2}\)", f"## Results (verified {stamp['date']})", t2)
                if t2 != t:
                    rp.write_text(t2)
                    print(f"readme date -> {stamp['date']}")
        except Exception as e:
            print("readme stamp skip:", e)
        print(f"stamped {stamp['date']} | targets={len(targets)}")

    if a.check_only:
        print("check-only — nothing fetched")
        return
    if not targets:
        print("no targets — up to date")
        return

    print(f"fetching {len(targets)} docs...")
    st = json.load(open(STATE)) if STATE.exists() else {"visited": {}, "failed": {}}
    vs, failed = st.get("visited", {}), st.get("failed", {})
    lines = [json.loads(l) for l in open(DOCS / "_index.jsonl")] if (DOCS / "_index.jsonl").exists() else []
    # de-dupe index, keep last occurrence
    seen, ded = set(), []
    for r in reversed(lines):
        if r["url"] not in seen:
            seen.add(r["url"]); ded.append(r)
    lines = list(reversed(ded))
    pos = {r["url"]: i for i, r in enumerate(lines)}

    sem = asyncio.Semaphore(a.concurrency)
    ok = fail = changed = same = 0

    async def one(url):
        nonlocal ok, fail, changed, same
        async with sem:
            try:
                data = await C.fetch_one(url)
                verbatim = datetime.now(timezone.utc).isoformat()
                rel = C.url_to_relpath(url)
                fp = DOCS / rel
                mr = pathlib.Path("_meta") / rel.with_suffix(".json")
                old_body = None
                if fp.exists():
                    try:
                        old_body = body_of(fp.read_text(encoding="utf-8"))
                    except Exception:
                        old_body = None
                old_method = ""
                try:
                    if (DOCS / mr).exists():
                        old_method = json.loads((DOCS / mr).read_text()).get("method", "") or ""
                except Exception:
                    pass
                if old_body is not None and old_body.strip() == data["markdown"].strip():
                    verified[url] = verbatim
                    vs[url] = vs.get(url, {"file": str(rel), "title": data["title"], "method": data["method"]})
                    same += 1
                    ok += 1
                    print(f"[same] {url}")
                    return
                # never replace a JS-rendered page with a much thinner last-resort fetch
                if (old_body is not None and data["method"].startswith("httpx")
                        and old_method and not old_method.startswith("httpx")
                        and len(old_body.strip()) > 400
                        and len(data["markdown"].strip()) < len(old_body.strip()) * 0.8):
                    verified[url] = verbatim
                    vs[url] = vs.get(url, {"file": str(rel), "title": data["title"], "method": old_method})
                    same += 1
                    ok += 1
                    print(f"[skip-downgrade] {url} (httpx {len(data['markdown'].strip())}B vs {len(old_body.strip())}B)")
                    return
                fp.parent.mkdir(parents=True, exist_ok=True)
                fm = (f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\n"
                      f"method: {data['method']}\nfetched_at: {verbatim}\n---\n\n")
                fp.write_text(fm + data["markdown"], encoding="utf-8")
                (DOCS / mr).parent.mkdir(parents=True, exist_ok=True)
                meta = {"url": url, "file": str(rel), "title": data["title"],
                        "method": data["method"], "fetched_at": verbatim}
                if data.get("fallback"):
                    meta["fallback"] = data["fallback"]
                (DOCS / mr).write_text(json.dumps(meta, indent=2))
                vs[url] = {"file": str(rel), "title": data["title"], "method": data["method"]}
                row = {"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}
                if url in pos:
                    lines[pos[url]] = row
                    print(f"[changed] {url}")
                else:
                    pos[url] = len(lines); lines.append(row)
                    print(f"[new] {url}")
                verified[url] = verbatim
                changed += 1
                ok += 1
            except Exception as e:
                failed[url] = str(e)[:300]
                fail += 1
                print(f"[fail] {url}: {e}")

    await asyncio.gather(*(one(u) for u in targets))
    # only keep verification entries for indexed pages
    all_urls = {r["url"] for r in lines}
    verified = {u: verified[u] for u in all_urls if u in verified}
    (DOCS / "_index.jsonl").write_text("".join(json.dumps(r) + "\n" for r in lines))
    VERIFIED.write_text(json.dumps(verified, indent=1, sort_keys=True))
    try:
        if C._crawler is not None:
            await C._crawler.close()
    except Exception:
        pass
    open(STATE, "w").write(json.dumps({"visited": vs, "failed": failed}))
    print(f"done: fetched={ok} changed={changed} unchanged={same} fail={fail}")

if __name__ == "__main__":
    asyncio.run(main())
