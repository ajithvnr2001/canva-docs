#!/bin/bash
# boot.sh — reinstall + start the Canva docs crawler after a spot-VM reallocation.
# Lives on /data (survives). Idempotent: safe to run any time.
set -e
UNIT_SRC="/data/opencode/canva/canva-crawl.service"
if [ ! -f "$UNIT_SRC" ]; then
  echo "FATAL: $UNIT_SRC missing (/data not attached?)" >&2
  exit 1
fi
cp -f "$UNIT_SRC" /etc/systemd/system/canva-crawl.service
systemctl daemon-reload
DONE=$(python3 - <<'PY'
import json
try:
    print(json.load(open('/data/opencode/canva/docs/_manifest.json')).get('done', False))
except Exception:
    print(False)
PY
)
if [ "$DONE" = "True" ]; then
  systemctl disable canva-crawl.service >/dev/null 2>&1 || true
  echo "canva crawl complete — nothing to resume."
  exit 0
fi
systemctl enable canva-crawl.service
if systemctl is-active --quiet canva-crawl.service; then
  echo "canva-crawl.service already active."
else
  systemctl start canva-crawl.service
  echo "canva-crawl.service started."
fi
