import flask_login
from flask import jsonify, g

from . import mobileApp
from app.models.game import Game
from flask_login import login_user, logout_user, login_required, current_user
from .auth import auth


# auth = HTTPBasicAuth()
#
#
# @auth.verify_password
# def verify_password(phone_or_token, password):
#     if phone_or_token == '':
#         return False
#     if password == '':
#         g.current_user = User.verify_auth_token(phone_or_token)
#         g.token_used = True
#         return g.current_user is not None
#     user = User.query.filter_by(phone=phone_or_token.lower()).first()
#     if not user:
#         return False
#     g.current_user = user
#     g.token_used = False
#     return user.verify_password(password)
#
#
# @auth.error_handler
# def auth_error():
#     return unauthorized('Incorrect login data')
#
#

@mobileApp.route('/game', methods=['GET'])
@auth.login_required
def is_user_in_games():
    print('33333333')
    print(g.current_user)
    print(g.current_user.active_games[0])
    if current_user.active_games[0] is not None:
        print(current_user.active_games[0].get_settings_to_json())
        return jsonify(current_user.active_games[0].get_settings_to_json())
    return jsonify({'id': 0})


@mobileApp.route('/', methods=["GET"])
@auth.login_required
def get_games():
    games = Game.query.all()
    return jsonify({'games': [game.to_json() for game in games]})
