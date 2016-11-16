# -*- coding: utf-8 -*-
#!/usr/bin/env python

from app import app
from app.extensions import mongo
# from app.models import Item, User
from app import models
from flask_script import Manager, Shell

manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=mongo.db,models=models)

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()



# from app import create_app
#
# app = create_app('dev')
#
# if __name__ == '__main__' :
#     app.run(debug=True)
