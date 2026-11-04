import os
import mysql.connector
from flask import Flask, render_template_string
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv("db.env"))

app = Flask(name)

DB_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASENAME"),
}

SITE = """
<html>
<head>
<title>week 2</title>
</head>
<body style="background: linear-gradient(pink, yellow, lightgreen, lightblue, violet); min-height: 100vh;">

<center>

<h1><font color="blue" face="Comic Sans MS">Week 2 Assignment</font></h1>

<font face="Comic Sans MS">
Welcome to my Week 2 project!!!!<br>
here is visitor count: <b><font color="red">{{ maara }}</font></b> !!!! (≧▽≦)
</font>

<br><br>

<hr>

<pre>
 /\/\
( o.o )
^ <
</pre>

<br><br><br>

<img src="https://static.wikia.nocookie.net/silly-cat/images/1/19/Thumbs_Up.png/revision/latest?cb=20231201204731" width="300">


<br>
<hr>

<p>
<a href="https://github.com/joni9231/Linux-Administration/tree/main/week2"><font size="6">github</font></a>
</p>

<br>

</center>

</body>
</html>
"""

def viewCount():
    sql_connection = mysql.connector.connect(**DB_config)
    try:
        cursor = sql_connection.cursor()
        cursor.execute("UPDATE laskuri SET maara = maara +1 WHERE id = 1")
        cursor.execute("SELECT maara FROM laskuri WHERE id = 1")
        (maara,) = cursor.fetchone()
        sql_connection.commit()
        return maara
    finally:
        sql_connection.close()

@app.route("/")
def index():
    maara = viewCount()
    return render_template_string(SITE, maara=maara)
