#!/bin/bash
d=/var/backups/vmA
t=$(date +%F_%H%M)
umask 077
if rsync -a -e "ssh -i /root/.ssh/sync_ed25519 -o BatchMode=yes" \
  ubuntu@192.168.1.225:/var/www/html/ /tmp/www-$t/ \
  && tar -czf $d/www-$t.tar.gz -C /tmp/www-$t .; then
  echo "$(date -Is) SUCCESS $t" >> /var/log/www-backup.log
else
  echo "$(date -Is) FAILURE $t" >> /var/log/www-backup.log
  rm -f $d/www-$t.tar.gz
fi
rm -rf /tmp/www-$t
ls -1t $d/www-*.tar.gz | tail -n +25 | xargs -r rm --