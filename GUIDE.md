# Canva Docs — Operations Guide

## Initial / resumed crawl

```bash
systemctl status canva-crawl            # active while crawling
tail -f /data/opencode/canva/crawl.log  # journal may buffer; this is the log
python3 crawl_canva.py --concurrency 10 # manual run (resumes)
```

The crawler seeds from `https://www.canva.dev/sitemap.xml` (771 in-scope URLs), then follows
in-scope links. Output goes to `docs/`; per-page metadata to `docs/_meta/`.

Completion check:

```bash
python3 -c "import json; m=json.load(open('docs/_manifest.json')); print(m['visited'], m['failed'], m.get('done'))"
```

`done: true` means every in-scope sitemap page was visited with zero failures.

## Daily update lanes

`update_incremental.py` (Actions, 09:45 UTC) processes:

1. **new** — sitemap URLs not indexed yet;
2. **lastmod-stale** — sitemap `<lastmod>` newer than `docs/_verified.json`;
3. **sitemap-missing** — indexed pages absent from `sitemap.xml` (the whole
   `/docs/extensions/**` tree + ~100 app API pages), oldest verification first,
   capped at 300/run.

Unchanged pages are not rewritten (no frontmatter churn); only `_verified.json`
advances. Use `--check-only` to preview, `--limit N` for a smoke test,
`--force URL` for one page.

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
