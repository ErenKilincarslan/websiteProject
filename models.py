from enum import unique
from bson.json_util import default
from flask_mongoengine import MongoEngine
from flask import jsonify
from flask_login import UserMixin

db = MongoEngine()

class User(db.Document,UserMixin):
    id = db.StringField(primary_key=True)
    email = db.StringField(required=True,unique=True)
    name = db.StringField()
    surname = db.StringField()
    password = db.StringField()
    is_authenticated = db.BooleanField(default=True)
    is_active = db.BooleanField(default=True)
    is_online = db.BooleanField(default=False)

    def to_json(self, *args, **kwargs):
        return super().to_json(*args, **kwargs)