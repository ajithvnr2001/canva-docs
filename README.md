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
crawl_canva.py         # full crawl (sitemap seeds + link discovery, resume-safe)
update_incremental.py  # daily: new + lastmod-stale + sitemap-missing rotation
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
  **new** sitemap URLs, **lastmod-stale** pages (sitemap timestamp newer than our
  verification), and **sitemap-missing** pages (`/docs/extensions/**` and legacy
  app API pages are not in `sitemap.xml`) oldest-first, up to 300 per run.
- Writes are content-aware: if a refreshed page's Markdown is unchanged, the page and
  its metadata are left untouched (only `_verified.json` advances), so daily runs do
  not churn the mirror.
- **VM unit** `canva-crawl.service` handles the initial/resume crawl; `boot.sh` is wired
  into `/data/opencode/boot-all.sh` so a reboot or reprovision restarts it automatically.
  After completion the unit stays installed but disabled (`docs/_manifest.json` `done`).

## Results (verified 2026-10-21)

- **982 pages** crawled end to end in **274.7 s** with **0 failures**
  (973 via Scrapling, 8 via Crawl4AI JS fallback, 1 via httpx)
- 771 in-scope sitemap URLs plus 213 link-discovered pages (211 retained after
  dropping two interactive Storybook SPA shells)
- ~23 MB Markdown mirror with 982 per-page metadata records
- Sections: Apps SDK + REST API reference, Admin API, Audit Logs, Button (JS/HTML/Android/iOS),
  Print partnerships, SCIM, Extensions, Flourish Charts, Agents/Connect
