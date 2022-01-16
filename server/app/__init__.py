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

    from app.main.service.gameService import gamePage
    from app.main.service.infoService import infoPage
    from app.main.service.userService import userPage
    app.register_blueprint(userPage)
    app.register_blueprint(infoPage)
    app.register_blueprint(gamePage)
    CORS(app)
    return app
