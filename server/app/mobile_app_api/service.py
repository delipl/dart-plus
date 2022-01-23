from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_login import login_user, logout_user, login_required, current_user

from app import db
from . import mobileApp
from app.models.user import User
from app.models.game import Game
from app.models.throw import Throw
from config import generate_http_response, config
from .errors import unauthorized, forbidden
from config import generate_http_response


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(phone, password):
    if phone == '':
        return False
    user = User.query.filter_by(phone=phone).first()
    if not user:
        return False
    g.current_user = user
    g.token_used = False
    return user.verify_password(password)


@auth.error_handler
def auth_error():
    return unauthorized('Incorrect login data')


@mobileApp.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous:
        return forbidden('Account has not been authorize')


@mobileApp.route('/tokens/', methods=['POST'])
def get_token():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Incorrect login data')
    return jsonify({'token': g.current_user.generate_auth_token(expiration=3600),
                    'expiration': 3600})


@mobileApp.route('/', methods=["GET"])
@auth.login_required
def get_games():
    games = Game.query.all()
    return jsonify({'games': [game.to_json() for game in games]})