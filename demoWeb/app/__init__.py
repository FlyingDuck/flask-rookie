# -*- coding: utf-8 -*-
from flask import Flask
from config import config
from flask_pymongo import PyMongo
# from flask.ext.pymongo import PyMongo

mongo = PyMongo()

def create_app(config_name='dev'):
    app = Flask(__name__)

    # 导入配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 初始化MongoDB
    mongo.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from api import api as api_buleprint
    app.register_blueprint(api_buleprint)

    return app
