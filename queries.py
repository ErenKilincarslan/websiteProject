from app import *


@app.route("/kayit_ekle")
def add_user():
    db.oguzlar.insert_one({'username': "eren", 'password': "1234"})
    return Flask.jsonify(message="success")