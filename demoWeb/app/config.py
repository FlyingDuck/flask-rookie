# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig:
    SECRET_KEY = '693bda65112eb4b1eab2bfe3fa8e672ad220fa7c' # MD5 ("flask-demo-web-app")
    PKYX_MAIL_SENDER = u'PK一下 <dongshujin@mail.com>'
    PKYX_MAIL_SUBJECT_PREFIX = '[PKYX]'

    @staticmethod
    def init_app(app):
        pass


class DevConfig(BaseConfig):
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'tutorial' #  pkyx

    @staticmethod
    def init_app(app):
        # from flask.ext.pymongo import PyMongo
        # from flask_pymongo import PyMongo
        # app = PyMongo(app)
        return app
        # pass


config = {
    'dev': DevConfig,
}