from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .user import userPage as userBlueprint
    app.register_blueprint(userBlueprint, url_prefix='/users')

    from .info import infoPage as infoBlueprint
    app.register_blueprint(infoBlueprint, url_prefix='/info')

    from .game import gamePage as gameBlueprint
    app.register_blueprint(gameBlueprint, url_prefix='/games')

    from .mobile_app_api import mobileApp as mobileAppBlueprint
    app.register_blueprint(mobileAppBlueprint, url_prefix='/mobileApp')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    CORS(app)

    return app
