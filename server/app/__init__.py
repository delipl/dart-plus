from socket import SocketIO
from flask_socketio import SocketIO, send, emit
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config



db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'mobileApp.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    socketio = SocketIO(app, cors_allowed_origins='*')

    from app.socket_game_comunication.socket_game_loop import GameLoopSocket
    socketio.on_namespace(GameLoopSocket('/gameLoop'))

    from .user import userPage as userBlueprint
    app.register_blueprint(userBlueprint, url_prefix='/users')

    from .game import gamePage as gameBlueprint
    app.register_blueprint(gameBlueprint, url_prefix='/games')

    from .mobile_app_api import mobileApp as mobileAppBlueprint
    app.register_blueprint(mobileAppBlueprint, url_prefix='/app')

    from .dart_board_api import dartBordApi as dartBoardApiBlueprint
    app.register_blueprint(dartBoardApiBlueprint, url_prefix='/dartboard')

    CORS(app)

    return app, socketio
