# -*- coding: utf-8 -*-
# from flask.ext.wtf import Form
from flask_wtf import FlaskForm, RecaptchaField
# from flask_wtf.html5 import EmailField
from wtforms.fields.html5 import EmailField, URLField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp


_required_text = u'该字段为必填项'

validators = {
    'email': [
        DataRequired(message=_required_text),
    ],
    'username': [
        DataRequired(message=_required_text),
        Length(min=2, max=18, message=u'用户名长度为2到18位')
    ],
    'password': [
        DataRequired(message=_required_text),
        Regexp(regex=r'^[A-Za-z0-9@#$%^&+=_-]{6,18}$',message=u'密码格式错误')
    ]
}


# 首先从WTF扩展中导入Form类，我们要定义的表单类会继承到这个Form类，接下来简单地为表单定义三个域，两个文本输入框，
# validators中加入了wtforms.validators中的DataRequired的实例，它将会把这两个文本框设置为必填项。最后还有一个
# 提交域，也就是提交该表单的按钮。
class PkForm(FlaskForm) :
    pk1 = StringField(validators=[DataRequired()])
    pk2 = StringField(validators=[DataRequired()])
    submit = SubmitField(label=u'pk一下')


class LoginForm(FlaskForm):
    email = EmailField(label=u'邮箱', validators=[DataRequired()])
    password = PasswordField(label=u'密码', validators=[DataRequired()])
    submit = SubmitField(label=u"登陆")

class RegisterForm(FlaskForm):
    email = EmailField(u'邮箱', validators=validators['email'])
    username = StringField(u'用户名', validators=validators['username'])
    password = PasswordField(u'密码', validators=validators['password'])
    repeat = PasswordField(u'重复密码', validators=validators['password'])


class BaseEntryForm(FlaskForm):
    title = StringField(u'名称', validators=[DataRequired(message=_required_text)])
    type = StringField(u'类别', validators=[DataRequired(message=_required_text)])


class ProfileForm(FlaskForm):
    username = StringField(u'呢称*', validators=validators['username'])
    location = StringField(u'所在地区', validators=[Length(max=64)])
    website = URLField(u'个人主页', validators=[Length(max=256)])
    introduction = TextAreaField(u'个人简介', validators=[Length(max=1024)])