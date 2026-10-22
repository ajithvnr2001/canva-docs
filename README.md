# Canva.dev — Full-Site End-to-End Crawler

Crawls **https://www.canva.dev/** end to end into clean Markdown — developer docs **and**
the rest of the site:

- **Developer docs** (`/docs/…`): Apps SDK + REST API reference, Admin API, Audit Logs,
  Button (JS/HTML/Android/iOS), Connect, SCIM, Extensions, **Print API**
- **Blog** (`/blog/…`): Canva Developers Blog (38 posts), Canva Engineering Blog
  (217 pages incl. 145 tag archives), and `/blog/subscribe`
- **Flourish Charts** (`/opensource/flourish-charts/…`, 80 pages)
- **Solutions** (`/solutions/…`, 4 pages), **Agents** (`/agents/`), **CLI** auth pages
  (`/cli/…`), **Print partnerships** (`/docs/print-partnerships/…`)

**Last verified: 2026-10-22**

## Scope & exceptions

Every page under `www.canva.dev` is in scope, including `/blog/` and `/docs/print/`
(the latter is listed in `robots.txt` but included here for a complete-site mirror).

Skipped as non-pages, duplicate representations, or unavailable:

- raw `*.md` / `llms.txt` exports, `/sources/*` OpenAPI YAML, `/example-assets/*`,
  `/_next/*`, and static assets
- interactive `/storybook/` demos and storybook/playroom `iframe.html` fragments
  (SPA shells with no textual docs)
- error routes `/404`, `/500`, `/_error`, `/_app`
- `/solutions/ai/` and `/solutions/autofill/` (Cloudflare Access sign-in shells, no
  public content)
- 10 stale build-manifest routes that return HTTP 404 (7 docs section-index aliases,
  2 removed engineering posts, 1 empty OAuth redirect stub). These are exact-match
  exclusions, so valid child pages (e.g. `/audit-events/list-audit-events/`) are
  still crawled.

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
docs/                  # Markdown mirror of the site root
docs/_meta/            # per-page fetch metadata (lastmod comparisons)
docs/_index.jsonl      # URL → file index
docs/_verified.json    # URL → last verification time (drives stale/rotation)
docs/_manifest.json    # crawl stats / done flag
canva-crawl.service    # VM unit to run/resume the crawl in the background
boot.sh                # reinstall + resume after VM reboot/reallocation
```

`docs/` mirrors the site root. The site's `/docs/` subtree is flattened
(`/docs/apps/x/` → `docs/apps/x.md`), while other sections keep their site path
(`/blog/…` → `docs/blog/…`, `/opensource/…` → `docs/opensource/…`,
`/solutions/…` → `docs/solutions/…`). The site root `/` redirects to `/docs/`, so it
maps to `docs/_index.md` with no duplicate homepage.

## Run

```bash
pip install -r requirements.txt
python3 -m playwright install chromium
python3 crawl_canva.py --concurrency 10          # resume by re-running
python3 update_incremental.py --check-only       # what would the daily run fetch?
python3 update_incremental.py --concurrency 10   # new + stale refresh
python3 audit_links.py                           # completeness audit (exit 1 on a live gap)
python3 audit_links.py --write                   # also refresh docs/_redirects.json
```

Crash-safe: every page is written immediately (`docs/…md` + `docs/_meta/…json`) and
`crawl_state.json` checkpoints progress; re-running skips finished pages.

## Automation

- **GitHub Actions** `.github/workflows/update-docs.yml` runs daily at **09:45 UTC**
  (workflow_dispatch too). Each run refreshes four lanes:
  **new** sitemap/build-manifest URLs, **lastmod-stale** pages (sitemap timestamp newer
  than our verification), **no-lastmod / not-in-inventory** pages oldest-first up to
  300 per run (current pool: 271), and **linked** — internal URLs referenced by
  mirrored pages but missing from both inventories; redirect aliases are recorded in
  `docs/_redirects.json` and their live 200 targets are fetched as new pages.
- A final **link-domain audit** step (`audit_links.py`) fails the run only if a live
  page is unmirrored, so gaps cannot stay silent.
- The **whole-site Next.js build manifest** (`_buildManifest.js`, keyed by the live
  buildId) is the authoritative route inventory. In addition, 33 pages are reachable
  only through the link graph beyond both the sitemap and manifest (Apps SDK API
  type pages, migration pages, etc.) and are kept in the rotation pool.
- Writes are content-aware: if a refreshed page's Markdown is unchanged, the page and
  its metadata are left untouched (only `_verified.json` advances), so daily runs do
  not churn the mirror.
- **VM unit** `canva-crawl.service` handles the initial/resume crawl; `boot.sh` is wired
  into `/data/opencode/boot-all.sh` so a reboot or reprovision restarts it automatically.
  After completion the unit stays installed but disabled (`docs/_manifest.json` `done`).

## URL accounting (2026-10-21)

Every URL under `www.canva.dev` is accounted for:

- **1,319 mirrored pages** (canonical URLs, 0 fetch failures)
- **57 healthy redirect aliases** recorded in `docs/_redirects.json`
  (legacy paths such as `/docs/apps/examples/x/` → `/docs/apps/feature-examples/x/`)
- **1 stale alias** redirecting to a 404 (site-side broken link:
  `/docs/apps/examples/multiple-intents/`)
- Excluded by design: 10 stale build-manifest routes returning 404, 2 Cloudflare-Access
  pages, and non-page/duplicate representations (see Scope & exceptions)

Independent checks, all clean at the same time: sitemap **1,048/1,048**, whole-site
build manifest **1,141/1,141**, `llms.txt` route inventories (**626** canonical URLs),
section-hub link graph, full-mirror link sweep (**1,377** internal URLs → 0 live gaps),
and search-engine / Common Crawl spot checks (only redirect aliases surfaced).
Re-run anytime: `python3 audit_links.py`.

## Results (verified 2026-10-22)

- **1,319 pages** in the mirror with **0 failures**
  (1,317 via Scrapling, 2 via Crawl4AI JS fallback)
- Coverage verified against two independent inventories: **1,048/1,048** sitemap URLs
  and **1,141/1,141** whole-site Next.js build-manifest routes, **0 missing**
- 33 pages found only by link discovery (beyond sitemap + manifest)
- 271-page no-lastmod rotation pool (all sitemap URLs carry `lastmod`)
- 28 MB Markdown mirror with 1,319 per-page metadata records
- Sections: 975 docs pages (incl. 16 Print API), 257 blog pages (38 Developers,
  217 Engineering incl. 145 tag archives, index + subscribe), 80 Flourish Charts,
  4 solutions, 2 CLI, 1 agents landing
