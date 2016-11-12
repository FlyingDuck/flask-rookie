# -*- coding: utf-8 -*-
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors



from flask import render_template, request, Response
from forms import PkForm

from . import main

@main.route('/')
def index():
    pk_form = PkForm()
    return render_template("index.html", form=pk_form)

@main.route('/pk', methods=['POST', 'GET'])
def pk():
    pk_form = PkForm(request.form)
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template("pk.html", pk1=pk1_name, pk2=pk2_name)
    return Response('Invalid input')



# 蓝本（Flask-Blueprint）有许多用途，其中一个常见的用途即是为应用的模块做url的划分。在一个应用的 URL 前缀和（或）子域上注册一个蓝图。
# URL 前缀和（或）子域的参数 成为蓝图中所有视图的通用视图参数（缺省情况下）。关于蓝本的详细说明：http://dormousehole.readthedocs.org/en/latest/blueprints.html#blueprints
# 在Blueprint的参数中还可以指定模块的静态文件路径以及模版文件路径。