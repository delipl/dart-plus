from flask import jsonify, g, request, current_app
import jwt
import time
import datetime
from app.models.user import User
from . import dartBordApi
from .decorators import token_required
from config import generate_http_response
from app.models.game import Game
from flask_httpauth import HTTPBasicAuth
from .errors import unauthorized, forbidden
from ..models.dart_board import DartBoard

#
# @dartBordApi.route('/settings', methods=["POST"])
# def get_settings():
#     dartBoardId = request.json.get('board_id')
#     # czy wyslij setting danej gry dla tej tarczy
#     game = Game()
#     return jsonify(game.get_settings_to_json())


@dartBordApi.route('/settings', methods=["POST"])
def get_settings():
    try:
        dartBoardId = request.json.get('board_id')
    except:
        return generate_http_response(False, "No json in post", 500)
    if dartBoardId is None:
        return generate_http_response(False, "Get no id", 401)
    game = DartBoard.query.get_or_404(dartBoardId).game
    if game is None:
        return generate_http_response(False, "Unknown id", 401)
    return jsonify(game.get_settings_to_json())


