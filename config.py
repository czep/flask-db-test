import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #print "envs:", SECRET_KEY, ", ", SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True 

class TestingConfig(Config):
    TESTING = True
     
class ProductionConfig(Config):
    pass
        
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig, 
    'default': DevelopmentConfig 
}
