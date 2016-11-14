# -*- coding: utf-8 -*-

from flask import render_template, request, Response

from forms import PkForm, LoginForm

from . import main

@main.route('/')
def index():
    pk_form = PkForm()
    lg_form = LoginForm()
    return render_template("index.html", form=pk_form, lg_form=lg_form)

@main.route('/pk', methods=['POST', 'GET'])
def pk():
    pk_form = PkForm(request.form)
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template("pk.html", pk1=pk1_name, pk2=pk2_name)
    return Response('Invalid input')

