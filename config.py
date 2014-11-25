import os
# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "r\xeb\x19\x13\x8c\xc9\xb0\x8e\xca\xcb\xf8\xec\x14\x91\xeb\xe0:8\x1b\x8d\x15V\rh"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
