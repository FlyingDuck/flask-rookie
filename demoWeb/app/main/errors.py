# -*- coding: utf-8 -*-
from flask import render_template
from . import main


# 为应用编写错误的响应视图十分重要，这里简单地定义了两个视图，分别对应错误404和错误500的响应，注意这里使用的main
# 为上一个中定义的蓝本对象，若在英语中注册了蓝本，被装饰器包装的视图函数都会注册到应用中，它会把 构建Blueprint时
# 所使用的名称（在本例为simple_page）作为函数端点 的前缀。

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@main.app_errorhandler(500)
def page_server_error(e):
    return render_template("500.html"), 500

