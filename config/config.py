import os

class config:
    """Base config."""
    SECRET_KEY = '2022'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class prod(config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class dev(config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True