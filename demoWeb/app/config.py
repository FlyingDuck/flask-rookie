# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig:
    SECRET_KEY = '693bda65112eb4b1eab2bfe3fa8e672ad220fa7c'
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    MAIL_SUBJECT_PREFIX = '[PKYX]'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'dongshujin@xiaoqianghome.com'

    @staticmethod
    def init_app(app):
        pass

class DevConfig(BaseConfig):
    MONGO_HOST = '127.0.0.1'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'tutorial'
    CELERY_IMPORTS = (
        "app.task.mail",
    )
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass

config = {
    'dev': DevConfig,
}