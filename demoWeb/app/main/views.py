# -*- coding: utf-8 -*-

from flask import render_template, request, Response, flash, redirect, url_for
from flask_login import current_user

from app.forms import PkForm, LoginForm, BaseEntryForm
from app.models import Item

from . import main

@main.route('/')
def index():
    lg_form = LoginForm()
    return render_template('index.html', lg_form=lg_form, title=u'首页')


@main.route('/pk', methods=['POST', 'GET'])
def pk():
    pk_form = PkForm(request.form)
    if pk_form.validate_on_submit():
        pk1_name = request.form.get('pk1')
        pk2_name = request.form.get('pk2')
        return render_template("pk.html", pk1=pk1_name, pk2=pk2_name)
    return Response('Invalid input')


@main.route('/create_entry', methods=['GET', 'POST'])
def create_entry():
    entry_form = BaseEntryForm()
    if entry_form.validate_on_submit():
        title = request.form['title'].strip()
        type = request.form['type'].strip()
        if not title:
            flash('属性不能为空', 'red')
        elif not type:
            flash('类型不能为空', 'red')
        elif Item.find_item(title):
            flash('词条已存在', 'yellow')
        else:
            status = Item.create_item(title, type)
            if status:
                Item.add_type(type)
                if current_user.is_authenticated:
                    current_user.add_create()
            return redirect(url_for('.item', title=title))
    else:
        for field, errors in entry_form.errors.items():
            for error in errors:
                flash("%s: %s" %(getattr(entry_form, field).label.text, error), 'red')
    types = Item.types()
    return render_template('create.html', entry_form=entry_form, title='创建条目', types=types)
