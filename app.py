from flask.helpers import url_for
from flask_login import LoginManager,login_user,current_user
from flask_login.utils import login_required, logout_user
from flask_mongoengine import MongoEngine
from flask import Flask,render_template,request,json,jsonify,current_app,flash,session
from passlib.hash import pbkdf2_sha256 as hasher
from werkzeug.utils import redirect
from uuid import uuid4
from models import db,User
from flask_session import Session


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/oguzlar"
app.config.from_object(__name__)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

sess = Session()


login_manager = LoginManager()
login_manager.login_view = "login"

sess.init_app(app)
db.init_app(app)
login_manager.init_app(app)

def get_user(user_id):
    user = User.object(id = user_id).first()
    if user is not None:
        return user

@login_manager.user_loader
def load_user(user_id):
    return get_user(user_id)

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


@login_manager.user_loader
def load_user(user_id):
    return User.objects(id = user_id).first()

@app.route("/login" , methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form["email"]
        user_password = request.form["password"]
        user_profile = User.objects(email = user_email).first()
        if user_profile is not None: 
            if hasher.verify(user_password ,user_profile["password"]):
                session["user"]=user_profile
                login_user(user_profile)
                user_profile.is_online = True
                flash('Logged in successfully.')
                return redirect(url_for("home_page"))
    else:
        return render_template("login.html")

@login_required
@app.route("/logout")
def logout():
    if session["user"] is not None:
        user = session["user"]
        user.is_online = False
        session["user"] = None
        logout_user()
        flash("You Logged Out Successfully.")
        return redirect(url_for("home_page"))
    return redirect(url_for("home_page"))

@login_required
@app.route("/admin_panel")
def panel_page():
    return render_template("admin.html")

@app.route("/kullanici_ekle")
def add_user():
    new_user = User()
    new_user.id = uuid4().hex
    new_user.email = "admin@oguzlargayrimenkul.com"
    new_user.name = "admin"
    new_user.surname = "admin"
    new_user.password = hasher.hash("admin")
    new_user.save()
    return redirect(url_for("home_page"))

@app.route("/kullanici_sil")
def delete_user():
    user_list = User.objects()
    print(user_list)
    pass

app.run(port=5000)