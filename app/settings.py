import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class DevConfig(Config):
    APP_SERVER = 'DEV'
    SECRET_KEY = 'Dev - tis is secret?'
    DEBUG = True


class TestConfig(Config):
    APP_SERVER = 'TEST'
    SECRET_KEY = 'Test - tis is secret?'


class ProdConfig(Config):
    APP_SERVER = 'PROD'
    SECRET_KEY = 'Prod - tis is secret?'
