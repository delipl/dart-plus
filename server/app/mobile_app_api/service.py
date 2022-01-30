import flask_login
from flask import jsonify, g, request

from . import mobileApp
from app.models.game import Game
from flask_login import login_user, logout_user, login_required, current_user
from .auth import auth
from app.models.dart_board import DartBoard
from .. import db
from ..models.user import User


@mobileApp.route('/game', methods=['GET'])
@auth.login_required
def is_user_in_games():
    print(g.current_user.name)
    if g.current_user.active_games is None:
        return jsonify({'game_status': 0})
    for game in g.current_user.active_games:
        if game.gameStatus == 1:
            return jsonify({'game_status': 1})
    for game in g.current_user.active_games:
        if game.gameStatus == 2:
            return jsonify({'game_status': 2})
    return jsonify({'game_status': 0})


@mobileApp.route('/', methods=["GET"])
@auth.login_required
def get_games():
    print('33333333')
    print(g.current_user)
    games = Game.query.all()
    return jsonify({'games': [game.to_json() for game in games]})


@mobileApp.route('/joinBoard', methods=['POST'])
@auth.login_required
def join_board():
    print(request.json)
    board_id = request.json.get('board_id')
    board = DartBoard.query.get_or_404(board_id)
    g.current_user.board = board
    db.session.commit()
    if g.current_user.active_games is None:
        game = Game(startPoints='301', doubleIn=False, doubleOut=False, gameStatus=2)
        game.boards.append(board)
        # add all players
        for user in User.query.all():
            user.active_games.append(game)

        db.session.add(game)
        db.session.commit()
        return jsonify({'game_status': 0, 'game_id': game.id})
    for game in g.current_user.active_games:
        if game.gameStatus == 1:
            return jsonify({'game_status': 1, 'game_id': game.id})
    for game in g.current_user.active_games:
        if game.gameStatus == 2:
            return jsonify({'game_status': 2, 'game_id': game.id})

    # create game
    game = Game(startPoints='301', doubleIn=False, doubleOut=False, gameStatus=2)
    game.boards.append(board)
    # add all players
    for user in User.query.all():
        user.active_games.append(game)

    db.session.add(game)
    db.session.commit()
    return jsonify({'game_status': 0, 'game_id': game.id})
