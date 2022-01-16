from datetime import datetime

from flask import request, jsonify, Blueprint

from app import db
from . import gamePage
from app.models.player import Player
from app.models.setting import Setting
from app.models.game import Game
from config import generate_http_response


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
    game = Game.querry.get_or_404(id)
    return jsonify(game.to_json())


# Creating game with players from settings
@gamePage.route("/games", methods=["POST"])
def create_new_game():
    setting = Setting.from_json(request.json)
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # TODO settings has to know players id
    game = Game(setting=setting, startTime=date, players_ids=request.json.get("playersId"),
                users_ids=request.json.get("playersId"))

    db.session.add(game)
    db.session.commit()


    # TUTAJ
    # for i in range(numberOfPlayers):
    #     players.append(Player(playersId[i], "Gracz" + str(i + 1), startPoints, 3))

    # creating players
    # players.append(Player(playersId[0], "Kuba", startPoints, 3))
    # players.append(Player(playersId[1], "Bartosz", startPoints, 255))
    # players.append(Player(playersId[2], "Artur", startPoints, 255))

    return generate_http_response(True, MESSAGE_OK, 200)


@gamePage.route("/games", methods=["PUT"])
def update_game():
    game = Game.querry.get_or_404(request.json.get('id'))
    game.update_from_json(request.json)
    return generate_http_response(True, "Good PUT", 200)
