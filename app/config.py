import os, secrets

class Config(object):
    # Configuration settings Database
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'e-school.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Administrator
    FLASK_ADMIN_SWATCH = 'lux'

    # DEBUG
    DEBUG = True