#!/usr/bin/env python3
"""
End-to-end crawler for https://www.canva.dev/docs/ (+ all in-scope developer surfaces).

Stack (same ladder as the other corpora):
  1. Scrapling (Fetcher)             - fast static fetch (primary)
  2. Crawl4AI (AsyncWebCrawler)      - JS/browser fallback with watchdog
  3. ScrapeGraphAI (convert_to_md)   - HTML -> clean markdown
  4. httpx                           - last-resort static fetch

Scope: www.canva.dev paths /docs/, /opensource/, /agents/, /developers/, /connect/.
Robots-respecting exclusions: /docs/print/*, /example-assets/*, storybook/playroom
iframes, raw *.md and llms.txt exports, /blog/*.

Crash-safe: per-page markdown + _meta json + crawl_state.json; rerun to resume.
Output mirror: /docs/apps/api/latest/ -> docs/apps/api/latest.md (site's /docs/ prefix
is stripped so the repo's docs/ mirrors the docs root).
"""
import asyncio
import os
import re
import json
import time
import hashlib
import importlib.util
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag, unquote
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup

# ---------- paths (repo-relative so GitHub Actions runners work; override via env) ----------
REPO_ROOT = Path(__file__).resolve().parent
BASE_URL = "https://www.canva.dev"
SITEMAP_URL = "https://www.canva.dev/sitemap.xml"
OUT_ROOT = Path(os.environ.get("DOCS_OUT", str(REPO_ROOT / "docs")))
TOOLS_ROOT = Path(os.environ.get("TOOLS_DIR", str(REPO_ROOT / "tools")))
STATE_FILE = Path(os.environ.get("CRAWL_STATE", str(REPO_ROOT / "crawl_state.json")))
INDEX_FILE = OUT_ROOT / "_index.jsonl"
MANIFEST_FILE = OUT_ROOT / "_manifest.json"

OUT_ROOT.mkdir(parents=True, exist_ok=True)
(OUT_ROOT / "_meta").mkdir(exist_ok=True, parents=True)

# ---------- load ScrapeGraphAI utils directly from cloned repo (bypass broken langchain imports) ----------
def load_module_from_file(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def _resolve_sg_utils():
    cands = [
        TOOLS_ROOT / "scrapegraph-ai" / "scrapegraphai" / "utils",
        REPO_ROOT / "tools" / "scrapegraph-ai" / "scrapegraphai" / "utils",
        Path("/data/opencode/cloudflare/tools/scrapegraph-ai/scrapegraphai/utils"),
        Path("/data/opencode/gcpdocs/tools/scrapegraph-ai/scrapegraphai/utils"),
    ]
    for c in cands:
        if (c / "convert_to_md.py").exists():
            return c
    try:  # pip-installed package fallback (utils files are langchain-free)
        import scrapegraphai
        c = Path(scrapegraphai.__file__).parent / "utils"
        if (c / "convert_to_md.py").exists():
            return c
    except Exception:
        pass
    return cands[0]

SCRAPEGRAPH_UTILS = _resolve_sg_utils()
convert_to_md_mod = load_module_from_file("sg_convert_to_md", str(SCRAPEGRAPH_UTILS / "convert_to_md.py"))
cleanup_html_mod = load_module_from_file("sg_cleanup_html", str(SCRAPEGRAPH_UTILS / "cleanup_html.py"))
sg_convert_to_md = convert_to_md_mod.convert_to_md
try:
    sg_cleanup_html = cleanup_html_mod.cleanup_html
    print("[scrapegraph-ai] loaded convert_to_md + cleanup_html from", SCRAPEGRAPH_UTILS)
except Exception as e:
    sg_cleanup_html = None
    print("[scrapegraph-ai] cleanup_html unavailable:", e)

# ---------- Scrapling ----------
from scrapling import Fetcher
print("[scrapling] Fetcher loaded:", Fetcher)

# ---------- Crawl4AI (lazy, only for fallback) ----------
_crawler = None
_crawler_lock = asyncio.Lock()
_browser_sem = asyncio.Semaphore(3)   # cap concurrent browser pages

async def get_crawler():
    global _crawler
    if _crawler is None:
        async with _crawler_lock:
            if _crawler is None:
                from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode  # noqa
                from crawl4ai.async_webcrawler import BrowserConfig
                browser_cfg = BrowserConfig(headless=True, verbose=False)
                crawler = AsyncWebCrawler(config=browser_cfg)
                await crawler.start()
                _crawler = crawler
                print("[crawl4ai] AsyncWebCrawler started")
    return _crawler

def oneline(s, n=300):
    return re.sub(r"\s+", " ", str(s)).strip()[:n]

# ---------- scope ----------
MAIN_HOST = "www.canva.dev"
ALLOWED_PREFIXES = ("/docs/", "/opensource/", "/agents/", "/developers/", "/connect/")
EXCLUDED_PREFIXES = ("/docs/print/", "/blog/", "/example-assets/")
BINARY_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".css", ".js",
               ".woff", ".woff2", ".ttf", ".mp4", ".webm", ".zip", ".pdf", ".json", ".txt")

def normalize_url(u, base=BASE_URL):
    if not u:
        return None
    u = u.strip()
    if u.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    abs_u = urljoin(base, u)
    abs_u, _ = urldefrag(abs_u)
    try:
        p = urlparse(abs_u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower().split(":")[0]
    if host == "canva.dev":
        host = MAIN_HOST
    if host != MAIN_HOST:
        return None
    path = p.path or "/"
    if path == "/docs":
        path = "/docs/"
    low = path.lower()
    for ext in BINARY_EXTS:
        if low.endswith(ext):
            return None
    # robots.txt disallows: /docs/print/*, /example-assets/*, storybook/playroom iframes,
    # /*/llms.txt, /*/*.md — skip all of them.
    if "iframe.html" in low or low.endswith(".md") or low.endswith("llms.txt"):
        return None
    # interactive Storybook demos (no textual docs; SPA renders an error shell when static)
    if "/storybook/" in low or low.endswith("/storybook"):
        return None
    def _excluded(pp):
        return any(pp == x.rstrip("/") or pp.startswith(x) for x in EXCLUDED_PREFIXES)
    if _excluded(path):
        return None
    if not any(path.startswith(x) for x in ALLOWED_PREFIXES):
        return None
    # strip /index suffixes if a page links them explicitly
    if path.endswith("/index.md"):
        path = path[:-len("/index.md")] + "/"
    elif path.endswith("/index"):
        path = path[:-len("/index")] + "/"
    canon = f"https://{MAIN_HOST}{path}"
    # enforce trailing slash for extension-less directory-style URLs
    if not canon.endswith("/") and "." not in canon.rsplit("/", 1)[-1]:
        canon += "/"
    return canon

def url_to_relpath(url):
    p = urlparse(url)
    path = unquote(p.path).strip("/")
    # strip the site's /docs/ prefix: repo docs/ mirrors the docs root
    if path == "docs":
        path = ""
    elif path.startswith("docs/"):
        path = path[len("docs/"):]
    if not path:
        rel = "_index"
    else:
        parts = []
        for seg in path.split("/"):
            seg = re.sub(r'[<>:"\\|?*\x00-\x1F]', "_", seg).strip()
            if len(seg) > 120:
                seg = seg[:100] + "_" + hashlib.md5(seg.encode()).hexdigest()[:8]
            if seg in ("", ".", ".."):
                seg = "_"
            parts.append(seg)
        rel = "/".join(parts) if parts else "_index"
    return Path(rel + ".md")

def extract_main_content_html(html, base_url):
    """Strip chrome, keep the article body. Canva docs render content inside <main>."""
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg", "header", "footer", "nav", "aside"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article")
    node = main if main else soup.find("body")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    if node:
        return str(node), title
    return html, title

def scrapegraph_markdown(html, url):
    try:
        return sg_convert_to_md(html, url)
    except Exception:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)

# ---------- fetch with Scrapling (sync -> thread) ----------
def scrapling_fetch_sync(url):
    t0 = time.time()
    page = Fetcher.get(url, stealthy_headers=True, follow_redirects=True, timeout=25)
    dt = time.time() - t0
    if page.status != 200:
        raise RuntimeError(f"scrapling status {page.status}")
    html = page.html_content
    if not html or len(html) < 500:
        raise RuntimeError("scrapling empty html")
    links = []
    try:
        for a in page.css("a"):
            href = a.attrib.get("href", "")
            if href:
                links.append(href)
    except Exception:
        pass
    title = ""
    try:
        t = page.css("title::text")
        if t:
            title = str(t[0]).strip()
    except Exception:
        pass
    if not title:
        try:
            h1 = page.css("h1::text")
            if h1:
                title = str(h1[0]).strip()
        except Exception:
            pass
    try:
        txt = page.text or ""
    except Exception:
        txt = ""
    return {"html": html, "links": links, "title": title, "text_len": len(txt), "elapsed": dt}

async def crawl4ai_fetch(url):
    crawler = await get_crawler()
    from crawl4ai import CrawlerRunConfig, CacheMode
    cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        only_text=False,
        excluded_tags=["nav", "footer", "header", "aside", "script", "style"],
        wait_until="domcontentloaded",
        page_timeout=45000,
    )
    async with _browser_sem:
        res = await asyncio.wait_for(crawler.arun(url=url, config=cfg), timeout=75)
    if not res or not res.success:
        raise RuntimeError(f"crawl4ai failed: {getattr(res, 'error_message', 'unknown')}")
    html = res.html or ""
    md = res.markdown or ""
    links = []
    try:
        internal = (res.links or {}).get("internal", []) if isinstance(res.links, dict) else []
        external = (res.links or {}).get("external", []) if isinstance(res.links, dict) else []
        for l in (internal + external):
            href = l.get("href") if isinstance(l, dict) else str(l)
            if href:
                links.append(href)
    except Exception:
        pass
    title = ""
    try:
        if res.metadata and isinstance(res.metadata, dict):
            title = res.metadata.get("title", "") or ""
    except Exception:
        pass
    return {"html": html, "markdown": md, "links": links, "title": title}

async def fetch_one(url):
    """Scrapling -> Crawl4AI -> httpx. Returns markdown + links + method."""
    # 1) Scrapling + ScrapeGraphAI
    try:
        r = await asyncio.to_thread(scrapling_fetch_sync, url)
        html = r["html"]
        main_html, parsed_title = extract_main_content_html(html, url)
        title = r["title"] or parsed_title or url
        md_body = scrapegraph_markdown(main_html, url)
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + md_body
        if len(md.strip()) < 600:
            raise RuntimeError(f"scrapling thin content ({len(md)} chars), fallback to crawl4ai")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"],
                "method": "scrapling+scrapegraph"}
    except Exception as e1:
        last_err = f"scrapling: {e1}"
    # 2) Crawl4AI
    try:
        r = await crawl4ai_fetch(url)
        html = r["html"]
        md_raw = r["markdown"]
        title = r["title"]
        if not title:
            _, parsed_title = extract_main_content_html(html, url) if html else ("", "")
            title = parsed_title or url
        try:
            main_html, _ = extract_main_content_html(html, url) if html else ("", title)
            md_sg = scrapegraph_markdown(main_html, url) if main_html else ""
        except Exception:
            md_sg = ""
        md_best = md_raw if len(md_raw or "") >= len(md_sg or "") else md_sg
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + (md_best or "")
        if len(md.strip()) < 200:
            raise RuntimeError(f"crawl4ai thin content: {last_err}")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"],
                "method": "crawl4ai+scrapegraph", "fallback": oneline(last_err)}
    except Exception as e2:
        last_err2 = f"{last_err} | crawl4ai: {e2}"
    # 3) httpx
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=25, headers={"User-Agent": "Mozilla/5.0 (compatible; docs-crawler)"}) as c:
            resp = await c.get(url)
            resp.raise_for_status()
            html = resp.text
            main_html, parsed_title = extract_main_content_html(html, url)
            md_body = scrapegraph_markdown(main_html, url)
            title = parsed_title or url
            header = f"# {title}\n\n> Source: {url}\n\n"
            md = header + md_body
            soup = BeautifulSoup(html, "lxml")
            links = [a.get("href", "") for a in soup.find_all("a", href=True)]
            return {"url": url, "title": title, "html": html, "markdown": md, "links": links,
                    "method": "httpx+scrapegraph", "fallback": oneline(last_err2)}
    except Exception as e3:
        raise RuntimeError(f"all fetchers failed for {url}: {last_err2} | httpx: {e3}")

# ---------- sitemap discovery ----------
async def load_sitemap_urls():
    urls = set()
    lastmod = {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
        r = await c.get(SITEMAP_URL)
        r.raise_for_status()
        import xml.etree.ElementTree as ET
        try:
            root = ET.fromstring(r.text)
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            sitemaps = [e.find("s:loc", ns).text for e in root.findall("s:sitemap", ns) if e.find("s:loc", ns) is not None]
            texts = []
            if sitemaps:
                print(f"[sitemap] index with {len(sitemaps)} shards")
                for sm in sitemaps:
                    try:
                        rr = await c.get(sm, timeout=30)
                        rr.raise_for_status()
                        texts.append(rr.text)
                    except Exception as e:
                        print(f"[sitemap] failed {sm}: {e}")
            else:
                texts = [r.text]
            for txt in texts:
                for u, d in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>(?:\s*<lastmod>\s*([^<]+?)\s*</lastmod>)?", txt, re.S):
                    n = normalize_url(u)
                    if not n:
                        continue
                    urls.add(n)
                    if d:
                        lastmod[n] = d
            for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text):
                n = normalize_url(u)
                if n:
                    urls.add(n)
        except Exception as e:
            print(f"[sitemap] parse failed, regex fallback: {e}")
            for u in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text):
                n = normalize_url(u)
                if n:
                    urls.add(n)
    print(f"[sitemap] {len(urls)} in-scope urls")
    return sorted(urls), lastmod

async def load_build_manifest_urls():
    """Next.js build manifest = authoritative route inventory. Catches pages that are
    absent from sitemap.xml *and* from the static link graph (e.g. API type-declaration
    pages and the Preview API reference)."""
    urls = set()
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=30) as c:
            h = await c.get(BASE_URL + "/docs/", timeout=30)
            h.raise_for_status()
            m = re.search(r'"buildId":"([^"]+)"', h.text)
            if not m:
                print("[manifest] buildId not found — skipped")
                return []
            bid = m.group(1)
            r = await c.get(f"{BASE_URL}/_next/static/{bid}/_buildManifest.js", timeout=30)
            if r.status_code != 200:
                print(f"[manifest] buildManifest HTTP {r.status_code} for build {bid[:12]}")
                return []
            for route in re.findall(r'"(/[^"\\]*)"', r.text):
                if not (route.startswith("/docs/") or route in ("/docs", "/agents")):
                    continue
                n = normalize_url(BASE_URL + route)
                if n:
                    urls.add(n)
            print(f"[manifest] build {bid[:12]}… -> {len(urls)} in-scope routes")
    except Exception as e:
        print(f"[manifest] failed ({e}) — continuing with sitemap only")
    return sorted(urls)

# ---------- main crawl ----------
async def main(max_pages=10000, concurrency=10):
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    visited, failed = {}, {}
    if STATE_FILE.exists():
        try:
            st = json.loads(STATE_FILE.read_text())
            visited = st.get("visited", {})
            failed = st.get("failed", {})
            print(f"[state] resumed: {len(visited)} visited, {len(failed)} failed")
        except Exception as e:
            print(f"[state] corrupt, starting fresh: {e}")

    sitemap_urls, lastmod = await load_sitemap_urls()
    manifest_urls = await load_build_manifest_urls()
    seeds = []
    seen = set()
    for u in sitemap_urls + manifest_urls + [BASE_URL + "/docs/"]:
        if u not in seen:
            seen.add(u)
            seeds.append(u)
    print(f"[seed] sitemap={len(sitemap_urls)} manifest={len(manifest_urls)} total seeds={len(seeds)}")

    queue = asyncio.Queue()
    queued = set()
    for u in seeds:
        if u not in visited:
            queue.put_nowait((u, 0))
            queued.add(u)

    stats = {"ok": 0, "fail": 0, "skipped_existing": 0, "by_method": {}, "by_host": {}}
    stats["ok"] = 0
    idx_f = open(INDEX_FILE, "a", encoding="utf-8")
    sem = asyncio.Semaphore(concurrency)

    async def worker(wid):
        nonlocal stats
        while True:
            url, depth = await queue.get()
            try:
                if len(visited) >= max_pages and url not in visited:
                    continue
                rel = url_to_relpath(url)
                fpath = OUT_ROOT / rel
                if url in visited and fpath.exists():
                    stats["skipped_existing"] += 1
                    continue
                if fpath.exists() and fpath.stat().st_size > 500 and url not in visited:
                    visited[url] = {"file": str(rel), "skipped": True}
                    continue
                async with sem:
                    try:
                        data = await fetch_one(url)
                        now_iso = datetime.now(timezone.utc).isoformat()
                        fpath.parent.mkdir(parents=True, exist_ok=True)
                        fm = (f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\n"
                              f"method: {data['method']}\nfetched_at: {now_iso}\n---\n\n")
                        fpath.write_text(fm + data["markdown"], encoding="utf-8")
                        meta_rel = Path("_meta") / rel.with_suffix(".json")
                        meta_path = OUT_ROOT / meta_rel
                        meta_path.parent.mkdir(parents=True, exist_ok=True)
                        meta = {"url": url, "file": str(rel), "title": data["title"],
                                "method": data["method"], "fetched_at": now_iso,
                                "html_len": len(data.get("html", "")), "md_len": len(data.get("markdown", "")),
                                "depth": depth}
                        if data.get("fallback"):
                            meta["fallback"] = data["fallback"]
                        meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
                        visited[url] = {"file": str(rel), "title": data["title"], "method": data["method"],
                                        "fetched_at": now_iso}
                        idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                        if len(visited) % 20 == 0:
                            idx_f.flush()
                        stats["ok"] += 1
                        m = data["method"].split()[0]
                        stats["by_method"][m] = stats["by_method"].get(m, 0) + 1
                        host = urlparse(url).netloc
                        stats["by_host"][host] = stats["by_host"].get(host, 0) + 1
                        for href in data.get("links", []):
                            n = normalize_url(href, base=url)
                            if not n or n in visited or n in queued:
                                continue
                            nd = depth + 1
                            if nd > 8:
                                continue
                            if len(queued) + len(visited) >= max_pages:
                                break
                            queued.add(n)
                            queue.put_nowait((n, nd))
                        if stats["ok"] % 50 == 0:
                            print(f"[progress] ok={stats['ok']} fail={stats['fail']} queue={queue.qsize()} methods={stats['by_method']}")
                            STATE_FILE.write_text(json.dumps({"visited": visited, "failed": failed,
                                                              "updated": datetime.now(timezone.utc).isoformat()}))
                    except Exception as e:
                        failed[url] = str(e)[:500]
                        stats["fail"] += 1
                        print(f"[fail] {url}: {str(e)[:180]}")
            finally:
                queue.task_done()

    t0 = time.time()
    tasks = [asyncio.create_task(worker(i)) for i in range(concurrency)]
    await queue.join()          # waits until every queued + discovered page is processed
    for t in tasks:
        t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)
    idx_f.close()

    global _crawler
    if _crawler is not None:
        try:
            await _crawler.close()
        except Exception:
            pass
    STATE_FILE.write_text(json.dumps({"visited": visited, "failed": failed,
                                      "updated": datetime.now(timezone.utc).isoformat()}))
    # persist verification ledger (drives stale/rotation decisions in the updater)
    vpath = OUT_ROOT / "_verified.json"
    ver = {}
    if vpath.exists():
        try:
            ver = json.loads(vpath.read_text())
        except Exception:
            ver = {}
    for u, info in visited.items():
        fa = info.get("fetched_at") if isinstance(info, dict) else None
        if fa:
            ver[u] = fa
    ver = {u: ver[u] for u in visited if u in ver}
    vpath.write_text(json.dumps(ver, indent=1, sort_keys=True))
    done = len(failed) == 0 and len(visited) >= len(seeds)
    manifest = {
        "base": BASE_URL,
        "sitemap": SITEMAP_URL,
        "sitemap_count": len(sitemap_urls),
        "build_manifest_count": len(manifest_urls),
        "total_seeds": len(seeds),
        "visited": len(visited),
        "failed": len(failed),
        "done": done,
        "stats": stats,
        "elapsed_sec": round(time.time() - t0, 1),
        "out_root": str(OUT_ROOT),
        "tools": ["scrapling (Fetcher)", "crawl4ai (AsyncWebCrawler fallback)",
                  "scrapegraph-ai (cleanup_html/convert_to_md)", "httpx (last resort)"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    try:  # merge: preserves updater stamps (last_verified) across resume runs
        prev = json.loads(MANIFEST_FILE.read_text()) if MANIFEST_FILE.exists() else {}
        prev.update(manifest)
        manifest = prev
    except Exception as e:
        print(f"[manifest] merge skipped: {e}")
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))
    print(f"[done] visited={len(visited)} failed={len(failed)} elapsed={manifest['elapsed_sec']}s done={done}")
    print(f"[done] manifest -> {MANIFEST_FILE}")

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-pages", type=int, default=10000)
    ap.add_argument("--concurrency", type=int, default=10)
    args = ap.parse_args()
    asyncio.run(main(max_pages=args.max_pages, concurrency=args.concurrency))
