# -*- coding: utf-8 -*-
from flask import Blueprint

users = Blueprint('users', __name__, url_prefix='/users')

from . import views