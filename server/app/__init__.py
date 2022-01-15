import time
from threading import Thread
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
from flask_sqlalchemy import SQLAlchemy

from config import config
from app.main.controller import infoController
from app.main.controller.gameController import delete_games
from app.main.database.database import create_tables
from app.main.service.gameService import gamePage
from app.main.service.infoService import infoPage, get_info
from app.main.service.userService import userPage


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    app.register_blueprint(userPage)
    app.register_blueprint(infoPage)
    app.register_blueprint(gamePage)
    CORS(app)
    return app
