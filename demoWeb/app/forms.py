# -*- coding: utf-8 -*-
# from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# 首先从WTF扩展中导入Form类，我们要定义的表单类会继承到这个Form类，接下来简单地为表单定义三个域，两个文本输入框，
# validators中加入了wtforms.validators中的DataRequired的实例，它将会把这两个文本框设置为必填项。最后还有一个
# 提交域，也就是提交该表单的按钮。
class PkForm(FlaskForm) :
    pk1 = StringField(validators=[DataRequired()])
    pk2 = StringField(validators=[DataRequired()])
    submit = SubmitField(label=u'pk一下')

