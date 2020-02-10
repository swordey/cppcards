from flask import render_template
from app import app
import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def main():
    with sqlite3.connect("app/db.db") as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()

        c.execute("SELECT * FROM interviews")
        datas = c.fetchall()

        out = {}
        for data in datas:
            tags_str = data["tags"]
            tags = tags_str.split(';')
            for tag in tags:
                if tag in out:
                    out[tag] += [data]
                else:
                    out[tag] = [data]
    return render_template("main.html", groups=out.keys())


@app.route('/<group>')
def mobil(group):
    with sqlite3.connect("app/db.db") as conn:
        conn.row_factory = dict_factory
        c = conn.cursor()

        c.execute("SELECT * FROM interviews")
        datas = c.fetchall()

        out = {}
        for data in datas:
            tags_str = data["tags"]
            tags = tags_str.split(';')
            for tag in tags:
                if tag in out:
                    out[tag] += [data]
                else:
                    out[tag] = [data]
    return render_template("cards.html", groups=out.keys(), datas=out[group], selected_group=group)

