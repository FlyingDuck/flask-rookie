# -*- coding: utf-8 -*-
from flask import current_app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash
from util import bson_to_json, bson_obj_id

import json

class User(UserMixin):
    def __init__(self, user_id, extras=None):
        self.id = user_id
        if (extras is not None) and isinstance(extras, dict):
            for name, attr in extras.items():
                setattr(self, name, attr)

    @staticmethod
    def gen_passwd_hash(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(passwd_hash, passwd):
        return check_password_hash(pwhash=passwd_hash, password=passwd)

    def gen_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps(bson_to_json({"id": self.id}))

    @staticmethod
    def verify_auth_token(token):
        from app import mongo
        s = Serializer(current_app.config['SECRET_KEY'])
        try :
            data = s.load(token)
        except:
            return None
        dict_ = json.loads(data)
        return mongo.db.users.find_one({"_id": bson_obj_id(dict_['id']['$oid'])})