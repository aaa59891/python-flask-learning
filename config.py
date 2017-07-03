class Config(object):
  DEBUG = False
  TESTING = False
  SECRET_KEY = '1qaz2wsz3edc5rf6tgb'
class ProdConfig(Config):
  pass
class DevConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@192.168.90.10:5432/chong_test'