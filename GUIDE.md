# Canva.dev Full-Site — Operations Guide

## Initial / resumed crawl

```bash
systemctl status canva-crawl            # active while crawling
tail -f /data/opencode/canva/crawl.log  # journal may buffer; this is the log
python3 crawl_canva.py --concurrency 10 # manual run (resumes)
```

The crawler seeds from `https://www.canva.dev/sitemap.xml` **and** the live whole-site
Next.js `_buildManifest.js` (1,048 sitemap + 1,141 manifest routes → 1,286 unique
seeds), then follows in-scope links beyond both (33 more pages, e.g. Apps SDK API type
pages). Output goes to `docs/`; per-page metadata to `docs/_meta/`.

Completion check:

```bash
python3 -c "import json; m=json.load(open('docs/_manifest.json')); print(m['visited'], m['failed'], m.get('done'))"
```

`done: true` means every live sitemap/build-manifest route was visited with zero
failures (the stale-404 and Cloudflare-Access routes exact-excluded in `README.md`).

## Daily update lanes

`update_incremental.py` (Actions, 09:45 UTC) processes:

1. **new** — live sitemap or whole-site build-manifest URLs not indexed yet;
2. **lastmod-stale** — sitemap `<lastmod>` newer than `docs/_verified.json`;
3. **no-lastmod / not-in-inventory** — indexed pages without a sitemap timestamp or
   absent from the live union (current pool: 271, e.g. type-declaration pages and
   link-only pages), oldest verification first, capped at 300/run;
4. **linked** — internal URLs referenced by mirrored pages but missing from the index
   and both inventories; healthy redirect aliases go to `docs/_redirects.json`, their
   live 200 targets are fetched as new pages (self-healing gap lane).

The build manifest (`_buildManifest.js`, fetched with the live buildId) is the
authoritative whole-site route inventory and catches pages missing from both the
sitemap and the static link graph. `--check-only` previews, `--limit N` smoke-tests,
`--force URL` refetches one page.

Completeness audit (also a CI step; exits 1 only on a live unmirrored page):

```bash
python3 audit_links.py          # sitemap + manifest + llms.txt + link sweep
python3 audit_links.py --write  # refresh docs/_redirects.json
```

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
