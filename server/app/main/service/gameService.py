from datetime import datetime

from flask import request, jsonify, Blueprint

from app.main.controller import gameController
from app.main.model.player import Player
from app.main.model.setting import Setting
from app.main.util.config import generate_http_response, MESSAGE_OK

gamePage = Blueprint('gameService', __name__, template_folder='templates')


@gamePage.route('/games', methods=["GET"])
def get_games():
    return jsonify(gameController.get_games())


@gamePage.route("/games/<id>", methods=["DELETE"])
def delete_game(id):
    return generate_http_response(gameController.delete_game(id))


@gamePage.route("/game/<id>", methods=["GET"])
def take_game(id):
    return jsonify(gameController.get_game(id).get_dictionary())


@gamePage.route("/games", methods=["POST"])
def create_new_game():
    setting_details = request.json
    id = setting_details["id"]
    numberOfPlayers = setting_details["numberOfPlayers"]
    startPoints = setting_details["startPoints"]
    doubleIn = setting_details["doubleIn"]
    doubleOut = setting_details["doubleOut"]
    playersId = setting_details["playersId"]

    setting = Setting(numberOfPlayers, startPoints, doubleIn, doubleOut)
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    players = []

    # TUTAJ
    # for i in range(numberOfPlayers):
    #     players.append(Player(playersId[i], "Gracz" + str(i + 1), startPoints, 3))
    players.append(Player(playersId[0], "Kuba", startPoints, 3))
    players.append(Player(playersId[1], "Bartosz", startPoints, 255))
    players.append(Player(playersId[2], "Artur", startPoints, 255))

    result = gameController.insert_game(id, 0, 0, date, playersId[0], 0, setting, players)
    return generate_http_response(result, MESSAGE_OK, 200)


@gamePage.route("/games", methods=["PUT"])
def update_game():
    game_details = request.json
    id = game_details["id"]
    if gameController.get_game(id) == "Game does not exist!":
        return "Game not exist"
    status = game_details["status"]
    throwingPlayerId = game_details["throwingPlayerId"]
    multiplier = game_details["multiplier"]
    value = game_details["value"]
    round = game_details["round"]
    playerList = game_details["playerList"]

    result = gameController.update_game(id, status, throwingPlayerId, multiplier, value, round,
                                        playerList)
    return generate_http_response(result, "Good PUT", 200)
