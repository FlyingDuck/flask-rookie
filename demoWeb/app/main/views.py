# -*- coding: utf-8 -*-

from flask import render_template, request, Response, flash, redirect, url_for, abort
from flask_login import current_user, login_required

from app.forms import PkForm, LoginForm, BaseEntryForm
from app.models import Item
from app.util import TypeRender

from . import main

from collections import defaultdict

import re


@main.route('/')
def index():
    lg_form = LoginForm()
    return render_template('index.html', lg_form=lg_form, title=u'首页')

pk_regx = re.compile(r'(\w+)\s+(pk|Pk|pK|PK)\s+(\w+)', re.IGNORECASE)

@main.route('/pk', methods=['GET', 'POST'])
def pk():
    if request.method == 'POST':
        pk_str = request.form.get('pk').strip()
        g = pk_regx.match(pk_str)
        if g:
            pk1_title = g.groups()[0]
            pk2_title = g.groups()[2]
            pk1_regx = re.compile(pk1_title, re.IGNORECASE)
            pk2_regx = re.compile(pk2_title, re.IGNORECASE)
            pk1_item = Item.find_item(pk1_regx)
            pk2_item = Item.find_item(pk2_regx)
            if pk1_item and pk2_item:
                # 按首字母大小排序
                rows_by_name = defaultdict(list)
                for attr in pk1_item['attributes']:
                    rows_by_name[attr['attr_name']].append(attr)
                for attr in pk2_item['attributes']:
                    # 保证顺序
                    if not attr['attr_name'] in rows_by_name.keys():
                        rows_by_name[attr['attr_name']].append({})
                    rows_by_name[attr['attr_name']].append(attr)

                for key, attrs in rows_by_name.items():
                    if len(attrs) == 1:
                        attrs.append({})
                return render_template('pk.html', pk1=pk1_item, pk2=pk2_item, rows=rows_by_name, TypeRender=TypeRender)
            else:
                if not pk1_item:
                    flash(u'搜索不到%s' % pk1_title, 'red')
                if not pk2_item:
                    flash(u'搜索不到%s' % pk2_title, 'red')
        else:
            flash(u'输入格式有误', 'red')
    return redirect(url_for('.index'))

@main.route('/item/<title>')
def item(title):
    item = Item.find_item(title)
    if not item:
        abort(404)
    Item.inc_view(title)
    return render_template('item.html', item=item, TypeRender=TypeRender)

@main.route('/create_entry', methods=['GET', 'POST'])
def create_entry():
    entry_form = BaseEntryForm()
    if entry_form.validate_on_submit():
        title = request.form['title'].strip()
        type = request.form['type'].strip()
        if not title:
            flash(u'属性不能为空', 'red')
        elif not type:
            flash(u'类型不能为空', 'red')
        elif Item.find_item(title):
            flash(u'词条已存在', 'yellow')
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
    return render_template('create.html', entry_form=entry_form, title=u'创建条目', types=types)
