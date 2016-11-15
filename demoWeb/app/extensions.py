# -*- coding: utf-8 -*-
from flask.ext.pymongo import PyMongo
from flask.ext.login import LoginManager
# from flask.ext.mail import Mail
# from flask.ext.celery import Celery
# from flask.ext.admin import Admin

from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_mail import Mail
from flask_celery import Celery

# admin = Admin()
mail = Mail()
mongo = PyMongo()
celery = Celery()
login_manager = LoginManager()

