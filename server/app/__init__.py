from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    from .user import userPage as userBlueprint
    app.register_blueprint(userBlueprint, url_prefix='/user')

    from .info import infoPage as infoBlueprint
    app.register_blueprint(infoBlueprint, url_prefix='/info')

    from .game import gamePage as gameBlueprint
    app.register_blueprint(gameBlueprint, url_prefix='/game')

    CORS(app)

    return app
