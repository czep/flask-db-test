# config_dev.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'CHANGE ME!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask-db-test.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
