# config_prod.py
SECRET_KEY = 'CHANGE ME!'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://test_user:test_password@/test_db'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
