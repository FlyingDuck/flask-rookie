# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login() :
    if request.method == 'POST':
        return "U delive a post request. What did U say ?"
    else:
        return "U delive a get request."


if __name__ == '__main__':
    app.run(debug=True)


