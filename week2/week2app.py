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
<title>week 2</title>
</head>
<body style="background: linear-gradient(pink, yellow, lightgreen, lightblue, violet); min-height: 100vh;">
<center>

<h1><font color="blue" face="Comic Sans MS">Week 2 Assignment</font></h1>

<font face="Comic Sans MS">
Welcome to my Week 2 project!!!!<br>
here is visitor count: <b><font color="red">{{ maara }}</font></b> !!!! ٩(^ᗜ^ )و ´-
</font>

<br><br>

<hr>

<pre style="font-size: 16px;">
This is made using MySQL as database.
The python script utilizes mysql.connector to communicate with the database.
Whenever the site is opened, The counter row is incremented by one and then the updated value is fetched.

Reboot test was successful, The site came back up by itself and no data was lost.

 /\\_/\\
( o.o )
 > ^ <
</pre>

<br><br><br>

<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjB1azc0dWRmN2d2Ym9idDA3NGtkcTUxbDRqbGJqOWtrcTU0Y3p5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gXXFrjHFJIMoqKr8UT/giphy.gif" width="300">


<br>
<hr>

<p>
<a href="https://github.com/joni9231/Linux-Administration/tree/main/week2"><font size="8">github</font></a>
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
