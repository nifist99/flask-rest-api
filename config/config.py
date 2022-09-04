import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class config:
    """Base config."""
    SECRET_KEY = os.getenv('SCREET_KEY')
    STATIC_FOLDER = os.getenv('STATIC_FOLDER')
    TEMPLATES_FOLDER = os.getenv('TEMPLATES_FOLDER')


class ProdConfig(config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True