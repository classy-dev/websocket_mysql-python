from flask import Flask, request, render_template
import pymysql
import threading
from config import *
from socketUnit import *

app = Flask(__name__)
db = pymysql.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)  # mysql db connection


# WebSocket Function
def run_socket():
    unit = SocketUnit()
    unit.run()

@app.route('/')
def get_data():
    cursor = db.cursor()

    # -------------get latest 10 liquidation data from mysql-------------
    sql = "SELECT * FROM liquidations ORDER BY timestamps DESC Limit 10"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)


if __name__ == "__main__":
    x = threading.Thread(target=run_socket, args=())
    x.start()
    app.run(debug=True)
    x.join()