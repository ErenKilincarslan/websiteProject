from flask import Flask
from flask import render_template

app = Flask(__name__)

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