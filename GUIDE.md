# Canva Docs — Operations Guide

## Initial / resumed crawl

```bash
systemctl status canva-crawl            # active while crawling
tail -f /data/opencode/canva/crawl.log  # journal may buffer; this is the log
python3 crawl_canva.py --concurrency 10 # manual run (resumes)
```

The crawler seeds from `https://www.canva.dev/sitemap.xml` **and** the live Next.js
`_buildManifest.js` (771 sitemap + 926 manifest routes → 1,008 unique seeds), then follows
in-scope links (20 more pages). Output goes to `docs/`; per-page metadata to `docs/_meta/`.

Completion check:

```bash
python3 -c "import json; m=json.load(open('docs/_manifest.json')); print(m['visited'], m['failed'], m.get('done'))"
```

`done: true` means every in-scope sitemap page was visited with zero failures.

## Daily update lanes

`update_incremental.py` (Actions, 09:45 UTC) processes:

1. **new** — sitemap or build-manifest URLs not indexed yet;
2. **lastmod-stale** — sitemap `<lastmod>` newer than `docs/_verified.json`;
3. **no-lastmod** — indexed pages without a sitemap timestamp (the whole
   `/docs/extensions/**` tree, Preview API, type-declaration pages, legacy app API
   pages), oldest verification first, capped at 300/run.

The build manifest (`_buildManifest.js`, fetched with the live buildId) is the
authoritative route inventory and catches pages missing from both the sitemap and the
static link graph. `--check-only` previews, `--limit N` smoke-tests, `--force URL`
refetches one page.

## Daily updates

GitHub Actions handles it (`.github/workflows/update-docs.yml`, 09:45 UTC):

```bash
gh workflow run daily-docs-update -R ajithvnr2001/canva-docs
```

Or locally:

```bash
python3 update_incremental.py --check-only   # new + stale counts
python3 update_incremental.py --concurrency 10
```

`_last_verified.json` and the README date are stamped on every update run.

## Reboot / reprovision

- Same disk: `@reboot` cron runs `/data/opencode/boot-all.sh` → `canva/boot.sh` reinstalls
  `canva-crawl.service` and resumes if `done` is not true.
- Full reprovision: run `bash /data/opencode/boot-all.sh` once (cloud-init custom-data not set
  on this VM), then the normal timers/units are restored.

## Push path

- VM: `./vm-ship.sh ajithvnr2001/canva-docs docs/ README.md`
- Actions: commits `docs/ README.md` directly.
