# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() :
    return "This is HomePage. <a href='/hello'>Say Hello</a>"

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # return "Hello World , Hello Flask!  Do U want know my <a href='/user/dongshujin'>name</a>"
    return render_template('hello.html', name=name)

@app.route('/user/<name>')
def showName(name):
    return "Wow, My name is %s, Do U want know my <a href='/age/25'>age</a>" % name;

@app.route('/age/<int:age>')
def showAge(age):
    return "Yes, my age is %s" % age

@app.route("/about")
def about():
    return "This is about us, we are renovators."

@app.route("/brands/")
def brands():
    return "Those are brands."


if __name__ == '__main__':
    app.debug = True
    app.run()
    # app.run(debug=True)
