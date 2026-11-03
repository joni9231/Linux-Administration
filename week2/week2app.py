import os

import mysql.connector

from flask import Flask, render_template_string

app = Flask(__name__)

DB_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "joni"),
    "password": os.getenv("DB_PASSWORD", "salasana123"),
    "database": os.getenv("DB_DATABASE_NAME", "kavijat"),
}



"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      max-width: 800px;
      margin: 40px auto;
      padding: 0 20px;
      font-family: sans-serif;
      line-height: 1.6;
      background: #f0f4f8;
      color: #203040;
    }
    h1, h2 { color: #005a8d; }
    pre { background: #fff; padding: 16px; overflow-x: auto; }
  </style>
</head>
<body>
  <h1>Week 2 Assignment</h1>
  <p>Welcome to my Week 2 project!!!!
    here is visitor count: [MAARA TAHAN] !!!!!!!!</p>



<pre>
 /\_/\
( o.o )
 > ^ <
</pre>

</body>
</html>
"""

def viewCount():
    sql_connection = mysql.connector.connect(**DB_config)
    cursor = sql_connection.cursor()
    // jatka sql juttua