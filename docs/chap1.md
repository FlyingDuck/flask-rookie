[hello.py](../chap1/hello.py)
---------


## 1
```
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello World"


if __name__ == '__main__':
    app.run()
```

1, 导入Flask类 `from flask import Flask`, 这个Flask实例将作为一个WSGI应用;
2, 如果是单一模块我们使用 `__name__`作为Flask实例的第一个参数;
3, 使用route()设置应用路由;
4, 启动应用


## 2

带参数的请求路径解析

- /url/path/with/variable-parts/<variable_name>
- /url/path/with/variable-parts/<int: variable_name>


```
...

@app.route('/user/<name>')
def showName(name):
    return "Wow, My name is %s, Do U want know my <a href='/age/25'>age</a>" % name;

@app.route('/age/<int:age>')
def showAge(age):
    return "Yes, my age is %s" % age
...

```

支持如下转换:

| Type         | Desc         |
|:------------:|:------------:|
| int          |    |
| float        | |
| path         | |


## 3

反斜线`/`重定向问题

```
... 

@app.route("/about")
def about():
    return "This is about us, we are renovators."

@app.route("/brands/")
def brands():
    return "Those are brands."
    
 ...
 
```

- `/brands/`: 访问这样一个不带反斜线的路径会被重定向到带反斜线的路径上
- `/about` : 访问这样一个带反斜线的路径会返回 404


[url_build.py](../chap1/url_build.py)
---------------

## 4

`url_for` 构建URL

- 第一个参数为函数名
- 其它参数为url参数, 未知的参数会作为请求参数添加到url中

```
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index() : pass

@app.route('/login')
def login(): pass

@app.route('/profile/<username>')
def profile(username) : pass

with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', password="123456")
    print url_for('profile', username="dong shujin")
```

结果:

> 
/
/login
/login?password=123456
/profile/dong%20shujin


[http_method.py](../chap1/http_method.py)
--------------------

## 5

HTTP Method: GET POST HEAD PUT DELETE OPTIONS
```
@app.route("/login", methods=['GET', 'POST'])
def login() :
    if request.method == 'POST':
        return "U delive a post request. What did U say ?"
    else:
        return "U delive a get request."
```


## 6

Static Files 静态文件


[request.py](../chap1/request.py)
-------------------------------

## 7

Request

URL参数(?key=value), 可以通过args访问

> searchword = request.args.get('key', '')