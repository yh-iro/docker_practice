#!/usr/bin/python3

import flask
import psycopg2

app = flask.Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host='postgres',
        user='postgres',
        database='postgres',
    )

    cur = conn.cursor()
    cur.execute('select * from meibo')
    rows = cur.fetchall()

    return str(rows[0])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
