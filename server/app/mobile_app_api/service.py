from flask import jsonify

from . import mobileApp
from flask_login import login_required
from app.models.game import Game


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
# @mobileApp.route('/tokens/', methods=['POST'])
# def get_token():
#     print("get token")
#     if g.current_user.is_anonymous or g.token_used:
#         return unauthorized('Incorrect login data')
#     return jsonify({'token': g.current_user.generate_auth_token(expiration=3600),
#                     'expiration': 3600})
#

@mobileApp.route('/', methods=["GET"])
@login_required
def get_games():
    games = Game.query.all()
    return jsonify({'games': [game.to_json() for game in games]})
