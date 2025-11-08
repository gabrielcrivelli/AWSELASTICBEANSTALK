#!/bin/bash
ENDPOINT="${1:-localhost:8000}"
curl -f http://$ENDPOINT/api/health || exit 1
echo "✅ Health check OK"
