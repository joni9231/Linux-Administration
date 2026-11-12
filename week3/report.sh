#!/bin/bash

set -euo pipefail

disk_status() {
  local usage="${1%\%}"
  if [ $usage -ge 80 ]; then
    echo "Warning"
  else
    echo "OK"
  fi

}

##Variables
OUT_DIR="/var/www/html/week3/"
TEMPLATE="/home/ubuntu/viikko3/template.html"
GITHUB_URL="https://github.com/joni9231/Linux-Administration/tree/main/week3"

GENERATED_AT=$(date '+%Y-%m-%d %H:%M:%S %Z')
UPTIME_TEXT=$(uptime -p)
DISK_USAGE=$(df -P / | awk 'NR == 2 {print $5}')
DISK_STATUS=$(disk_status "$DISK_USAGE")
MEM_TOTAL=$(free -m | awk '/^Mem:/ {print $2}')
MEM_AVAILABLE=$(free -m | awk '/^Mem:/ {print $7}')


export GENERATED_AT UPTIME_TEXT DISK_STATUS DISK_USAGE MEM_TOTAL MEM_AVAILABLE GITHUB_URL

TMP=$(mktemp "$OUT_DIR/.index.XXXXXX")
envsubst '$GENERATED_AT $UPTIME_TEXT $DISK_STATUS $DISK_USAGE $MEM_TOTAL $MEM_AVAILABLE $GITHUB_URL' < "$TEMPLATE" > "$TMP"
chmod 644 "$TMP"
mv "$TMP" "$OUT_DIR/index.html"