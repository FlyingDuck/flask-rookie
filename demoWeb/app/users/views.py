# -*- coding: utf-8 -*-
from flask import flash, redirect, url_for, render_template, request
from flask_login import login_user, login_required

from app import mongo
from app.forms import RegisterForm, LoginForm
from app.models import User

from . import users

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    lg_form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        passwd = form.password.data
        rp_passwd = form.repeat.data
        if passwd != rp_passwd:
            flash(u'两次密码不相同', 'WARNING')
        elif mongo.db.users.find_one({'email': email}) is not None:
            flash(u'邮箱已经被注册', 'WARING')
        else:
            mongo.db.users.insert({'email': email, 'username': username, 'password': User.gen_passwd_hash(passwd)})
            flash(u'注册成功', 'SUCCESS')
            return redirect(url_for('.login'))
    return render_template('register.html', form=form, lg_form=lg_form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_user = mongo.db.users.find_one({'email': form.email.data})
        if db_user is not None:
            db_passwd = db_user.get('password', None)
            if User.verify_password(db_passwd, form.password.data):
                user = User(db_user['_id'])
                login_user(user)
                flash(u'登陆成功', 'SUCCESS')
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash(u'密码错误', 'WARING')
        else:
            flash(u'用户不存在', 'WARING')
    return render_template('login.html', form=form)


@users.route('/profile')
@login_required
def profile():
    return render_template('profile.html')