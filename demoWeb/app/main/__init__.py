# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors






# 蓝本（Flask-Blueprint）有许多用途，其中一个常见的用途即是为应用的模块做url的划分。在一个应用的 URL 前缀和（或）子域上注册一个蓝图。
# URL 前缀和（或）子域的参数 成为蓝图中所有视图的通用视图参数（缺省情况下）。关于蓝本的详细说明：http://dormousehole.readthedocs.org/en/latest/blueprints.html#blueprints
# 在Blueprint的参数中还可以指定模块的静态文件路径以及模版文件路径。