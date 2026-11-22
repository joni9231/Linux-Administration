# Linux administration week 4. (Backups and replication)

## Summary
Server B stores hourly backups of server A, And a real time replication of the visitor counter on server A.

## Servers
- Server A: http://195.148.21.248/week2/
- Server B: http://128.214.252.207/week4/

## Contents
- 'week4.py' The read-only app that runs on server B
- 'backup_script.sh' The backup script that archives the contents of server A to server B
- 'b_crontab.txt' Cron config that runs the backup script hourly on server B
- 'mysql_config.cnf's Are the database configs of the respective servers


