#!/usr/bin/env python

import os
   
from app import create_app, db
from app.models import Stuff
from flask.ext.script import Manager, Shell

app = create_app()
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Settings=Settings)

manager.add_command("shell", Shell(make_context = make_shell_context))

@manager.command
def init_database():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    manager.run()
    