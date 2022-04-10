import os
import random

from flask import jsonify

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "hui"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ID_MAX = 65535
    ID_MIN = 50
    MESSAGE_OK = "Good"
    MESSAGE_ERROR = "Error"
    NOT_ACCEPTABLE = 406
    INTERNAL_SERVER_ERROR = 500
    OK = 200
    ROOM_NAME = "/game/"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def generate_http_response(status, message=Config.MESSAGE_ERROR, code=Config.NOT_ACCEPTABLE):
    dictionary = {"status": status, "message": message}
    return jsonify(dictionary), code


def get_dictionary(objects: list):
    dictionary = []
    for i in objects:
        dictionary.append(i.get_dictionary())
    return dictionary

