#!/usr/bin/env bash
# Usage: ./scripts/smoke_test.sh http://localhost:8000
# Used after a deploy to confirm the app is actually alive.
set -euo pipefail
URL="${1:?Usage: smoke_test.sh <base-url>}"
for i in {1..10}; do
  if curl -fsS "$URL/health" | grep -q '"status":"ok"'; then
    echo "Smoke test passed"; exit 0
  fi
  echo "Attempt $i failed, retrying..."; sleep 3
done
echo "Smoke test FAILED"; exit 1
