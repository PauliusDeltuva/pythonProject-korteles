from flask import Flask, render_template, g
import sqlite3
from korteles import app


# app = Flask(__name__)

DATABASE = 'cards.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("sign-up.html")

@app.route("/base")
def base():
    return render_template("base.html")



@app.route('/')
def home():
    db = get_db()
    cur = db.execute('SELECT id, name, description, price, image FROM cards')
    products = cur.fetchall()
    return render_template('base.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)


