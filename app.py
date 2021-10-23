from flask.helpers import url_for
from flask_pymongo import PyMongo
from flask import Flask,render_template,Request
from werkzeug.wrappers import request
from werkzeug.utils import redirect

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/oguzlar"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/iletisim")
def contact_page():
    return render_template("contact.html")

@app.route("/ilanlar")
def properties_page():
    return render_template("properties.html")


@app.route("/blog")
def blog_page():
    return render_template("blog.html")

@app.route("/404")
def error_page():
    return render_template("404.html")

@app.route("/giris_yap")
def login():
    return render_template("register.html")

@app.route("/kayit_ekle")
def add_user():
    db.oguzlar.insert_one({'username': "admin", 'password': "admin"})

@app.route("/kayit_sil")
def delete_user():
    db.oguzlar.delete_many({'username' : 'eren'})