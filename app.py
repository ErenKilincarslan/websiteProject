from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index-2.html")

@app.route("/iletisim")
def contact():
    return render_template("contact.html")