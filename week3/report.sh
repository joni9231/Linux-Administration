disk_status() {
  local usage="{$1}"
  if [ $usage -gt 80 ]; then
    echo "Warning"
  else
    echo "OK"
  fi

}




#Variables
GENERATED_AT=$(date '+%Y-%m-%d %H:%M:%S %Z')
UPTIME_TEXT=$(uptime -p)
DISK_USAGE=$(df -P / | awk 'NR == 2 {print $5}')
DISK_STATUS=$(disk_status "$DISK_USAGE")
MEM_TOTAL=$(free -m | awk '/^Mem:/ {print $2}')
MEM_AVAILABLE=$(free -m | awk '/^Mem:/ {print $7}')

export GENERATED_AT UPTIME_TEXT DISK_STATUS MEM_TOTAL MEM_AVAILABLE