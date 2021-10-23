from flask.helpers import url_for
from app import *

app.config["MONGO_URI"] = "mongodb://localhost:27017/oguzlar"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route('/kayit_ekle')
def add_user():
    db.oguzlar.insert_one({'username': "eren", 'password': "1234"})
    return True

@app.route('/kayit_sil')    
def delete_user():
    db.oguzlar.delete_many({ 'username' : 'eren'})
    return True