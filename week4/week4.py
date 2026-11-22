import os
import mysql.connector
from flask import Flask, render_template_string
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv("db.env"))

app = Flask(__name__)

DB_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE_NAME"),
}

SITE = """
<html>
<head>
<title>week 4</title>
</head>
<body style="background: linear-gradient(pink, yellow, lightgreen, lightblue, violet); min-height: 100vh;">
<center>

<h1><font color="blue" face="Comic Sans MS">Week 4 Assignment</font></h1>

<font face="Comic Sans MS">
Welcome to my Week 4 project!!!!<br>
READ ONLY visitor count: <b><font color="red">{{ maara }}</font></b> !!!! ٩(^ᗜ^ )و ´-
</font>

<br><br>

<a href="http://195.148.21.248/week2/"><font size="6">Week 2</font></a>
&nbsp;|&nbsp;
<a href="http://128.214.252.207/week4/"><font size="6">Week 4 (this page)</font></a>
&nbsp;|&nbsp
<a href="https://github.com/joni9231/Linux-Administration/tree/main/week4"><font size="6">github</font></a>
<hr>
</center>

<div style="width: 800px; margin: auto; font-family: 'Comic Sans MS';">

<h2><font color="purple">Server B and copying</font></h2>
<p>
Server B was created in cPouta from a snapshot of server A.<br>
I set a floating IP and opened the necessary ports for SSH (22) and sql traffic (3306) (from the server A)
</p>

<h2><font color="purple">Storage, users and permissions</font></h2>
<p>
On server A the files are stored in /var/www/html and backed up to /var/backups/vmA on server B, outside of the public web directory.
The files are owned by root with permissions 600, meaning only root can read or modify them.
The database replication is done through a dedicated replicator user that has minimal privileges and cannot modify the database.
</p>

<h2><font color="purple">Hourly file backups</font></h2>
<p>The cron line</p>
0 * * * * /usr/local/bin/www-backup.sh
<p>Backup log:</p>
<pre>
<b>sudo cat /var/log/www-backup.log</b>
2026-11-20T09:00:02+02:00 SUCCESS 2026-11-20_0900
2026-11-20T10:00:02+02:00 SUCCESS 2026-11-20_1000
2026-11-20T11:00:03+02:00 SUCCESS 2026-11-20_1100
2026-11-20T12:00:02+02:00 SUCCESS 2026-11-20_1200
2026-11-20T13:00:04+02:00 SUCCESS 2026-11-20_1300
2026-11-20T14:00:02+02:00 SUCCESS 2026-11-20_1400
</pre>
<p>Backup files:</p>
<pre>
<b>sudo ls -l /var/backups/vmA</b>
-rw------- 1 root root 4133 Nov 20 09:00 www-2026-11-20_0900.tar.gz
-rw------- 1 root root 4129 Nov 20 10:00 www-2026-11-20_1000.tar.gz
-rw------- 1 root root 4131 Nov 20 11:00 www-2026-11-20_1100.tar.gz
-rw------- 1 root root 4133 Nov 20 12:00 www-2026-11-20_1200.tar.gz
-rw------- 1 root root 4133 Nov 20 13:00 www-2026-11-20_1300.tar.gz
-rw------- 1 root root 4132 Nov 20 14:00 www-2026-11-20_1400.tar.gz
</pre>

<h2><font color="purple">Database replication</font></h2>
<pre>
<b>date; uptime; sudo mysql -e "SHOW REPLICA STATUS\G" | egrep "Replica_IO_Running|Replica_SQL_Running|Seconds_Behind_Source|Last_.*Error|Source_Host"</b>
        Fri Nov 20 16:41:51 EET 2026
        16:41:51 up  3:53,  1 user,  load average: 0.06, 0.10, 0.09
        Source_Host: 192.168.1.225
        Replica_IO_Running: Yes
        Replica_SQL_Running: Yes
        Last_Error:
        Seconds_Behind_Source: 0
        Last_IO_Error:
        Last_SQL_Error:
        Replica_SQL_Running_State: Replica has read all relay log; waiting for more updates
        Last_IO_Error_Timestamp:
        Last_SQL_Error_Timestamp:
</pre>
<p>
There are no errors and the replica is 0 seconds behind, so replication is healthy. 

Replication does not replace historical backups because the changes carry over to the other server at a fast pace, meaning there is no earlier, healthy point to roll back to if a mistake happens.
</p>

<h2><font color="purple">Read only</font></h2>
<p>Config file:</p>
<pre>
<b>sudo cat /etc/mysql/mysql.conf.d/60-replication.cnf</b>
[mysqld]
server_id = 2              # PITÄÄ erota A:sta - kloonissa tarkista!
relay_log = replica-relay-bin
read_only = ON             # sovellus ei voi vahingossa kirjoittaa replikaan
event_scheduler = OFF
bind_address = 127.0.0.1
</pre>
<p>Test (trying to write to the replica):</p>
<pre>
<b>mysql> UPDATE laskuri SET maara = 67 WHERE id = 1;</b>
ERROR 1290 (HY000): The MySQL server is running with the --super-read-only option so it cannot execute this statement
</pre>

<h2><font color="purple">Reboot test</font></h2>
<pre>
<b>date</b>
Fri Nov 20 12:48:20 EET 2026
<b>reboot</b>
Connection to 128.214.252.207 closed by remote host
</pre>
<p>
The server was rebooted at 12:48. The backup log above shows that the 13:00
and 14:00 backups still ran. The replication status has date and uptime to show that it also ran upon reboot.
</p>

<h2><font color="purple">Restoration test</font></h2>
<pre>
<b>sudo tar -xzf /var/backups/vmA/www-2026-11-20_1300.tar.gz -C /tmp/restore-test ./index.html</b>
<b>sha256sum /tmp/restore-test/index.html</b>
dce61e547be50ef45966aa597f431eb31cdd61f1c3d267094209109f88d03440  /tmp/restore-test/index.html

<b>sudo ssh -i /root/.ssh/sync_ed25519 ubuntu@192.168.1.225 sha256sum /var/www/html/index.html</b>
dce61e547be50ef45966aa597f431eb31cdd61f1c3d267094209109f88d03440  /var/www/html/index.html
</pre>
<p>
Took a file out of the latest backup, and compared its sha256sum with the file
on server A. The checksums match, so the restored file is identical.
</p>

<h2><font color="purple">one thing learned</font></h2>
<pre>
<b>Its good to document things. Went backwards to a previous snapshot and i had no clue what i had done after that point. </b>
</pre>
</div>

<center>
<hr>
<pre>
 /\\_/\\
( o.o )
 > ^ <
</pre>

<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3JwZTRrN251b2pvcm8zaDh4ZWZjNzA1anI1NjVqeHd2N2p5M2hnNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mcsPU3SkKrYDdW3aAU/giphy.gif" width="300">

<br>
<hr>

<br>
</center>

</body>
</html>
"""
def viewCount():                                               #Does not increase value
    sql_connection = mysql.connector.connect(**DB_config)
    try:
        cursor = sql_connection.cursor()
        cursor.execute("SELECT maara FROM laskuri WHERE id = 1")
        (maara,) = cursor.fetchone()
        return maara
    finally:
        sql_connection.close()

@app.route("/")
def index():
    maara = viewCount()
    return render_template_string(SITE, maara=maara)