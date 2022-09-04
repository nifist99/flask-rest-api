import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config(object):
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    ENV = 'production'
    
class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True