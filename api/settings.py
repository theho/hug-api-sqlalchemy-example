import os


class Config:
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    SECRET_KEY = 'sc62ko&m&3g*rx8r3j2pinf6ae1%#=m5#g&hho2mu_tea-#&us'


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/mmm'
