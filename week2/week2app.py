import os
import mysql.connector
from flask import Flask, render_template_string
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv("db.env"))

app = Flask(__name__)

DB_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "xxx"),
    "password": os.getenv("DB_PASSWORD", "xxx"),
    "database": os.getenv("DB_DATABASE_NAME", "xxx"),
}

SITE = """
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
      font-family: "Comic Sans MS", "Comic Sans", cursive;
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
    here is visitor count: {{ maara }} !!!!!!!!</p>



<pre>

</pre>

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



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)