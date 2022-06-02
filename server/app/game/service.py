from datetime import datetime
from flask import request, jsonify, Blueprint

from app import db
from . import gamePage
from app.models.user import User
from app.models.game import Game
from app.models.throw import Throw
from config import generate_http_response, config


@gamePage.route('/', methods=["GET"])
def get_games():
    games = Game.query.all()
    return jsonify({'games': [game.to_json() for game in games]})


@gamePage.route('/', methods=["DELETE"])
def delete_games():
    games = Game.query.all()
    for game in games:
        db.session.delete(game)

    db.session.commit()
    return generate_http_response(True, "DELETE GAMES", 200)


@gamePage.route("/<id>", methods=["DELETE"])
def delete_game(id):
    game = Game.query.get_or_404(id)
    db.session.delete(game)
    return generate_http_response(True, "DELETE GAME", 200)


@gamePage.route("/<id>", methods=["GET"])
def take_game(id):
    game = Game.query.get_or_404(id)
    return jsonify(game.get_settings_to_json())


# Creating game with players from settings
@gamePage.route("/", methods=["POST"])
def create_new_game():
    usersId = request.json.get('playersId')
    users = [User.query.get_or_404(user_id) for user_id in usersId]

    startPoints = request.json.get('startPoints')
    doubleIn = request.json.get('doubleIn')
    doubleOut = request.json.get('doubleOut')
    throwingUserId = users[0].id

    game = Game(gameStatus=1, startPoints=startPoints, doubleIn=doubleIn,
                doubleOut=doubleOut, throwingUserId=throwingUserId)

    for user in users:
        game.players.append(user)

    db.session.add(game)
    db.session.commit()
    return generate_http_response(True, "OK", 200)


@gamePage.route("/", methods=["PUT"])
def update_game():
    game_id = request.json.get('id')
    status = request.json.get('status')
    throwingPlayerId = request.json.get('throwingPlayerId')
    multiplier = request.json.get('multiplier')
    value = request.json.get('value')
    round = request.json.get('round')
    players = request.json.get('players')
    players_id = [player['id'] for player in players]
    players_attempts = [player['attempts'] for player in players]
    players_points = [player['points'] for player in players]

    users = [User.query.get_or_404(player_id) for player_id in players_id]
    for i in range(len(users)):
        users[i-1].attempts = players_attempts[i-1]
        users[i-1].points = players_points[i-1]

    users[throwingPlayerId-1].throws_multiplier = multiplier
    users[throwingPlayerId-1].throws_value = value
    throw = Throw(value=value, multiplier=multiplier, player=users[throwingPlayerId-1])
    db.session.add(throw)

    game = Game.query.get_or_404(game_id)
    game.gameStatus = status
    game.throwingUserId = throwingPlayerId
    game.round = round

    db.session.commit()
    return generate_http_response(True, "Good PUT", 200)
