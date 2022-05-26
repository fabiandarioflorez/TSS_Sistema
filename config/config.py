# Esto es la configuracion mediante objetos

class Config(object):
    'Esta es la configuracion base'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/TSS_db_sistema"
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

class ProductionConfig(Config):
    'Esta es la configuracion para Produccion'
    DEBUG = False

class DevelopmentConfig(Config):
    'Esta es la configuracion para Desarrollo'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'
    
