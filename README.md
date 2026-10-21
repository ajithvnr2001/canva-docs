# Canva Developer Docs — End-to-End Crawler

Crawls **https://www.canva.dev/docs/** end to end (all documented surfaces) into clean Markdown:

- **Apps SDK** (`/docs/apps/…` incl. REST API reference, MCP, UI Kit, design guidelines)
- **Admin API** (`/docs/admin/…`)
- **Audit Logs** (`/docs/audit-logs/…`)
- **Button** (`/docs/button/…` — JS/HTML/Android/iOS)
- **Print partnerships** (`/docs/print-partnerships/…`)
- **SCIM** (`/docs/scim/…`) and in-doc reference domains
- **Flourish Charts** (`/opensource/flourish-charts/…`), plus `/agents/`, `/developers/`, `/connect/`

Scope is robots-aware: `/docs/print/*`, `/blog/*`, `/example-assets/*`, raw `*.md`/`llms.txt`
exports, storybook/playroom iframes and interactive `/storybook/` demos (SPA shells with
no textual docs) are excluded.

**Last verified: 2026-10-21**

## Stack

Same fallback ladder as the other corpora:

1. **Scrapling** `Fetcher` — primary static fetch
2. **Crawl4AI** `AsyncWebCrawler` — JS/browser fallback (75 s watchdog)
3. **ScrapeGraphAI** `convert_to_md` / `cleanup_html` — HTML → clean Markdown
4. **httpx** — last-resort static fetch

## Layout

```
crawl_canva.py         # full crawl (sitemap + Next.js build manifest + link discovery)
update_incremental.py  # daily: new, lastmod-stale, and no-lastmod rotation
docs/                  # Markdown mirror (site /docs/ prefix stripped)
docs/_meta/            # per-page fetch metadata (lastmod comparisons)
docs/_index.jsonl      # URL → file index
docs/_verified.json    # URL → last verification time (drives stale/rotation)
docs/_manifest.json    # crawl stats / done flag
canva-crawl.service    # VM unit to run/resume the crawl in the background
boot.sh                # reinstall + resume after VM reboot/reallocation
```

## Run

```bash
pip install -r requirements.txt
python3 -m playwright install chromium
python3 crawl_canva.py --concurrency 10          # resume by re-running
python3 update_incremental.py --check-only       # what would the daily run fetch?
python3 update_incremental.py --concurrency 10   # new + stale refresh
```

Crash-safe: every page is written immediately (`docs/…md` + `docs/_meta/…json`) and
`crawl_state.json` checkpoints progress; re-running skips finished pages.

## Automation

- **GitHub Actions** `.github/workflows/update-docs.yml` runs daily at **09:45 UTC**
  (workflow_dispatch too). Each run refreshes three lanes:
  **new** sitemap/build-manifest URLs, **lastmod-stale** pages (sitemap timestamp newer
  than our verification), and **no-lastmod** pages (`/docs/extensions/**`, Preview API,
  type-declaration pages, and anything absent from `sitemap.xml`) oldest-first, up to
  300 per run.
- The **Next.js build manifest** (`_buildManifest.js`, keyed by the live buildId) is used
  as an authoritative route inventory: it catches pages that are absent from both
  `sitemap.xml` and the static link graph (46 such pages found on 2026-10-21).
- Writes are content-aware: if a refreshed page's Markdown is unchanged, the page and
  its metadata are left untouched (only `_verified.json` advances), so daily runs do
  not churn the mirror.
- **VM unit** `canva-crawl.service` handles the initial/resume crawl; `boot.sh` is wired
  into `/data/opencode/boot-all.sh` so a reboot or reprovision restarts it automatically.
  After completion the unit stays installed but disabled (`docs/_manifest.json` `done`).

## Results (verified 2026-10-21)

- **1,028 pages** in the mirror with **0 failures**
  (1,019 via Scrapling, 8 via Crawl4AI JS fallback, 1 via httpx)
- Coverage verified against two independent inventories: **771/771** sitemap URLs and
  **926/926** Next.js build-manifest routes, **0 missing**
- 211 pages found by link discovery; **46 more** found only via the build manifest
  (Preview API reference, TypeScript type declarations, Java/Spark SDK pages)
- 16 Print API pages excluded because `robots.txt` disallows `/docs/print/*`;
  blog, example assets and interactive Storybook shells are out of scope
- ~23 MB Markdown mirror with 1,028 per-page metadata records
- Sections: Apps SDK + REST API reference, Admin API, Audit Logs, Button (JS/HTML/Android/iOS),
  Print partnerships, SCIM, Extensions, Flourish Charts, Agents/Connect
