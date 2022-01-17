from datetime import datetime
from flask import request, jsonify, Blueprint

from app import db
from . import gamePage
from app.models.setting import Setting
from app.models.user import User
from app.models.game import Game
from config import generate_http_response, config


@gamePage.route('/games', methods=["GET"])
def get_games():
    games = Game.querry.all()
    return jsonify({'games': [game.to_json() for game in games]})


@gamePage.route('/games', methods=["DELETE"])
def delete_games():
    games = Game.querry.all()
    for game in games:
        db.session.delete(game)

    db.session.commit()
    return generate_http_response(True, "DELETE GAMES", 200)


@gamePage.route("/games/<id>", methods=["DELETE"])
def delete_game(id):
    game = Game.querry.get_or_404(id)
    db.session.delete(game)
    return generate_http_response(True, "DELETE GAME", 200)


@gamePage.route("/game/<id>", methods=["GET"])
def take_game(id):
    game = Game.query.get_or_404(id)
    return jsonify(game.to_json())


# Creating game with players from settings
@gamePage.route("/games", methods=["POST"])
def create_new_game():
    settingId = request.json.get('id')
    amountOfUsers = request.json.get('numberOfPlayers')
    startPoints = request.json.get('startPoints')
    doubleIn = request.json.get('doubleIn')
    doubleOut = request.json.get('doubleOut')

    usersId = request.json.get('playersId')
    players_nicks = [User.querry.filter_by(id=userId).nick for userId in usersId]

    players = [Player(nick=players_nicks[i], points=startPoints, attempts=255,
                      user=User.querry.filter_by(id=usersId[i]), setting_id=settingId)
               for i in range(len(usersId))]
    for player in players:
        db.session.add(player)

    setting = Setting(amountOfUsers=amountOfUsers, startPoints=startPoints, doubleIn=doubleIn,
                      doubleOut=doubleOut, players=players, settingId=settingId)
    db.session.add(setting)

    game = Game(setting_id=setting.id, startTime=datetime.now())
    db.session.add(game)

    db.session.commit()

    return generate_http_response(True, config.MESSAGE_OK, 200)


@gamePage.route("/games", methods=["PUT"])
def update_game():
    setting = Setting.query.get_or_404(request.json.get('id'))
    db.session.delete(setting)
    game = Game.querry.filter_by(settig_id=request.json.get('id'))
    db.session.delete(game)
    game.gameStatus = request.json.get('status')
    game.numberOfThrow = request.json.get('numberOfThrow')
    game.throwingUserId = request.json.get('throwingUserId')
    game.round = request.json.get('round')

    # TODO szukanie listy playerów zrobić w osobnj metodzie
    players_dict = request.json.get('players')
    usersId = players_dict['id']
    playersId = [User.query.get_or_404(userId).player_Id for userId in usersId]
    players = [Player.querry.get_or_404(playerId) for playerId in playersId]

    for player in players:
        if player.user.id == game.throwingUserId:
            db.session.delete(player)
            player.throws_multiplier = request.json.get('throws_multiplier')
            player.throws_value = request.json.get('throws_value')
            db.session.add(player)

    # TODO może trzeba baedzie uaktualnić playerów/useróœ w relacjach

    db.session.add(setting)
    db.session.add(game)

    db.session.commit()
    return generate_http_response(True, "Good PUT", 200)
